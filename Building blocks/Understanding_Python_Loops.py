# 1. Write a program that uses a for loop to print the numbers 1 to 10
for i in range(1,11):
    print(i)


# 2. Write a program that uses a while loop to print the even numbers between 1 and 20
i = 0
while i < 20:
    i += 1
    print(i)


# 3. Write a program that uses a for loop to calculate the sum of the numbers 1 -10
sum = 0
for i in range(1,11):
    sum += i
    print(sum)


# 4. Write a program that uses a while loop to calulate the factorial of the number entered by the user
num = int(input("Enter the number: "))
b= num
factorial = 1
while num>0:
    factorial *= num
    num -=1
print(f"{b} factorial ({b}!) is {factorial}!")  


# 5. Write a program that uses a for loop to print the multiplication table of anumber entered by the user


# 6. Write a program that uses a while loop to find the largest number in a list entered by the user.

# 7. Write a program that uses a for loop to print the Fibonacci sequence up to a number entered by the user.
user_limit = int(input("Enter a number, upper limit of sequence: "))
sequence = 0
while num < user_limit:
    sequence += num
    print(sequence)
    
# 8. Write a program that uses a while loop to find the GCD (greatest common divisor) of two numbers entered by the user.

# 9. Write a program that uses a for loop to print the ASCII values of the letters A to Z.

# 10.Write a program that uses a while loop to print the prime numbers between 1 and 50.