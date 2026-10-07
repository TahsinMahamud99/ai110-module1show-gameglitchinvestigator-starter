from logic_utils import check_guess, get_range_for_difficulty

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

def test_regression_high_guess_vs_46():
    # Bug: guessing 50 against secret 46 used to say "Go HIGHER"
    assert check_guess(50, 46) == "Too High"

def test_regression_low_guess_vs_47():
    # Bug: guessing 1 against secret 47 used to say "Go LOWER"
    assert check_guess(1, 47) == "Too Low"

def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)

def test_hint_direction_is_consistent_for_every_guess():
    # Bug: hints were reversed, and flipped on even attempts when the secret
    # was compared as a string. Int vs int must always give the right outcome.
    secret = 47
    for guess in range(1, 101):
        expected = "Win" if guess == secret else ("Too High" if guess > secret else "Too Low")
        assert check_guess(guess, secret) == expected
