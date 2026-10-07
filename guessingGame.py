import random
def guess(x):

 random_number=random.randint(1,x)
 guess=0
 while guess !=random_number:

     guess=int(input(f"guess number from 1 to {x}:"))
     if guess<random_number:
         print("you guessed the wrong number.too low")

     elif guess>random_number:
        print("you guessed the wrong number.too high")
     else:
         print("congrats!")
         print(f"you guessed the {random_number}")

def computer_guess(x):
    low=1
    high=x
    feedback= ''

    while feedback != 'c' :
        if low!=high:

            guess=random.randint(low,high)
        else:
            guess = low  # could also be high b/c low=high

        feedback=input(f"{guess} too high(H) , too low(L) or correct(c)??").lower()
        if feedback == 'h':
            high=guess-1
        elif feedback == 'l':
            low=guess+1
        else:
            print(f"you guessed the correct number{guess}.hurray!")



computer_guess(150)

