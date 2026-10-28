# Kasus 3: program gagal ketika file kosong (ZeroDivisionError).
# Dibuat self-contained: file kosong dibuat sementara oleh program ini sendiri.
import os
import tempfile


def rata_rata_file(path):
    with open(path, "r", encoding="utf-8") as f:
        nilai = [float(b) for b in f if b.strip()]
    return sum(nilai) / len(nilai)   # BUG: len(nilai) bisa 0


with tempfile.TemporaryDirectory() as tmp:
    kosong = os.path.join(tmp, "kosong.txt")
    open(kosong, "w", encoding="utf-8").close()
    print(rata_rata_file(kosong))
