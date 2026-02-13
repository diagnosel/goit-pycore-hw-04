
def parse_input(user_input):
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        # тут буде обробка інших команд

if __name__ == "__main__":
    main()