import random

def choose_random_words():
    # making a list of words and randomly choosing one
    word_list = ['car', 'skate', 'shirt', 'pants', 'shoes', 'house', 'bike']
    random_word = random.choice(word_list)
    return random_word

def get_initial_health():
    current_health = 3
    return current_health
    
# The function below has parameter which will receive current_health later on
def decrement_health(current_health):
    return current_health - 1

print("1. Play\n2. Quit")
user_input = input("Select an option: ")

try:
    user_input_to_int = int(user_input)
    
    if user_input_to_int == 1:
        chosen_word = choose_random_words()
        
        # The random word is hidden according to its length
        # It replaces the letters with the "X" to hide
        hidden_word = ["x"] * len(chosen_word)

        player_health = get_initial_health()
        
        # Shows the letter of the user's guess on the hidden word and spaces it in between
        print(" ".join(hidden_word))
        
        # If the word was not found yet and the player didn't lose, it'll keep running
        while "x" in hidden_word and player_health > 0:
            user_guess = input("Enter a letter: ")

            if user_guess in chosen_word:
                print("Correct!")
                
                for i in range(len(chosen_word)):
                    if chosen_word[i] == user_guess:
                        hidden_word[i] = user_guess
                print(" ".join(hidden_word))
                
            else:
                print("Wrong!")
                player_health = decrement_health(player_health)
                print(f"You got {player_health} life(ves)!")
    
        if player_health > 0:
            print("You win!")
        else:
            print("Game over! The word was:", chosen_word)
        
    elif user_input_to_int == 2:
        print("Leaving...")
            
    else:
        print("Enter a valid option by providing its index!")
                
except ValueError:
    print("Enter a valid input!")