"""                                 Implementation Task
implementation task of creating a simple contact book for data structure and algorithm courses
"""

class Node:
    # Node untuk singly Linkedlist
    def __init__(self, data):
        self.data = data
        self.next = None
        
class buku_kontak_maju_jaya:
    def __init__(self):
        # Membuat list kosong
        self.head = None
        self.tail = None
        self.count = 0


    def tambah_kontak(self, data):
        #menambahkan item pada list
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1


    def cari_kontak(self, target):
         # mencari item di list
        if self.head is None:
            print("Buku kontak Kosong")
            return
        else:
            current = self.head
            while current is not None:
                nama = current.data.split(",")
                if target == nama[0]:
                    print(f"Ditemukan {nama[0]} : {nama[1]}")
                    break
                else:
                    current = current.next
            else:
                print(f"Kontak {target} tidak tersedia")


    def cari_kontak_prefix(self, pretarget):
         # mencari item di list dg prefix
        if self.head is None:
            print("Buku kontak Kosong")
            return
        else:
            current = self.head
            while current is not None:
                if current.data.startswith(pretarget):
                    x = current.data.split(",")
                    print(f"Ditemukan {x[0]} : {x[1]}")
                    current = current.next
                else:
                    current = current.next


    def update_kontak(self, target, update):
         # perbaharui data di list
        if self.head is None:
            print("Buku kontak Kosong")
            return
        else:
            current = self.head
            while current is not None:
                name = current.data.split(",")
                if target == name[0]:
                    name0 = current.data.split(",")
                    name1 = update.split(",")
                    print(f"Kontak {name0[0]} : {name0[1]} telah diperbaharui menjadi {name1[0]} : {name1[1]}")
                    current.data = update
                    break

                else:
                    current = current.next
            else:
                print(f"Kontak {target} tidak tersedia")


    def tampilkan_daftar_kontak(self):
        #menampilkan semua data di list
        if self.head is None:
            print("Buku kontak Kosong")
            return
        else:
            no = 0
            current = self.head
            print("Buku Kontak Maju Jaya")
            while current is not None:
                namee = current.data.split(",")
                no += 1
                print(f"{no}. {namee[0]} : {namee[1]}")
                current = current.next


    def jumlah_kontak(self):
        #menampilkan jumlah data di list
        print(f"Terdapat {self.count} kontak dalam buku kontak")



buku = buku_kontak_maju_jaya()

while True:
    menu = int(input("""
          | BUKU KONTAK MAJU JAYA |

     1. Tambahkan Kontak Baru
     2. Cari Kontak Spesifik
     3. Cari Kontak
     4. Perbaharui Kontak
     5. Tampilkan Seluruh Kontak
     6. Tampilkan Jumlah Kontak

     0. Exit

     Pilih menu diatas: """))

    if menu == 1:
        jumlah = int(input("Masukkan jumlah kontak yang akan ditambahkan: "))
        for i in range(jumlah):
            kontak = input(f"Kontak {i+1}. Nama, Nomor Handphone :")
            buku.tambah_kontak(kontak)
        else:
            print(f"\n| Sejumlah {jumlah} kontak telah ditambahkan |")

    elif menu == 2:
        cari = input("Masukkan kontak yang ingin dicari: ")
        buku.cari_kontak(cari)

    elif menu == 3:
        carii = input("Masukkan kontak yang ingin dicari: ")
        buku.cari_kontak_prefix(carii)

    elif menu == 4:
        inputan = input("Masukkan kontak yang akan diperbaharui: ")
        inputan0 = input("\nMasukkan detail kontak yang baru: ")
        buku.update_kontak(inputan, inputan0)

    elif menu == 5:
        buku.tampilkan_daftar_kontak()

    elif menu == 6:
        buku.jumlah_kontak()

    elif menu == 0:
        exit()
