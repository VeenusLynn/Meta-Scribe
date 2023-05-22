import dotenv
import os


from utils import * 


dotenv.load_dotenv()

# Get API key from .env file
API_KEY = os.getenv("API_KEY")



#######################
VERSION = get_version()#
########################


def main():

    # Prompt the user for their choice
    print("Choose an option:")
    print("1. See current champion rotation")
    print("2. Get information about a specific champion")
    print("3. Get information about a specific item")
    print("4. Get information about a specific rune")
    print("5. Get information about a specific summoner spell")
    print("6. Get a champion's splash art")
    print("7. Get a champion's skin splash art")
    print("8. Get a champion's current stats")
    print("9. Get a champion's counters")
    print("10. Get a champion's recommended runes")
    print("11. Get a champion's recommended spells")
    print("12. Get a champion's recommended build")
    print("13. Get a champion's recommended skill order")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Get champion rotation
        print_champion_rotation()

    elif choice == "2":
        # Prompt the user for a champion name
        champion_name = input("Enter a champion name: ")
        print_champion_info_by_name(champion_name)

    elif choice == "3":
        item_name = input("Enter an item name: ")
        print_item_info_by_name(item_name)
        

    elif choice == "4":
        rune_name = input("Enter a rune name: ")
        print_rune_info_by_name(rune_name)
        

    elif choice == "5":
        spell_name = input("Enter a summoner spell name: ")
        print_summoner_spell_info_by_name(spell_name)


    elif choice == "6":
        champion_name = input("Enter a champion name: ")
        print_champion_splash_art(champion_name)


    elif choice == "7":
        champion_name = input("Enter a champion name: ")
        skin_number = input("Enter a skin number: ")
        print_champion_skin_splash_art(champion_name, skin_number)


    elif choice == "8":
        champion_name = input("Enter a champion name: ")
        print_champion_tier(champion_name)
        print_champion_winrate(champion_name)
        print_champion_pickrate(champion_name)
        print_champion_banrate(champion_name)

    elif choice == "9":
        champion_name = input("Enter a champion name: ")
        print_champion_counters(champion_name)

    elif choice == "10":
        champion_name = input("Enter a champion name: ")
        print_champion_recommended_runes(champion_name)

    elif choice == "11":
        champion_name = input("Enter a champion name: ")
        print_champion_recommended_spells(champion_name)

    elif choice == "12":
        champion_name = input("Enter a champion name: ")
        print_champion_recommended_build(champion_name)


    elif choice == "13":
        champion_name = input("Enter a champion name: ")
        print_champion_skill_order(champion_name)

    else:
        print("Invalid choice.")


if __name__ == '__main__':
    main()