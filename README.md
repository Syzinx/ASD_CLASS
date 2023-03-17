# POSTEST3 ALOGARITMA DAN STRUTUR DATA "LINKED LIST"

Nama : chandra perdana phang

NIM  : 2209116025

# SINGLY LINKED LIST

Singly linked list adalah salah satu struktur data yang digunakan untuk menyimpan kumpulan data dalam urutan tertentu. Pada singly linked list, setiap elemen dalam list diwakili oleh sebuah objek yang disebut node. Setiap node berisi dua bagian utama, yaitu data yang ingin disimpan dan pointer ke node berikutnya dalam list.

Pada singly linked list, setiap node hanya memiliki satu pointer yang mengarah ke node berikutnya dalam list, kecuali node terakhir yang tidak memiliki pointer berikutnya dan biasanya diwakili dengan null atau nilai kosong. Inilah yang membuat singly linked list berbeda dengan struktur data linked list lainnya, seperti doubly linked list yang memiliki dua pointer pada setiap node.

Pada singly linked list, akses ke elemen-elemen di dalam list hanya dapat dilakukan dengan cara mengunjungi setiap node dari awal hingga elemen yang diinginkan ditemukan. Hal ini membuat pencarian elemen pada singly linked list lebih lambat daripada pada struktur data lain seperti array, tetapi singly linked list memiliki keunggulan dalam operasi-insert dan delete pada suatu elemen, dimana operasi tersebut cukup dilakukan dengan mengubah alamat pointer dari elemen terdekat.

Keuntungan lain dari singly linked list adalah dapat memperbesar ukuran list tanpa perlu mengalokasikan memori secara kontinu seperti pada array. Hal ini memungkinkan singly linked list untuk digunakan pada situasi di mana ukuran list sering berubah-ubah atau tidak diketahui sebelumnya. Singly linked list banyak digunakan dalam implementasi berbagai algoritma dan struktur data lain, seperti stack, queue, dan tree.


# CARA KERJA PROGRAM BESERTA OUTPUT

•	Saat program dijalankan, pengguna diminta untuk memasukkan nama dan saldo awal mereka. Data ini kemudian disimpan dalam objek EWallet.

![image](https://user-images.githubusercontent.com/126861865/225858370-690cdf18-66d5-45ac-9c90-ccc78ec96666.png)


•	Setelah pengguna memasukkan nama dan saldo awal, program akan menampilkan menu awal, yang berisi beberapa opsi untuk mengelola e-wallet.

![image](https://user-images.githubusercontent.com/126861865/225858551-aa651c50-ed36-460c-a829-5a5ee5c58989.png)


•	Ketika pengguna memilih opsi untuk menambah saldo, program akan meminta input dari pengguna untuk jumlah uang yang ingin ditambahkan. Jika input valid, program akan   memanggil method untuk menambah saldo di objek EWallet.

![image](https://user-images.githubusercontent.com/126861865/225858803-1977d8bd-eaa8-48bf-b238-3f3906118fb2.png)

![image](https://user-images.githubusercontent.com/126861865/225858972-7703f75d-e8da-4471-b1d9-dc617b634227.png)


•	Ketika pengguna memilih opsi untuk menarik saldo, program akan meminta input dari pengguna untuk jumlah uang yang ingin ditarik. Jika input valid dan saldo mencukupi, program akan memanggil method untuk mengurangi saldo di objek EWallet.

![image](https://user-images.githubusercontent.com/126861865/225859534-af7f33ab-2e9e-4226-9149-11a280d59ed2.png)

![image](https://user-images.githubusercontent.com/126861865/225860423-7918e616-26dc-41c6-b8de-77fdbf50a6be.png)


•	Ketika pengguna memilih opsi untuk mentransfer saldo, program akan meminta input dari pengguna untuk jumlah uang yang ingin ditransfer dan nama penerima transfer. Jika input valid dan saldo mencukupi, program akan memanggil method untuk mentransfer saldo di objek EWallet.

![image](https://user-images.githubusercontent.com/126861865/225860620-8e4bd9da-baf0-4b06-adfc-0c14c49cc60a.png)


•	Setelah setiap transaksi, program akan membuat objek Transaksi dengan data transaksi terkait, kemudian membuat objek Node dengan objek Transaksi sebagai isinya. Node ini akan ditambahkan ke linked list riwayat transaksi di objek EWallet.

•	Ketika pengguna memilih opsi untuk menampilkan riwayat transaksi, program akan menampilkan isi linked list riwayat transaksi dalam bentuk tabel.

![image](https://user-images.githubusercontent.com/126861865/225861463-293f6f79-c0fd-4b24-b82d-b8d62ad905ce.png)


•	Program akan terus berjalan hingga pengguna memilih opsi keluar.

![image](https://user-images.githubusercontent.com/126861865/225861704-f9d9bee9-f99a-45ad-8c5b-36e1eec9aab3.png)

Dengan cara kerja ini, program dapat membantu pengguna dalam mengelola e-wallet mereka, seperti menambah saldo, menarik saldo, atau mentransfer saldo ke pengguna lain, serta memberikan riwayat transaksi yang terperinci.


# FUNGSIONALITAS PROGRAM

Program ini memiliki beberapa fungsionalitas yang cukup lengkap untuk mengelola akun e-wallet atau dompet digital pengguna. Pertama-tama, program ini memungkinkan pengguna untuk menambah saldo pada akun e-wallet mereka. Dalam kasus ini, pengguna dapat memasukkan jumlah uang yang ingin ditambahkan ke dalam akun e-wallet mereka. Setelah itu, program akan menambahkan jumlah tersebut ke saldo akun e-wallet pengguna.

Selain menambah saldo, program juga memungkinkan pengguna untuk mengurangi saldo pada akun e-wallet mereka. Ini berguna ketika pengguna ingin melakukan pembayaran atau menarik sejumlah uang dari akun mereka. Pengguna dapat memasukkan jumlah uang yang ingin ditarik dan program akan mengurangi jumlah tersebut dari saldo akun e-wallet pengguna.

Selanjutnya, program ini memungkinkan pengguna untuk melakukan transfer uang ke akun e-wallet pengguna lain. Dalam kasus ini, pengguna harus memasukkan nomor akun e-wallet tujuan dan jumlah uang yang ingin ditransfer. Setelah itu, program akan memeriksa apakah saldo akun e-wallet pengguna mencukupi untuk melakukan transfer dan kemudian mengurangi saldo pengguna yang melakukan transfer dan menambah saldo pada akun e-wallet tujuan.

Terakhir, program ini juga memungkinkan pengguna untuk melihat riwayat transaksi yang telah dilakukan. Program akan menyimpan transaksi dalam bentuk linked list dan kemudian menampilkan riwayat transaksi tersebut dalam bentuk tabel. Pengguna dapat melihat transaksi apa saja yang telah dilakukan, seperti jumlah uang yang ditambahkan, jumlah uang yang ditarik, atau transfer uang ke akun e-wallet pengguna lain.

Dengan fungsionalitas-fungsionalitas tersebut, program ini cukup lengkap untuk mengelola akun e-wallet pengguna secara efektif dan efisien. Program ini juga cukup mudah digunakan dan dapat dioperasikan oleh pengguna dengan mudah melalui menu-menu yang telah disediakan.


# BAGAIMANA APLIKASI BEKERJA

•	Aplikasi ini bekerja dengan menggunakan linked list untuk menyimpan riwayat transaksi pengguna. Ketika pengguna memasukkan nama dan saldo awal, program akan menampilkan menu awal. Menu awal akan menawarkan beberapa pilihan kepada pengguna, seperti top up saldo, withdraw saldo, transfer saldo, dan menampilkan riwayat transaksi.

•	Jika pengguna memilih opsi top up saldo, program akan meminta input dari pengguna, seperti jumlah uang yang ingin ditambahkan. Setelah pengguna memasukkan jumlah uang, program akan membuat objek Transaksi yang berisi data transaksi top up dan menambahkan objek tersebut ke linked list riwayat transaksi. Selain itu, program juga akan menambahkan jumlah uang yang ditambahkan ke saldo pengguna.

•	Jika pengguna memilih opsi withdraw saldo, program akan meminta input dari pengguna, seperti jumlah uang yang ingin ditarik. Setelah pengguna memasukkan jumlah uang, program akan membuat objek Transaksi yang berisi data transaksi withdraw dan menambahkan objek tersebut ke linked list riwayat transaksi. Selain itu, program juga akan mengurangi jumlah uang yang ditarik dari saldo pengguna.

•	Jika pengguna memilih opsi transfer saldo, program akan meminta input dari pengguna, seperti jumlah uang yang ingin ditransfer dan nama penerima transfer. Setelah pengguna memasukkan input, program akan membuat dua objek Transaksi, satu untuk transaksi pengirim dan satu lagi untuk transaksi penerima. Kemudian, program akan menambahkan objek transaksi pengirim ke linked list riwayat transaksi pengirim dan objek transaksi penerima ke linked list riwayat transaksi penerima. Selain itu, program juga akan mengurangi jumlah uang yang ditransfer dari saldo pengirim dan menambahkan jumlah uang yang ditransfer ke saldo penerima.

•	Jika pengguna memilih opsi menampilkan riwayat transaksi, program akan menampilkan riwayat transaksi pengguna dalam bentuk tabel. Program akan mengambil data dari linked list riwayat transaksi pengguna dan menampilkannya dalam bentuk tabel dengan menggunakan method yang tersedia pada kelas LinkedList.

•	Program akan terus berjalan hingga pengguna memilih opsi keluar. Ketika pengguna memilih opsi keluar, program akan menampilkan pesan keluar dan mengakhiri program.


# ELEMEN PENTING YANG DIGUNAKAN DALAM PROGRAM

•	Class Transaksi: digunakan untuk membuat objek Transaksi yang berisi jenis transaksi, jumlah uang, dan waktu transaksi dilakukan.

•	Class Node: digunakan untuk membuat objek node dalam linked list yang berisi objek Transaksi dan pointer ke node selanjutnya.

•	Class LinkedList: digunakan untuk membuat objek linked list yang berisi objek-objek node.

•	Class EWallet: digunakan untuk membuat objek e-wallet yang berisi nama pemilik, saldo, dan linked list riwayat transaksi. Class ini juga memiliki metode untuk melakukan top up saldo, withdraw, transfer, dan melihat riwayat transaksi.

•	Library os: digunakan untuk membersihkan layar setiap kali program dijalankan.

•	Library datetime: digunakan untuk mengambil waktu saat transaksi dilakukan.

•	Library prettytable: digunakan untuk menampilkan tabel yang berisi riwayat transaksi pengguna.

# TERIMA KASIH TELAH MEMBACA IMPLEMENTASI PROGRAM SAYA PADA PENERAPAN SINGLY LINKED LIST
