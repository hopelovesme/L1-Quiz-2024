import random

# Main introduction for code
print("+-=Math Quiz=-+")
print("Welcome to the Maths Quiz!")
name = input("What is your name? (optional)\n")

# Input name
print(f"Hello {name}!")


# Not want instructions
def instructions():
    while True:
        want_instructions = input(f"Would you like to read the instructions {name}? (Please enter yes or no)\n").lower()
        if want_instructions == "no" or want_instructions == "n":
            print("You chose no")
            input("-Press enter to start-")
            return

# Want instructions 
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

# Global variables
score = 0
num1 = random.randrange(2, 20)
num2 = random.randrange(2, 20)
question_number = 0
question_count = 0
final_question_count = 0

# int_checker method
def int_checker(question):
    while True:
        try:
            user_answer = float(input(question))
            return user_answer
        except:
            print("Please enter a valid integer")


# one_question method
def one_question():
    global question_types, score, question_count
    question_types = random.choice(all_question_types)
    first_number = random.randrange(2, 20)
    second_number = random.randrange(2, 20)
    correct_answer = 0

    # Main
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

# Number of questions wanted
round_count = int_checker("How many questions would you like?\n")

print("The amount of questions you chose is {}".format(round_count))

for round_number in range(int(round_count)):
    one_question()

# Percentage variable for end of code summary
percentage = round(score / question_count * 100, 1)

# End results for code
print("---------------------------")
print("---------RESULTS-----------")
print("---------------------------")

# Percentage and score out of number of questions inputted
print("Your score is {}%".format(percentage))
print("Well done!!!")
print(f"You Got {score} / {round_count} correct!")
print("Thank you for playing!!!!!!!!!!")
