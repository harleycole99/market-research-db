import pytest
from main import clean_name


def test_clean_name_removes_whitespace():
    # Setup: A name with messy spaces
    messy_name = "  Testy  "

    # Action: Call the function we haven't written yet
    result = clean_name(messy_name)

    # Assert: Check if the result is what we expect
    assert result == "Testy"


def test_clean_name_only_accepts_alphabetic_characters():
    wrong_name = "Charl7"

    result = clean_name(wrong_name)

    assert result is None
