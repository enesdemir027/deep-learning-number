import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

print(f"egitim verisi: {x_train.shape}")
print(f"test verisi: {x_test.shape}")

x_train = x_train / 255.0
x_test = x_test / 255.0


plt.figure(figsize=(12, 4))
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(x_train[i], cmap='gray')
    plt.title(f"Rakam: {y_train[i]}")
    plt.axis('off')
plt.suptitle("veri seti")
plt.tight_layout()
plt.show()


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

history = model.fit(
    x_train, y_train,
    epochs=10,
    validation_data=(x_test, y_test)
)

test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"\ndoğruluk: {test_acc:.2%}")

uploaded = files.upload()

for filename in uploaded.keys():
    from PIL import Image
    
    print(f"\yükle: {filename}")

    img = Image.open(filename).convert('L')
    img = img.resize((28, 28))
    img_array = np.array(img)

    img_array = img_array / 255.0
    img_array = 1 - img_array  # Zemin beyaz, rakam siyah olsun

    tahmin = model.predict(img_array.reshape(1, 28, 28), verbose=0)
    sonuc = np.argmax(tahmin)
    olasilik = tahmin[0][sonuc] * 100
    
    print(f"🤖 Tahmin edilen rakam: {sonuc}")
    print(f"📊 Olasılık: %{olasilik:.2f}")
    
    plt.figure(figsize=(4, 4))
    plt.imshow(img_array, cmap='gray')
    plt.title(f"Tahmin: {sonuc} ( %{olasilik:.2f} )")
    plt.axis('off')
    plt.show()

model.save('rakam.h5')
print("\n kayit edildi: rakam.h5")

files.download('rakam.h5')
