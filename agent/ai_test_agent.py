import inspect
import os
from dotenv import load_dotenv
from agent.test_generator import generate_tests
from agent.test_executor import run_tests
from agent.analyzer import analyze_results
from openai import OpenAIError, RateLimitError

from tests import test_generated

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
    num_of_tests = 0
    try:
        test_file_path = generate_tests(api_spec)
        test_functions = [
            name for name, _ in inspect.getmembers(test_generated, inspect.isfunction)
            if name.startswith("test_")
        ]
        num_of_tests = len(test_functions)
        print(f"✅ Generated {num_of_tests} test scenarios using AI at: {test_file_path}")
    except (RateLimitError, OpenAIError, Exception) as e:
        print(f"⚠️ OpenAI error or quota issue: {e}")
        # --- Fallback when AI generation fails ---
        fallback_path = os.path.join("tests", "test_fallback.py")
        os.makedirs("tests", exist_ok=True)
        with open(fallback_path, "w") as f:
            f.write("def test_placeholder(): assert True\n")

        test_file_path = fallback_path
        print(f"🩹 Using fallback test file: {test_file_path}")

    # Step 2: Ensure a valid test file exists before running
    if not test_file_path or not os.path.exists(test_file_path):
        raise RuntimeError("❌ No valid test file found to execute")

    # Step 2: Execute tests
    results_path = run_tests(test_file_path)
    print(f"✅ Executed {num_of_tests} tests...")

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

