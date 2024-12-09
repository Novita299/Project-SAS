class Item:
    def __init__(self, item_id, nama, stok):
        self.item_id = item_id
        self.nama = nama
        self.stok = stok

    def __str__(self):
        return f"ID Barang: {self.item_id}, Nama: {self.nama}, Stok: {self.stok}"


class Borrower:
    def __init__(self, nama):
        self.nama = nama
        self.item_ids = []  # Menyimpan daftar ID barang yang dipinjam

    def pinjam(self, item_id):
        self.item_ids.append(item_id)

    def __str__(self):
        return f"Nama Peminjam: {self.nama}, ID Barang yang Dipinjam: {', '.join(self.item_ids)}"


class LoanManager:
    def __init__(self):
        self.barang = []
        self.peminjam = []

    def tambah_barang(self, item_id, nama, stok):
        item = Item(item_id, nama, stok)
        self.barang.append(item)
        print(f"Barang '{nama}' telah ditambahkan.")

    def tampilkan_barang(self):
        if not self.barang:
            print("Tidak ada barang yang tersedia.")
        else:
            for item in self.barang:
                print(item)

    def tambah_peminjam(self, nama_peminjam, item_ids):
        peminjam = Borrower(nama_peminjam)

        for item_id in item_ids:
            for item in self.barang:
                if item.item_id == item_id:
                    if item.stok > 0:
                        item.stok -= 1
                        peminjam.pinjam(item_id)
                        print(f"{nama_peminjam} telah meminjam {item.nama}.")
                    else:
                        print(f"Maaf, {item.nama} tidak tersedia.")
                    break
            else:
                print(f"Barang dengan ID {item_id} tidak ditemukan.")

        self.peminjam.append(peminjam)

    def tampilkan_peminjam(self):
        if not self.peminjam:
            print("Tidak ada peminjam saat ini.")
        else:
            for peminjam in self.peminjam:
                print(peminjam)

    def kembalikan_barang(self, item_id):
        for peminjam in self.peminjam:
            if item_id in peminjam.item_ids:
                for item in self.barang:
                    if item.item_id == item_id:
                        item.stok += 1
                        peminjam.item_ids.remove(item_id)
                        print(f"{peminjam.nama} telah mengembalikan {item.nama}.")
                        return
        print(f"Tidak ada catatan peminjaman untuk barang dengan ID {item_id}.")


# Fungsi utama untuk interaksi dengan pengguna
def main():
    manajer_peminjaman = LoanManager()

    while True:
        print("\nMenu:")
        print("1. Tambah Barang")
        print("2. Tampilkan Data Barang")
        print("3. Tambah Peminjam")
        print("4. Tampilkan Data Peminjam")
        print("5. Kembalikan Barang")
        print("6. Keluar")
        
        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == '1':
            item_id = input("Masukkan ID Barang: ")
            nama = input("Masukkan Nama Barang: ")
            stok = int(input("Masukkan Stok Barang: "))
            manajer_peminjaman.tambah_barang(item_id, nama, stok)

        elif pilihan == '2':
            manajer_peminjaman.tampilkan_barang()

        elif pilihan == '3':
            nama_peminjam = input("Masukkan Nama Peminjam: ")
            item_ids = input("Masukkan ID Barang yang Dipinjam (pisahkan dengan koma jika lebih dari satu): ").split(',')
            item_ids = [item_id.strip() for item_id in item_ids]  # Menghapus spasi
            manajer_peminjaman.tambah_peminjam(nama_peminjam, item_ids)

        elif pilihan == '4':
            manajer_peminjaman.tampilkan_peminjam()

        elif pilihan == '5':
            item_id = input("Masukkan ID Barang yang Dikembalikan: ")
            manajer_peminjaman.kembalikan_barang(item_id)

        elif pilihan == '6':
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()