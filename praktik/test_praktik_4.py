"""Menjalankan test case yang SAMA terhadap versi awal dan versi perbaikan.

    python3 praktik/test_praktik_4.py awal      # harapannya ada yang FAIL
    python3 praktik/test_praktik_4.py perbaikan # harapannya semua PASS
"""
import contextlib
import importlib.util
import io
import os
import sys

NAMA_FILE = {
    "awal": "praktik_4_awal_bermasalah.py",
    "perbaikan": "praktik_4_debugging.py",
}

versi = sys.argv[1] if len(sys.argv) > 1 else "perbaikan"
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), NAMA_FILE[versi])

spec = importlib.util.spec_from_file_location("modul_uji", path)
modul = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):  # versi awal mencetak saat di-import
    spec.loader.exec_module(modul)

# (ID, target, input, expected)
TEST = [
    ("T1", "rata-rata", [80, 60, 90, 70], 75.0),
    ("T2", "rata-rata", [100, 80], 90.0),
    ("T3", "status", 60, "Lulus"),
    ("T4", "status", 59, "Tidak lulus"),
    ("T5", "tertinggi", [80, 60, 90, 70], 90),
    # tambahan: kondisi kosong, satu elemen, dan batas atas
    ("T6", "rata-rata", [], 0),
    ("T7", "tertinggi", [], None),
    ("T8", "tertinggi", [55], 55),
    ("T9", "status", 61, "Lulus"),
]

FUNGSI = {
    "rata-rata": modul.hitung_rata_rata,
    "status": modul.status,
    "tertinggi": modul.nilai_tertinggi,
}

print(f"Versi: {versi}")
print(f"{'ID':<3} | {'Target':<9} | {'Input':<18} | {'Expected':<12} | {'Actual':<22} | Status")
lulus = 0
for id_tc, target, masukan, expected in TEST:
    try:
        actual = FUNGSI[target](masukan)
    except Exception as e:  # noqa: BLE001 - dicatat sebagai hasil uji
        actual = f"{type(e).__name__}"
    ok = actual == expected
    lulus += ok
    print(f"{id_tc:<3} | {target:<9} | {str(masukan):<18} | {str(expected):<12} | "
          f"{str(actual):<22} | {'PASS' if ok else 'FAIL'}")

print(f"\nLulus {lulus}/{len(TEST)}")
raise SystemExit(0 if lulus == len(TEST) else 1)
