#program for multiple functions
def box(word):
    legenth = 4 + len(word)
    print("-" * legenth)
    print("| {} |".format(word))
    print("-" * legenth)

def display_lower_case(word):
    print(word.lower())

def upper_case(word):
    print(word.upper())

def inverted(word):
    mirrored = ""
    for letter in range(len(word)-1,-1,-1):
         print(word[letter], end="")
    print("\n")

def repetition(word):
    print("How many times should the word be displayed?")
    times = int(input())

    for repetition in range(0,times,1):
        if (repetition % 2 == 0):
            print(word.lower())
        else:
            print(word.upper())

def run():
    print("Choose a word")
    word = input()
    response = 0

    while (response != 6):
        print("What would you like to do with this word?")
        print("[1] Box")
        print("[2] Lower-case")
        print("[3] Upper-case")
        print("[4] Mirrored")
        print("[5] Repeated")
        print("[6] Exit")

        response = int(input()) 
 

        if (response == 1):
            box(word)
        elif (response == 2):
            display_lower_case(word)
        elif (response == 3):
            upper_case(word)
        elif (response == 4):
            inverted(word)
        elif (response == 5):
            repetition(word)
        elif (response == 6):
            break
        else:
            print("Not an option!") 

run()