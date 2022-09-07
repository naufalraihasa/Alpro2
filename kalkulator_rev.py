def kalkulator_Versi_dua ():
    while True:
        try:
            operasi = int(input('''masukan jenis operasi yang ingin dilakukan !
            =========== perkalian (x) => 0 ===========
            =========== pembagian (/) => 1 ===========
            =========== penjumlahan (+) => 2 ===========
            =========== pengurangan (-) => 3 ===========
            => '''))

            if operasi == 0 :
                angka1 = int(input('masukan angka pertama : '))
                angka2 = int(input('masukan angka kedua : '))
                perkalian = angka1 * angka2
                print("hasil perkalian dari ",angka1," x ",angka2," adalah", perkalian)
                return perkalian

            elif operasi == 1 :
                angka1 = int(input('masukan angka pertama : '))
                angka2 = int(input('masukan angka kedua : '))
                pembagian = angka1 / angka2
                print("hasil pembagian dari ", angka1, " / ", angka2, " adalah", pembagian)
                return pembagian

            elif operasi == 2 :
                angka1 = int(input('masukan angka pertama : '))
                angka2 = int(input('masukan angka kedua : '))
                penjumlahan = angka1 + angka2
                print("hasil penjumlahan dari ", angka1, " + ", angka2, " adalah", penjumlahan)
                return penjumlahan

            elif operasi == 3 :
                angka1 = int(input('masukan angka pertama : '))
                angka2 = int(input('masukan angka kedua : '))
                pengurangan = angka1 - angka2
                print("hasil pengurangan dari ", angka1, " - ", angka2, " adalah", pengurangan)
                return pengurangan

            elif operasi > 3:
                print("error".center(55, "-"))
                print("masukan nilai yang sesuai".center(55, "-"))
                continue

        except ValueError:
            print("error".center(55,"-"))
            print("masukan nilai yang sesuai".center(55,"-"))

    kalkulator()