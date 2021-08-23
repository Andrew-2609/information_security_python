import hashlib


def main():
    file_a = "text1.txt"
    file_b = "text2.txt"

    hash_one = hashlib.new("ripemd160")
    hash_two = hashlib.new("ripemd160")

    hash_one.update(open(file_a, "rb").read())
    hash_two.update(open(file_b, "rb").read())

    if hash_one.digest() != hash_two.digest():
        print(f"The file {file_a} is different from {file_b}")
    else:
        print(f"The file {file_a} is equal to {file_b}")


if __name__ == '__main__':
    main()
