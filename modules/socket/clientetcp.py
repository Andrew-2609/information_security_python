import socket
import sys


def main():
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("The connection failed! Error: ".format(e))
        sys.exit()
    else:
        print("Socket successfully created!")
        target_host = input("Type the host or ip to be connected to: ")
        target_port = int(input("Type the port to be connected to: "))

        try:
            connection.connect((target_host, target_port))
        except socket.error as e:
            print("It wasn't possible to connect to host: {} on port {}".format(target_host, target_port))
            print("Error: {}".format(e))
            sys.exit()
        else:
            print("TCP cliente successfully connected! Host: {} on port: {}".format(target_host, target_port))
            connection.shutdown(2)


if __name__ == '__main__':
    main()
