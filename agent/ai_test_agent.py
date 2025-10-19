import os
from dotenv import load_dotenv
from agent.test_generator import generate_tests
from agent.test_executor import run_tests
from agent.analyzer import analyze_results
from openai import OpenAIError, RateLimitError

load_dotenv()

def run_ai_test_agent(api_spec: str):
    """
    Main AI test agent:
    1. Generate tests (AI or mock)
    2. Execute tests via pytest
    3. Analyze results (AI or mock)
    """
    # Step 1: Generate tests
    print("🧠 Generating tests...")
    try:
        test_file_path = generate_tests(api_spec)
        print(f"✅ Generated test scenarios using AI at: {test_file_path}")
    except (RateLimitError, OpenAIError, Exception) as e:
        print(f"⚠️ OpenAI error or quota issue: {e}")

    # Step 2: Execute tests
    print("⚙️ Executing tests...")
    results_path = run_tests(test_file_path)

    # Step 3: Analyze results
    print("🔍 Analyzing results...")
    insights = analyze_results(results_path)

    print("\n=== AI Insights ===")
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
    run_ai_test_agent(api_spec)
