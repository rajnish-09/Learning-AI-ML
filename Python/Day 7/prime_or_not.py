# Program to check if the entered number is prime or not using function

def is_prime(number):
    if(number < 2):
        print(f"{number} is neither prime nor composite.")
        return
    else:
        for i in range(2,number):
            if number%i == 0:
                print(f"{number} is not a prime number.")
                return
        print(f"{number} is a prime number.")
        return

num = int(input("Enter a number: "))
is_prime(num)

