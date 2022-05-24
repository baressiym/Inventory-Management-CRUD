dictionaryGudang = {
    'sf001' : {
        'tanggal' : '24052022',
        'kode' : 'sf001',
        'nama' : 'Sofa',
        'tipe' : 'Merah',
        'jumlah' : '10'
    },
    'dr001' : {
        'tanggal' : '24052022',
        'kode' : 'dr001',
        'nama' : 'Drawer',
        'tipe' : 'Small',
        'jumlah' : '3'
    },
    'lm001' : {
        'tanggal' : '24052022',
        'kode' : 'lm001',
        'nama' : 'Lamp',
        'tipe' : 'Stand',
        'jumlah' : '2'
    },
    'fa001' : {
        'tanggal' : '24052022',
        'kode' : 'fa001',
        'nama' : 'Fan',
        'tipe' : 'Ceiling',
        'jumlah' : '7'
    }
}


def tampilanMenu():
    while True :
        print('-------------------------')
        print('IKE4 Inventory Management')
        print('-------------------------')
        print()
        print('List Menu :')
        print('1. List barang yang ada di gudang')
        print('2. Tambah barang ke gudang')
        print('3. Atur barang yang ada di gudang')
        print('4. Hapus barang dari gudang')
        print('5. Exit')
        
        menu_input = int(input('Masukkan opsi yang diinginkan [1-5] :'))

        if menu_input == 1:
            pilihanMenu1()
        
        elif menu_input == 2:
            tambahBarang()
        
        elif menu_input == 3:
            editBarang()
        
        elif menu_input == 4:
            hapusBarang()
        
        elif menu_input == 5:
            print('Good Bye!')
            break
        
        else:
            print('Pilihan yang anda masukkan salah')
        
def pilihanMenu1() :
    while True :
        print('1. Semua List Barang')
        print('2. Detail List Barang')
        print('3. Kembali Ke Menu')
        menu_pilihanMenu1 = int(input('Pilih list yang ingin anda lihat : '))
        if menu_pilihanMenu1 == 1:
            if len(dictionaryGudang) != 0:
                print('Daftar Barang \n')
                print('Tanggal \t|Kode\t|Nama\t\t|Tipe\t|Jumlah\t')
                for key in dictionaryGudang:
                    print('{}\t|{}\t|{}\t\t|{}\t|{}\t'.format(dictionaryGudang[key]['tanggal'],dictionaryGudang[key]['kode'],dictionaryGudang[key]['nama'],dictionaryGudang[key]['tipe'],dictionaryGudang[key]['jumlah']))
        elif menu_pilihanMenu1 == 2:
            menu_detail = input('Masukkan Kode Produk :').lower()
            for a in dictionaryGudang:
                if menu_detail == dictionaryGudang[a]['kode']:
                    print('Tanggal\t\t|Kode\t|Nama\t|Tipe\t|Jumlah\t')
                    print('{}\t|{}\t|{}\t|{}\t|{}'.format(dictionaryGudang[a]['tanggal'],dictionaryGudang[a]['kode'],dictionaryGudang[a]['nama'],dictionaryGudang[a]['tipe'],dictionaryGudang[a]['jumlah']))
                    break
                else:
                    print('Pilihan yang anda masukkan salah')
                    break
            print('Detail List Barang')
        elif menu_pilihanMenu1 == 3:
            tampilanMenu()
        else:
            print('Pilihan yang anda masukkan salah')

def tambahBarang():
    while True:
        print('1. Tambah Barang ke Gudang')
        print('2. Kembali Ke Menu')
        menu_pilihanMenu = int(input('Pilih list yang ingin anda lihat : '))
        if menu_pilihanMenu == 1:
            input_kode= input('Masukkan Kode Produk : ').lower()
            counter = 0
            for a in dictionaryGudang:
                if input_kode == dictionaryGudang[a]['kode']:
                    print('Data Sudah Ada!!!')
                    break
                elif counter == len(dictionaryGudang)-1:
                    input_tanggal = input('Masukkan Input Tanggal (DDMMYYYY) : ')
                    input_namaproduk = input('Masukkan Nama Produk : ')
                    input_tipe = input('Masukkan Tipe Produk : ')
                    input_jumlah = input('Masukkan Jumlah Produk : ')
                    dictionaryGudang[f'barang {len(dictionaryGudang)+1}'] = {
                            'tanggal' : input_tanggal ,
                            'kode' : input_kode,
                            'nama' : input_namaproduk,
                            'tipe' : input_tipe,
                            'jumlah' : input_jumlah }
                    while True:
                        input_yakin = input('Apakah anda sudah yakin? (Y/N) ').upper()
                        if input_yakin == 'Y':
                            print('Data Tersimpan')
                            break
                        elif input_yakin == 'N':
                            dictionaryGudang.popitem()
                            break
                        else:
                            print('Pilihan Anda Salah')
                    break
                else:
                    counter+=1
                    continue
        elif menu_pilihanMenu == 2:
            tampilanMenu()
        else:
            print('Pilihan yang anda masukkan salah')

def editBarang() :
    while True:
        print('1. Edit barang yang ada di gudang')
        print('2. Kembali ke Menu')
        menu_editbarang = int(input('Pilih list yang ingin anda lihat : '))
        if len(dictionaryGudang) != 0:
                print('Daftar Barang yang Ada di Gudang\n')
                print('Tanggal \t|Kode\t|Nama\t\t|Tipe\t|Jumlah\t')
                for key in dictionaryGudang:
                    print('{}\t|{}\t|{}\t\t|{}\t|{}\t'.format(dictionaryGudang[key]['tanggal'],dictionaryGudang[key]['kode'],dictionaryGudang[key]['nama'],dictionaryGudang[key]['tipe'],dictionaryGudang[key]['jumlah']))
        if menu_editbarang == 1:
            input_keys = input('Masukkan kode produk : ').lower()
            if input_keys in dictionaryGudang.keys():
                print(f'Produk yang ingin diubah adalah : {dictionaryGudang[input_keys]}')
                edit_kolom = input('Masukkan kolom yang ingin diganti: ')
                if edit_kolom == 'tanggal':
                    ubahTanggal = input('Update tanggal (DDMMYYYY):').lower()
                    confTanggal = input('Apakah anda sudah yakin? (Y/N)').upper()
                    if confTanggal == 'Y':
                        dictionaryGudang[input_keys]['tanggal'] = ubahTanggal
                        print('Tanggal Masuk berhasil diubah!')
                        break
                    elif confTanggal == 'N':
                        print('Tanggal Masuk Tidak Diubah')
                elif edit_kolom == 'kode': 
                    ubahKode = input('Update Kode :').lower()
                    confKode = input('Apakah anda sudah yakin? (Y/N): ').upper()
                    if confKode == 'Y':
                        dictionaryGudang[input_keys]['kode'] = ubahKode
                        print('Kode Produk berhasil diubah!')
                        break
                    elif confKode == 'N':
                        print('Kode Produk Tidak Diubah')
                elif edit_kolom == 'nama':
                    ubahNama = input('Update nama :').lower()
                    confNama = input('Apakah anda sudah yakin? (Y/N)').upper()
                    if confNama == 'Y':
                        dictionaryGudang[input_keys]['nama'] = ubahNama
                        print('Nama Produk berhasil diubah!')
                        break
                    elif confNama == 'N':
                        print('Nama Produk Tidak Diubah')
                elif edit_kolom == 'tipe':
                    ubahSatuan = input('Update tipe :').lower()
                    confSatuan = input('Apakah anda sudah yakin? (Y/N)').upper()
                    if confSatuan == 'Y':
                        dictionaryGudang[input_keys]['tipe'] = ubahSatuan
                        print('Tipe berhasil diubah!')
                        break
                    elif confSatuan == 'N':
                        print('Satuan Tidak Diubah')
                elif edit_kolom == 'jumlah':
                    ubahJumlah = input('Update jumlah :').upper()
                    confJumlah = input('Apakah anda sudah yakin? (Y/N)').upper()
                    if confJumlah == 'Y':
                        dictionaryGudang[input_keys]['jumlah'] = ubahJumlah
                        print('Jumlah berhasil diubah!')
                        break
                    elif confJumlah == 'N':
                        print('Jumlah Tidak Diubah')
            else:
                print('Data yang Anda Cari Tidak Ada !!!')
            break
        elif menu_editbarang == 2:
            break
        else:
            print('Pilihan yang anda masukkan salah')

def hapusBarang():
    while True:
        print('1. Hapus stok barang gudang')
        print('2. Kembali ke Menu')
        menu_hapusBarang = int(input('Pilih list yang ingin anda lihat : '))
        if len(dictionaryGudang) != 0:
            print('Daftar Barang yang Ada di Gudang\n')
            print('Tanggal \t|Kode\t|Nama\t\t|Tipe\t|Jumlah\t')
            for key in dictionaryGudang:
                print('{}\t|{}\t|{}\t\t|{}\t|{}\t'.format(dictionaryGudang[key]['tanggal'],dictionaryGudang[key]['kode'],dictionaryGudang[key]['nama'],dictionaryGudang[key]['tipe'],dictionaryGudang[key]['jumlah']))
        if menu_hapusBarang == 1:
            input_kode = input('Masukkan kode produk yang ingin dihapus : ').lower()
            if input_kode in dictionaryGudang.keys():
                print(f'Produk yang ingin dihapus adalah : {dictionaryGudang[input_kode]}')
                conf_del = input('Apakah anda yakin ingin menghapus data ini? (Y/N) : ').upper()
                if conf_del == 'Y':
                    del dictionaryGudang[input_kode]
                    print('Data berhasil dihapuss')
                    break
                elif conf_del == 'N':
                    print('Data tidak terhapus')
                    break
                else :
                    print('Menu yang anda masukkan salah')
                    break
            else:
                print('Data Yang Anda Cari Tidak Ada !!!')
            break
        elif menu_hapusBarang == 2:
            break
        else:
            print('Pilihan yang anda masukkan salah')

tampilanMenu()
