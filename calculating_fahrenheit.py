#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in <September> <2022>
# A program that calculates fahrenheit from celsius


def fahrenheit():
    # Calculates fahrenheit from celsius

    try:
        celsius_text = input("\nEnter a temperature in celsius: ")
        celsius_number = float(celsius_text)
        if celsius_number % 1 == 0:
            celsius_number = int(celsius_text)
        fahrenheit = celsius_number * (9 / 5) + 32
        if fahrenheit % 1 == 0:
            fahrenheit = int(fahrenheit)
        print("\n{0}°C = {1}°F.".format(celsius_number, fahrenheit))
    except ValueError:
        print("\nError: {} isn't a number.".format(celsius_text))
    finally:
        print("\nDone.")


def main():
    # Calls a function

    fahrenheit()


if __name__ == "__main__":
    main()
