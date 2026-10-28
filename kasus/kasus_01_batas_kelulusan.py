# Kasus 1: program berjalan tanpa error, tetapi nilai 60 dinyatakan tidak lulus.
def status_lulus(nilai):
    if nilai > 60:   # BUG: batas 60 seharusnya termasuk lulus (>=)
        return "Lulus"
    return "Tidak lulus"


print(status_lulus(75))
print(status_lulus(60))
print(status_lulus(59))
