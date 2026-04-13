
import random

num = random.randint(1, 10)

wrong_count = 0

while wrong_count < 3:
    try:
        print("-------------")
        user_guess = int(input("Guess the number: "))
        if user_guess == num:
            print("***Correctly guessed***")
            break
        else:
            print("--Incorrect guess--")
            if user_guess > num:
                print("--Guess lower--")
            elif user_guess < num:
                print("--Guess higher--")
            wrong_count += 1
    except ValueError:
        print("Wrong input!!!")
        break
    except Exception as e:
        print(e)
        break

    
if wrong_count == 3:
    print("-------------")
    print("3 attempts used!!!")
    