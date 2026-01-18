import random
print("Welcome to Hangman where you will have guess one letter at a time.")
maximum_atempts=6
atempts=0

word_list=["Programmer","Coder","Developer","Player","List","Game"]
random_word=random.choice(word_list)
letters=len(random_word)*["_"]
print("Word:"+" ".join(letters))

while atempts<maximum_atempts and "_" in letters:

    guess=input("Guess the letters in this word ")
    if guess in random_word:
        print("Good guess, keep going!")
        for i in range(len(random_word)):
            if random_word[i]==guess:
                letters[i]=guess
        print("Word:"+" ".join(letters))

    else:
        atempts+=1
        print("Incorrect guess, try harder!")

if "_" not in letters:
    print("Congrats, You guessed the word")

else:
    print("Game over the original word was "+ random_word)
    

