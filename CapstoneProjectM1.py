# Capstone Project Module 1 - Purwadhika JDSOL-014
# Oleh ANANDA RAHMAH FAUZIYAH
# Membuat mini aplikasi dengan fitur utama CRUD (Create, Read, Update, Delete) menggunakan python
# Case Study : Penjualan barang toko 

#Kumpulan Data dan Function Mini Aplikasi :
## Detail Data Barang:
dataBarang = [
    {
        'IDBarang': '0000001', 
        'namaBarang': "V (BTS) 'Layover' (Set)", 
        'jumlahStock': 10,
        'harga': 700000, 
        'IDKategori': '1306131', 
        'kategori': 'Album'
    },
    {
        'IDBarang': '0000002', 
        'namaBarang': "BEYOND THE STORY",
        'jumlahStock': 15,
        'harga': 625000, 
        'IDKategori': '1306132',
        'kategori': 'Book'
    },
    {
        'IDBarang': '0000003',
        'namaBarang': "Official Light Stick Special Edition",
        'jumlahStock': 17,
        'harga': 750000, 
        'IDKategori': '1306133',
        'kategori': 'Merch'
    },
    {
        'IDBarang': '0000004',
        'namaBarang': "Bantal Leher RJ",
        'jumlahStock': 5,
        'harga': 550000, 
        'IDKategori': '1306134',
        'kategori': 'BT21'
    },
    {
        'IDBarang': '0000005',
        'namaBarang': "Special 8 Photo-Folio Set",
        'jumlahStock': 10,
        'harga': 3315000,
        'IDKategori': '1306135',
        'kategori': 'Photobook'
    }
]

keranjang = [] #proses pembelian
daftarRiwayatTransaksi = [] #setelah melakukan pembelian

# Function untuk pemberitahuan / notifikasi (yang digunakan lebih dari 1 kali)
def pemberitahuan (notif):
    if notif == 0:
        print('Masukkan Y atau N saja.')
    elif notif == 1:
        print('Pilihan Tidak Valid.')
    elif notif == 2:
        print('Pilihan Tidak Valid. Masukkan Y atau N saja')
    elif notif == 3:
        print('Pilihan Tidak Valid. Masukkan angka yang sesuai')
    elif notif == 4:
        print('ID Barang tidak valid. Harus berupa angka dan sebanyak 7 digit.')
    elif notif == 5:
        print('Input tidak valid. Masukkan hanya angka')
    elif notif == 6:
        print('ID Kategori tidak valid. Harus berupa angka dan sebanyak 7 digit.')

# Function untuk validasi
def validasiID(id):
    return len(id) == 7 and id.isdigit()

def validasi(cek,input):
    if cek == 1 : #cek input Y / N
        if input == '0':
            return input
        elif input not in ('Y','N'):
            pemberitahuan(0)
            return False
        else :
            return True

# Function row tabel pada menampilkan data 
def rowTabelData ():
    print('-'*121)
    print('| ID Barang\t| Nama Barang\t\t\t\t| Jumlah Stock\t| Harga\t\t| ID Kategori\t| Kategori\t|')
    print('-'*121)

# Function konfirmasi kembali ke menu utama
def konfirmasiKembali():
    while True :
        backMenu = input("Ingin Kembali Ke Menu Utama? (Y/N) : ")
        if backMenu.upper() == 'Y':
            return True
        elif backMenu.upper() == 'N' :
            return False
        else:
            pemberitahuan(2)

# CRUD #
# Function menampilkan data barang (READ)
## semua data
def menampilkanDataBarang(filterKategori=None, sortBy=None):
    # Menyiapkan daftar barang yang akan ditampilkan / filter data berdasarkan kategori
    filteredData = dataBarang
    if filterKategori:
        filteredData = [barang for barang in dataBarang if barang['kategori'].lower() == filterKategori.lower()]
    
    # Menampilkan data barang
    print('\nDaftar Barang:')
    rowTabelData()
    for barang in filteredData:
        print('| {:<10}\t| {:<35}\t| {:<12}\t| {:<10}\t| {:<12}\t| {:<10} \t|'.format(
            barang['IDBarang'], barang['namaBarang'], barang['jumlahStock'], barang['harga'], barang['IDKategori'], barang['kategori']))
    print('-'*121)

## data yang dicari
def menampilkanCariBarang(cariNama):
    print('Hasil Pencarian untuk "{}":'.format(cariNama))
    rowTabelData()
    ditemukan = False
    for barang in dataBarang:
        if cariNama.lower() in barang['namaBarang'].lower():
            ditemukan = True
            print('| {:<10}\t| {:<35}\t| {:<12}\t| {:<10}\t| {:<12}\t| {:<10} \t|'.format(
                barang['IDBarang'], barang['namaBarang'], barang['jumlahStock'], barang['harga'], barang['IDKategori'], barang['kategori']))
            print('-'*121)
    if not ditemukan:
        print('\t\t\t\t\t\tBarang tidak ditemukan\t\t\t\t\t\t')
        print('-'*121)


# Function menambah data barang (CREATE)
def menambahBarang() :
    while True:
        pilih = input("Ingin menambahkan barang baru? (Y/N): ").upper()
        if pilih == 'N':
            if konfirmasiKembali():
                break
        
        elif pilih == 'Y':
            menampilkanDataBarang()
            while True: 
                IDbarang = (input('Masukkan ID Barang (sebanyak 7 angka): '))
                if not validasiID(IDbarang):
                    pemberitahuan(4)
                # cek duplikasi ID Barang
                elif any(barang['IDBarang'] == IDbarang for barang in dataBarang):
                    print("ID Barang sudah ada. Tidak dapat menambahkan barang dengan ID yang sama.")
                else: 
                    break
            
            namaBarang = input("Masukkan Nama Barang: ")

            try:
                jumlahStock = int(input("Masukkan Jumlah Stock: "))
            except ValueError:
                pemberitahuan(5)
                continue

            try:
                harga = int(input("Masukkan Harga: "))
            except ValueError:
                pemberitahuan(5)
                continue
            
            while True:
                IDKategori = input("Masukkan ID Kategori (sebanyak 7 angka): ")
                if not validasiID(IDKategori):
                    pemberitahuan(6)
                else:
                    break

            kategori = input("Masukkan Kategori: ")

            barangBaru = {'IDBarang': IDbarang,'namaBarang': namaBarang,'jumlahStock': jumlahStock,'harga': harga,'IDKategori': IDKategori,'kategori': kategori}
            simpan = input("Apakah Anda ingin menyimpan data ini? (Y/N): ").upper()
            if simpan == 'Y' :
                dataBarang.append(barangBaru)
                print("Barang berhasil ditambahkan.")
            else:
                print("Barang tidak ditambahkan")
            
            print('Berikut adalah daftar barang terbaru.')
            menampilkanDataBarang()

        else:
            pemberitahuan(2)

# Function mengupdate data barang (UPDATE)
def mengupdateBarang():
    while True:
        pilih = input("Ingin mengupdate data barang tertentu? (Y/N): ").upper()
        if pilih == 'N':
            if konfirmasiKembali():
                break
            else:
                continue
        
        elif pilih == 'Y' :
            menampilkanDataBarang()
            IDbarang = input('Masukkan ID Barang (sebanyak 7 angka) yang ingin diupdate: ')
            if not validasiID(IDbarang):
                pemberitahuan(4)
                continue

            found = False
            for i, barang in enumerate(dataBarang):
                if barang['IDBarang'] == IDbarang:
                    found = True
                    print("ID Barang: {}, Nama Barang: {}". format(barang['IDBarang'], barang['namaBarang']))
                    konfirmasi = input(f"Apakah Anda yakin ingin mengupdate barang dengan ID {IDbarang} dan nama {barang['namaBarang']}? (Y/N): ").upper()
                    if konfirmasi == 'Y':
                        while True:
                            print('''Pilih kolom yang ingin diubah:
                            1. Nama Barang
                            2. Jumlah Stock
                            3. Harga
                            4. ID Kategori
                            5. Kategori
                            0. Kembali''')
                            kolom = input("Masukkan angka kolom yang ingin diubah: ")
                            if kolom == '0':
                                break
                            elif kolom == '1':
                                barang['namaBarang'] = input("Masukkan Nama Barang baru: ")
                            elif kolom == '2':
                                try:
                                    barang['jumlahStock'] = int(input("Masukkan Jumlah Stock baru: "))
                                except ValueError:
                                    pemberitahuan(5)
                                    continue
                            elif kolom == '3':
                                try:
                                    barang['harga'] = int(input("Masukkan Harga baru: "))
                                except ValueError:
                                    pemberitahuan(5)
                                    continue
                            elif kolom == '4':
                                while True:
                                    IDKategori = input("Masukkan ID Kategori (sebanyak 7 angka) baru: ")
                                    if validasiID(IDKategori):
                                        barang['IDKategori'] = IDKategori
                                        break
                                    else:
                                        pemberitahuan(6)
                            elif kolom == '5':
                                barang['kategori'] = input("Masukkan Kategori baru: ")
                            else:
                                pemberitahuan(3)

                            simpan = input("Apakah Anda ingin menyimpan perubahan ini? (Y/N): ").upper()
                            if simpan == 'Y':
                                dataBarang[i] = barang
                                print("Barang berhasil diupdate.")
                                
                                print('Berikut adalah daftar barang terbaru.')
                                menampilkanDataBarang()
                                break
                            else:
                                print("Perubahan tidak disimpan.")
                                break
                    else:
                        print("Update dibatalkan.")
                    break

            if not found:
                print("Barang dengan ID {} tidak ditemukan.".format(IDbarang))

        else :
            pemberitahuan(2)


# Function menghapus baris data barang (DELETE)
def menghapusBarang() :
    while True:
        pilih = input("Ingin menghapus baris data barang tertentu? (Y/N): ").upper()
        if pilih == 'N':
            if konfirmasiKembali():
                break
            else:
                continue
        
        elif pilih == 'Y':
            menampilkanDataBarang()
            IDbarang = input('Masukkan ID Barang (sebanyak 7 angka) yang ingin dihapus: ')
            if not validasiID(IDbarang):
                pemberitahuan(4)
                continue

            found = False
            for i, barang in enumerate(dataBarang):
                if barang['IDBarang'] == IDbarang:
                    found = True
                    print('ID Barang: {}, Nama Barang: {}'.format(barang['IDBarang'], barang['namaBarang']))
                    konfirmasi = input(f"Apakah Anda yakin ingin menghapus barang dengan ID barang {IDbarang} dan nama barang {barang['namaBarang']}? (Y/N): ").upper()
                    if konfirmasi == 'Y':
                        del dataBarang[i]
                        print("Barang dengan ID barang 1{} berhasil dihapus.".format(IDbarang))
                        
                        print('Berikut adalah daftar barang terbaru.')
                        menampilkanDataBarang()
                    
                    else:
                        print('Penghapusan dibatalkan.')
                        break

            if not found:   
                print("Barang dengan ID {} tidak ditemukan.".format(IDbarang))

        else:
            pemberitahuan(2)

# Function untuk membeli barang
## Function untuk merekam transaksi dan mengosongkan keranjang setelah pembelian.
def emptyCartandRecordTransaction(nama, totalHarga):
    global keranjang, daftarRiwayatTransaksi
    daftarRiwayatTransaksi.append({'nama': nama, 'totalHarga': totalHarga, 'items': keranjang.copy()})
    keranjang.clear()

## Function pembelian barang
def beliBarang():
    global keranjang
    while True: 
        menampilkanDataBarang()
        beli = input('Ingin membeli barang? (Y/N): ').upper()
        if beli == 'N':
            if konfirmasiKembali():
                break

        elif beli == 'Y':
            while True:
                try: #agar tidak error ketika diinput selain int
                    indexBarang = int(input('Masukkan index barang yang ingin dibeli: '))
                except ValueError:
                    pemberitahuan(5)
                    continue
                
                if indexBarang < 0 or indexBarang >= len(dataBarang):
                    print('Index tidak valid. Silakan coba lagi.')
                    continue
                
                try:
                    jmlBarang = int(input('Masukkan jumlah yang ingin dibeli: '))
                except ValueError:
                    pemberitahuan(5)
                    continue
                
                if jmlBarang > dataBarang[indexBarang]['jumlahStock']:
                    print('Stock tidak cukup, stock {} tinggal {} buah'.format(dataBarang[indexBarang]['namaBarang'], dataBarang[indexBarang]['jumlahStock']))
                else:
                    dataBarang[indexBarang]['jumlahStock'] -= jmlBarang
                    keranjang.append({
                        'nama': dataBarang[indexBarang]['namaBarang'],'jmlBarang': jmlBarang,'harga': dataBarang[indexBarang]['harga'],'index': indexBarang})
                
                print('Isi Cart:')
                print('-'*81)
                print('| Nama Barang \t\t\t\t| Jumlah Barang \t| Harga \t|')
                print('-'*81)
                for item in keranjang:
                    print('| {:<35}\t| {:<15} \t| {:<12} \t|'.format(item['nama'], item['jmlBarang'], item['harga']))
                print('-'*81)

                while True:
                    check = input('Mau beli yang lain? (Y/N): ').upper()
                    if check == 'N': 
                        break
                    elif check != 'Y':
                        pemberitahuan(2)
                        continue
                    else:
                        break
                
                if check == 'N':
                    break
            
            #proses pembayaran
            print('Daftar Belanja:')
            print('-'*97)
            print('| Nama Barang \t\t\t\t| Jumlah Barang \t| Harga \t| Total Harga \t|')
            print('-'*97)
            totalHarga = 0
            for item in keranjang:
                totalItem = item['jmlBarang'] * item['harga']
                print('| {:<35}\t| {:<15}\t| {:<12}\t| {:<12} \t|'.format(item['nama'], item['jmlBarang'], item['harga'], totalItem))
                totalHarga += totalItem
                print('-'*97)

            while True:
                print('Total Yang Harus Dibayar = {}'.format(totalHarga))
                
                try:    
                    jmlUang = int(input('Masukkan jumlah uang: '))
                except ValueError:
                    pemberitahuan(5)
                    continue
                
                nama = input('Masukkan nama Anda: ')
                if jmlUang > totalHarga:
                    kembalian = jmlUang - totalHarga
                    print('Terima kasih, {}. Uang kembali Anda: {}'.format(nama, kembalian))
                    emptyCartandRecordTransaction(nama, totalHarga)
                    break
                elif jmlUang == totalHarga:
                    print('Terima kasih, {}.'.format(nama))
                    emptyCartandRecordTransaction(nama, totalHarga)
                    break
                else:
                    kekurangan = totalHarga - jmlUang
                    print('Maaf, {}, uang Anda kurang sebesar {}'.format(nama, kekurangan))
            
            # Menampilkan data barang terbaru
            print('Data barang terbaru: ')
            menampilkanDataBarang()

            # Menanyakan apakah ingin kembali ke menu sebelumnya atau melakukan pembelian lagi
            repeat = input('Ingin membeli barang lagi? (Y/N): ').upper()
            if repeat == 'N':
                if konfirmasiKembali():
                    break
        else:
            pemberitahuan(2)

## Function Riwayat transaksi
def riwayatTransaksi():
    while True:  
        print('\nRiwayat Transaksi:')
        print('-'*161)
        print('| Nama \t\t\t| Total Harga\t| Items ')
        print('-'*161)
        for transaksi in daftarRiwayatTransaksi:
            formatItems = ', '.join(['{} x {}'.format(item['nama'], item['jmlBarang']) for item in transaksi['items']])
            print('| {:<15} \t| {:<12} \t| {:<50} '.format(transaksi['nama'], transaksi['totalHarga'], formatItems))
            print('-'*161)
        
        if konfirmasiKembali():
            break
        
# Function menu 
## Function sub menu
def subMenu () :
    while True :
        print('''\nPilih Menu Yang Diinginkan : \n
        1. Menampilkan seluruh data
        2. Melakukan pencarian data berdasarkan nama barang
        3. Memfilter data berdasarkan nama kategori
        0. Kembali ke menu sebelumnya \n''')
        pilih = input('Masukkan angka menu yang diinginkan: ')
        
        if pilih == '1' :
            menampilkanDataBarang()
            if konfirmasiKembali():
                break
        elif pilih == '2' :
            cariNama = input('Masukkan nama barang yang dicari: ')
            menampilkanCariBarang(cariNama)
            if konfirmasiKembali():
                break
        elif pilih == '3':
            kategori = input('Masukkan nama kategori untuk difilter: ')
            menampilkanDataBarang(filterKategori=kategori)
            if konfirmasiKembali():
                break
        elif pilih == '0' :
            break
        else :
            pemberitahuan(1)

## Function menu penjual
def menuPenjual():
    while True :
        print('''\nSelamat Datang di Boltiao Store!💜\n
            1. Menampilkan daftar barang
            2. Menambahkan barang
            3. Mengupdate data barang 
            4. Menghapus baris data barang
            0. Kembali ke halaman utama\n''')
        pilihMenu = input('Masukkan angka menu yang diinginkan: ') 

        if pilihMenu == '1':
            subMenu()
        elif pilihMenu == '2' :
            menambahBarang()
        elif pilihMenu == '3':
            mengupdateBarang()
        elif pilihMenu == '4' :
            menghapusBarang()
        elif pilihMenu == '0':
            break
        else:
            pemberitahuan(1)

# Function menu pembeli
def menuPembeli():
    while True:
        print('''\nSelamat Datang di Boltiao Store!💜\n
        1. Menampilkan daftar barang 
        2. Membeli barang
        3. Riwayat transaksi
        0. Kembali ke halaman utama\n''')
        pilih = input('Masukkan angka menu yang diinginkan: ')

        if pilih == '1':
            subMenu()
        elif pilih == '2':
            beliBarang()
        elif pilih == '3':
            riwayatTransaksi()
        elif pilih == '0':
            break
        else:
            pemberitahuan(3)

# MINI APLIKASI DIJALANKAN
while True:
    print('''\nSelamat Datang di Boltiao Store!💜\nPilih Menu:
    1. Penjual
    2. Pembeli
    0. Keluar Aplikasi\n''')
    pilih = input('Masukkan angka menu yang diinginkan: ')

    if pilih == '1':
        menuPenjual()
    elif pilih == '2':
        menuPembeli()
    elif pilih == '0':
        while True :
                konfirmasiInput = input('Anda yakin untuk keluar aplikasi? (Y/N): ').upper() #konfirmasi input exit program
                if validasi(1, konfirmasiInput):
                    if konfirmasiInput == '0' :
                        pemberitahuan(0)
                        continue
                    break
        if konfirmasiInput == 'Y' :
                    print('Terima Kasih, Borahae!💜')
                    break
    else:
        pemberitahuan(1)