from src.keyboard import Keyboard

keyboard = Keyboard('Dark Project KD87A', 9600, 5)


def test_str():
    assert str(keyboard) == "Dark Project KD87A"


def test_change_lang():
    keyboard.change_lang()
    assert keyboard.language == 'RU'
