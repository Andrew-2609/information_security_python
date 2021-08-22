import os

print("#" * 60)

ip_or_host = input("Type the IP or host to be verified: ")
times = input("Type the number of times it'll ping: ")

print("-" * 60)
os.system("ping -c {} {}".format(times, ip_or_host))
print("-" * 60)
