a="ya"
while (a=="ya")or(a=="YA")or(a=="iya") :
	b=int(input("masukan umur kamu :"))
	c=input("tolong isi NIK dibawah ini :")
	d=input("pilih stasiun awal:")
	e=input("pilih stasiun akhir:")
	f=input("pilih kereta yang ingin digunakan :")
	if b<=17:
		print("kamu tidak perlu antigen lagi")
		print("NIK :",c)
		print("stasiun awal :",d)
		print("stasiun akhir :",e)
		print("kerta yang digunakan",f)
	else:
		print("kamu harus antigenten lebih dahulu")
		print("kamu tidak perlu antigen lagi")
		print("NIK :",c)
		print("stasiun awal :",d)
		print("stasiun akhir :",e)
		print("kerta yang digunakan",f)
	a=input("apakah kamu mau mengulangi?")
print("terima kasih")
	

		