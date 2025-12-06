class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data = {}

    def tambah(self):
        print("\n=== Tambah Data Mahasiswa ===")
        nama = input("Masukkan nama mahasiswa : ")
        try:
            nilai = float(input("Masukkan nilai         : "))
        except ValueError:
            print("Input nilai harus berupa angka!\n")
            return

        self.data[nama] = nilai
        print(f"Data mahasiswa '{nama}' berhasil ditambahkan.\n")

    def tampilkan(self):
        print("\n=== Daftar Nilai Mahasiswa ===")
        if not self.data:
            print("Belum ada data yang tersimpan.\n")
            return

        for nama, nilai in self.data.items():
            print(f"- {nama} : {nilai}")
        print()

    def hapus(self, nama):
        print("\n=== Hapus Data Mahasiswa ===")
        if nama in self.data:
            del self.data[nama]
            print(f"Data mahasiswa '{nama}' berhasil dihapus.\n")
        else:
            print("Nama mahasiswa tidak ditemukan!\n")

    def ubah(self, nama):
        print("\n=== Ubah Data Mahasiswa ===")
        if nama in self.data:
            try:
                nilai_baru = float(input("Masukkan nilai baru : "))
            except ValueError:
                print("Input nilai harus berupa angka!\n")
                return

            self.data[nama] = nilai_baru
            print(f"Data mahasiswa '{nama}' berhasil diubah.\n")
        else:
            print("Nama mahasiswa tidak ditemukan!\n")


if __name__ == "__main__":
    daftar = DaftarNilaiMahasiswa()

    while True:
        print("=== MENU PROGRAM ===")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            daftar.tambah()
        elif pilihan == "2":
            daftar.tampilkan()
        elif pilihan == "3":
            nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
            daftar.hapus(nama)
        elif pilihan == "4":
            nama = input("Masukkan nama mahasiswa yang akan diubah: ")
            daftar.ubah(nama)
        elif pilihan == "5":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid!\n")
