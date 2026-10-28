# Pertemuan 13 - Debugging dan Testing

Nama: Rasyad Fazri Mulyono
NIM: 2225250023
Kelas: 3A

## Kasus
Program pengolah nilai (`praktik/praktik_4_awal_bermasalah.py`) berjalan tanpa SyntaxError tetapi menghasilkan output salah: rata-rata, status nilai 60, dan nilai tertinggi. Versi awal disimpan apa adanya; versi perbaikan ada di `praktik/praktik_4_debugging.py`.

Output aktual versi awal untuk `[80, 60, 90, 70]`:
```
Rata-rata: 60.0     (seharusnya 75.0)
Status 60: Tidak lulus   (seharusnya Lulus)
Tertinggi: 0        (seharusnya 90)
```

## Test Case
Test yang sama dijalankan pada kedua versi (`praktik/test_praktik_4.py`). T1-T5 dari modul, T6-T9 tambahan.

| ID | Target | Input | Expected | Actual Awal | Status Awal | Actual Setelah | Status Setelah |
|----|--------|-------|----------|-------------|-------------|----------------|----------------|
| T1 | rata-rata | [80, 60, 90, 70] | 75.0 | 60.0 | FAIL | 75.0 | PASS |
| T2 | rata-rata | [100, 80] | 90.0 | 36.0 | FAIL | 90.0 | PASS |
| T3 | status | 60 | Lulus | Tidak lulus | FAIL | Lulus | PASS |
| T4 | status | 59 | Tidak lulus | Tidak lulus | PASS | Tidak lulus | PASS |
| T5 | tertinggi | [80, 60, 90, 70] | 90 | 0 | FAIL | 90 | PASS |
| T6 | rata-rata | [] | 0 | 0.0 | PASS | 0 | PASS |
| T7 | tertinggi | [] | None | 0 | FAIL | None | PASS |
| T8 | tertinggi | [55] | 55 | 0 | FAIL | 55 | PASS |
| T9 | status | 61 | Lulus | Lulus | PASS | Lulus | PASS |

Versi awal: 3/9 PASS. Versi perbaikan: 9/9 PASS.

Catatan: T6 lolos pada versi awal hanya kebetulan, karena `0 / 5 = 0.0`. Ini contoh program yang tampak benar pada satu kasus tetapi salah secara logika.

## Bug Report
| Bug ID | Gejala | Test | Lokasi | Akar penyebab | Perbaikan | Retest |
|--------|--------|------|--------|---------------|-----------|--------|
| B01 | Rata-rata 60.0 dan 36.0 | T1, T2 | `hitung_rata_rata`, `/ 5` | Pembagi di-hardcode 5, hanya benar bila datanya tepat 5 buah | `sum(nilai) / len(nilai)` dan cek list kosong | PASS |
| B02 | Nilai 60 tidak lulus | T3 | `status`, `nilai > 60` | Operator `>` mengecualikan batas; seharusnya `>=` | Ubah menjadi `>=` | PASS |
| B03 | Tertinggi selalu 0 | T5, T7, T8 | `nilai_tertinggi` | Dua penyebab: nilai awal `0` (bukan elemen data) dan operator `<` terbalik, sehingga tak pernah berubah | Mulai dari `nilai[0]`, bandingkan dengan `>`, tangani list kosong (`None`) | PASS |

Bukti tracing B03 untuk `[80, 60, 90, 70]` pada versi awal: `tertinggi` = 0; untuk x = 80, 60, 90, 70 kondisi `x < 0` selalu False sehingga tidak pernah berubah dan hasil tetap 0.

Seluruh perbaikan berupa perubahan minimal, lalu semua test dijalankan ulang (tidak ada regresi pada T4, T9).

## Retest
`python3 praktik/test_praktik_4.py perbaikan` menghasilkan **9/9 PASS**.
Versi perbaikan: `Rata-rata: 75.0`, `Status 60: Lulus`, `Tertinggi: 90`.

## Cara Menjalankan
Dari root folder proyek:
```
python3 praktik/praktik_4_debugging.py
python3 praktik/test_praktik_4.py awal
python3 praktik/test_praktik_4.py perbaikan
```
Kasus dan latihan: `python3 kasus/kasus_01_batas_kelulusan.py` dst. (`kasus_03` sengaja berakhir `ZeroDivisionError` sebagai bahan analisis traceback).

## Refleksi
Teknik yang paling membantu adalah menulis test case dulu, terutama nilai batas (60) dan data kosong. Satu test yang gagal langsung menunjukkan lokasi bug, sedangkan program awal yang hanya dijalankan sekali terlihat "jalan" tetapi menyimpan tiga kesalahan logika.

## Referensi/Bantuan
Bahan ajar Pertemuan 13, Python 3 Documentation, VS Code Debugging Python. Dibantu Claude untuk menyusun test, tabel, dan dokumentasi; penulis wajib dapat menjelaskan analisis dan perbaikannya.
