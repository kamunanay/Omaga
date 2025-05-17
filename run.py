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
        self.version = "5.0-mobile"
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
            'speedtest': 'pip install speedtest-cli'
        }
        
        missing = [lib for lib in required if not self.is_installed(lib)]
        if missing:
            self.print_color("\nERROR: Jalankan di Termux:", 'red')
            print("pkg update && pkg install python clang")
            print("pip install " + " ".join(missing))
            sys.exit(1)

    def is_installed(self, lib):
        try:
            __import__(lib)
            return True
        except ImportError:
            return False

    def print_color(self, text, color):
        print(f"{self.colors[color]}{text}{self.colors['reset']}")

    def show_banner(self):
        os.system('clear')
        banner = f"""
{self.colors['cyan']}
╔═╗┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐  ╔╦╗┌─┐┌┬┐┌─┐┬  ┬┌─┐┬─┐
║  ├─┤├┤ ├─┘├┴┐├┤ ├┬┘  ║║║├┤  │ │ │└┐┌┘├┤ ├┬┘
╚═╝┴ ┴└  ┴  ┴ ┴└─┘┴└─  ╩ ╩└─┘ ┴ └─┘ └┘ └─┘┴└─
{self.colors['magenta']}       Network & Electrical Tools v{self.version}
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
            self.print_color(f"[{item[0]}] {item[1]}", item[2])
        
        print(f"\n{self.colors['cyan']}╰───────────────────────────────────────────╯{self.colors['reset']}")
        return input(f"\n{self.colors['yellow']}➤ Pilih menu [1-9]: {self.colors['reset']}")

    def loading_animation(self, message):
        frames = cycle(["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"])
        for _ in range(15):
            print(f"\r{self.colors['blue']}{next(frames)} {message}...{self.colors['reset']}", end="")
            time.sleep(0.1)
        print("\r" + " "*50 + "\r", end="")

    def script_tools(self):
        try:
            self.print_color("\n🛠️  Script Tools Network", 'cyan')
            ip_info = requests.get('https://api.ipify.org?format=json').json()
            self.print_color(f"\n📡 IP Publik: {ip_info['ip']}", 'green')
            
            self.loading_animation("Melakukan ping ke 8.8.8.8")
            ping_result = subprocess.run(
                ['ping', '-c', '3', '8.8.8.8'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            self.print_color("\n📶 Hasil Ping:", 'cyan')
            print(ping_result.stdout.decode()[:200])
            
        except Exception as e:
            self.print_color(f"\n❌ Error: {str(e)}", 'red')

    def check_password_strength(self):
        password = getpass(f"{self.colors['yellow']}⌨  Masukkan password: {self.colors['reset']}")
        strength = 0
        criteria = {
            'length': len(password) >= 8,
            'uppercase': any(c.isupper() for c in password),
            'lowercase': any(c.islower() for c in password),
            'digit': any(c.isdigit() for c in password),
            'special': any(not c.isalnum() for c in password)
        }
        
        strength = sum(criteria.values())
        self.loading_animation("Menganalisis password")
        
        # Tampilan progress bar
        progress = "▰" * strength + "▱" * (5 - strength)
        color = 'red' if strength < 3 else 'yellow' if strength < 4 else 'green'
        
        print(f"\n{self.colors[color]}")
        print("╔══════════════════════════════╗")
        print("║       HASIL ANALISIS         ║")
        print("╠═══════════════╦══════════════╣")
        print(f"║ Kekuatan      ║ {progress:<10} ║")
        print("╠═══════════════╩══════════════╣")
        print("║ Kriteria:                    ║")
        for name, met in criteria.items():
            status = "✓" if met else "✗"
            color_status = 'green' if met else 'red'
            print(f"║  {self.colors[color_status]}{status}{self.colors[color]} {name:<10}          ║")
        print("╚══════════════════════════════╝")
        print(self.colors['reset'])

    def technical_calculations(self):
        while True:
            self.show_banner()
            self.print_color("\n🔌 PERHITUNGAN TEKNIS LISTRIK", 'red')
            menu = [
                ("1", "Hitung Daya (P)", 'cyan'),
                ("2", "Hitung Tegangan (V)", 'blue'),
                ("3", "Hitung Arus (I)", 'magenta'),
                ("4", "Hitung Hambatan (R)", 'green'),
                ("5", "Kembali ke Menu Utama", 'yellow')
            ]
            
            for item in menu:
                self.print_color(f"[{item[0]}] {item[1]}", item[2])
            
            choice = input(f"\n{self.colors['yellow']}➤ Pilih perhitungan [1-5]: {self.colors['reset']}")
            
            if choice == '1':
                self.calculate_power()
            elif choice == '2':
                self.calculate_voltage()
            elif choice == '3':
                self.calculate_current()
            elif choice == '4':
                self.calculate_resistance()
            elif choice == '5':
                return
            else:
                self.print_color("Pilihan tidak valid!", 'red')
                time.sleep(1)

    def calculate_power(self):
        self.show_banner()
        self.print_color("\n⚡ HITUNG DAYA (P)", 'cyan')
        print(f"{self.colors['blue']}Pilih rumus:")
        print("1. P = V × I")
        print("2. P = V² / R")
        print("3. P = I² × R")
        print(f"{self.colors['reset']}")
        
        try:
            formula = input(f"{self.colors['yellow']}➤ Pilih rumus [1-3]: {self.colors['reset']}")
            if formula == '1':
                v = float(input("Masukkan Tegangan (V): "))
                i = float(input("Masukkan Arus (A): "))
                result = v * i
                unit = "Watt"
            elif formula == '2':
                v = float(input("Masukkan Tegangan (V): "))
                r = float(input("Masukkan Hambatan (Ω): "))
                result = (v ** 2) / r
                unit = "Watt"
            elif formula == '3':
                i = float(input("Masukkan Arus (A): "))
                r = float(input("Masukkan Hambatan (Ω): "))
                result = (i ** 2) * r
                unit = "Watt"
            else:
                raise ValueError
                
            self.print_color(f"\n🔋 Hasil Perhitungan: {result:.2f} {unit}", 'green')
        except (ValueError, ZeroDivisionError):
            self.print_color("\n❌ Input tidak valid atau pembagian dengan nol!", 'red')
        input("\nTekan Enter untuk melanjutkan...")

    # [Method calculate_voltage, current, resistance dengan tampilan serupa...]

    def main(self):
        while True:
            choice = self.show_menu()
            
            if choice == '1':
                self.script_tools()
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
                self.print_color("\n👋 Keluar...", 'magenta')
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
        print(f"\n{tool.colors['red']}🛑 Dihentikan!{tool.colors['reset']}")
        sys.exit()
