import random

# ---------------------------------------------( 1 == rock ) ( 2 == paper ) ( 3 == scissors ) ---------------------------------------------------------------------------------------

# if true then something is wrong
def user_input_length_handling(user):
    if user > 3 or user < 1:
        return True
    return False

# start the game
def play_game():
    user_score, ai_score = 0, 0
    while True:
        try:
            user_choice = int(input("(3.scissors)\n(2.paper)\n(1.rock)\npick: "))
        except:    
            print("\ntype a single integer please!\n")
            continue
        # make sure we get 1, 2 or 3
        if user_input_length_handling(user_choice):
            print("\nselect an option with a single integer 1-3\n")
            continue

        # lets check who won
        ai_choice = random.randint(1, 3)
        if user_choice == 1:
            if ai_choice == 1:
                print("\nai also chose rock, draw")
            elif ai_choice == 2:
                print("\nai chose paper, you lost")
                ai_score += 1
            elif ai_choice == 3:
                print("\nai chose scissors, you won")
                user_score += 1
        elif user_choice == 2:
            if ai_choice == 1:
                print("\nai chose rock, you win")
                user_score += 1
            elif ai_choice == 2:
                print("\nai also chose paper, draw")
            elif ai_choice == 3:
                print("\nai chose scissors, you lost")
                ai_score += 1
        else:
            if ai_choice == 1:
                print("\nai chose rock, you lost")
                ai_score += 1
            elif ai_choice == 2:
                print("\nai chose paper, you win")
                user_score += 1
            elif ai_choice == 3:
                print("\nai also chose scissors, draw")

        # show score
        print(f"(your score: {user_score}) (ai score: {ai_score})\n")

# main starts the function that starts the game
def main():
    play_game()

# run main
if __name__ == "__main__":
    main()