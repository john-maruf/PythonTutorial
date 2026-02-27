def show_menu():
    print("\nMenu")
    print("1. Add a number")
    print("2. Show all numbers")
    print("3. Show sum")
    print("4. Exit")

numbers = []

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        num = int(input("Enter a number: "))
        numbers.append(num)
        print("Number added.")

    elif choice == "2":
        if len(numbers) == 0:
            print("No numbers yet.")
        else:
            print("Numbers:", numbers)

    elif choice == "3":
        total = 0
        for n in numbers:
            total += n
        print("Sum:", total)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
