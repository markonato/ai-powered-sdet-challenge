import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
import pytest

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    client = OpenAI(api_key=api_key)
else:
    client = None

def run_tests(test_file: str) -> str:
    """
    Run pytest on the given test file and save JSON results.
    """
    os.makedirs("results", exist_ok=True)
    results_file = f"results/test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    pytest_args = [
        test_file,
        "--json-report",
        f"--json-report-file={results_file}",
        "-q"
    ]

    pytest.main(pytest_args)
    print(f"📄 Results saved at: {results_file}")
    return results_file

def analyze_results(results_path: str, mock=False) -> str:
    """
    Analyze pytest results using AI. If mock=True or API unavailable, return mock summary.
    """
    if mock or client is None:
        return "🤖 Mock analysis: All tests passed. No OpenAI analysis available."

    with open(results_path, "r") as f:
        data = json.load(f)

    summary = {
        "total": len(data.get("tests", [])),
        "passed": sum(1 for t in data["tests"] if t["outcome"] == "passed"),
        "failed": sum(1 for t in data["tests"] if t["outcome"] == "failed"),
        "errors": [t for t in data["tests"] if t["outcome"] == "failed"],
    }

    prompt = f"""
You are an expert QA analyst. Analyze the following pytest results:
{json.dumps(summary, indent=2)}

Summarize test quality, failure patterns, and suggest improvements.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content.strip()
