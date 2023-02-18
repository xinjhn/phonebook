import pickle
import os
import pathlib


class Phonebook:
    depan  = ''
    akhir = ''
    nomor = 0

    def tambahData(self):
        self.depan = input('Masukkan Nama Depan: ')
        self.akhir = input('Masukkan Nama Akhir: ')
        self.nomor = int(input('enter phone number: '))


def buat():
    book = Phonebook()
    book.tambahData()
    tulisDataKeFile(book)


def tulisDataKeFile(book):
    file = pathlib.Path('Phonebook.data')

    if file.exists():
        infile = open('Phonebook.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(book)
        infile.close()
        os.remove('Phonebook.data')
    else:
        oldlist = [book]
    outfile = open('newphonebook.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newphonebook.data', 'Phonebook.data')


def tampilkanKontak():
    file = pathlib.Path('Phonebook.data')

    if file.exists():
        infile = open('Phonebook.data', 'rb')
        mylist = pickle.load(infile)

        for item in mylist:
            print('Nama Depan\tNama Akhir\t\tNomor')
            print(item.depan, '\t\t', item.akhir, '\t\t\t', item.nomor)

        infile.close()
    else:
        print('no data found')


def perbaruiKontak(nama):
    file = pathlib.Path('Phonebook.data')
    if file.exists():
        infile = open('Phonebook.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('Phonebook.data')

        for item in oldlist:
            if item.depan == nama:
                item.depan = input('Masukkan Nama Depan: ')
                item.akhir = input('Masukkan Nama Akhir: ')
                item.nomor = int(input('Masukkan Nomor Telepon'))
            else:
                print('Data Tidak Ditemukan!')

        outfile = open('newphonebook.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newphonebook.data', 'Phonebook.data')


def cariKontak(nama):
    file = pathlib.Path('Phonebook.data')
    infile = open('Phonebook.data', 'rb')
    mylist = pickle.load(infile)
    infile.close()
    found = False

    for item in mylist:
        if item.awal == nama:
            print('number: ', item.nomor)
            found = True
        else:
            print('no data found')


def hapusKontak(nama, namaAkhir):
    file = pathlib.Path('Phonebook.data')
    infile = open('Phonebook.data', 'rb')
    oldlist = pickle.load(infile)
    infile.close()

    newlist = []
    for item in oldlist:
        if item.depan != nama and item.akhir != namaAkhir:
            newlist.append(item)
        os.remove('Phonebook.data')
        outfile = open('newphonebook.data', 'wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newphonebook.data', 'Phonebook.data')


select = ''
while select != 6:
    print('=================== \tSelamat Datang di PhoneBook\t ===================')
    print('\t1. Buat Kontak')
    print('\t2. Tampilkan Kontak')
    print('\t3. Edit Kontak')
    print('\t4. Cari Kontak')
    print('\t5. Hapus Kontak')
    print('\t6. Keluar')
    select = input()

    if select == '1':
        buat()
        print('Kontak Telah Dibuat!')
    elif select == '2':
        tampilkanKontak()
    elif select == '3':
        nama = input('Masukkan Nama Kontak: ')
        perbaruiKontak(nama)
        print('Kontak Diperbarui!')
    elif select == '4':
        nama = input('Masukkan Nama Kontak: ')
        cariKontak(nama)
    elif select == '5':
        nama = input('Masukkan Nama Depan: ')
        namaAkhir = input('Msaukkan Nama Akhir: ')
        hapusKontak(nama, namaAkhir)
        print('Kontak Telah Dihapus !')
    elif select == '6':
        print('=================== \t\tTerima Kasih\t\t ===================')
        break
