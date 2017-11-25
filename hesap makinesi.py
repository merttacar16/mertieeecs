print ("Islem Secimi")
print (""" 1.Toplama
2.Cikarma
3.Carpma
4.Bolme""")
islem = input ("Seciniz(1/2/3/4):") 
sayi1 = int(raw_input("Ilk Sayiyi Giriniz:"))
sayi2 = int(raw_input("Ikinci Sayiyi Giriniz:")) 

sayi1 = int(sayi1)
sayi2 = int(sayi2)

def topla(sayi1, sayi2):
    toplam = sayi1+sayi2
    return toplam
def cikarma(sayi1, sayi2):
    kalan = sayi1-sayi2
    return kalan
def carp(sayi1, sayi2):
	carpim = sayi1*sayi2
    return carpim
def bol(sayi1, sayi2):
	bolum = sayi1/sayi2
    return bolum 

if(islem == "1"):
	print(str(topla(sayi1,sayi2)))
elif(islem == "2"):
	print(str(cikarma(sayi1,sayi2)))
elif islem == "3":
	print(str(carp(sayi1,sayi2)))
elif (islem == "4"):
	print(str(bol(sayi1,sayi2)))	
else:
    print(str("Lütfen 1 ile 4 arasında bir işlem seçiniz"));   	
 