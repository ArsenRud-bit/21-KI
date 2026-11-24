"""Безпечне введення."""
from exceptions import QuitGame


def read_int(prompt, low, high):
    while True:
        try:
            value = int(input(prompt).strip())
            if not low <= value <= high:
                raise ValueError
            return value
        except ValueError:
            print(f"  ! Введіть ціле число від {low} до {high}.")
        except (EOFError, KeyboardInterrupt):
            raise QuitGame()