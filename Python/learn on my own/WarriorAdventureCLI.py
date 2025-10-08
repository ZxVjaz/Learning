# WarriorAdventureCLI.py
import random
import os  # ⭐ IMPORT INI

def clear_screen():
    os.system('cls')  # ⭐ FUNGSI CLEAR SCREEN

# Player stats
player = {
    "health": 100,
    "max_health": 100,
    "damage": 10,
    "coins": 50
}

# Shop items
shop_items = {
    "1": {"name": "Health Potion", "price": 20, "effect": "heal", "value": 30},
    "2": {"name": "Strength Potion", "price": 30, "effect": "damage", "value": 5},
    "3": {"name": "Max Health Upgrade", "price": 50, "effect": "max_health", "value": 20}
}

# Enemies
enemies = [
    {"name": "Goblin", "health": 50, "damage": 8, "coins": 10, "difficulty": "easy"},
    {"name": "Orc", "health": 80, "damage": 12, "coins": 20, "difficulty": "medium"},
    {"name": "Troll", "health": 120, "damage": 15, "coins": 30, "difficulty": "hard"},
    {"name": "Dragon", "health": 200, "damage": 25, "coins": 50, "difficulty": "boss"}
]

def show_stats():
    print(f"\n=== Player Stats ===")
    print(f"Health: {player['health']}/{player['max_health']}")
    print(f"Damage: {player['damage']}")
    print(f"Coins: {player['coins']}")
    print("=" * 18)

def shop():
    while True:
        clear_screen()  # ⭐ CLEAR SCREEN DI AWAL SHOP
        print('=' * 40)
        print(' ' * 15 + 'SHOP')
        print('=' * 40)
        print(f"Your coins: {player['coins']}")
        print("Available items:")
        
        for key, item in shop_items.items():
            print(f"{key}. {item['name']} - {item['price']} coins")
            if item['effect'] == 'heal':
                print(f"   Effect: Restores {item['value']} health")
            elif item['effect'] == 'damage':
                print(f"   Effect: Permanently increases damage by {item['value']}")
            elif item['effect'] == 'max_health':
                print(f"   Effect: Permanently increases max health by {item['value']}")
        
        print("4. Back to Main Menu")
        
        choice = input('\nEnter your choice (1-4): ')
        
        if choice == '4':
            break
        elif choice in shop_items:
            item = shop_items[choice]
            if player['coins'] >= item['price']:
                player['coins'] -= item['price']
                
                if item['effect'] == 'heal':
                    player['health'] = min(player['max_health'], player['health'] + item['value'])
                    print(f"\nYou used {item['name']} and restored {item['value']} health!")
                elif item['effect'] == 'damage':
                    player['damage'] += item['value']
                    print(f"\nYou used {item['name']} and permanently increased your damage by {item['value']}!")
                elif item['effect'] == 'max_health':
                    player['max_health'] += item['value']
                    player['health'] += item['value']
                    print(f"\nYou used {item['name']} and permanently increased your max health by {item['value']}!")
                
                input("\nPress Enter to continue...")  # ⭐ TUNGGU USER TEKAN ENTER
                show_stats()
            else:
                print("\nNot enough coins!")
                input("Press Enter to continue...")
        else:
            print("\nInvalid choice. Please enter a number between 1-4.")
            input("Press Enter to continue...")

def rock_paper_scissors_battle(enemy):
    choices = ['rock', 'paper', 'scissors']
    
    while enemy['health'] > 0 and player['health'] > 0:
        clear_screen()  # ⭐ CLEAR SCREEN SETIAP ROUND BATTLE
        print(f"\nA wild {enemy['name']} appears!")
        print(f"Enemy Health: {enemy['health']}, Enemy Damage: {enemy['damage']}")
        print(f"Your Health: {player['health']}/{player['max_health']}")
        
        # Player choice
        player_choice = input("\nChoose (rock/paper/scissors): ").lower()
        while player_choice not in choices:
            print("Invalid choice! Choose rock, paper, or scissors.")
            player_choice = input("Choose (rock/paper/scissors): ").lower()
        
        # Enemy choice
        enemy_choice = random.choice(choices)
        print(f"Enemy chose: {enemy_choice}")
        
        # Determine winner
        if player_choice == enemy_choice:
            print("It's a tie! No damage dealt.")
        elif (player_choice == 'rock' and enemy_choice == 'scissors') or \
             (player_choice == 'paper' and enemy_choice == 'rock') or \
             (player_choice == 'scissors' and enemy_choice == 'paper'):
            # Player wins round
            damage_dealt = player['damage']
            enemy['health'] -= damage_dealt
            print(f"You win this round! You deal {damage_dealt} damage to {enemy['name']}!")
        else:
            # Enemy wins round
            damage_taken = enemy['damage']
            player['health'] -= damage_taken
            print(f"You lose this round! {enemy['name']} deals {damage_taken} damage to you!")
        
        input("\nPress Enter to continue...")  # ⭐ TUNGGU SEBELUM NEXT ROUND
        
        # Check if battle is over
        if enemy['health'] <= 0:
            clear_screen()
            print(f"\nYou defeated the {enemy['name']}!")
            player['coins'] += enemy['coins']
            print(f"You earned {enemy['coins']} coins!")
            input("\nPress Enter to continue...")
            return True
        elif player['health'] <= 0:
            clear_screen()
            print("\nYou have been defeated!")
            input("\nPress Enter to continue...")
            return False
    
    return False

def start_game():
    clear_screen()  # ⭐ CLEAR SCREEN DI AWAL GAME
    print('=' * 40)
    print(' ' * 10 + 'STARTING GAME')
    print('=' * 40)
    
    # Reset player health at start of new game (but keep upgrades)
    player['health'] = player['max_health']
    
    # Enemy progression based on difficulty
    difficulty_levels = ['easy', 'medium', 'hard', 'boss']
    
    for level in difficulty_levels:
        # Select random enemy of current difficulty
        available_enemies = [e for e in enemies if e['difficulty'] == level]
        enemy = random.choice(available_enemies).copy()
        
        clear_screen()
        print(f"\n=== {level.upper()} LEVEL ===")
        
        if rock_paper_scissors_battle(enemy):
            if level == 'boss':
                clear_screen()
                print("\n🎉 CONGRATULATIONS! YOU BEAT THE GAME! 🎉")
                print("You are the true Warrior Adventure champion!")
                input("\nPress Enter to return to main menu...")
                break
            
            # Heal player between battles (50% of max health)
            heal_amount = player['max_health'] // 2
            player['health'] = min(player['max_health'], player['health'] + heal_amount)
            clear_screen()
            print(f"\nYou rest and recover {heal_amount} health before the next battle.")
            show_stats()
            
            continue_game = input("\nContinue to next level? (y/n): ").lower()
            if continue_game != 'y':
                print("Returning to main menu...")
                break
        else:
            print("Game Over! Returning to main menu...")
            # Reset player health after defeat
            player['health'] = player['max_health']
            input("\nPress Enter to continue...")
            break

def main():
    while True:
        clear_screen()  # ⭐ CLEAR SCREEN DI AWAL MENU
        print('=' * 40)
        print(' ' * 10 + 'Warrior Adventure')
        print('=' * 40)
        print('Welcome to the Warrior Adventure game!')
        
        show_stats()
        print('\nMenu:')
        print('1. Start Game')
        print('2. Shop')
        print('3. Quit')
    
        # Get user input and handle choices
        choice = input('\nEnter your choice (1-3): ')
        if choice == '1':
            start_game()
        elif choice == '2':
            shop()
        elif choice == '3':
            clear_screen()
            print('Quitting the game. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 3.')
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()