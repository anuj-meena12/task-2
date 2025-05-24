
def check_even_odd():
    try:
        num = int(input("Enter an integer: "))
        if num % 2 == 0:
            print(f"{num} is Even.")
        else:
            print(f"{num} is Odd.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    check_even_odd()
