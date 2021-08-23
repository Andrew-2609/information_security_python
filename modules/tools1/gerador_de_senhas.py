import random
import string


def main():
    size = int(input("How many digits will your password have?\n"))
    chars = string.ascii_letters + string.digits + "!@#$%&*()-ç^{}[];:/<>|=+,."

    rnd = random.SystemRandom()

    print("\nPassword: ")
    print("".join(rnd.choice(chars) for i in range(size)))


if __name__ == '__main__':
    main()
