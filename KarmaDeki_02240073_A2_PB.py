max_pokedex=1025
cards_per_page=64
grid_width=8

class PokemonBinder:
    def __init__(self):
        self.max_pokedex = 1025
        self.cards_per_page = 64
        self.grid_width = 8
        self.binder = {}
        self.added_cards = set()

    def calculate_position(self, pokedex_number):
        card_index = pokedex_number - 1
        page_number = card_index // 64 + 1
        position_in_page = card_index % 64
        row = position_in_page // 8 + 1
        column = position_in_page % 8 + 1
        return page_number, (row, column)
    

    def add_card(self):
        pokedex = input("HELLO, can you enter Pokedex number between 1-1025: ")
        if pokedex.isdigit():
            p_n = int(pokedex)          #p_n = pokedex number
            if 1 <= p_n <= self.max_pokedex:
                if p_n in self.added_cards:
                    page, pos = self.binder[p_n]
                    print(f"Page: {page}")
                    print(f"Position: {pos}")
                    print("Status: It already exists.")
                else:
                    page, pos = self.calculate_position(p_n)
                    self.binder[p_n] = (page, pos)
                    self.added_cards.add(p_n)
                    print(f"Page: {page}")
                    print(f"Position: {pos}")
                    print("Status: Newly added.")
            else:
                print("SORRY, invalid number. Can you please enter between 1 and 1025.")
        else:
            print("Please enter a valid number.")
            
        add_more_card = input("Do you want to add more cards? (yes/no): ").strip().lower()
        if add_more_card == "yes":
            self.add_card()
        elif add_more_card == "no":
            print("OK. Let's return to main menu.")
            self.main_menu()


    def reset_binder(self):
        w = input("Do you really want to reset (confirm or exit): ").lower()
        if w == "confirm":
            self.binder.clear()
            self.added_cards.clear()
            print("Binder has been reset.")
        else:
            print("Reset is cancelled.")
        
        
    def view_status(self):
        total = len(self.added_cards)
        percent = (total / self.max_pokedex) * 100
        print(f"Total cards: {total}")
        print(f"Completion: {round(percent, 2)}%")
        if total == self.max_pokedex:
            print("HURRY! You have caught them all!")


    def end_session(self):
        print(f"Session ended. Total cards: {len(self.added_cards)}")
        print("ThankYou!")
    

    def main_menu(self):
        while True:
            print("\n1. Add Pokemon Card")
            print("2. Reset Binder")
            print("3. View Collection Status")
            print("4. Exit Program")
            option = input("Choose an option (1-4): ")

            if option == '1':
                self.add_card()
            elif option == '2':
                self.reset_binder()
            elif option == '3':
                self.view_status()
            elif option == '4':
                self.end_session()
                break
            else:
                print("Invalid option. Please choose from 1 to 4.")
    
