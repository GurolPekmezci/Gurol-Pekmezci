import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Veriyi oku
if not os.path.exists('data.csv'):
    print("Hata: 'data.csv' dosyası bulunamadı. Lütfen önce veri_olustur.py dosyasını çalıştırın.")
    exit()

df = pd.read_csv('data.csv')

# Grafik tasarımını ayarla
sns.set_theme(style="whitegrid")
plt.figure(figsize=(18, 6))

# 1. Grafik: Yorgunluk Endeksi Çan Eğrisi (Dağılım Grafiği)
plt.subplot(1, 3, 1)
sns.histplot(df['Yorgunluk_Endeksi'], kde=True, color='red', stat='density', bins=25)
plt.title('Yorgunluk Endeksi Dağılımı (Çan Eğrisi)', fontsize=14)
plt.xlabel('Yorgunluk Endeksi (0-100)', fontsize=12)
plt.ylabel('Yoğunluk', fontsize=12)

# 2. Grafik: Başarı Oranı Çan Eğrisi (Dağılım Grafiği)
plt.subplot(1, 3, 2)
sns.histplot(df['Basari_Orani'], kde=True, color='blue', stat='density', bins=25)
plt.title('Saha İçi İsabet Oranı Dağılımı (Çan Eğrisi)', fontsize=14)
plt.xlabel('İsabet Oranı (%)', fontsize=12)
plt.ylabel('Yoğunluk', fontsize=12)

# 3. Grafik: Yorgunluk vs İsabet Oranı Analizi (Regresyon ile Dağılım)
plt.subplot(1, 3, 3)
sns.regplot(
    x='Yorgunluk_Endeksi', 
    y='Basari_Orani', 
    data=df, 
    scatter_kws={'alpha': 0.6, 'color': 'purple', 's': 20}, 
    line_kws={'color': 'black', 'linewidth': 2}
)
plt.title('Yorgunluk vs İsabet Oranı Analizi', fontsize=14)
plt.xlabel('Yorgunluk Endeksi', fontsize=12)
plt.ylabel('İsabet Oranı (%)', fontsize=12)

# Grafikleri estetik olarak yerleştir
plt.tight_layout()

# Grafiği kaydet (opsiyonel)
plt.savefig('analiz_grafikleri.png', dpi=300)

print("Görselleştirme tamamlandı! 'analiz_grafikleri.png' kaydedildi.")
# Grafikleri ekranda göster
plt.show()
