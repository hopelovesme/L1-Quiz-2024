import random

print("+-=Math Quiz=-+")
print("Welcome to the Maths Quiz!")
name = input("What is your name? (optional)\n")

print(f"Hello {name}!")


# instructions
def instructions():
    while True:
        want_instructions = input(f"Would you like to read the instructions {name}? (Please enter yes or no)\n").lower()
        if want_instructions == "no" or want_instructions == "n":
            print("You chose no")
            input("-Press enter to start-")
            return

        elif want_instructions == "yes" or want_instructions == "y":
            print("You chose yes")
            print("Instructions:")
            print(
                "1) You will be asked to put in the amount of questions you would like to have in your math quiz. Please put in a reasonable whole number.\n",
                "2) In the Quiz there will be a variety of different basic math questions (either +, -, /, * )",
                "the symbols '/' means division.\n",
                "3) Once you've answered all of your questions you will be given a score out of 100% and you will be able to see what ",
                "questions you got correct or incorrect (You may go back through the quiz if you wish)\n",
                "GOOD LUCK ON YOUR QUIZ!!!!!")
            input("-Please press enter to start-\n")
            return

        else:
            print("Please choose a valid response (yes or no)")


instructions()

# question types
all_question_types = ["+", "-", "x", "/"]

score = 0
num1 = random.randrange(2, 20)
num2 = random.randrange(2, 20)
question_number = 0
question_count = 0
final_question_count = 0


def int_checker(question):
    while True:
        try:
            user_answer = float(input(question))
            return user_answer
        except:
            print("Please enter a valid integer")


# main
def one_question():
    global question_types, score, question_count
    question_types = random.choice(all_question_types)
    first_number = random.randrange(2, 20)
    second_number = random.randrange(2, 20)
    correct_answer = 0

    if question_types == "+":
        correct_answer = first_number + second_number
    elif question_types == "-":
        correct_answer = first_number - second_number
    elif question_types == "x":
        correct_answer = first_number * second_number
    elif question_types == "/":
        correct_answer = first_number / second_number
    correct_answer = round(correct_answer, 1)
    question = int_checker(
        "What is {} {} {}? (please round to one decimal place)\n".format(first_number, question_types, second_number))

    question = round(question, 1)
    if question == round(correct_answer, 1):
        print("Correct!")
        score += 1
        question_count += 1
    else:
        print(f"Incorrect :( ------- The correct answer was {correct_answer}")
        question_count += 1


round_count = int_checker("How many questions would you like?\n")

print("The amount of questions you chose is {}".format(round_count))

for round_number in range(int(round_count)):
    one_question()

percentage = round(score / question_count * 100, 1)


print("---------------------------")
print("---------RESULTS-----------")
print("---------------------------")

print("Your score is {}%".format(percentage))
print("Well done!!!")
print(f"You Got {score} / {round_count} correct!")
print("Thank you for playing!!!!!!!!!!")
