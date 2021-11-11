#Data
Ikan = 25000
Es = 6000
Rujak = 8000

#Proses
print("=====MASUKKAN JUMLAH YANG DIPESAN=====")
a = int(input("IKAN BAKAR       Rp 25.000,00   : "))
b = int(input("ES DOGER         Rp 6.000,00    : "))
c = int(input("RUJAK CINGUR     Rp 8.000,00    : "))

#Total harga per item
a1 = Ikan*a
b1 = Es*b
c1 = Rujak*c

print("=====TOTAL=====")
print("TOTAL IKAN BAKAR        : Rp ",a1)
print("TOTAL ES DOGER          : Rp ",b1)
print("TOTAL RUJAK CINGUR      : Rp ",c1)

#Total

total = a1+b1+c1
print("Jumlah total biaya yang harus dibayar adalah Rp",total)
