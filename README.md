	# AI-Powered Test Agent for FastAPI

An intelligent agent that automatically generates, executes, and analyzes tests for a **FastAPI Task Management API** using AI.  
This project demonstrates **AI-driven testing**, **smart reporting**, and **quick demo scripts**.

---

## 🚀 Features

- **Smart Test Generation**
  - Generates both positive and negative test scenarios automatically.
  - Creates realistic test data based on your API schema.
- **Intelligent Test Execution**
  - Runs tests automatically with `pytest`.
  - Tracks execution time and test results.
- **AI-Powered Analysis**
  - Provides natural language insights from test results.
  - Detects patterns in failures and suggests improvements.
- **Quick Demo Script**
  - Fully automated demo showing test generation, execution, and AI insights.
- **Smart Reporting**
  - Generates concise summaries of tests executed and their outcomes.
---

## 🛠️ Tech Stack

- Python 3.14+
- [FastAPI](https://fastapi.tiangolo.com/)
- [pytest](https://docs.pytest.org/)
- [requests](https://docs.python-requests.org/)
- [OpenAI API](https://platform.openai.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---


---

## ⚡ Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/your-username/task_ai_tester.git
cd task_ai_tester

2. Create virtual environment

python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3. Install dependencies

pip install -r requirements.txt


4. Set OpenAI API key

Create a .env file in the project root:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx

5. Run FastAPI server

uvicorn api.app:app --reload


6. Run the AI Test Agent demo
python demo.py


📝 Notes

Tests are generated dynamically using AI; the number of scenarios may vary.

Results are saved to results/ folder; previous results are cleared automatically.

Mock mode allows you to run the demo without using real OpenAI API credits.



🔧 Customization

Modify api/models.py to add new fields or business rules.

Update agent/test_generator.py to control AI prompt or test style.

Configure test execution parameters in agent/test_executor.py.


💡 Future Improvements

Parallel test execution for faster feedback.

Support for multiple API versions.

Richer AI insights with code suggestions for failures.

Integration with CI/CD pipelines.
