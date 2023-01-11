#tipe data:angka satuan yg tidak ada komanya(integer)
data_integer=11
print("data: ",data_integer)
print("-bertype",type (data_integer))

#tipe data:angka yg pake koma(float)
data_float=2.8
print("data: ",data_float)
print("-bertype",type (data_float))

#tipe data:kumpulan karakter(string)
data_string="raden"
print("data: ",data_string)
print("-bertype",type (data_string))

#tipe data: biner True/False(boolean)
data_bool=True
print("data: ",data_bool)
print("-bertype",type (data_bool))

#bilangan kompleks nantinya akan muncul (j)
#yang disebut imajiner
data_complex=complex(7,8)
print("data: ",data_complex)
print("-bertype",type (data_complex))

#mengimpor tipe data dari bahasa C
from ctypes import c_double
data_c_double=c_double(10.5)
print("data: ",data_c_double)
print("-bertype",type (data_c_double))
#islower=untuk mengecek apakah semua huruf dalam elemen merupakan huruf kecil atau tidak,jika iya maka akan true,jika tidak maka akan false
a="villa"
b="Villa"
c="VILLA"
print(a.islower())
print(b.islower())
print(c.islower())
#split() -> Digunakan untuk memisahkan string sesuai dengan separator yang kita inginkan dan mengembalikan hasilnya sebagai sebuah list.
teks="halo,nama saya budi"
x=teks.split(",")
print(x)
#count()-> Digunakan untuk menghitung berapa kali sebuah value muncul dalam sebuah string
tulisan="halo lur,nang kene aku lagi karo sedulur liane,monggo mampir lur"
z=tulisan.count(",")
print(z)
