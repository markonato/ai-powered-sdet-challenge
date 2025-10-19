import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_results(results_path: str) -> str:
    """Analyze pytest results with AI and summarize insights."""
    with open(results_path, "r") as f:
        data = json.load(f)

    summary = {
        "total": len(data.get("tests", [])),
        "passed": sum(1 for t in data["tests"] if t["outcome"] == "passed"),
        "failed": sum(1 for t in data["tests"] if t["outcome"] == "failed"),
        "errors": [t for t in data["tests"] if t["outcome"] == "failed"],
    }

    prompt = f"""
You are an expert QA analyst.
Here are the pytest results:
{json.dumps(summary, indent=2)}

Please:
1. Summarize the overall test quality.
2. Identify common failure patterns or potential causes.
3. Suggest improvements for test coverage or API robustness.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return response.choices[0].message.content.strip()
