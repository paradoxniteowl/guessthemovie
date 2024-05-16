from emoji import emojize
from random import choice

print("Welcome to guess the movie!\nYou will get a combination of emojis and will try to guess the name of the movie.\nYou have 3 lives. If you miss 3 questions, you lose.")
start = input("Press enter to start")
score = 0
lives = 3
national_treasure = emojize(":flag_united_states:""\n"":trophy:")
full_metal_jacket = emojize(":elevator:""\n"":building_construction:""\n"":coat:")
twelve_angry_men = emojize(":twelve_oclock:""\n"":enraged_face:""\n"":man:")
citizen_kane = emojize(":man:""\n"":flag_united_states:""\n"":white_cane:")
lord_of_the_rings = emojize(":crown:""\n"":ring:")
oppenheimer = emojize(":cowboy_hat_face:""\n"":bomb:")
the_thing = emojize(":alien:""\n"":red_question_mark:")
miracle_on_ice = emojize(":sparkles:""\n"":left_right_arrow:""\n"":ice:")
heavyweights = emojize(":boy:""\n"":hamburger:""\n"":tent:")
all_the_presidents_men = emojize(":man:""\n"":top_arrow:""\n"":flag_united_states:")

possible_questions = [national_treasure, full_metal_jacket, twelve_angry_men, citizen_kane, lord_of_the_rings, oppenheimer, the_thing, miracle_on_ice, heavyweights, all_the_presidents_men]

while True:
    question = choice(possible_questions)
    print(f"{question}\n")
    print("What is this movie?\n")
    answer = input(">> ")
    if question == possible_questions[0]:
        if answer.lower() == "national treasure":
            print("correct!")
            score += 1
        else:
            print("incorrect!")
            lives -= 1
    elif question == possible_questions[1]:
        if answer.lower() == "full metal jacket":
            print("correct!")
            score += 1
        else:
            print("incorrect!")
            lives -= 1
    elif question == possible_questions[2]:
        if answer.lower() == "12 angry men" or answer.lower() == "twelve angry men":
            print("correct!")
            score += 1
        else:
            print("incorrect!")
            lives -= 1
    elif question == possible_questions[3]:
        if answer.lower() == "citizen kane":
            print("correct!")
            score += 1
        else:
            print("incorrect!")
            lives -= 1
    elif question == possible_questions[4]:
        if answer.lower() == "lord of the rings":
            print("correct!")
            score += 1
        else:
            print("incorrect!")
            lives -= 1
    elif question == possible_questions[5]:
        if answer.lower() == "oppenheimer":
            print("correct!")
            score += 1
        else:
            print("incorrect!")
            lives -= 1
    elif question == possible_questions[6]:
        if answer.lower() == "the thing":
            print("correct!")
            score += 1
        else:
            print("incorrect!")
            lives -= 1
    elif question == possible_questions[7]:
        if answer.lower() == "miracle on ice":
            print("correct!")
            score += 1
        else:
            print("incorrect!")
            lives -= 1
    elif question == possible_questions[8]:
        if answer.lower() == "heavyweights":
            print("correct!")
            score += 1
        else:
            print("incorrect!")
            lives -= 1
    elif question == possible_questions[9]:
        if answer.lower() == "all the president's men":
            print("correct!")
            score += 1
        else:
            print("incorrect!")
            lives -= 1

    if lives <= 0 or score >= 10 or not possible_questions:
        break
    else:
        continue
