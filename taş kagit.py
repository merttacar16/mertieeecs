print("Tas Kagit Makas Oyunu")

('Tas' > 'Makas')
('Tas' < 'Kagit')
('Kagit' > 'Makas')
print("Secilecek Olan Karakterler")
print("""1.Tas
2.Kagit
3.Makas""")
oyuncu1 = input("1.Oyuncu Karakter Seciniz:")
oyuncu2 = input("2.Oyuncu Karakter Seciniz:")

if(oyuncu1>oyuncu2):
	print("1.Oyuncu Kazandı");
elif(oyuncu2>oyuncu1):
	print("2.Oyuncu Kazandı"); 
else:
	print("Lütfen Tekrardan 1 ile 3 arasında bir karakter seçiniz");

