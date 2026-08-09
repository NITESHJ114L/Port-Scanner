import socket

target = input("Enter target hostname or IP address: ")

print("\nPort Scanner")
print("------------")
print("Target:", target)

try:
    target_ip = socket.gethostbyname(target)
    print("IP Address:", target_ip)

    for port in range(1, 101):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print("Port", port, "is OPEN")

        sock.close()

    print("\nScan completed.")

except socket.gaierror:
    print("Invalid hostname or IP address.")