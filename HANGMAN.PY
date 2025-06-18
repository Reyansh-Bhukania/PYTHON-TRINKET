import random
def hangman():
    """This function helps make the game called Hangman"""
    words=["Magnificent","Rocked","Mouthwatering","Motivate","Doomsday","Cooked","Ate"]
    word_to_guess=random.choice(words)
    guessed_word=["_"]*len(word_to_guess)