menulist = [
    '1. Report data Karyawan',
    '2. Mengubah data Karyawan',
    '3. Menambah data Karyawan',
    '4. Menghapus data Karyawan',
    '5. Keluar'
]

datakaryawan = [
    {'NIP': 1111, 'employeename': 'Bukayo Saka', 'domisili': 'Surabaya', 'jabatan': 'Staff', 'divisi': 'Finance'},
    {'NIP': 1112, 'employeename': 'Declan Rice', 'domisili': 'Semarang', 'jabatan': 'Lead', 'divisi': 'Engineer'},
    {'NIP': 1113, 'employeename': 'William Saliba', 'domisili': 'Semarang', 'jabatan': 'Staff', 'divisi': 'Finance'},
    {'NIP': 1114, 'employeename': 'Gabriel Jesus', 'domisili': 'Bandung', 'jabatan': 'Staff', 'divisi': 'Data'},
    {'NIP': 1115, 'employeename': 'Ben White', 'domisili': 'Jakarta', 'jabatan': 'Staff', 'divisi': 'Engineer'},
    {'NIP': 1116, 'employeename': 'Martin Odegaard', 'domisili': 'Jakarta', 'jabatan': 'Lead', 'divisi': 'Data'}
]

userinput = '' # Agar langsung jalan looping
while userinput != '5': # Agar melakukan looping terus sampai user pilih menu 5
    print("\n======== Sistem Informasi Karyawan ========\n")
    for menu in menulist: # Agar tidak perlu menulis print satu - satu
        print(menu)

    userinput = input('Silahkan pilih menu (pilih angka 1-5): ')

    # ===================== MENU 1: REPORT DATA =====================
    if userinput == '1':
        while True:  # Bisa diakses berulang kali tanpa harus balik ke menu utama setiap kali selesai 1 menu
            print("\n======== Report Data Karyawan ========\n")
            print('1. Tampilkan semua data karyawan')
            print('2. Tampilkan data karyawan sesuai NIP')
            print('3. Kembali ke menu utama')
            pilihanusermenu1 = input('Silahkan pilih menu (masukkan angka 1 - 3): ')

            if pilihanusermenu1 == '1':
                if len(datakaryawan) == 0: # Memastikan list tidak kosong sebelum ditampilkan, biar tidak keluar output kosong
                    print('Data karyawan kosong.')
                else:
                    print("\n== Daftar Seluruh Data Karyawan ==")
                    for index, karyawan in enumerate(datakaryawan): # Menampilkan no urut + data karyawan
                        print(f"{index+1}. NIP: {karyawan['NIP']}, Nama: {karyawan['employeename']}, "
                              f"Domisili: {karyawan['domisili']}, Jabatan: {karyawan['jabatan']}, Divisi: {karyawan['divisi']}")

                # Menu kecil setelah tampilkan data
                while True: # Bisa diakses berulang kali tanpa harus balik ke menu utama setiap kali selesai 1 menu
                    print("\n99. Kembali ke Report Data Karyawan")
                    print("00. Menu Utama")
                    submenu = input("Pilihan Anda: ")
                    if submenu == '99':
                        break  #kembali ke report data karyawan
                    elif submenu == '00':
                        userinput = ''  # Memaksa kembali ke menu utama
                        break
                    else:
                        print("Pilihan tidak valid, coba lagi.")

                if submenu == '00':
                    break  # keluar dari submenu report data karyawan

            elif pilihanusermenu1 == '2':
                if len(datakaryawan) == 0:
                    print('Data karyawan kosong.')
                else:
                    try: # Mencegah program error ketika user salah ketik
                        nipinput = int(input('Masukkan NIP karyawan yang ingin Anda lihat: '))
                        ditemukan = False # Untuk menandai apakah data ketemu atau tidak. Kalau tidak ketemu setelah loop, kita beri pesan
                        for pegawai in datakaryawan:
                            if pegawai['NIP'] == nipinput:
                                print(f"\nData Karyawan:")
                                print(f"NIP      : {karyawan['NIP']}")
                                print(f"Nama     : {karyawan['employeename']}")
                                print(f"Domisili : {karyawan['domisili']}")
                                print(f"Jabatan  : {karyawan['jabatan']}")
                                print(f"Divisi   : {karyawan['divisi']}")
                                ditemukan = True
                                break
                        if not ditemukan:
                            print('Data yang Anda cari tidak ditemukan.')
                    except ValueError: # Program tidak error tapi muncul pesan
                        print('NIP harus berupa angka!')
                input("\nTekan ENTER untuk kembali...")
                continue

            elif pilihanusermenu1 == '3':
                break  # kembali ke menu utama

            else:
                print('Pilihan tidak valid di submenu report.')
                continue

    # ===================== MENU 2: UBAH DATA =====================
    elif userinput == '2':
        print("\n======== Ubah Data Karyawan ========\n")
        if len(datakaryawan) == 0: # Mengecek panjang list datakaryawan. Kalau 0, berarti tidak ada data yang bisa diubah
            print("Data karyawan kosong.")
            continue

        try: # Mencegah program error ketika user salah ketik
            nipinput = int(input("Masukkan NIP karyawan yang ingin diubah: "))
        except ValueError:# Program tidak error tapi muncul pesan
            print("NIP harus berupa angka!")
            continue

        # Cari data
        index_karyawan = None # Karena kita belum tahu apakah NIP yang dimasukkan user ada di list data karyawan atau tidak, 
                               # bisa dipakai untuk menampilkan pesan “Data karyawan tidak ditemukan”.
        for i, pegawai in enumerate(datakaryawan): # Menampilkan no urut + data karyawan
            if pegawai['NIP'] == nipinput:
                index_karyawan = i
                break

        if index_karyawan is None:
            print("Data karyawan tidak ditemukan.")
            continue

        # Tampilkan data lama
        karyawan = datakaryawan[index_karyawan]
        print(f"\nData Karyawan:")
        print(f"NIP      : {karyawan['NIP']}")
        print(f"Nama     : {karyawan['employeename']}")
        print(f"Domisili : {karyawan['domisili']}")
        print(f"Jabatan  : {karyawan['jabatan']}")
        print(f"Divisi   : {karyawan['divisi']}")

        # Input data baru dengan or agar ketika string kosong maka nilai lama dipertahankan
        nama_baru = input("Nama baru (kosongkan jika tidak diubah): ") or karyawan['employeename']
        domisili_baru = input("Domisili baru (kosongkan jika tidak diubah): ") or karyawan['domisili']
        jabatan_baru = input("Jabatan baru (kosongkan jika tidak diubah): ") or karyawan['jabatan']
        divisi_baru = input("Divisi baru (kosongkan jika tidak diubah): ") or karyawan['divisi']

        # Konfirmasi perubahan
        konfirmasi = input("\nApakah Anda yakin ingin melakukan perubahan? (y/n): ").lower()
        if konfirmasi == 'y':
            datakaryawan[index_karyawan]['employeename'] = nama_baru
            datakaryawan[index_karyawan]['domisili'] = domisili_baru
            datakaryawan[index_karyawan]['jabatan'] = jabatan_baru
            datakaryawan[index_karyawan]['divisi'] = divisi_baru
            print("\nData karyawan berhasil diperbarui.")
        else:
            print("\nPerubahan dibatalkan.")

    # ===================== MENU 3: TAMBAH DATA =====================
    elif userinput == '3':
        print("\n======== Tambah Data Karyawan ========\n")

        try: # Mencegah program error ketika user salah ketik
            nip_baru = int(input("Masukkan NIP karyawan baru: "))
        except ValueError:# Program tidak error tapi muncul pesan
            print("NIP harus berupa angka!")
            continue

        # Cek apakah NIP sudah ada
        nip_sama = False # Melakukan pemeriksaan asumsi tidak ada nip yang sama
        for karyawan in datakaryawan:
            if karyawan['NIP'] == nip_baru: # Membandingkan nilai nip yang ada di data dengan nilai nip baru yang dimasukkan user
                nip_sama = True # Jika ditemukan kesamaan maka akan ditandai sebagai duplikat
                break

        if nip_sama:
            print(f"NIP {nip_baru} sudah digunakan oleh karyawan lain!")
            continue # Program menampilkan peringatan lalu continue untuk kembali ke awal menu

        nama_baru = input("Masukkan nama karyawan: ")
        domisili_baru = input("Masukkan domisili karyawan: ")
        jabatan_baru = input("Masukkan jabatan karyawan: ")
        divisi_baru = input("Masukkan divisi karyawan: ")

        # Konfirmasi menambahkan dictionary data karyawan baru ke list datakaryawan
        konfirmasi = input("\nApakah Anda yakin ingin menambah data ini? (y/n): ").lower()
        if konfirmasi == 'y':
            datakaryawan.append({
                'NIP': nip_baru,
                'employeename': nama_baru,
                'domisili': domisili_baru,
                'jabatan': jabatan_baru,
                'divisi': divisi_baru
            })
            print("Data karyawan berhasil ditambahkan.")
        else:
            print("Penambahan data dibatalkan.")

    # ===================== MENU 4: HAPUS DATA =====================
    elif userinput == '4':
        print("\n======== Hapus Data karyawan ========\n")
        if len(datakaryawan) == 0: # Mengecek panjang list datakaryawan. Kalau 0, berarti tidak ada data yang bisa dihapus.
            print("Data karyawan kosong.")
            continue

        try: # Mencegah program error ketika user salah ketik
            nip_hapus = int(input("Masukkan NIP karyawan yang ingin dihapus: "))
        except ValueError: # Program tidak error tapi muncul pesan
            print("NIP harus berupa angka!")
            continue

        index_karyawan = None
        for i, pegawai in enumerate(datakaryawan): # Menampilkan no urut + data karyawan
            if pegawai['NIP'] == nip_hapus:
                index_karyawan = i
                break

        if index_karyawan is None:
            print("Data karyawan tidak ditemukan.")
            continue

        # Tampilkan data yang akan dihapus
        karyawan = datakaryawan[index_karyawan]
        print(f"\nData yang akan dihapus:")
        print(f"NIP      : {karyawan['NIP']}")
        print(f"Nama     : {karyawan['employeename']}")
        print(f"Domisili : {karyawan['domisili']}")
        print(f"Jabatan  : {karyawan['jabatan']}")
        print(f"Divisi   : {karyawan['divisi']}")

        # Konfirmasi hapus
        konfirmasi = input("\nApakah Anda yakin ingin menghapus data ini? (y/n): ").lower()
        if konfirmasi == 'y':
            datakaryawan.pop(index_karyawan) # untuk menghapus data karyawan
            print("Data karyawan berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")

    # ===================== MENU 5: KELUAR =====================
    elif userinput == '5':
        print('Anda telah keluar dari aplikasi.')

    else:
        print('Menu yang Anda pilih tidak valid. Silakan pilih angka 1-5.')
