import random as rd

geussed_int = rd.randint(1,101)

print(geussed_int)

user_guess = int(input("Guess a number between 1 and 100: "))

for i in range (3):
    if geussed_int != user_guess:
        miss_value = user_guess - geussed_int
        print(f"Try again, you missed by {miss_value}")
        user_guess = int(input("Guess a number between 1 and 100: "))

    else:
        print("Jin-yas!")
        break
