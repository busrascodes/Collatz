import random
import math

class RSU:
    """Basit Rastgele Sayı Üreteci"""
    
    def __init__(self, seed):
        self.seed = seed
        self.state = seed
    
    def next(self):
        """Sonraki rastgele sayı"""
        self.state = (self.state * 1103515245 + 12345) % (2**31)
        return self.state
    
    def generate_bits(self, n):
        """n adet rastgele bit üret"""
        bits = []
        for _ in range(n):
            # En son biti al
            bit = self.next() % 2
            bits.append(bit)
        return bits


def ki_kare_testi(bits):
    """Ki-kare testi yapıyor"""
    n = len(bits)
    zeros = bits.count(0)
    ones = bits.count(1)
    
    expected = n / 2
    chi_square = ((zeros - expected)**2 / expected + 
                  (ones - expected)**2 / expected)
    
    # Kritik değer: 3.841
    is_random = chi_square < 3.841
    
    return {
        'zeros': zeros,
        'ones': ones,
        'chi_square': chi_square,
        'is_random': is_random
    }


def test_rsu():
    """RSÜ'yü test et"""
    print("=" * 50)
    print("RASTGELE SAYI ÜRETECI (RSÜ) TEST")
    print("=" * 50)
    
    # Bit üret
    rsu = RSU(seed=42)
    bits = rsu.generate_bits(10000)
    
    # Sonuçlar
    result = ki_kare_testi(bits)
    
    # Yazdır
    print(f"\nTohum: 42")
    print(f"Bit Sayısı: 10000")
    print(f"\n0 Sayısı: {result['zeros']} ({result['zeros']/100:.1f}%)")
    print(f"1 Sayısı: {result['ones']} ({result['ones']/100:.1f}%)")
    print(f"\nKi-Kare Değeri: {result['chi_square']:.4f}")
    print(f"Kritik Değer: 3.841")
    
    if result['is_random']:
        print("\n✓ RASTGELE KABUL EDİLDİ")
    else:
        print("\n✗ RASTGELE DEĞİL")
    
    # İlk 100 bit göster
    print(f"\nİlk 100 bit:")
    print(''.join(map(str, bits[:100])))
    
    print("\n" + "=" * 50)


if __name__ == "__main__":
    test_rsu()