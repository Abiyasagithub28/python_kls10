#Dalam Python, operator berlaku berbeda tergantung pada tipe data.
#Hasil operasi perkalian * bilangan 100 dan 2 adalah 200.
#Namun, hasil operasi perkalian string '100' dan '2' adalah '100100'. Dengan kata lain, hasil operasi perkalian dari string 'Halo' dan numerik 2 adalah 'HaloHalo', tetapi operasi perkalian pada huruf tersebut berbeda dengan operasi perkalian pada nilai numerik.
print(10*2)#temukan perkalian numerik 10 dan 2
print("villa"*2)#temukan perkalian string'villa' dan 2
print("10"*2)#temukan perklaian string'100' dan 2
#mengubah tipe data
int('10')/2 #tidak akan error karna pada dasarnya string 10 itu angka
#ubah string '10' menjadi bilangan bulat dan dibagi dengan 2