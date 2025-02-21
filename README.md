# Valorant Instalock

Valorant Instalock, ajan seçim ekranında belirlediğiniz ajanı hızlı bir şekilde seçmenizi sağlayan bir otomasyon yazılımıdır.

## Özellikler
- Otomatik olarak ajan seçim ekranınında işlemler yapar.
- Belirlediğiniz ajanı mümkün olan en kısa sürede seçer.
- Python ve PyAutoGUI kullanılarak geliştirilmiştir.



## Kurulum ve Kullanım
1. **Depoyu Klonlayın**
```bash
git clone https://github.com/k0laa/Valorant_Instalock.git
cd Valorant_Instalock
```
2. **Bağımlılıkları Yükleyin**
```bash
pip install -r requirements.txt
```
3. **Scripti Çalıştırın**
```bash
python main.py
```
4. **Ajan Seçimi**
   - Script çalıştırıldıktan sonra ajan seçim ekranında en hızlı şekilde belirlediğiniz ajanı seçecektir.

## Dikkat Edilmesi Gerekenler
- Yazılımın düzgün çalışabilmesi için ekran çözünürlüğünüzün *1920x1080* olmalı ve UI ölçeklendirmenizin varsayılan ayarlarda olması önerilir.
- PyAutoGUI'nin ekran koordinatlarını doğru algılayabilmesi için oyunu tam ekran penceresiz modunda çalıştırmanız önerilir.
