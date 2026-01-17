# RSÜ - Basit Sözde Kod

## Algoritma

```
ALGORİTMA RSU(seed)

1. state = seed

2. n kere tekrarla:
   a. state = (state × 1103515245 + 12345) mod 2^31
   b. bit = state mod 2
   c. bit'i diziye ekle

3. Dönüş: bit dizisi
```

## Ki-Kare Testi

```
ALGORİTMA KiKareTesti(bits)

1. n = bits'in uzunluğu
2. zeros = bits'deki 0 sayısı
3. ones = bits'deki 1 sayısı

4. expected = n / 2

5. chi_square = ((zeros - expected)² / expected) +
                ((ones - expected)² / expected)

6. Eğer chi_square < 3.841:
      Rastgele KABUL
   Değilse:
      Rastgele DEĞİL
```