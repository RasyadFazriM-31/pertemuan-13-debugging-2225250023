# Latihan 2 - Menelusuri fungsi
# Step Into pada hitung_diskon(200000, 10):
#   total=200000, persen=10 -> diskon=20000.0 -> return 180000.0
def hitung_diskon(total, persen):
    diskon = total * persen / 100
    return total - diskon


print(hitung_diskon(200000, 10))
