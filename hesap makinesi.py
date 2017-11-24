print ("Islem Secimi")
print (""" 1.Toplama
2.Cikarma
3.Carpma
4.Bolme""")
islem = input ("Seciniz(1/2/3/4):") 
sayi1 = input ("Ilk Sayiyi Giriniz:")
sayi2 = input ("Ikinci Sayiyi Giriniz:") 

sayi1 = int(sayi1)
sayi2 = int(sayi2)

if(islem == "1"):
	print(sayi1+sayi2);
elif(islem == "2"):
	print(sayi1-sayi2);
elif islem == "3":
    print (sayi1*sayi2);
elif (islem == "4"):
    print(sayi1/sayi2);  
else:
    print("Lütfen 1 ile 4 arasında bir işlem seçiniz");   	
 