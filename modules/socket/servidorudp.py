import socket
import sys


def main():
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print("The connection failed! Error: {}".format(e))
        sys.exit()
    else:
        print("Socket successfully created!")
        host = "localhost"
        port = 5432

        connection.bind((host, port))

        message = "\nServer: Hello, Client!"

        while 1:
            data, address = connection.recvfrom(4096)

            if data:
                print("Server sending message...")
                connection.sendto(data + (message.encode()), address)


if __name__ == '__main__':
    main()
