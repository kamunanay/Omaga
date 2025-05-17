import os
import sys
import time
import subprocess
import requests
import platform
from getpass import getpass

class MobileTools:
    def __init__(self):
        self.version = "4.0-mobile"
        self.author = "GanzMods"
        self.check_dependencies()
        
    def check_dependencies(self):
        required = {
            'requests': 'pip install requests',
            'speedtest': 'pip install speedtest-cli'
        }
        
        missing = [lib for lib in required if not self.is_installed(lib)]
        if missing:
            print("\033[1;31mERROR: Jalankan di Termux:\033[0m")
            print("pkg update && pkg install python clang")
            print("pip install " + " ".join(missing))
            sys.exit(1)

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
        print("8. Kalkulator Biaya Listrik")
        print("9. Perhitungan Teknis Listrik")
        print("10. Info Sistem")
        print("11. Keluar\033[0m")
        print("\033[1;36m" + "═"*50 + "\033[0m")
        
        choice = input("\033[1;33mPilih menu [1-11]: \033[0m")
        return choice

    # ... [Metode yang sama sebelumnya] ...

    def technical_electric_calculations(self):
        os.system('clear')
        print("\033[1;36m\n=== Perhitungan Teknis Listrik ===")
        print("1. Hitung Daya (P)")
        print("2. Hitung Tegangan (V)")
        print("3. Hitung Arus (I)")
        print("4. Hitung Hambatan (R)")
        print("5. Kembali ke Menu Utama\033[0m")
        choice = input("\033[1;33mPilih jenis perhitungan [1-5]: \033[0m")
        
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
            print("\033[1;31mPilihan tidak valid!\033[0m")
            time.sleep(1)

    def calculate_power(self):
        os.system('clear')
        print("\033[1;36m\n=== Menghitung Daya (P) ===")
        print("Pilih rumus:")
        print("1. P = V × I (Tegangan × Arus)")
        print("2. P = V² / R (Tegangan kuadrat / Hambatan)")
        print("3. P = I² × R (Arus kuadrat × Hambatan)\033[0m")
        formula = input("\033[1;33mPilih rumus [1-3]: \033[0m")
        
        try:
            if formula == '1':
                v = float(input("Masukkan Tegangan (V): "))
                i = float(input("Masukkan Arus (A): "))
                p = v * i
                print(f"\033[1;36mDaya (P) = \033[1;32m{p:.2f} Watt\033[0m")
            elif formula == '2':
                v = float(input("Masukkan Tegangan (V): "))
                r = float(input("Masukkan Hambatan (Ω): "))
                p = (v ** 2) / r
                print(f"\033[1;36mDaya (P) = \033[1;32m{p:.2f} Watt\033[0m")
            elif formula == '3':
                i = float(input("Masukkan Arus (A): "))
                r = float(input("Masukkan Hambatan (Ω): "))
                p = (i ** 2) * r
                print(f"\033[1;36mDaya (P) = \033[1;32m{p:.2f} Watt\033[0m")
            else:
                print("\033[1;31mPilihan tidak valid!\033[0m")
        except ValueError:
            print("\033[1;31mInput tidak valid! Masukkan angka.\033[0m")
        except ZeroDivisionError:
            print("\033[1;31mError: Pembagian dengan nol!\033[0m")
        input("\nTekan Enter untuk melanjutkan...")

    def calculate_voltage(self):
        os.system('clear')
        print("\033[1;36m\n=== Menghitung Tegangan (V) ===")
        print("Pilih rumus:")
        print("1. V = I × R (Arus × Hambatan)")
        print("2. V = P / I (Daya / Arus)\033[0m")
        formula = input("\033[1;33mPilih rumus [1-2]: \033[0m")
        
        try:
            if formula == '1':
                i = float(input("Masukkan Arus (A): "))
                r = float(input("Masukkan Hambatan (Ω): "))
                v = i * r
                print(f"\033[1;36mTegangan (V) = \033[1;32m{v:.2f} Volt\033[0m")
            elif formula == '2':
                p = float(input("Masukkan Daya (W): "))
                i = float(input("Masukkan Arus (A): "))
                v = p / i
                print(f"\033[1;36mTegangan (V) = \033[1;32m{v:.2f} Volt\033[0m")
            else:
                print("\033[1;31mPilihan tidak valid!\033[0m")
        except ValueError:
            print("\033[1;31mInput tidak valid! Masukkan angka.\033[0m")
        except ZeroDivisionError:
            print("\033[1;31mError: Pembagian dengan nol!\033[0m")
        input("\nTekan Enter untuk melanjutkan...")

    def calculate_current(self):
        os.system('clear')
        print("\033[1;36m\n=== Menghitung Arus (I) ===")
        print("Pilih rumus:")
        print("1. I = V / R (Tegangan / Hambatan)")
        print("2. I = P / V (Daya / Tegangan)\033[0m")
        formula = input("\033[1;33mPilih rumus [1-2]: \033[0m")
        
        try:
            if formula == '1':
                v = float(input("Masukkan Tegangan (V): "))
                r = float(input("Masukkan Hambatan (Ω): "))
                i = v / r
                print(f"\033[1;36mArus (I) = \033[1;32m{i:.2f} Ampere\033[0m")
            elif formula == '2':
                p = float(input("Masukkan Daya (W): "))
                v = float(input("Masukkan Tegangan (V): "))
                i = p / v
                print(f"\033[1;36mArus (I) = \033[1;32m{i:.2f} Ampere\033[0m")
            else:
                print("\033[1;31mPilihan tidak valid!\033[0m")
        except ValueError:
            print("\033[1;31mInput tidak valid! Masukkan angka.\033[0m")
        except ZeroDivisionError:
            print("\033[1;31mError: Pembagian dengan nol!\033[0m")
        input("\nTekan Enter untuk melanjutkan...")

    def calculate_resistance(self):
        os.system('clear')
        print("\033[1;36m\n=== Menghitung Hambatan (R) ===")
        print("Pilih rumus:")
        print("1. R = V / I (Tegangan / Arus)")
        print("2. R = V² / P (Tegangan kuadrat / Daya)")
        print("3. R = P / I² (Daya / Arus kuadrat)\033[0m")
        formula = input("\033[1;33mPilih rumus [1-3]: \033[0m")
        
        try:
            if formula == '1':
                v = float(input("Masukkan Tegangan (V): "))
                i = float(input("Masukkan Arus (A): "))
                r = v / i
                print(f"\033[1;36mHambatan (R) = \033[1;32m{r:.2f} Ohm\033[0m")
            elif formula == '2':
                v = float(input("Masukkan Tegangan (V): "))
                p = float(input("Masukkan Daya (W): "))
                r = (v ** 2) / p
                print(f"\033[1;36mHambatan (R) = \033[1;32m{r:.2f} Ohm\033[0m")
            elif formula == '3':
                p = float(input("Masukkan Daya (W): "))
                i = float(input("Masukkan Arus (A): "))
                r = p / (i ** 2)
                print(f"\033[1;36mHambatan (R) = \033[1;32m{r:.2f} Ohm\033[0m")
            else:
                print("\033[1;31mPilihan tidak valid!\033[0m")
        except ValueError:
            print("\033[1;31mInput tidak valid! Masukkan angka.\033[0m")
        except ZeroDivisionError:
            print("\033[1;31mError: Pembagian dengan nol!\033[0m")
        input("\nTekan Enter untuk melanjutkan...")

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
                self.electricity_calculator()
            elif choice == '9':
                self.technical_electric_calculations()
            elif choice == '10':
                self.system_info()
            elif choice == '11':
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
