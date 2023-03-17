import os #import os untuk memudahkan
from datetime import datetime    # import library datetime untuk mengambil waktu saat transaksi dilakukan
from prettytable import PrettyTable    # import library prettytable untuk menampilkan riwayat transaksi dalam tabel
import time
os.system("cls")

class Transaksi:
    def __init__(self, jenis, jumlah):
        self.jenis = jenis    # jenis transaksi, misalnya 'Tambah Saldo' atau 'Kurangi Saldo'
        self.jumlah = jumlah    # jumlah uang yang terlibat dalam transaksi
        self.waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    # waktu transaksi dilakukan dalam format 'YYYY-MM-DD HH:MM:SS'

class Node:
    def __init__(self, transaksi=None):
        self.transaksi = transaksi    # objek Transaksi yang menjadi isi node
        self.next_node = None    # pointer yang menunjukkan node selanjutnya dalam linked list

class LinkedList:
    def __init__(self):
        self.head = None    # node pertama dalam linked list
        self.tail = None    # node terakhir dalam linked list

    def is_empty(self):
        return self.head == None    # linked list kosong jika tidak ada node di dalamnya

    def tambah_transaksi(self, transaksi):
        new_node = Node(transaksi)    # membuat node baru dengan isi objek Transaksi
        if self.is_empty():
            self.head = new_node    # jika linked list kosong, node baru menjadi node pertama dan terakhir
            self.tail = new_node
        else:
            self.tail.next_node = new_node    # jika linked list sudah ada node, node baru ditambahkan di akhir
            self.tail = new_node    # node baru menjadi node terakhir

    def tampil_transaksi(self):
        table = PrettyTable()    # membuat objek tabel dari library prettytable
        table.field_names = ["Jenis", "Jumlah", "Waktu"]    # membuat nama kolom tabel
        current_node = self.head    # pointer awal menunjukkan node pertama
        while current_node != None:
            table.add_row([current_node.transaksi.jenis, current_node.transaksi.jumlah, current_node.transaksi.waktu])    # menambahkan isi node ke dalam baris tabel
            current_node = current_node.next_node    # pointer ditunjukkan ke node selanjutnya
        print(table)    # menampilkan tabel

class EWallet:
    def __init__(self, nama, saldo=0):
        self.nama = nama    # nama pemilik e-wallet
        self.saldo = saldo    # jumlah saldo dalam e-wallet
        self.riwayat = LinkedList()    # membuat objek linked list untuk menyimpan riwayat transaksi
    
    def tambah_saldo(self, jumlah):
        self.saldo += jumlah    # menambahkan jumlah saldo dalam e-wallet
        transaksi = Transaksi("Top Up Saldo", jumlah)    # membuat objek Transaksi untuk transaksi tambah saldo
        self.riwayat.tambah_transaksi(transaksi)    # menambahkan objek Transaksi ke dalam linked list riwayat transaksi
        print(f"Saldo berhasil ditambahkan sejumlah {jumlah}.")

    def kurangi_saldo(self, jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah    # mengurangi jumlah saldo dalam e-wallet
            transaksi = Transaksi("withdraw", jumlah)   # membuat objek transaksi
            self.riwayat.tambah_transaksi(transaksi)   # menambahkan transaksi ke riwayat
            print(f"berhasil withdraw sejumlah {jumlah}.")
        else:
            print("Saldo tidak mencukupi.")

    def transfer(self, nama_penerima, jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah   # mengurangi saldo pengirim
            transaksi = Transaksi(f"Transfer ke {nama_penerima}", jumlah)   # membuat objek transaksi
            self.riwayat.tambah_transaksi(transaksi)   # menambahkan transaksi ke riwayat
            print(f"Transfer berhasil dilakukan sejumlah {jumlah} ke {nama_penerima}.")
        else:
            print("Saldo tidak mencukupi.")

    def tampil_riwayat(self):
        print(f"Riwayat Transaksi E-Wallet {self.nama}:")
        self.riwayat.tampil_transaksi()   # menampilkan riwayat transaksi menggunakan metode tampil_transaksi()


if __name__ == "__main__":
    print("="*52)
    print("="*5, "Selamat datang di aplikasi E-Wallet!".center(40), "="*5)
    print("="*52)
    nama = input("Masukkan nama Anda: ")
    saldo = int(input("Masukkan saldo awal Anda: "))
    ewallet = EWallet(nama, saldo) #input nama dan saldo awal user
    print("wait..")
    time.sleep(2)
    os.system("cls")
    print(f"\nSelamat datang di E-Wallet {ewallet.nama}")

while True:
    # menampilkan menu awal
    
    print(f"Silakan pilih menu yang diinginkan:\n"
        '''
        ||===================================||
        ||               Menu :              ||
        ||===================================||
        ||      1. Top Up Saldo              ||
        ||      2. withdraw Saldo            ||
        ||      3. Transfer Saldo            ||
        ||      4. Cek Saldo                 ||
        ||      5. Tampil Riwayat Transaksi  ||
        ||      6. EXIT                      ||
        ||===================================||\n''')

    # meminta input dari pengguna untuk memilih menu
    pilihan_menu = input("Masukkan pilihan menu: ")

    if pilihan_menu == "1":
        os.system("cls")
        # meminta input dari pengguna untuk jumlah saldo yang ingin ditambahkan
        print("wait..")
        time.sleep(2)
        jumlah_saldo = float(input("Masukkan nominal top up: "))
        # memanggil method tambah_saldo pada objek EWallet
        ewallet.tambah_saldo(jumlah_saldo)
        time.sleep(3)
        os.system("cls")

    elif pilihan_menu == "2":
        os.system("cls")
        # meminta input dari pengguna untuk jumlah saldo yang ingin dikurangi
        jumlah_saldo = float(input("Masukkan nominal Withdraw: "))
        print("wait..")
        time.sleep(2)
        # memanggil method kurangi_saldo pada objek EWallet
        ewallet.kurangi_saldo(jumlah_saldo)
        time.sleep(3)
        os.system("cls")

    elif pilihan_menu == "3":
        os.system("cls")
        # meminta input dari pengguna untuk nama penerima dan jumlah saldo yang ingin ditransfer
        nama_penerima = input("Masukkan nama penerima: ")
        jumlah_saldo = float(input("Masukkan jumlah saldo yang ingin ditransfer: "))
        print("wait..")
        time.sleep(2)
        # memanggil method transfer pada objek EWallet
        ewallet.transfer(nama_penerima, jumlah_saldo)
        time.sleep(3)
        os.system("cls")

    elif pilihan_menu == "4":
        os.system("cls")
        print("wait..")
        time.sleep(2)
        # mencetak saldo terkini dari objek EWallet
        print(f"Saldo terkini E-Wallet {ewallet.nama}: {ewallet.saldo}")
        time.sleep(2)

    elif pilihan_menu == "5":
        os.system("cls")
        print("wait..")
        time.sleep(2)
        # menampilkan riwayat transaksi dari objek EWallet
        ewallet.tampil_riwayat()
        time.sleep(2)

    elif pilihan_menu == "6":
        print("wait..")
        time.sleep(2)
        print ("="*5, "Terimakasih telah melakukan transaksi di E-Wallet Chandra".center(40), "="*5)
        # keluar dari loop while
        break

    else:
        print("Pilihan menu tidak valid. Silakan pilih menu yang tersedia.")
        time.sleep(2)
        os.system("cls")