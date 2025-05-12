import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

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
    parser.add_argument("-th", "--threads", type=int, default=50, help="Number of threads (default=50)")
    args = parser.parse_args()

    target = args.target
    ports = [int(p.strip()) for p in args.port.split(",")]
    thread_count = args.threads

    print(f"[*] Scanning {target} using {thread_count} threads...")
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        for port in ports:
            executor.submit(scan_port, target, port)

if __name__ == "__main__":
    main()