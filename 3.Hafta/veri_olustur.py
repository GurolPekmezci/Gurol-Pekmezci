import pandas as pd
import numpy as np

# Eğitim ve tekrarlanabilirlik için random seed ayarlaması
np.random.seed(42)

# Toplam oyuncu sayısı
n_players = 500

# 1'den 500'e kadar ardışık Oyuncu ID'leri
oyuncu_ids = np.arange(1, n_players + 1)

# Yorgunluk_Endeksi üretimi (Normal Dağılım: Çan Eğrisi)
# Ortalama 50, Standart Sapma 15
yorgunluk_endeksi = np.random.normal(loc=50, scale=15, size=n_players)
# Değerleri 0 ile 100 arasında sınırlandırma
yorgunluk_endeksi = np.clip(yorgunluk_endeksi, 0, 100)

# Basari_Orani (Saha İçi İsabet Yüzdesi) üretimi
# Senaryo gereği analize uygun olması için, yorgunluk arttıkça isabetin düşmesini (negatif korelasyon) sağlıyoruz.
# Rastgelelik (Çan eğrisi formu) katmak amacıyla normal dağılımlı bir "gürültü" ekliyoruz.
gürültü = np.random.normal(loc=0, scale=6, size=n_players)
basari_orani = 75 - (yorgunluk_endeksi * 0.6) + gürültü

# Yine değerleri %0 ile %100 arasında sınırlandırıyoruz
basari_orani = np.clip(basari_orani, 0, 100)

# Sözlük yapısından veriyi tablo formatına (DataFrame) çeviriyoruz
df = pd.DataFrame({
    'Oyuncu_ID': oyuncu_ids,
    'Yorgunluk_Endeksi': np.round(yorgunluk_endeksi, 2),
    'Basari_Orani': np.round(basari_orani, 2)
})

# Veriyi çalışma dizinine 'data.csv' olarak kaydediyoruz
df.to_csv('data.csv', index=False)
print("Veri üretimi tamamlandı! 'data.csv' dosyası başarıyla oluşturuldu.")
