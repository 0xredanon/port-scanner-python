import socket
import argparse

def scan_port(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((target, port))
        print(f"[+] Port {port} is open")
        sock.close()
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP or Hostname")
    parser.add_argument("-p", "--port", required=True, help="Comma-separated list of ports")
    args = parser.parse_args()

    target = args.target
    ports = [int(p.strip()) for p in args.port.split(",")]

    print(f"[*] Scanning {target}...")
    for port in ports:
        scan_port(target, port)

if __name__ == "__main__":
    main()