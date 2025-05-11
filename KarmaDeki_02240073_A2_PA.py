import random
import KarmaDeki_02240073_A2_PB

def main():
        print("\nWELCOME to GAME MENU!")
        print("Choose a game you want to play:")
        print("1. Guess Number") 
        print("2. Rock Paper Scissors")
        print("3. Trivia")
        print("4. Pokemon Binder")
        print("5. Exit the game")

        choice = input("Enter your choice (1-4): ")
        return choice


class GuessNumberGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.guesses = 0 
        self.max_number = 100
        #self.max_attempt = 10

    def play(self):
        print("WELCOME to the number guessing game!")
        while True:
            guess = int(input("Please make your guess between 1 to 100: "))
            self.guesses += 1

            if guess < self.secret_number:
                print("Your guess is TOO LOW. Guess a bigger number than this.")
            elif guess > self.secret_number:
                print("Your guess is TOO HIGH. Guess a smaller number than this.")
            else:
                print(f"Fantastic! You guessed it in {self.guesses} tries.")
                self.calculate_score()
                break

    def calculate_score(self):
        score = max(0, self.max_number - self.guesses)
        print(f"Your score: {score}")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again == "yes":
            self.secret_number = random.randint(1, 100)
            self.guesses = 0
            self.play() 
        elif play_again == "no":
                 print("Thank you for playing!")
        else:   
                 print("Invalid input. Please enter 'yes' or 'no'.")
        return
            


class RockPaperScissorsGame:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.computer_score = 0

    def play(self):
        print("Make your CHOICE from ROCK, PAPER, SCISSORS or enter quit or exit to leave the game.")
        while True:
            user = input("Enter your choice: ").lower().strip()
            if user == "exit" or user == "quit":
                break
            if user not in self.choices:
                print("Invalid choice.Can yoy please enter a valid choice.")
                continue
            
            computer = random.choice(self.choices)
            print(f"Computer chose: {computer}")

            if user == computer:
                print("It's a tie! Try Again.")
            elif (user == "rock" and computer == "scissors") or \
                 (user == "paper" and computer == "rock") or \
                 (user == "scissors" and computer == "paper"):
                print("WOW! You nailed it!")
                self.user_score += 1
            else:
                print("Oops! You loss to computer. Try winning next time.")
                self.computer_score += 1
                
            print(f"Score: You {self.user_score} - {self.computer_score} Computer")

        print("See You in Next Game.")
        print(f"Final Score: You {self.user_score} - {self.computer_score} Computer")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again == "yes":
            self.user_score = 0
            self.computer_score = 0
            self.play()
        else :
            print("Thank you for playing!")
            return
            

class TriviaGame:
    def __init__(self):
        self.categories = ["bhutan", "funfact", "exit"]
        self.total_score = 0
        
    def play(self):
        print("Choose a category (Bhutan, FunFact) or 'exit' to quit.")
        while True:
            category = input("Which category do you want to try?: ").lower().strip()
            if category == "exit" or category == "quit":
                print("Thank you for trying out my quiz!")
                break
            if category not in self.categories:
                print("Invalid category. Choose from the given categories.")
                continue

            if category == "bhutan":
                print("A/ When was the Second prince of Bhutan born?")
                print("1. 2018", "2.2019", "3.2020", "4.2021")
                self.answer = "3"
                user_answer = input("Enter your option: ")
                if user_answer == self.answer:
                    print("Correct!")
                    self.total_score += 1
                else:   
                    print("NO! Second prince of Bhutan was born in 2020")

                print("B/ When was the royal wedding of bhutan?")
                print("1.October 13,2011" , "2.October 23,2012", "3.October 15,2013", "4.November 13,2014")
                self.answer = "1"
                user_answer = input("Enter your option: ")
                if user_answer == self.answer:
                    print("Correct!")
                    self.total_score += 1
                else:   
                    print("SORRY! Wrong answer. Royal wedding of Bhutan was on October 13,2011")
             

            elif category == "funfact":
                print("A/ What company was initially known as Blue Ribbon Sports?")
                print("1.Puma", "2.Nike", "3.Adidus", "4.Jordan")
                self.answer = "2"
                user_answer = input("Enter your option: ")
                if user_answer == self.answer:
                    print("Correct!")
                    self.total_score += 1
                else:  
                    print("Oops! Wrong choice. It's Nike")

                print("B/ What is What is the only planet in our solar system to rotate cockwise on its axis?")
                print("1.Earth", "2.Jupiter", "3.Mercury", "4.Venus")
                self.answer = "4"
                user_answer = input("Enter your option: ")
                if user_answer == self.answer:
                    print("WOW! You are brilliant!")
                    self.total_score += 1
                else:  
                    print("SORRY! It's Venus")
            print(f"Score: {self.total_score}")

        try_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if try_again == "yes":
            self.total_score = 0
            self.play()
        else:
            print("Thank you for playing!")
            return



if __name__ == "__main__":
    while True:
        choice = main()
        if choice == "1":
            game = GuessNumberGame()
            game.play()
        elif choice == "2":
            game = RockPaperScissorsGame()
            game.play()
        elif choice == "3":
            game = TriviaGame()
            game.play()
        elif choice == "4":
            binder = KarmaDeki_02240073_A2_PB.PokemonBinder()
            binder.main_menu()
        elif choice == "5":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

        continue_game = input("Do you want to continue playing? (yes/no): ").strip().lower()
        if continue_game == "yes":
            continue
        elif continue_game == "no":
            print("THANKYOU for trying out my GAMES!!")
            break



        