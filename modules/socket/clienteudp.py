import socket
import sys


def main():
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print("The connection failed! Error: {}".format(e))
        sys.exit()
    else:
        print("Socket Client successfully created!")
        host = "localhost"
        port = 5432
        message = input("Type your name: ")

        try:
            connection.sendto(message.encode(), (host, port))

            data, server = connection.recvfrom(4096)
            data = data.decode()

            print("\n" + ("-" * 60))

            print("Client: Hi, my name is {}. Nice to meet you, Server!\n{data}".format(message, data=data))
        finally:
            print("\nClient: Closing connection.")
            connection.close()


if __name__ == '__main__':
    main()
