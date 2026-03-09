from logic_utils import check_guess
from app import parse_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# Bug fix: invalid inputs must return ok=False so attempts are never incremented for bad guesses,
# preventing "Attempts left" from going negative (Brandon + Claude).
def test_invalid_guess_does_not_consume_attempt():
    # Empty string
    ok, val, err = parse_guess("")
    assert ok is False and val is None

    # None
    ok, val, err = parse_guess(None)
    assert ok is False and val is None

    # Non-numeric string
    ok, val, err = parse_guess("abc")
    assert ok is False and val is None


# Bug fix: difficulty selection was not changing the guess range shown on the page.
# get_range_for_difficulty was hardcoded to 1-100 in the UI and New Game button ignored difficulty.
def test_difficulty_range_changes_with_difficulty():
    easy_low, easy_high = get_range_for_difficulty("Easy")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")

    # Each difficulty must return a distinct high bound
    assert easy_high != normal_high
    assert hard_high != normal_high

    # Easy should be the smallest range (easiest to guess)
    assert easy_high < normal_high


def test_valid_guess_is_parsed_correctly():
    # A normal integer string must parse successfully
    ok, val, err = parse_guess("42")
    assert ok is True and val == 42 and err is None

    # A float string should be truncated to int
    ok, val, err = parse_guess("7.9")
    assert ok is True and val == 7 and err is None
