import math

def validasi_input(pesan):

    while True:
        try:
            nilai = float(input(pesan))
            if nilai < 0:
                print("Error: Nilai tidak boleh negatif!")
                continue
            return nilai
        except ValueError:
            print("Error: Masukan harus berupa angka!")

def hitung_persegi(): # HITUNG PESERGI
    """
    Fungsi untuk menghitung persegi
    Mencari sisi jika diketahui luas atau keliling
    """
    print("\nMasukkan Luas Persegi (0 jika tdk ada) : ", end="")
    luas = validasi_input("")
    print("Masukkan Keliling Persegi (0 jika tdk ada) : ", end="")
    keliling = validasi_input("")
    
    print("\nDiketahui :")
    if luas != 0:
        print(f"Luas\t\t: {luas:.1f}")
        sisi = math.sqrt(luas)
        keliling = 4 * sisi
        print("\nMaka...")
        print(f"Panjang Sisi\t: {sisi:.1f}")
        print(f"Keliling\t: {keliling:.1f}")
    elif keliling != 0:
        print(f"Keliling\t: {keliling:.1f}")
        sisi = keliling / 4
        luas = sisi * sisi
        print("\nMaka...")
        print(f"Panjang Sisi\t: {sisi:.1f}")
        print(f"Luas\t\t: {luas:.1f}")
    else:
        print("Data tidak cukup untuk melakukan perhitungan!")

def hitung_persegi_panjang(): # HITUNG PESERGI PANJANG
    """
    Fungsi untuk menghitung persegi panjang
    Mencari panjang/lebar jika diketahui lebar/panjang dan luas/keliling
    """
    print("\nApa yang ingin dicari?")
    print("1. Panjang")
    print("2. Lebar")
    pilihan = input("Masukkan pilihan (1-2): ")
    
    if pilihan == '1':
        print("\nMasukkan lebar (0 jika tdk ada) : ", end="")
        lebar = validasi_input("")
        print("Masukkan Luas (0 jika tdk ada) : ", end="")
        luas = validasi_input("")
        print("Masukkan Keliling (0 jika tdk ada) : ", end="")
        keliling = validasi_input("")
        
        print("\nDiketahui :")
        if lebar != 0 and luas != 0:
            print(f"Lebar\t\t: {lebar:.1f}")
            print(f"Luas\t\t: {luas:.1f}")
            panjang = luas / lebar
            keliling = 2 * (panjang + lebar)
            print("\nMaka...")
            print(f"Panjang\t\t: {panjang:.1f}")
            print(f"Keliling\t: {keliling:.1f}")
        elif lebar != 0 and keliling != 0:
            print(f"Lebar\t\t: {lebar:.1f}")
            print(f"Keliling\t: {keliling:.1f}")
            panjang = (keliling / 2) - lebar
            luas = panjang * lebar
            print("\nMaka...")
            print(f"Panjang\t\t: {panjang:.1f}")
            print(f"Luas\t\t: {luas:.1f}")
        else:
            print("Data tidak cukup untuk melakukan perhitungan!")
            
    elif pilihan == '2':
        print("\nMasukkan panjang (0 jika tdk ada) : ", end="")
        panjang = validasi_input("")
        print("Masukkan Luas (0 jika tdk ada) : ", end="")
        luas = validasi_input("")
        print("Masukkan Keliling (0 jika tdk ada) : ", end="")
        keliling = validasi_input("")
        
        print("\nDiketahui :")
        if panjang != 0 and luas != 0:
            print(f"Panjang\t\t: {panjang:.1f}")
            print(f"Luas\t\t: {luas:.1f}")
            lebar = luas / panjang
            keliling = 2 * (panjang + lebar)
            print("\nMaka...")
            print(f"Lebar\t\t: {lebar:.1f}")
            print(f"Keliling\t: {keliling:.1f}")
        elif panjang != 0 and keliling != 0:
            print(f"Panjang\t\t: {panjang:.1f}")
            print(f"Keliling\t: {keliling:.1f}")
            lebar = (keliling / 2) - panjang
            luas = panjang * lebar
            print("\nMaka...")
            print(f"Lebar\t\t: {lebar:.1f}")
            print(f"Luas\t\t: {luas:.1f}")
        else:
            print("Data tidak cukup untuk melakukan perhitungan!")

def hitung_lingkaran(): #HITUNG LINGKARAN
    """
    Fungsi untuk menghitung lingkaran
    Mencari radius jika diketahui luas atau keliling
    """
    PI = 3.14159
    print("\nMasukkan Luas Lingkaran (0 jika tdk ada) : ", end="")
    luas = validasi_input("")
    print("Masukkan Keliling Lingkaran (0 jika tdk ada) : ", end="")
    keliling = validasi_input("")
    
    print("\nDiketahui :")
    if luas != 0:
        print(f"Luas\t\t: {luas:.1f}")
        radius = math.sqrt(luas / PI)
        keliling = 2 * PI * radius
        print("\nMaka...")
        print(f"Radius\t\t: {radius:.1f}")
        print(f"Keliling\t: {keliling:.1f}")
    elif keliling != 0:
        print(f"Keliling\t: {keliling:.1f}")
        radius = keliling / (2 * PI)
        luas = PI * radius * radius
        print("\nMaka...")
        print(f"Radius\t\t: {radius:.1f}")
        print(f"Luas\t\t: {luas:.1f}")
    else:
        print("Data tidak cukup untuk melakukan perhitungan!")

def main():
    """
    Fungsi utama program
    """
    while True:
        print("Pilih Bangun Datar:")
        print("1.Persegi")
        print("2.Persegi Panjang")
        print("3.Lingkaran")
        
        pilihan = input("Masukkan pilihan Anda (1-3): ")
        
        if pilihan == '1':
            hitung_persegi()
        elif pilihan == '2':
            hitung_persegi_panjang()
        elif pilihan == '3':
            hitung_lingkaran()
        else:
            print("Pilihan tidak valid!")
            continue
        
        ulang = input("\nIngin mengulang Program (y/n): ").lower()
        if ulang != 'y':
            print("\nTerima kasih telah menggunakan program Bagun Datar Sederhana by Daniel!")
            break
        print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    main()
