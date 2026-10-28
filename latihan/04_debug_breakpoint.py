# Latihan 4 - Bug rata-rata: versi SUDAH diperbaiki.
# Pasang breakpoint pada baris 'total = sum(data)' lalu amati panel Variables.
def rata_rata(data):
    if len(data) == 0:
        return 0
    total = sum(data)
    return total / len(data)


print(rata_rata([80, 90, 70]))      # 80.0
print(rata_rata([100, 80]))         # 90.0
print(rata_rata([75]))              # 75.0
print(rata_rata([]))                # 0 (tidak ZeroDivisionError)
