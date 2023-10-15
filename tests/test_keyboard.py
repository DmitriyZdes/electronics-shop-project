from src.keyboard import Keyboard

kb = Keyboard("Клавиатура", 5000, 5)

assert repr(kb) == "Keyboard('Клавиатура', 5000, 5, 'EN')"

assert kb.language == "EN"
assert kb.change_lang() == "RU"
assert kb.change_lang() != "SLVK"
