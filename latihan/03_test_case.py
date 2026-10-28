# Latihan 3 - Bug batas kelulusan: versi SUDAH diperbaiki (>= 60).
# Versi awal memakai '>' sehingga test 60 gagal.
def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


tes = [(59, "Tidak lulus"), (60, "Lulus"), (61, "Lulus")]
for nilai, expected in tes:
    actual = status_lulus(nilai)
    print(f"{nilai}: expected={expected}, actual={actual}, "
          f"{'PASS' if actual == expected else 'FAIL'}")
