# 🧠 El Yazısı Rakam Tanıma - Deep Learning

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&duration=3000&pause=500&color=2D9C7C&center=true&vCenter=true&width=550&lines=MNIST+%7C+TensorFlow+%7C+97.66%25+Do%C4%9Fruluk" />
</p>
<p align="center">
  <img src="https://img.shields.io/badge/TensorFlow-2.19.0-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/Doğruluk-97.66%25-2D9C7C?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Veri-MNIST-3776AB?style=for-the-badge" />
</p>

---

## 📌 Proje Hakkında

Bu proje, **MNIST veri seti** kullanılarak eğitilmiş bir **derin öğrenme modelidir**. El yazısıyla yazılmış rakamları (0-9) tanıyabilir.

- 🎯 **Test Doğruluğu:** %97.66
- 🏗️ **Model Mimarisi:** Dense (128-64) + Dropout
- ⚙️ **Optimizer:** Adam
- 📉 **Kayıp Fonksiyonu:** Sparse Categorical Crossentropy

---

## 🛠️ Kullanılan Teknolojiler

| Teknoloji | Versiyon |
|-----------|----------|
| Python | 3.12+ |
| TensorFlow | 2.19.0 |
| NumPy | - |
| Matplotlib | - |
| Pillow | - |

## 📊 Model Mimarisi

| Katman (Layer) | Çıktı Şekli (Output Shape) | Parametre Sayısı |
|----------------|---------------------------|------------------|
| flatten (Flatten) | (None, 784) | 0 |
| dense (Dense) | (None, 128) | 100,480 |
| dropout (Dropout) | (None, 128) | 0 |
| dense_1 (Dense) | (None, 64) | 8,256 |
| dense_2 (Dense) | (None, 10) | 650 |

**Toplam Parametre:** 109,386

## 📈 Eğitim Sonuçları

| Epoch | Eğitim Doğruluğu | Test Doğruluğu | Eğitim Kaybı | Test Kaybı |
|-------|------------------|----------------|--------------|------------|
| 1 | 91.38% | 95.84% | 0.2879 | 0.1341 |
| 2 | 95.87% | 97.01% | 0.1356 | 0.0966 |
| 3 | 96.75% | 97.10% | 0.1050 | 0.0973 |
| 4 | 97.14% | 97.38% | 0.0891 | 0.0803 |
| 5 | 97.60% | 97.35% | 0.0756 | 0.0842 |
| 6 | 97.83% | 97.57% | 0.0675 | 0.0753 |
| 7 | 97.95% | 97.64% | 0.0626 | 0.0840 |
| 8 | 98.18% | 97.90% | 0.0561 | 0.0736 |
| 9 | 98.29% | 98.10% | 0.0518 | 0.0692 |
| 10 | **98.33%** | **97.66%** | 0.0500 | 0.0846 |

---

## 🚀 Çalıştırma

### 1. Gereksinimleri Yükle

```bash
pip install tensorflow numpy matplotlib pillow
2. Modeli Yükle ve Test Et
python
import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image


model = keras.models.load_model('rakam.h5')


img = Image.open('rakam.png').convert('L')
img = img.resize((28, 28))
img_array = np.array(img) / 255.0
img_array = 1 - img_arra

tahmin = model.predict(img_array.reshape(1, 28, 28))
sonuc = np.argmax(tahmin)
print(f"Tahmin edilen rakam: {sonuc}")
📥 Model Dosyası
Eğitilmiş model: rakam.h5

📊 Örnek Çıktı
text
🎯 Test Doğruluğu: 97.66%
🤖 Tahmin edilen rakam: 9
📊 Olasılık: %99.85
🧪 Kendi Rakamınla Dene
Beyaz bir kağıda siyah kalemle rakam yaz

Fotoğrafını çek

Resmi 28x28 boyutuna getir

Yukarıdaki kodu çalıştır

