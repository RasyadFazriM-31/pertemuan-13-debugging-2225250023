# Kasus 2: benar untuk satu data, salah untuk data lain.
def rata_rata(data):
    total = sum(data)
    return total / 5   # BUG: pembagi di-hardcode 5


print(rata_rata([80, 90, 70]))   # seharusnya 80.0
print(rata_rata([50, 50, 50, 50, 50]))   # kebetulan benar: 50.0
