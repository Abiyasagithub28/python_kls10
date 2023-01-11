listbulan = [
  'a','januari', 'februari', 'maret', 'april', 'mei',
  'juni', 'juli', 'agustus','october','november','desember'
]

bulanYangDicari = input('masukan bulan yang dicari: ')

for i, bulan in enumerate(listbulan):
  if bulan.lower() == bulanYangDicari.lower():
    print('bulan yang anda cari  adalah bulan ke : ', i)
    break
else:
  print('tidak adaa')
