print("+-=Math Quiz=-+")
print("Welcome to the Maths Quiz!")
name = input("What what is your name? (optional). If you do not wish to put in your name  -Press Enter-.")

print(f"Hello {name}!")


def instructions():
    while True:
        want_instructions = input(f"Would you like to read the instructions {name}? (Please enter yes or no)").lower()
        if want_instructions == "no" or want_instructions == "n":
            print("You chose no")
            input("-Press enter to start-")
            againAndAgain()
            return

        elif want_instructions == "yes" or want_instructions == "y":
            print("You chose yes")
            print("Instructions:")
            print(
                "1) You will be asked to put in the amount of questions you would like to have in your math quiz. Please put in a reasonable whole number. ",
                "2) In the Quiz there will be a variety of different basic math questions (either +, -, /, * ), "
                "the symbols '/' means division and '*' means multiplication",
                "3) once you've answered all of your questions you will be given a score out of 100% and you will be able to see what "
                "questions you got correct or incorrect (You may go back through the quiz if you wish) ",
                "GOOD LUCK ON YOUR QUIZ!!!!!")
            input("-Please press enter to start-")
            againAndAgain()
            return

        else:
            print("Please choose a valid response (yes or no)")


def againAndAgain():
    print("Before you start, how many questions would you like to answer in your quiz?")
    numberOfProblems = input()
    numberOfProblems = int(numberOfProblems)

    if numberOfProblems > 20:
        print("Sorry, that is too many questions for this quiz :( please chose a number lower than 20 ")
        againAndAgain()
        return
    if numberOfProblems < 4:
        print("That is not enough questions! Please chose a number higher than 4!")
        return
    else:
        print(f"okay! {numberOfProblems} it is!")

    main()


import random

all_question_types = ["+", "-", "x", "/"]

score = 0
first_number = random.randrange(1, 20)
second_number = random.randrange(1, 20)
question_number = 0
question_count = 0
final_question_count = 0


def int_checker(question):
    while True:
        try:
            return int(input(question))
        except:
            print("Please enter a valid number")


def one_question():
    global question_types, score
    question_types = random.choice(all_question_types)
    first_number = random.randrange(1, 20)
    second_number = random.randrange(1, 20)
    correct_answer = 0.0

    if question_types == "+":
        correct_answer = first_number + second_number
    elif question_types == "-":
        correct_answer = first_number - second_number
    elif question_types == "*":
        correct_answer = first_number * second_number
    elif question_types == "/":
        correct_answer = first_number / second_number
    correct_answer = round(correct_answer, 1)
    question = "What is {} {} {}? (rounded to the first decimal place)\n".format(first_number, question_types,
                                                                                 second_number)
    user_answer = float(input(question))
    user_answer = round(user_answer, 1)
    if user_answer == round(correct_answer, 1):
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The correct answer was {correct_answer}")


def main():
    global question_number, question_count, final_question_count
    while True:
        game = input("Are you ready to play? (Y/N)\n").capitalize()
        if game == "Yes" or game == "Y":
            question_count = question_number + int_checker("How many questions do you want?\n")
            final_question_count += question_count
            print("Okay Then! Starting Quiz")
            break

        elif game == "No" or game == "N":
            print("Too Bad you playing")
        else:
            print("Please put in a valid answer")

    for question_number in range(question_count):
        print(f"Question {question_number + 1}")
        one_question()


print("---------------------------")
print("---------RESULTS-----------")
print("---------------------------")

print(f"you're score is {score}%")
print("Well done!!!")
print(f"You Got {score} / {final_question_count} correct!")
print("Thank you for playing!!!!!!!!!!")

print("~~~~~Math Quiz~~~~~")
username = input("Enter your name please\n").capitalize()
print("Welcome to the game {}".format(username))


