#!/usr/bin/env python3
"""A simple terminal game: Guess the Number."""

from __future__ import annotations

import random


def choose_difficulty() -> tuple[int, int]:
    """Return (max_number, attempts) based on difficulty selection."""
    while True:
        print("\nChoose difficulty:")
        print("1) Easy   (1-20, 8 attempts)")
        print("2) Medium (1-50, 7 attempts)")
        print("3) Hard   (1-100, 6 attempts)")
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            return 20, 8
        if choice == "2":
            return 50, 7
        if choice == "3":
            return 100, 6

        print("Invalid choice. Please try again.")


def get_guess(min_value: int, max_value: int) -> int:
    """Prompt until a valid integer guess is given."""
    while True:
        raw = input(f"Enter your guess ({min_value}-{max_value}): ").strip()
        if not raw.isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(raw)
        if min_value <= guess <= max_value:
            return guess

        print(f"Your guess must be between {min_value} and {max_value}.")


def play_round() -> bool:
    """Play one round. Return True if the player wants another round."""
    max_number, attempts = choose_difficulty()
    secret = random.randint(1, max_number)
    remaining = attempts

    print(f"\nI've picked a number between 1 and {max_number}.")
    print(f"You have {attempts} attempts. Good luck!")

    while remaining > 0:
        guess = get_guess(1, max_number)
        remaining -= 1

        if guess == secret:
            print(f"🎉 Correct! You guessed it with {remaining} attempts left.")
            break

        if guess < secret:
            print("Too low!")
        else:
            print("Too high!")

        if remaining > 0:
            print(f"Attempts remaining: {remaining}")
    else:
        print(f"💥 Out of attempts. The number was {secret}.")

    while True:
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again in {"y", "yes"}:
            return True
        if again in {"n", "no"}:
            return False
        print("Please enter 'y' or 'n'.")


def main() -> None:
    print("=== Guess the Number ===")
    while play_round():
        pass
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
