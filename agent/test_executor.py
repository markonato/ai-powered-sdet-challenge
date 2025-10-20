import json
import os
from typing import Any

import pytest
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    client = OpenAI(api_key=api_key)
else:
    client = None

def run_tests(test_file: str) -> dict[str, str | int | Any]:
    """
    Run pytest on the given test file and save JSON results.
    """
    results_file = f"tests/results.json"

    pytest_args = [
        test_file,
        "--json-report",
        f"--json-report-file={results_file}",
        "--disable-warnings",
        "-q"
    ]

    pytest.main(pytest_args)
    with open(results_file, "r") as f:
        report = json.load(f)

    summary = {
        "result_file": results_file,
        "num_generated_tests": int(report["summary"]["collected"]),
        "num_executed_tests": int(report["summary"]["total"]),
        "duration": report["duration"]
    }

    return summary
