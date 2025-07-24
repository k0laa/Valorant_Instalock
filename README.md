<img title="" src="images\default.jpg" alt="Valorant Instalock" data-align="left" style="zoom:50%;">

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
  python app.py
```

veya:

4. **app.exe dosyası oluşturma**

```bash
  pyinstaller --onefile --noconsole app.py
```

exe doyası oluşturulduktan sonra `dist` klasöründe `app.exe` dosyasını bulabilirsiniz.

**UYARI**: `app.exe` doyasını `dist` klasöründen çıkarmayınız. Aksi taktirde uygulama düzgün çalışmayacaktır. Kısayol oluşturup masaüstüne taşıyabilirsiniz.

5. **Ajan Seçimi**
   - uygulamayı çalıştırdıktgan sonra valorant hesabınızıdaki açık olan ajanları işaretleyin.
   - oyun içinde sırada olduğunuzdan emin olun ve oyun bulunduktan sonra seri şekilde uygulamadaki "seç" butonuna tıklayın ve bekleyin.
   - ajan seçtikten sonra uygulamayı durdurmak için q tuşuna bir kaç saniye basılı tutun yada 30 saniye bekleyin.

## Dikkat Edilmesi Gerekenler

- Yazılımın düzgün çalışabilmesi için ekran çözünürlüğünüzün
  ***1920x1080*** olmalı ve UI ölçeklendirmenizin varsayılan ayarlarda olması önerilir.
- PyAutoGUI'nin ekran koordinatlarını doğru algılayabilmesi için oyunu tam ekran penceresiz modunda çalıştırmanız önerilir.


