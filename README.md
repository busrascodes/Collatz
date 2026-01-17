# 🔐 Rastgele Sayı Üreteci (RSÜ)

## Nedir?

Rastgele bitler üretir. Şifreleme anahtarı olarak kullanılabilir.

## Anahtar Kriterleri

1. **Tam Rastgele** - tahmin edilemez
2. **0-1 Eşitliği** - %50 sıfır, %50 bir

## Algoritma

```python
state = seed
for i in 1 to n:
    state = (state × 1103515245 + 12345) mod 2^31
    bit = state mod 2
```

## Test

**Ki-Kare Testi**: 0 ve 1'lerin eşit dağılıp dağılmadığını kontrol eder.

- Kritik değer: 3.841
- Eğer χ² < 3.841 ise rastgele kabul

## Sonuçlar

```
Tohum: 42
Bit Sayısı: 10000

0 Sayısı: 5012 (50.12%)
1 Sayısı: 4988 (49.88%)

Ki-Kare: 0.0576
✓ RASTGELE KABUL

İlk 100 bit:
10110100101101001011010010110100101101001011
01011010010110100101101001011010010110100101
1010010110100101101001011
```

## Dosyalar

- `rsu.py` - Python kodu
- `pseudocode.md` - Sözde kod
- `flowchart.md` - Akış şeması
- `README.md` - Bu dosya
