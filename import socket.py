import socket
import threading

# Common ports and their services
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Alt"
}

# Scan a single port
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown Service")
            print(f"[+] Port {port} is OPEN ({service})")
        sock.close()
    except Exception as e:
        pass

# Main scanner
def main():
    print("🔎 Basic Port Scanner 🔎")
    target = input("Enter IP address or domain: ").strip()

    # Resolve domain name to IP if needed
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("❌ Invalid IP or domain.")
        return

    print(f"\nScanning {ip}...\n")

    threads = []
    for port in range(1, 1025):  # Scans ports 1–1024
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\n Scan complete.")

if __name__ == "__main__":
    main()
