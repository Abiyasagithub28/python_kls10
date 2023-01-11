#belajar casting
#merubah tipe data ke yang lainya
#tipe data=int, str, float, boolean
import string
#import dari string ke tipe data lainya
print("====INTEGER====")
data_int= 9;
print("data =",data_int ,"type= ",type (data_int))

data_str    = str(data_int)
data_float  = float(data_int)
data_bool   = bool(data_int)#akan false jika nilai int 0

print("data =",data_str ,"type= ",type (data_str))
print("data =",data_float ,"type= ",type (data_float))
print("data =",data_bool ,"type= ",type (data_bool))

#import dari float ke tipe data lainya
print("====FLOAT====")
data_float= 2.5;
print("data =",data_float ,"type= ",type (data_float))

data_str    = str(data_float)
data_int    = int(data_float)
data_bool   = bool(data_float)#akan false jika nilai float 0

print("data =",data_str ,"type= ",type (data_str))
print("data =",data_int ,"type= ",type (data_int))
print("data =",data_bool ,"type= ",type (data_bool))

#mengubah tipe data dari bool ke lainya
print("====BOOLEAN====")
data_bool= True #False dan True diawali dengan huruf besar
print("data =",data_bool ,"type= ",type (data_bool))

data_str     = str(data_bool)
data_int     = int(data_bool)
data_float   = float(data_bool)

print("data =",data_str   ,"type= ",type (data_str))
print("data =",data_int   ,"type= ",type (data_int))
print("data =",data_float ,"type= ",type (data_float))

#import dari string ke tipe data lainya
print("====STRING====")
data_str= "1002"
print("data =",data_str ,"type= ",type (data_str))

data_int     = int(data_str)#tidak akan tercetak jika yang dimasukan huruf dari string
data_float   = float(data_str)#tidak akan tercetak jika yang dimasukan huruf dari string
data_bool    = bool(data_str)#jika ingin tercetak False,cukup dengan string saja tanpa ada tambahan apapun

print("data =",data_int   ,"type= ",type (data_int))
print("data =",data_float ,"type= ",type (data_float))
print("data =",data_bool  ,"type= ",type (data_bool))

#mengambil input data dari user

#data yang dimasukan pasti string
data=input("masukan nama :")
print("nama saya adalah :",data,"type =",type(data))

#jika ingin mengambil integer,float
angka=int(input("masukan angka :"))
nomer=float(input("masukan angka :"))
print("data :",angka,"type =",type(angka))
print("data :",nomer,"type =",type(nomer))

#jika yg ingin diambil boolean
biner=bool(input("masukan nilai boolean :"))
print("nilanya adalah :",biner,"type =",type(biner))

#jika ingin nilai  booleanya false ,maka harus ditambahi integer
biner=bool(int(input("masukan nilai boolean :")))
print("nilanya adalah :",biner,"type =",type(biner))




