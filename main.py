import sys
import time
import random
import string
from getpass import getpass

class GanzCLIV2:
    def __init__(self):
        self.running = True
        self.colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'reset': '\033[0m'
        }
    
    def clear_screen(self):
        print("\033c", end="")
    
    def show_banner(self):
        self.clear_screen()
        print(f"""{self.colors['blue']}
    ╔═╗┌─┐┌┐┌┌┬┐┬ ┬┌─┐┬─┐  ╔╦╗┌─┐┌┬┐┌─┐┬  ┬
    ║  │ ││││ │ │││├─┤├┬┘   ║ │ │ ││├┤ └┐┌┘
    ╚═╝└─┘┘└┘ ┴ └┴┘┴ ┴┴└─   ╩ └─┘─┴┘└─┘ └┘ {self.colors['reset']}
    {self.colors['yellow']}Termux Security Toolkit v2.0{self.colors['reset']}
    """)
    
    def animated_loading(self, msg="Memproses"):
        chars = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
        start_time = time.time()
        while time.time() - start_time < 3:
            for c in chars:
                sys.stdout.write(f"\r{self.colors['green']}{msg} {c}{self.colors['reset']}")
                sys.stdout.flush()
                time.sleep(0.1)
        print()
    
    def main_menu(self):
        while self.running:
            self.show_banner()
            print(f"{self.colors['yellow']}[ Menu Utama ]{self.colors['reset']}")
            print("1. Brute Force Simulasi")
            print("2. Analisis Kekuatan Sandi")
            print("3. Keluar")
            
            try:
                choice = input("\nPilih opsi: ")
                
                if choice == '1':
                    self.brute_force_menu()
                elif choice == '2':
                    self.password_analysis_menu()
                elif choice == '3':
                    self.exit_app()
                else:
                    print(f"{self.colors['red']}Pilihan tidak valid!{self.colors['reset']}")
                    time.sleep(1)
            except KeyboardInterrupt:
                self.exit_app()

    def generate_password_list(self, count=20000):
        base_chars = string.ascii_letters + string.digits + "!@#$%^&*"
        passwords = []
        for _ in range(count):
            length = random.randint(8, 16)
            password = ''.join(random.choices(base_chars, k=length))
            passwords.append(password)
        return passwords

    def brute_force_menu(self):
        self.clear_screen()
        print(f"{self.colors['yellow']}[ Mode Brute Force ]{self.colors['reset']}\n")
        
        target_user = input("Masukkan username target: ")
        print(f"\n{self.colors['blue']}Membuat 20.000 kombinasi sandi...{self.colors['reset']}")
        self.animated_loading("Generating Password")
        
        password_list = self.generate_password_list()
        target_password = getpass("Masukkan sandi simulasi: ")
        
        print(f"\n{self.colors['yellow']}Memulai proses brute force...{self.colors['reset']}")
        print(f"{self.colors['red']}Tekan Ctrl+C untuk berhenti{self.colors['reset']}\n")
        
        found = False
        start_time = time.time()
        
        try:
            for idx, password in enumerate(password_list, 1):
                sys.stdout.write(f"\r{self.colors['green']}Progress: {idx}/20000 "
                               f"({(idx/20000)*100:.1f}%) | "
                               f"Current: {password}{' '*10}{self.colors['reset']}")
                sys.stdout.flush()
                
                if password == target_password:
                    found = True
                    break
                
                time.sleep(0.01)  # Simulasi delay
            
            elapsed = time.time() - start_time
            print(f"\n\n{self.colors['blue']}Waktu proses: {elapsed:.2f} detik{self.colors['reset']}")
            
            if found:
                print(f"{self.colors['green']}[+] Sandi ditemukan: {password}{self.colors['reset']}")
            else:
                print(f"{self.colors['red']}[-] Sandi tidak ditemukan dalam daftar{self.colors['reset']}")
            
            input("\nTekan Enter untuk lanjut...")
            
        except KeyboardInterrupt:
            print(f"\n{self.colors['red']}Proses dihentikan pengguna!{self.colors['reset']}")
            time.sleep(1)

    def password_analysis_menu(self):
        self.clear_screen()
        print(f"{self.colors['yellow']}[ Analisis Sandi ]{self.colors['reset']}\n")
        
        password = getpass("Masukkan sandi untuk dianalisis: ")
        score = 0
        feedback = []
        
        
        length = len(password)
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(not c.isalnum() for c in password)
        
        
        score += min(length * 4, 40)  # Maks 40 untuk panjang
        if has_upper: score += 10
        if has_lower: score += 10
        if has_digit: score += 15
        if has_special: score += 25
        
        
        if length < 8:
            feedback.append("Terlalu pendek (minimal 8 karakter)")
        elif length < 12:
            feedback.append("Panjang cukup, tapi bisa lebih panjang")
        else:
            feedback.append("Panjang sangat baik")
            
        if not has_upper:
            feedback.append("Tambah huruf kapital (A-Z)")
        if not has_lower:
            feedback.append("Tambah huruf kecil (a-z)")
        if not has_digit:
            feedback.append("Tambah angka (0-9)")
        if not has_special:
            feedback.append("Tambah karakter khusus (!@#$%)")
        
        
        print(f"\n{self.colors['blue']}Hasil Analisis:{self.colors['reset']}")
        print(f"Skor Keamanan: {self.get_score_bar(score)} {score}/100")
        
        print(f"\n{self.colors['yellow']}Rekomendasi:{self.colors['reset']}")
        for item in feedback:
            print(f" - {item}")
            
        input("\nTekan Enter untuk kembali...")

    def get_score_bar(self, score):
        bar_length = 20
        filled = int(score / 100 * bar_length)
        return f"{self.colors['green']}{'█'*filled}{self.colors['red']}{'░'*(bar_length-filled)}{self.colors['reset']}"

    def exit_app(self):
        print(f"\n{self.colors['blue']}Keluar dari aplikasi...{self.colors['reset']}")
        self.running = False
        sys.exit(0)

if __name__ == "__main__":
    app = GanzCLIV2()
    app.main_menu()
