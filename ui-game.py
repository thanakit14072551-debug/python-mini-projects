games = ['The Legend of Zelda', 'Super Mario Bros', 'Minecraft', 'Fortnite']


def game_capitalize(game_name):
    return game_name.capitalize()

if __name__ == "__main__":
    print("===== My Game List =====")

    print('1. show games')
    print('2. add game')
    print('3. remove game')
    print('4. exit')

    while True:
        choice = input("Enter your choice: ")

        if choice == '1':
            print("My Games:")
            for i, game in enumerate(games, start=1):
               print(f"{i}. {game}")
        elif choice == '2':
            add_game = input('Enter the game name: ')
            add_game = game_capitalize(add_game)
            games.append(add_game)
        elif choice == '3':
            remove_game = input('Enter the game name to remove: ')
            remove_game = game_capitalize(remove_game)
            if remove_game in games:
                games.remove(remove_game)
                print(f"{remove_game} has been removed from the list.")
            else:
             print(f"{remove_game} is not in the list.")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")