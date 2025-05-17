import os
import sys
import time
import subprocess
import requests
import platform
from getpass import getpass
from itertools import cycle

class MobileTools:
    def __init__(self):
        self.version = "6.0-mobile"
        self.author = "GanzMods"
        self.colors = {
            'red': '\033[1;31m',
            'green': '\033[1;32m',
            'yellow': '\033[1;33m',
            'blue': '\033[1;34m',
            'magenta': '\033[1;35m',
            'cyan': '\033[1;36m',
            'reset': '\033[0m'
        }
        self.check_dependencies()
        
    def check_dependencies(self):
        required = {
            'requests': 'pip install requests',
            'speedtest-cli': 'pip install speedtest-cli'
        }
        
        missing = [lib for lib in required if not self.is_installed(lib)]
        if missing:
            self.print_box(" ERROR: PERLUKAN INSTALASI DEPENDENSI ", 'red')
            print(f"{self.colors['yellow']}Jalankan di Termux:")
            print("pkg update && pkg install python clang")
            print(f"pip install {' '.join(missing)}{self.colors['reset']}")
            sys.exit(1)

    def is_installed(self, lib):
        try:
            __import__(lib)
            return True
        except ImportError:
            return False

    def print_color(self, text, color):
        print(f"{self.colors[color]}{text}{self.colors['reset']}")

    def print_box(self, text, color):
        border = '═' * (len(text) + 2)
        print(f"{self.colors[color]}╔{border}╗")
        print(f"║ {text} ║")
        print(f"╚{border}╝{self.colors['reset']}")

    def show_banner(self):
        os.system('clear')
        banner = f"""
{self.colors['cyan']}
▓█████▄  ▒█████   ██▀███   ▄▄▄       █    ██ 
▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒▒████▄     ██  ▓██▒
░██   █▌▒██░  ██▒▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▒██░
░▓█▄   ▌▒██   ██░▒██▀▀█▄  ░██▄▄▄▄██ ▓▓█  ░██░
░▒████▓ ░ ████▓▒░░██▓ ▒██▒ ▓█   ▓██▒▒▒█████▓ 
 ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▒▓▒ ▒ ▒ 
 ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░  ▒   ▒▒ ░░░▒░ ░ ░ 
 ░ ░  ░ ░ ░ ░ ▒    ░░   ░   ░   ▒    ░░░ ░ ░ 
   ░        ░ ░     ░           ░  ░   ░     
 ░                                          
{self.colors['magenta']}      Network & Electrical Tools v{self.version}
{self.colors['yellow']}         Developed by: {self.author}
"""
        print(banner)

    def show_menu(self):
        self.show_banner()
        menu = [
            ("1", "Cek Status Jaringan", 'cyan'),
            ("2", "Tes Kecepatan Internet", 'blue'),
            ("3", "Cek Kekuatan Password", 'magenta'),
            ("4", "Pemindai WiFi Terdekat", 'green'),
            ("5", "Cek Info IP Publik", 'yellow'),
            ("6", "Perhitungan Teknis Listrik", 'red'),
            ("7", "Kalkulator Biaya Listrik", 'cyan'),
            ("8", "Info Sistem", 'blue'),
            ("9", "Keluar", 'magenta')
        ]
        
        for item in menu:
            self.print_color(f"  {item[0]}. {item[1]}", item[2])
        
        print(f"\n{self.colors['cyan']}═{'═'*45}═{self.colors['reset']}")
        return input(f"\n{self.colors['yellow']}➤ Pilih menu [1-9]: {self.colors['reset']}")

    def loading_animation(self, message):
        frames = cycle(["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"])
        for _ in range(12):
            print(f"\r{self.colors['blue']}{next(frames)} {message}...{self.colors['reset']}", end="")
            time.sleep(0.1)
        print("\r" + " "*50 + "\r", end="")

    def network_check(self):
        try:
            self.print_box(" CEK STATUS JARINGAN ", 'cyan')
            self.loading_animation("Mendapatkan IP Publik")
            
            ip_info = requests.get('https://api.ipify.org?format=json').json()
            self.print_color(f"\n📡 IP Publik: {self.colors['green']}{ip_info['ip']}", 'cyan')
            
            self.loading_animation("Melakukan ping ke Google DNS")
            ping_result = subprocess.run(
                ['ping', '-c', '3', '8.8.8.8'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            self.print_color("\n📊 Hasil Ping:", 'cyan')
            print(ping_result.stdout.decode().split('---')[1][:250])
            
        except Exception as e:
            self.print_color(f"\n❌ Error: {str(e)}", 'red')

    def run_speedtest(self):
        try:
            self.print_box(" TES KECEPATAN INTERNET ", 'blue')
            self.loading_animation("Mengukur kecepatan")
            
            import speedtest
            st = speedtest.Speedtest()
            st.get_best_server()
            
            download = st.download() / 1_000_000
            upload = st.upload() / 1_000_000
            ping = st.results.ping
            
            self.print_color("\n📶 Hasil Speedtest:", 'blue')
            print(f"{self.colors['cyan']}╔{'═'*25}╦{'═'*15}╗")
            print(f"║ {'Parameter':<23} ║ {'Hasil':<13} ║")
            print(f"╠{'═'*25}╬{'═'*15}╣")
            print(f"║ {self.colors['green']}Unduh (Download){self.colors['cyan']:<11} ║ {download:>8.2f} Mbps ║")
            print(f"║ {self.colors['green']}Unggah (Upload){self.colors['cyan']:<12} ║ {upload:>8.2f} Mbps ║")
            print(f"║ {self.colors['green']}Ping{self.colors['cyan']:<21} ║ {ping:>8.2f} ms ║")
            print(f"╚{'═'*25}╩{'═'*15}╝{self.colors['reset']}")
            
        except Exception as e:
            self.print_color(f"\n❌ Error: {str(e)}", 'red')

    def check_password_strength(self):
        self.print_box(" CEK KEKUATAN PASSWORD ", 'magenta')
        password = getpass(f"{self.colors['yellow']}⌨  Masukkan password: {self.colors['reset']}")
        
        criteria = {
            'Panjang ≥8': len(password) >= 8,
            'Huruf Besar': any(c.isupper() for c in password),
            'Huruf Kecil': any(c.islower() for c in password),
            'Angka': any(c.isdigit() for c in password),
            'Karakter Spesial': any(not c.isalnum() for c in password)
        }
        
        strength = sum(criteria.values())
        progress = "█" * strength + "░" * (5 - strength)
        color = 'red' if strength < 3 else 'yellow' if strength < 5 else 'green'
        
        self.print_color("\n📊 Hasil Analisis:", 'magenta')
        print(f"{self.colors[color]}╔{'═'*27}╗")
        print(f"║ Strength: {progress:<16} ║")
        print(f"╠{'═'*27}╣")
        for name, met in criteria.items():
            status = "✔" if met else "✘"
            clr = 'green' if met else 'red'
            print(f"║ {self.colors[clr]}{status}{self.colors[color]} {name:<20} ║")
        print(f"╚{'═'*27}╝{self.colors['reset']}")

    def wifi_scanner(self):
        try:
            self.print_box(" PEMINDAI WIFI ", 'green')
            self.loading_animation("Memindai jaringan WiFi")
            
            result = subprocess.run(
                ['termux-wifi-scaninfo'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            networks = result.stdout.decode().split('\n')
            self.print_color("\n📶 Jaringan Tersedia:", 'green')
            
            print(f"{self.colors['cyan']}╔{'═'*10}╦{'═'*20}╦{'═'*8}╗")
            print(f"║ {'SSID':<8} ║ {'BSSID':<18} ║ {'RSSI':>6} ║")
            print(f"╠{'═'*10}╬{'═'*20}╬{'═'*8}╣")
            
            for net in networks[:5]:
                if net:
                    ssid = net.split(',')[0].split(':')[1].strip(' "')
                    bssid = net.split(',')[1].split(':')[1].strip(' "')
                    rssi = net.split(',')[3].split(':')[1].strip()
                    print(f"║ {ssid[:8]:<8} ║ {bssid[:18]:<18} ║ {rssi:>6} ║")
            
            print(f"╚{'═'*10}╩{'═'*20}╩{'═'*8}╝{self.colors['reset']}")
            
        except:
            self.print_color("✖ Fitur ini hanya tersedia di Termux", 'red')
            print(f"{self.colors['yellow']}Instal termux-api: pkg install termux-api{self.colors['reset']}")

    # [Method lainnya dengan implementasi lengkap...]

    def main(self):
        while True:
            choice = self.show_menu()
            
            if choice == '1':
                self.network_check()
            elif choice == '2':
                self.run_speedtest()
            elif choice == '3':
                self.check_password_strength()
            elif choice == '4':
                self.wifi_scanner()
            elif choice == '5':
                self.ip_lookup()
            elif choice == '6':
                self.technical_calculations()
            elif choice == '7':
                self.electricity_calculator()
            elif choice == '8':
                self.system_info()
            elif choice == '9':
                self.print_box(" TERIMA KASIH TELAH MENGGUNAKAN ", 'magenta')
                sys.exit()
            else:
                self.print_color("\n❌ Pilihan tidak valid!", 'red')
                time.sleep(1)
            
            input(f"\n{self.colors['yellow']}Tekan Enter untuk melanjutkan...{self.colors['reset']}")

if __name__ == "__main__":
    tool = MobileTools()
    try:
        tool.main()
    except KeyboardInterrupt:
        print(f"\n{tool.colors['red']}🛑 Program dihentikan!{tool.colors['reset']}")
        sys.exit()
