import random
import os
class Indomieku:
    def __init__(self):
        rasa = ["Ayam Bawang", "Kari Ayam", "Soto Padang"]
        randomRasa = random.choice(rasa)
        wadah = ["mangkok", "piring", "tupperware"]
        randomWadah = random.choice(wadah)

        os.system("cls")
        print(f"Cara Memasak Indomie Rasa {randomRasa}")

        print(f"1. Rebus air sampai mendidih...")
        print(f"2. Setelah air mendidih, masukkan mie ke dalam air...")
        print(f"3. Tunggu mie sampai matang selama 3 menit...")
        print(f"4. Setelah mie matang, masukkan mie kedalam {randomWadah} yang sudah disiapkan...")
        print(f"5. Masukkan kuah hasil rebusan sesuai selera...")
        print(f"6. Setelah itu tuang bumbu dan aduk sampai rata...")
        print(f"5. Indomie siap dimakan...")

def main():
    run = Indomieku()

if __name__ == "__main__":
    main()