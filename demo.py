from agent.ai_test_agent import run_ai_test_agent

if __name__ == "__main__":
    print("🚀 Quick Demo: AI Test Agent Workflow")

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
    print("\n🤖 AI Test Agent Starting...")
    run_ai_test_agent(api_spec)

    print("\n\n🎉 Demo completed! Check 'test/results.json' and AI insights above.")
