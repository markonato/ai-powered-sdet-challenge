import os
from agent.ai_test_agent import run_ai_test_agent
from agent.analyzer import analyze_results

RESULTS_DIR = "results"

def clear_results_folder():
    import shutil
    if os.path.exists(RESULTS_DIR):
        shutil.rmtree(RESULTS_DIR)
    os.makedirs(RESULTS_DIR, exist_ok=True)
    print(f"🗑 Cleared previous results in {RESULTS_DIR}/")

if __name__ == "__main__":
    print("🚀 Quick Demo: AI Test Agent Workflow")

    # Step 0: Clean old results
    clear_results_folder()

    # Step 1: Define a simple API spec or path to OpenAPI JSON
    api_spec = """
FastAPI Task Management API:

Endpoints:
POST /tasks - Create task (title, description, priority, due_date)
GET /tasks - List all tasks
GET /tasks/{id} - Get task by ID
PUT /tasks/{id} - Update task
DELETE /tasks/{id} - Delete task
PATCH /tasks/{id}/status - Mark task as completed/pending

Rules:
Priority: low, medium, high
Status: pending, completed
Due dates cannot be in the past
Title required (1-100 chars)
Description optional (max 500 chars)
"""

    # Step 2: Run AI agent to generate, execute, and analyze tests
    print("\n🧠 Running AI Test Agent...")
    run_ai_test_agent(api_spec)  # use mock=True to avoid quota issues

    # Step 3: Smart Reporting
    print("\n📝 Generating Smart Test Report...")
    report_summary = analyze_results(
        os.path.join(RESULTS_DIR, os.listdir(RESULTS_DIR)[0]),  # pick latest results JSON
        #mock=True  # Use mock to avoid AI calls if needed
    )

    # Step 4: Show report
    print("\n=== Smart Test Report ===")
    print(report_summary)

    print("\n🎉 Demo complete! Check 'results/' folder and AI insights above.")
