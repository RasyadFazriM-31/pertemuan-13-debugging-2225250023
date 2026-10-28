# Latihan 1 - Tracing perulangan
# Tabel tracing (i, total sebelum, total sesudah):
#   i=1: 1 -> 1
#   i=2: 1 -> 2
#   i=3: 2 -> 6
#   i=4: 6 -> 24
# Prediksi output: 24 (yaitu 4!)
total = 1
for i in range(1, 5):
    total = total * i
print(total)
