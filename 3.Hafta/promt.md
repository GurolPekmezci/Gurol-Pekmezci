# 3. Hafta - Proje Prompt (İstem) ve Etkileşim Geçmişi

Bu dosya, projenin oluşturulması sırasında yapay zeka ile yapılan konuşmaların ve verilen komutların bir özetidir.

## 1. İlk İstek (Proje Başlangıcı)
**Kullanıcı:**
> Yeni bir klasör oluştur, adı "3. hafta" olsun. İçinde bir Python kodu olsun, bu kod "data.csv" dosyasını oluştursun. Dosyada 3 sütunda 500 basketbol oyuncusunun verisi yer almalı:
> 
> Oyuncu_ID: 1'den 500'e kadar sıralı kimlik numaraları.
> 
> Yorgunluk_Endeksi: 0 ile 100 arasında, oyuncuların maç sonundaki fiziksel tükenmişlik seviyelerini temsil eden normal dağılımlı (çan eğrisi) veriler.
> 
> Basari_Orani: %0 ile %100 arasında, oyuncuların şut isabet yüzdelerini temsil eden normal dağılımlı (çan eğrisi) veriler.
> 
> Bu verileri bir basketbol takımındaki oyuncuların yorgunluk seviyelerinin saha içi isabet oranlarına etkisini analiz etmek için kullanacağız. Veri setinin kurgusunu bu performans metriği üzerine açıkla ve görselleştirme (çan eğrisi grafiği) için de ayrı bir kod hazırla.

**Yapay Zeka Yanıtı ve İşlem:**
- `3.Hafta` klasörü aktif çalışma alanı olarak kullanıldı.
- `veri_olustur.py` dosyası yazıldı ve çalıştırılarak `data.csv` verisi oluşturuldu. (Yorgunluk ile Başarı oranı arasına, analizi daha anlamlı kılmak için negatif yönde bir korelasyon eklendi ve rastgele gürültü ile normal dağılımları sağlandı.)
- Verileri görselleştirmek için `gorsellestir.py` dosyası yazıldı.
- Kullanıcıya sistemin mantığı ("Takıma ait yorgunluk arttıkça isabetin düştüğü analitik bir yapı kuruldu") anlatıldı.

---

## 2. İkinci İstek (İngilizce Dosyaların Üretilmesi)
**Kullanıcı:**
> generate_date.py dosyası ve visualize_data.py dosyalarını da oluştururmusun

**Yapay Zeka Yanıtı ve İşlem:**
- Hatalı yazılan "generate_date.py" ismi, doğru formu olan `generate_data.py` olarak düzeltildi.
- Türkçe kodların ve değişkenlerin/yorum satırlarının İngilizce versiyonlarını içeren `generate_data.py` ve `visualize_data.py` adlı iki yeni kod eklendi.

---

## 3. Üçüncü İstek (Bütün Konuşmaların Kaydedilmesi)
**Kullanıcı:**
> bana bu konuşmaları pront.md dosyasına çevirirmisin

**Yapay Zeka Yanıtı ve İşlem:**
- İstek üzerine, konuşma metinlerini ve süreç boyunca yapılan komut aktarımlarını içeren `pront.md` belge dosyası oluşturuldu.
