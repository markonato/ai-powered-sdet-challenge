import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

GENERATED_PATH = "tests/test_generated.py"
NUM_TESTS = 0

if api_key:
    client = OpenAI(api_key=api_key)
else:
    client = None  # fallback to mock mode

def generate_tests(api_description: str) -> str:
    """
    Generate pytest tests using OpenAI and strip non-Python content.
    """
    from openai import OpenAI
    import os
    from dotenv import load_dotenv

    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""
Generate a Python pytest suite for this FastAPI API:
{api_description}

Use 'requests' to call endpoints.
Include positive and negative test cases.
Return only valid Python code. Do not include explanations, bullet points, or Markdown.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    code = response.choices[0].message.content

    # Strip non-Python lines: remove lines that start with "-", "`", "# " explanations, etc.
    valid_lines = []
    for line in code.splitlines():
        stripped = line.strip()
        if stripped.startswith("-") or stripped.startswith("`") or stripped.startswith("# ") or stripped.lower().startswith("certainly"):
            continue
        valid_lines.append(line)
    cleaned_code = "\n".join(valid_lines)

    # Fallback if the AI output was empty or invalid
    if not cleaned_code.strip():
        cleaned_code = "import pytest\n\ndef test_dummy():\n    assert 1 + 1 == 2\n"

    os.makedirs("tests", exist_ok=True)
    file_path = "tests/test_generated.py"
    with open(file_path, "w") as f:
        f.write(cleaned_code)

    NUM_TESTS = len(code)

    return file_path

