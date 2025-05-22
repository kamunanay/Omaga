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
            ("9", "Port Scanner", 'magenta'),
            ("10", "DNS Lookup", 'green'),
            ("11", "MAC Addreas Lookup", 'yellow'),
            ("12", "Konversi Satuan", 'red'),
            ("13", "Keluar", 'magenta'),  
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
                    parts = net.split(',')
                    ssid = parts[0].split(':')[1].strip(' "') if len(parts) > 0 else "N/A"
                    bssid = parts[1].split(':')[1].strip(' "') if len(parts) > 1 else "N/A"
                    rssi = parts[3].split(':')[1].strip() if len(parts) > 3 else "N/A"
                    print(f"║ {ssid[:8]:<8} ║ {bssid[:18]:<18} ║ {rssi:>6} ║")
            
            print(f"╚{'═'*10}╩{'═'*20}╩{'═'*8}╝{self.colors['reset']}")
            
        except:
            self.print_color("✖ Fitur ini hanya tersedia di Termux", 'red')
            print(f"{self.colors['yellow']}Instal termux-api: pkg install termux-api{self.colors['reset']}")

    def ip_lookup(self):
        try:
            self.print_box(" CEK INFO IP PUBLIK ", 'yellow')
            self.loading_animation("Mengumpulkan data")
            
            response = requests.get('https://ipinfo.io/json')
            data = response.json()
            
            self.print_color("\n🌍 Informasi IP:", 'yellow')
            print(f"{self.colors['cyan']}╔{'═'*25}╦{'═'*20}╗")
            print(f"║ {'Parameter':<23} ║ {'Nilai':<18} ║")
            print(f"╠{'═'*25}╬{'═'*20}╣")
            print(f"║ IP Address           ║ {self.colors['green']}{data.get('ip', 'N/A'):<18}{self.colors['cyan']} ║")
            print(f"║ Kota                 ║ {self.colors['green']}{data.get('city', 'N/A'):<18}{self.colors['cyan']} ║")
            print(f"║ Region               ║ {self.colors['green']}{data.get('region', 'N/A'):<18}{self.colors['cyan']} ║")
            print(f"║ Negara               ║ {self.colors['green']}{data.get('country', 'N/A'):<18}{self.colors['cyan']} ║")
            print(f"║ Provider             ║ {self.colors['green']}{data.get('org', 'N/A')[:17]:<18}{self.colors['cyan']} ║")
            print(f"╚{'═'*25}╩{'═'*20}╝{self.colors['reset']}")
            
        except Exception as e:
            self.print_color(f"\n❌ Error: {str(e)}", 'red')

    def technical_calculations(self):
        while True:
            self.show_banner()
            self.print_box(" PERHITUNGAN TEKNIS LISTRIK ", 'red')
            menu = [
                ("1", "Hitung Daya (P)", 'cyan'),
                ("2", "Hitung Tegangan (V)", 'blue'),
                ("3", "Hitung Arus (I)", 'magenta'),
                ("4", "Hitung Hambatan (R)", 'green'),
                ("5", "Kembali ke Menu Utama", 'yellow')
            ]
            
            for item in menu:
                self.print_color(f"  {item[0]}. {item[1]}", item[2])
            
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
        self.print_box(" HITUNG DAYA (P) ", 'cyan')
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
            elif formula == '2':
                v = float(input("Masukkan Tegangan (V): "))
                r = float(input("Masukkan Hambatan (Ω): "))
                result = (v ** 2) / r
            elif formula == '3':
                i = float(input("Masukkan Arus (A): "))
                r = float(input("Masukkan Hambatan (Ω): "))
                result = (i ** 2) * r
            else:
                raise ValueError
                
            self.print_color(f"\n⚡ Hasil Perhitungan: {self.colors['green']}{result:.2f} Watt{self.colors['reset']}", 'cyan')
        except (ValueError, ZeroDivisionError):
            self.print_color("\n❌ Input tidak valid atau pembagian dengan nol!", 'red')
        input("\nTekan Enter untuk melanjutkan...")

    def calculate_voltage(self):
        self.show_banner()
        self.print_box(" HITUNG TEGANGAN (V) ", 'blue')
        print(f"{self.colors['cyan']}Pilih rumus:")
        print("1. V = I × R")
        print("2. V = P / I")
        print(f"{self.colors['reset']}")
        
        try:
            formula = input(f"{self.colors['yellow']}➤ Pilih rumus [1-2]: {self.colors['reset']}")
            if formula == '1':
                i = float(input("Masukkan Arus (A): "))
                r = float(input("Masukkan Hambatan (Ω): "))
                result = i * r
            elif formula == '2':
                p = float(input("Masukkan Daya (W): "))
                i = float(input("Masukkan Arus (A): "))
                result = p / i
            else:
                raise ValueError
                
            self.print_color(f"\n⚡ Hasil Perhitungan: {self.colors['green']}{result:.2f} Volt{self.colors['reset']}", 'blue')
        except (ValueError, ZeroDivisionError):
            self.print_color("\n❌ Input tidak valid atau pembagian dengan nol!", 'red')
        input("\nTekan Enter untuk melanjutkan...")

    def calculate_current(self):
        self.show_banner()
        self.print_box(" HITUNG ARUS (I) ", 'magenta')
        print(f"{self.colors['cyan']}Pilih rumus:")
        print("1. I = V / R")
        print("2. I = P / V")
        print(f"{self.colors['reset']}")
        
        try:
            formula = input(f"{self.colors['yellow']}➤ Pilih rumus [1-2]: {self.colors['reset']}")
            if formula == '1':
                v = float(input("Masukkan Tegangan (V): "))
                r = float(input("Masukkan Hambatan (Ω): "))
                result = v / r
            elif formula == '2':
                p = float(input("Masukkan Daya (W): "))
                v = float(input("Masukkan Tegangan (V): "))
                result = p / v
            else:
                raise ValueError
                
            self.print_color(f"\n⚡ Hasil Perhitungan: {self.colors['green']}{result:.2f} Ampere{self.colors['reset']}", 'magenta')
        except (ValueError, ZeroDivisionError):
            self.print_color("\n❌ Input tidak valid atau pembagian dengan nol!", 'red')
        input("\nTekan Enter untuk melanjutkan...")

    def calculate_resistance(self):
        self.show_banner()
        self.print_box(" HITUNG HAMBATAN (R) ", 'green')
        print(f"{self.colors['cyan']}Pilih rumus:")
        print("1. R = V / I")
        print("2. R = V² / P")
        print("3. R = P / I²")
        print(f"{self.colors['reset']}")
        
        try:
            formula = input(f"{self.colors['yellow']}➤ Pilih rumus [1-3]: {self.colors['reset']}")
            if formula == '1':
                v = float(input("Masukkan Tegangan (V): "))
                i = float(input("Masukkan Arus (A): "))
                result = v / i
            elif formula == '2':
                v = float(input("Masukkan Tegangan (V): "))
                p = float(input("Masukkan Daya (W): "))
                result = (v ** 2) / p
            elif formula == '3':
                p = float(input("Masukkan Daya (W): "))
                i = float(input("Masukkan Arus (A): "))
                result = p / (i ** 2)
            else:
                raise ValueError
                
            self.print_color(f"\n⚡ Hasil Perhitungan: {self.colors['green']}{result:.2f} Ohm{self.colors['reset']}", 'green')
        except (ValueError, ZeroDivisionError):
            self.print_color("\n❌ Input tidak valid atau pembagian dengan nol!", 'red')
        input("\nTekan Enter untuk melanjutkan...")

    def electricity_calculator(self):
        try:
            self.print_box(" KALKULATOR BIAYA LISTRIK ", 'cyan')
            print(f"{self.colors['blue']}Masukkan data berikut:")
            
            watt = float(input("Daya perangkat (Watt): "))
            hours = float(input("Pemakaian per hari (jam): "))
            cost = float(input("Biaya per kWh (Rp): "))
            
            daily = (watt * hours / 1000) * cost
            monthly = daily * 30
            annual = daily * 365
            
            self.print_color("\n📊 Hasil Perhitungan:", 'cyan')
            print(f"{self.colors['green']}╔{'═'*20}╦{'═'*15}╗")
            print(f"║ {'Periode':<18} ║ {'Biaya':<13} ║")
            print(f"╠{'═'*20}╬{'═'*15}╣")
            print(f"║ Harian           ║ Rp{daily:>10,.2f} ║")
            print(f"║ Bulanan          ║ Rp{monthly:>10,.2f} ║")
            print(f"║ Tahunan          ║ Rp{annual:>10,.2f} ║")
            print(f"╚{'═'*20}╩{'═'*15}╝{self.colors['reset']}")
            
        except ValueError:
            self.print_color("\n❌ Input harus berupa angka!", 'red')
        input("\nTekan Enter untuk melanjutkan...")

    def system_info(self):
        self.print_box(" INFO SISTEM ", 'blue')
        print(f"{self.colors['cyan']}╔{'═'*25}╦{'═'*20}╗")
        print(f"║ {'Parameter':<23} ║ {'Nilai':<18} ║")
        print(f"╠{'═'*25}╬{'═'*20}╣")
        print(f"║ Sistem Operasi       ║ {self.colors['green']}{platform.system():<18}{self.colors['cyan']} ║")
        print(f"║ Versi Sistem         ║ {self.colors['green']}{platform.release():<18}{self.colors['cyan']} ║")
        print(f"║ Arsitektur           ║ {self.colors['green']}{platform.machine():<18}{self.colors['cyan']} ║")
        print(f"║ Versi Python         ║ {self.colors['green']}{platform.python_version():<18}{self.colors['cyan']} ║")
        print(f"╚{'═'*25}╩{'═'*20}╝{self.colors['reset']}")

    def port_scanner(self):
        try:
            self.print_box(" PORT SCANNER ", 'magenta')
            target = input(f"{self.colors['yellow']}Masukkan IP target: {self.colors['reset']}")
            port_range = input("Masukkan range port (contoh: 1-100): ")

            start_port, end_port = map(int, port_range.split('-'))
            self.loading_animation("Memindai port")

            print(f"\n{self.colors['cyan']}╔{'═'*10}╦{'═'*15}╗")
            print(f"║ {'Port':<8} ║ {'Status':<13} ║")
            print(f"╠{'═'*10}╬{'═'*15}╣")
            
            for port in range(start_port, end_port+1):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((target, port))
                if result == 0:
                    print(f"║ {port:<8} ║ {self.colors['green']}Terbuka{' '*(7)}{self.colors['cyan']} ║")
                sock.close()
            
            print(f"╚{'═'*10}╩{'═'*15}╝{self.colors['reset']}")
            
        except Exception as e:
            self.print_color(f"\n❌ Error: {str(e)}", 'red')

    def dns_lookup(self):
        try:
            self.print_box(" DNS LOOKUP ", 'green')
            domain = input(f"{self.colors['yellow']}Masukkan domain: {self.colors['reset']}")
            
            self.loading_animation("Mencari informasi DNS")
            ip_address = socket.gethostbyname(domain)
            
            print(f"\n{self.colors['cyan']}╔{'═'*20}╦{'═'*20}╗")
            print(f"║ {'Domain':<18} ║ {'IP Address':<18} ║")
            print(f"╠{'═'*20}╬{'═'*20}╣")
            print(f"║ {domain[:18]:<18} ║ {self.colors['green']}{ip_address:<18}{self.colors['cyan']} ║")
            print(f"╚{'═'*20}╩{'═'*20}╝{self.colors['reset']}")
            
        except Exception as e:
            self.print_color(f"\n❌ Error: {str(e)}", 'red')

    def unit_converter(self):
        try:
            self.print_box(" KONVERSI SATUAN ", 'red')
            print(f"{self.colors['cyan']}Pilih konversi:")
            print("1. Volt ke Milivolt (mV)")
            print("2. Ampere ke Miliampere (mA)")
            print("3. Ohm ke Kiloohm (kΩ)")
            print("4. Watt ke Kilowatt (kW)")
            
            choice = input(f"\n{self.colors['yellow']}➤ Pilih konversi [1-4]: {self.colors['reset']}")
            value = float(input("Masukkan nilai: "))
            
            conversions = {
                '1': {'from': 'V', 'to': 'mV', 'factor': 1000},
                '2': {'from': 'A', 'to': 'mA', 'factor': 1000},
                '3': {'from': 'Ω', 'to': 'kΩ', 'factor': 0.001},
                '4': {'from': 'W', 'to': 'kW', 'factor': 0.001}
            }
            
            result = value * conversions[choice]['factor']
            
            print(f"\n{self.colors['green']}{value} {conversions[choice]['from']} = {result:.2f} {conversions[choice]['to']}{self.colors['reset']}")
            
        except Exception as e:
            self.print_color(f"\n❌ Error: {str(e)}", 'red')

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
                self.port_scanner()
            elif choice == '10':
                self.dns_lookup()
            elif choice == '11':
                self.mac_lookup()
            elif choice == '12':
                self.unit_converter()
            elif choice == '13':
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
