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

```bash
1. Clone the repo

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

Results are saved to test/result.json; previous results are cleared automatically.


🔧 Customization

Modify api/models.py to add new fields or business rules.

Update agent/test_generator.py to control AI prompt or test style.

Configure test execution parameters in agent/test_executor.py.


💡 Future Improvements

Parallel test execution for faster feedback.

Support for multiple API versions.

Richer AI insights with code suggestions for failures.

Integration with CI/CD pipelines.

Allow mock mode to run the demo without using real OpenAI API credits.
```

---


---

# 🧠 AI Insight example

## Test Quality Analysis Report

### 1. Overall Test Quality
- **Total Tests:** 6
- **Passed:** 5
- **Failed:** 1
- **Errors:** 0

The overall test quality is high, with a pass rate of approximately **83.33%**. However, the single failure indicates a potential issue in the API or the test logic that requires attention.

---

### 2. Common Failure Patterns or Potential Causes
- **Failure Details:**
  - The test `test_update_task` failed due to an assertion error where the expected status code was `404`, but the actual response was `422`.
  - **Potential Causes:**
    - The API might be returning a `422 Unprocessable Entity` status code due to invalid input or request formatting.
    - The test might be incorrectly assuming that a non-existent task ID should return a `404 Not Found`, while the API could be validating the input and returning a `422` instead.

---

### 3. Suggestions for Improvements
- **Test Coverage:**
  - **Add Tests for Edge Cases:** Include tests that cover scenarios where invalid data is sent to the API, such as missing required fields or incorrect data types.
  - **Verify API Responses:** Ensure that the API responses are validated not only for status codes but also for response bodies, especially for error messages.
  
- **API Robustness:**
  - **Error Handling:** Improve error handling in the API to provide more informative error messages for different failure scenarios.
  - **Documentation:** Ensure that the API documentation clearly states the expected responses for various scenarios, including error codes.

---

### 4. Response Times and Optimizations
- **Setup Duration:** 0.000065 seconds (passed)
- **Call Duration:** 0.006891 seconds (failed)
- **Teardown Duration:** 0.000130 seconds (passed)

### Suggestions for Optimizations:
- **Reduce Call Duration:**
  - Investigate the performance of the API endpoint being tested. If the call duration is consistently high, consider optimizing the backend logic or database queries.
  - Implement caching mechanisms for frequently accessed data to reduce response times.

---

### 5. Categorization of Different Types of Failures
- **Assertion Failures:** 
  - The current failure is categorized as an assertion failure due to mismatched expected and actual values.
  
- **Setup/Teardown Failures:** 
  - No failures were reported in setup or teardown phases, indicating that the test environment is stable.

---

### 6. Executive Summary
The test suite demonstrates a strong overall quality with a high pass rate. However, the single failure in the `test_update_task` highlights a potential issue with the API's response to invalid task IDs. To enhance test coverage and API robustness, it is recommended to include additional tests for edge cases and improve error handling in the API. Furthermore, optimizing response times for API calls could lead to better performance and user experience.

---

### 📊 Summary
- **Total Tests:** 6
- **Passed:** 5
- **Failed:** 1
- **Response Time:** 0.006891 seconds (failed)
- **Improvement Areas:** Test Coverage, API Robustness, Performance Optimization

By addressing the identified issues and implementing the suggested improvements, the quality and reliability of the testing process can be significantly enhanced.