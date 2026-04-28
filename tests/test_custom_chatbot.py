# run using python3 -m pytest -s -v -k custom_chatbot.py

import importlib.util
import os
import pytest

name = "dr. chris brown"
favorite_class = "cs5704"

# Helper to load student_code module
def load_student_code():
    path = os.path.join('problems', 'custom_chatbot', 'student_code.py')
    spec = importlib.util.spec_from_file_location('student_code', path)
    student_code = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(student_code)
    return student_code

# Parametrize test cases
@pytest.mark.parametrize("prompt, expected", [
    ("What is the professsors name?", name),
    ("What is the classes name?", favorite_class),
])
def test_student_answers(prompt, expected):
    student_code = load_student_code()
    result = student_code.ask_ollama(prompt)
    assert isinstance(result, str)
    assert expected.lower() in result.lower()

def test_output_answers():
    student_code = load_student_code()
    result = student_code.ask_ollama("What are the four chapter Titles?")
    assert isinstance(result, str)
    print(result)
    assert "software" in result.lower()
    assert "process" in result.lower()

    result = student_code.ask_ollama("which phase focuses on creating a working prototype of a software system to evaluate its feasibility and identify requirements before moving on to more complex stages like design, development, testing, or maintenance?")
    assert isinstance(result, str)
    print(result)
    assert "design" in result.lower()


    