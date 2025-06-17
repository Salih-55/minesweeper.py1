# Minesweeper - Python Console Game

## Proje Hakkında

Bu proje, klasik **Mayın Tarlası (Minesweeper)** oyununu Python programlama dili kullanarak konsol ortamında yeniden yaratmayı amaçlamaktadır. Oyun, oyuncunun mayınları tahmin edip güvenli alanları açmaya çalıştığı stratejik bir bulmaca oyunudur.

---

## Özellikler

- **Dinamik Oyun Tahtası:** Oyuncu tarafından belirlenen boyutta kare bir oyun tahtası oluşturulur (3x3 ile 20x20 arasında).
- **Rastgele Mayın Yerleştirme:** Belirlenen sayıda mayın, oyun tahtasına rastgele yerleştirilir.
- **Mayın Sayısı Gösterimi:** Her açılan hücre, çevresindeki mayınların sayısını gösterir.
- **Hücre Açma ve Rekürsif Temizleme:** 0 mayınlı hücre açıldığında, komşu hücreler otomatik olarak açılır.
- **Oyuncu Kazanma/Kaybetme Kontrolü:** Tüm güvenli hücreler açıldığında oyuncu kazanır. Mayına basıldığında oyun biter.
- **Basit Konsol Arayüzü:** Kolay anlaşılır ve kullanımı basit metin tabanlı oyun arayüzü.

---

## Dosya Yapısı

- `minesweeper.py`: Oyunun ana kodlarını içeren Python dosyası.
- `Test.minesweeper.py`: Board sınıfı için birim testlerin yazıldığı dosya.
- `README.md`: Projenin bu açıklama dosyası.

---

## Kullanım

1. Python 3.x yüklü olduğundan emin olun.  
2. Terminal veya PyCharm gibi IDE’de `minesweeper.py` dosyasını çalıştırın:

```bash
python minesweeper.py
