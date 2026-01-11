import random
print("Welcome to Hangman where you will have guess one letter at a time.")

word_list=["Programmer","Coder","Developer","Player","List","Game"]
random_word=random.choice(word_list)
letters=len(random_word)*["_"]
print("Word:"+" ".join(letters))

guess=input("Guess the letters in this word ")
if guess in random_word:
    print("Good guess, keep going!")

else:
    print("Incorrect guess, try harder!")
    

