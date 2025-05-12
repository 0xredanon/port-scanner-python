import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port, banner=False, output_file=None):
    try:
        with socket.socket() as sock:
            sock.settimeout(1)
            sock.connect((target, port))
            result = f"[+] Port {port} is open"

            if banner:
                try:
                    sock.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
                    banner_data = sock.recv(1024).decode(errors='ignore').strip()
                    result += f" | Banner: {banner_data.splitlines()[0]}"
                except:
                    result += " | Banner: [Failed to grab]"

            print(result)
            if output_file:
                with open(output_file, "a") as f:
                    f.write(result + "\n")

    except:
        pass

def main():
    parser = argparse.ArgumentParser(description="Advanced Multithreaded Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP or Hostname")
    parser.add_argument("-p", "--port", required=True, help="Comma-separated list of ports")
    parser.add_argument("-th", "--threads", type=int, default=50, help="Number of threads (default=50)")
    parser.add_argument("-b", "--banner", action="store_true", help="Enable banner grabbing")
    parser.add_argument("-o", "--output", help="Output file to save results")

    args = parser.parse_args()

    target = args.target
    ports = [int(p.strip()) for p in args.port.split(",")]
    thread_count = args.threads

    print(f"[*] Scanning {target} using {thread_count} threads...")
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        for port in ports:
            executor.submit(scan_port, target, port, args.banner, args.output)

if __name__ == "__main__":
    main()