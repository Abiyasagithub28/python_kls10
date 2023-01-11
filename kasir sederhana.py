a=int(input("harga buku RP.3000 :"))
b=a*3000
c=int(input("harga pulpen RP.2000 :"))
d=c*2000
e=int(input("harga spidol RP.5000 :"))
f=e*5000
g=int(input("harga gantungan RP.5000 :"))
h=g*5000
i=int(input("harga pensil RP.4000 :"))
j=i*4000
k=int(input("harga label RP.6000 :"))
l=k*6000
m=int(input("harga penghapus RP.2000 :"))
n=m*2000
o=int(input("harga papan tulis RP.7000 :"))
p=o*7000
q=int(input("harga tipex RP.3000 :"))
r=q*3000
s=int(input("harga golok RP.5000 :"))
t=s*5000

total_barang=(a+c+e+g+i+k+m+o+q+s)
total_harga=(b+d+f+h+j+i+n+r+t)
if total_barang >= 5:
    print("kamu mendapat diskon 50%")
    diskon = total_harga * 50/100
    print("total yg dibayar : Rp.",diskon)
elif total_barang >= 7:
    print("kamu mendapat diskon 50%")
    diskon = total_harga * 70/100
    print("total yg dibayar : Rp.",diskon)
else :
    print("total yg harus dibayar :Rp.",total_harga)
