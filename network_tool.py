import os

def ping_test(host):
    print(f"Pinging {host}...")
    os.system(f"ping -c 4 {host}")

def main():
    print("Simple Network Troubleshooting Tool")
    host = input("Enter IP or website: ")
    ping_test(host)

if __name__ == "__main__":
    main()
