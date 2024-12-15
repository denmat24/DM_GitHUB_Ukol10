from typing import NoReturn

def fizzbuzz(n: int) -> NoReturn:
    """
    Prints Fizz, Buzz, or FizzBuzz for numbers from 1 to n based on divisibility.
    """
    for number in range(1, n + 1):
        output = ""
        if number % 3 == 0:
            output += "Fizz"
        if number % 5 == 0:
            output += "Buzz"
        print(output or number)

def main() -> NoReturn:
    """
    Main function to run the FizzBuzz game.
    """
    max_number = 30
    print("START FIZZBUZZ GAME")
    fizzbuzz(max_number)
    print("END FIZZBUZZ GAME")

if __name__ == "__main__":
    main()




