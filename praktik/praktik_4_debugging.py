# Program SESUDAH perbaikan (perubahan minimal pada tiap bug).
def hitung_rata_rata(nilai):
    if len(nilai) == 0:          # B01: tangani list kosong
        return 0
    return sum(nilai) / len(nilai)   # B01: pembagi mengikuti jumlah data


def status(nilai):
    if nilai >= 60:              # B02: batas 60 termasuk lulus
        return "Lulus"
    return "Tidak lulus"


def nilai_tertinggi(nilai):
    if len(nilai) == 0:          # B03: tangani list kosong
        return None
    tertinggi = nilai[0]         # B03: mulai dari elemen pertama, bukan 0
    for x in nilai[1:]:
        if x > tertinggi:        # B03: operator dibalik (> bukan <)
            tertinggi = x
    return tertinggi


if __name__ == "__main__":
    nilai = [80, 60, 90, 70]
    print("Rata-rata:", hitung_rata_rata(nilai))
    print("Status 60:", status(60))
    print("Tertinggi:", nilai_tertinggi(nilai))
