import string
import secrets

from enum import Enum


# Define the set of characters to be used in the password, three strings means three modes.


class CharcterSet(Enum):
    ONLYNUMBER = string.digits
    NOPUNCTUATION = string.ascii_letters + string.digits
    ALLCHARCTER = string.ascii_letters + string.digits + string.punctuation


# Define a list of CharcterSet , in order to quickly transfer mode code to corresponding character set.

CharcterSetList = [
    CharcterSet.ALLCHARCTER,
    CharcterSet.ONLYNUMBER,
    CharcterSet.NOPUNCTUATION,
]

# Define Prompt Enum class , in order to amend prompts more easily .


class Prompt(Enum):
    GetPasswordInt = "How many passwords do you want to generate? "
    GetPasswordLength = "Enter the length of the password(s): "
    GetGenerationMode = "Choose password generation mode: (1) Only Number (2) Don't use punctuation (0) All ascii character "
    ValueErrorOccured = "Please enter a valid integer."
    PasswordGenerated = "Generated passwords:"


def generate_password(length: int, generation_mode_code: int = 0) -> str:
    """
    generate_password

    Generate a random password of the specified length by the specified mode.

    Args:
        length (int): specify the length of password.
        generation_mode_code (int): specify the generation mode of password: (1) Only Number (2) Don't use punctuation (0/default) All ascii character.

    Returns:
        str: a password string
    """
    password = "".join(
        secrets.choice(CharcterSetList[generation_mode_code].value)
        for i in range(length)
    )
    return password


def main():
    # Prompt the user for the number of passwords to generate and their length
    while True:
        try:
            num_pass = int(input(Prompt.GetPasswordInt.value))
            password_length = int(input(Prompt.GetPasswordLength.value))
            generation_mode_code = int(input(Prompt.GetGenerationMode.value))
            break
        except ValueError:
            print(Prompt.ValueErrorOccured.value)
            continue
    # Generate the specified number of passwords and print them to the console
    print(Prompt.PasswordGenerated.value)
    for i in range(num_pass):
        password = generate_password(password_length, generation_mode_code)
        print(f"{i+1}. {password}")


if __name__ == "__main__":
    main()
