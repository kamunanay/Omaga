jiimport os
import sys
import time
import hashlib
import re
import subprocess
import requests
import platform
from getpass import getpass

class MobileTools:
    def __init__(self):
        self.version = "2.0-mobile"
        self.author = "GanzMods"
        self.check_dependencies()
        

    def is_installed(self, lib):
        try:
            __import__(lib)
            return True
        except ImportError:
            return False

    def show_menu(self):
        os.system('clear')
        print(f"""\033[1;36m
    ███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
    ████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
    ██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝██║  ██║
    ██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██║  ██║
    ██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
    ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
        \033[1;35mMobile Network Tools v{self.version}\033[0m
             \033[1;33mDeveloped by: {self.author}\033[0m
""")
        print("\033[1;32m1. Cek Status Jaringan")
        print("2. Tes Kecepatan Internet")
        print("3. Cek Kekuatan Password")
        print("4. Pemindai WiFi Terdekat")
        print("5. Cek Info IP Publik")
        print("6. Pemendek URL")
        print("7. Konversi Satuan Data")
        print("8. Kalkulator Sederhana")
        print("9. Info Sistem")
        print("10. Keluar\033[0m")
        print("\033[1;36m" + "═"*50 + "\033[0m")
        
        choice = input("\033[1;33mPilih menu [1-10]: \033[0m")
        return choice

    def run_network_check(self):
        try:
            ip_info = requests.get('https://api.ipify.org?format=json').json()
            print(f"\n\033[1;36mIP Publik: \033[1;32m{ip_info['ip']}\033[0m")
            
            ping_result = subprocess.run(
                ['ping', '-c', '3', '8.8.8.8'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print("\n\033[1;36mHasil Ping:\033[0m")
            print(ping_result.stdout.decode()[:200])
            
        except Exception as e:
            print(f"\033[1;31mError: {str(e)}\033[0m")

    def run_speedtest(self):
        try:
            import speedtest
            st = speedtest.Speedtest()
            st.get_best_server()
            
            print("\n\033[1;36mMengukur kecepatan unduh...\033[0m")
            download = st.download() / 1_000_000
            print("\033[1;36mMengukur kecepatan unggah...\033[0m")
            upload = st.upload() / 1_000_000
            
            print(f"\n\033[1;36mHasil Speedtest:")
            print(f"Unduh: \033[1;32m{download:.2f} Mbps")
            print(f"\033[1;36mUnggah: \033[1;32m{upload:.2f} Mbps\033[0m")
            
        except Exception as e:
            print(f"\033[1;31mError: {str(e)}\033[0m")

    def check_password_strength(self):
        password = getpass("Masukkan password: ")
        strength = 0
        
        if len(password) >= 8: strength += 1
        if any(c.isupper() for c in password): strength += 1
        if any(c.islower() for c in password): strength += 1
        if any(c.isdigit() for c in password): strength += 1
        if any(not c.isalnum() for c in password): strength += 1
        
        levels = ["Sangat Lemah", "Lemah", "Sedang", "Kuat", "Sangat Kuat"]
        print(f"\n\033[1;36mTingkat Keamanan: \033[1;32m{levels[strength]}\033[0m")

    def wifi_scanner(self):
        try:
            print("\n\033[1;36mMemindai WiFi...\033[0m")
            result = subprocess.run(
                ['termux-wifi-scaninfo'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print(result.stdout.decode())
        except:
            print("\033[1;31mInstall termux-api dulu:\npkg install termux-api\033[0m")

    def ip_lookup(self):
        try:
            response = requests.get('https://ipinfo.io/json')
            data = response.json()
            print(f"\n\033[1;36mIP: {data['ip']}")
            print(f"Lokasi: {data['city']}, {data['region']}")
            print(f"Provider: {data['org']}\033[0m")
        except Exception as e:
            print(f"\033[1;31mError: {str(e)}\033[0m")

    def url_shortener(self):
        url = input("Masukkan URL panjang: ")
        try:
            response = requests.get(f'https://tinyurl.com/api-create.php?url={url}')
            print(f"\n\033[1;36mURL Pendek: \033[1;32m{response.text}\033[0m")
        except Exception as e:
            print(f"\033[1;31mError: {str(e)}\033[0m")

    def data_converter(self):
        print("\n\033[1;36mContoh: 1000 MB = 1 GB")
        value = float(input("Masukkan nilai: "))
        print(f"\n{value} MB = \033[1;32m{value/1000} GB")
        print(f"{value} GB = \033[1;32m{value*1000} MB\033[0m")

    def simple_calculator(self):
        try:
            expr = input("Masukkan ekspresi (contoh: 2+3*5): ")
            result = eval(expr)
            print(f"\n\033[1;36mHasil: \033[1;32m{result}\033[0m")
        except:
            print("\033[1;31mEkspresi tidak valid!\033[0m")

    def system_info(self):
        print(f"\n\033[1;36mSistem Operasi: \033[1;32m{platform.system()}")
        print(f"\033[1;36mVersi Python: \033[1;32m{platform.python_version()}")
        print(f"\033[1;36mArsitektur: \033[1;32m{platform.machine()}\033[0m")

    def main(self):
        while True:
            choice = self.show_menu()
            
            if choice == '1':
                self.run_network_check()
            elif choice == '2':
                self.run_speedtest()
            elif choice == '3':
                self.check_password_strength()
            elif choice == '4':
                self.wifi_scanner()
            elif choice == '5':
                self.ip_lookup()
            elif choice == '6':
                self.url_shortener()
            elif choice == '7':
                self.data_converter()
            elif choice == '8':
                self.simple_calculator()
            elif choice == '9':
                self.system_info()
            elif choice == '10':
                print("\n\033[1;31mKeluar...\033[0m")
                sys.exit()
            else:
                print("\n\033[1;31mPilihan tidak valid!\033[0m")
                time.sleep(1)
            
            input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    tool = MobileTools()
    try:
        tool.main()
    except KeyboardInterrupt:
        print("\n\033[1;31mDihentikan!\033[0m")
        sys.exit()
