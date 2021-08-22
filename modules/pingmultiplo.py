import os

with open("hosts.txt") as file:
    dump = file.read()
    dump = dump.splitlines()

    print('#' * 60)
    for ip in dump:
        print('-' * 60)
        os.system("ping -c 2 {}".format(ip))
        print('-' * 60)
