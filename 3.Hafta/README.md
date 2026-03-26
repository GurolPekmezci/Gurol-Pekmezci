# 3. Hafta - Basketbol Veri Analizi Projesi

Bu proje, bir basketbol takımındaki 500 oyuncunun **yorgunluk seviyelerinin** (fiziksel tükenmişlik), **saha içi isabet oranlarına** (şut başarı yüzdesi) olan etkisini modellemek ve analiz etmek amacıyla geliştirilmiştir. Veriler, istatistiksel açıdan gerçeğe uygun (Normal Dağılım / Çan Eğrisi) yapıdadır ve yorgunluk arttıkça başarı oranının düşeceği (negatif korelasyon) senaryosuna göre kurgulanmıştır.

## Proje Dosyaları
* **`veri_olustur.py`** : Oyuncuların Yorgunluk (0-100) ve Başarı Oranı (%0-100) verilerini sentetik ve istatistiksel standartlara (normal dağılıma) uygun şekilde üretir ve kaydeder.
* **`gorsellestir.py`** : Üretilen veriyi okuyarak seaborn ve matplotlib aracılığıyla yoğunluk dağılım (çan eğrisi) grafiklerini ve iki değişken arasındaki ilişkiyi gösteren saçılım/regresyon grafiklerini (scatter/regression plot) çizer.
* **`generate_data.py` & `visualize_data.py`** : Kodların ve açıklamalarının birebir İngilizce versiyonlarıdır. Global ve standart kullanım içindir.
* **`data.csv`** : İçerisinde 500 oyuncuya ait ID, Yorgunluk_Endeksi ve Basari_Orani bilgilerini barındıran veri kümesidir. `veri_olustur.py` çalıştırılarak elde edilir.
* **`promt.md`** : Yapay zeka ile kurulan proje geliştirme adım-adım diyalog ve Prompt (İstem) geçmişini saklayan belgedir.

## Kurulum ve Kullanım

Sistemin çalışabilmesi için cihazınızda Python ile birlikte `pandas`, `numpy`, `matplotlib` ve `seaborn` kütüphanelerinin yüklü olması gerekir. Eksikse; terminalden şu komutla yükleyebilirsiniz:
```bash
pip install pandas numpy matplotlib seaborn
```

### 1- Verileri Üretmek
Terminal (veya komut satırı) üzerinden aşağıdaki komutu çalıştırarak `data.csv` dosyasını oluşturabilirsiniz:
```bash
python veri_olustur.py
```
*(veya İngilizce versiyonu için: `python generate_data.py`)*

### 2- Grafikleri Görüntülemek
Oluşan CSV dosyasındaki analiz grafikleri, regresyon doğruları ve çan eğrisi formlarını görüntülemek (veya diske `analysis_plots.png` olarak kaydetmek) için:
```bash
python gorsellestir.py
```
*(veya İngilizce versiyonu için: `python visualize_data.py`)*
