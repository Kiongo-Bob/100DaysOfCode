import random as rd
word_list = ['function', 'generates', 'word', 'specified', 'length','repeatedly', 'selecting','random', 'letter', 'from', 'letters', 'string', 'concatenating', 'result']
chosen_word = rd.choice(word_list)
print(chosen_word)
print(type(chosen_word))

#Generate as anay blanks as letters in random word
hidden_word = ""

for i in range(len(chosen_word)):
    hidden_word += '_'
print(hidden_word)
life = 4
#User guess a letter
#Check if letter in word
while True:
    guess_letter = input("Enter a letter: ").lower()
    if guess_letter in chosen_word:
        
        print(guess_letter)
    else:
        life -= 1