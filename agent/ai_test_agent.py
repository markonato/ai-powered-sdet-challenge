import os

from dotenv import load_dotenv
from openai import OpenAIError, RateLimitError

from agent.analyzer import analyze_results
from agent.test_executor import run_tests
from agent.test_generator import generate_tests

load_dotenv()

def run_ai_test_agent(api_spec: str):
    """
    Main AI test agent:
    1. Generate tests (AI)
    2. Execute tests via pytest
    3. Analyze results (AI)
    """
    # Step 1: Generate tests
    try:
        test_file_path = generate_tests(api_spec)
    except (RateLimitError, OpenAIError, Exception) as e:
        print(f"⚠️ OpenAI error or quota issue: {e}")
        test_file_path = "no_filepath"

    # Ensure a valid test file exists before running
    if not test_file_path or not os.path.exists(test_file_path):
        raise RuntimeError("❌ No valid test file found to execute")

    # Step 2: Execute tests
    summary = run_tests(test_file_path)
    print("............\n")
    print(f"✅ Generated {summary["num_generated_tests"]} test scenarios using AI")
    print(f"✅ Executed {summary["num_executed_tests"]} tests in {summary["duration"]:.2f} seconds")

    # Step 3: Analyze results
    insights = analyze_results(summary["result_file"])
    print("\n🧠 AI Analysis:")
    print(insights)

    return insights

if __name__ == "__main__":
    api_spec = """
FastAPI Task Management API:
POST /tasks - create task
GET /tasks - list tasks
GET /tasks/{id} - get task
PUT /tasks/{id} - update task
DELETE /tasks/{id} - delete task
PATCH /tasks/{id}/status - mark completed/pending
"""
