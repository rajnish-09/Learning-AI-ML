# A secret number is saved by default. User input numbers until they found secret number is found

def validate_number(number):
    secret_number = 30
    if number > secret_number:
        print("Too high")
        return False
    elif number < secret_number:
        print("Too low")
        return False
    elif number == secret_number:
        print("Correct. You won!!")
        return True


while True:
    user_input = int(input("Enter a number: "))
    if validate_number(user_input):
        break
