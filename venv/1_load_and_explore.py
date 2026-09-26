"""
GRU ile trafik hacmi tahmini
GRU: Gated Recurrent Unit

problem tanımı: şehir içi ana yollardaki, geçmiş verilere bakarak, gelecektek saatlerdeki trafik yoğunluğunu tahmin etmek 

data: https://archive.ics.uci.edu/dataset/492/metro+interstate+traffic+volume
2012-2018 arası saatlik ölçümleri içeriyor, 48000 sample var ve hedef değişkenimiz trafik yoğunluğu
features
date_time(zaman), holiday, temp(sıcaklık kelvin cinsinden), rain-snow, clouds_all (bulutluluk oranı), wheather_main(genel hava durumu)

teknolojiler-araçlar: başlıca kütüphaneler;
pytorch : GRU tabanlı zaman serisi modeli
FastAPI web sunucu oluşturur, modelimizi rest api olarak servis etmemizi sağlar
Streamlit: web tabanlı kullanıcı arayüzü oluşturmak için kullanılır 

plan ve program 
-veri analizi (1_load_and_explore.py)
-veri ön işleme (2_preprocessing.py)
-model eğitimi(3_train.py)
-test ve değerlendirme (4_test.py)
-FastAPI servisleştirme (5_main_api.py)
-FastAPI testi (6_test_requests.py)
-Streamlit (7_app_streamlit.py)
-deployement(biz bu projede yapmayacağız)

install libraries freeze
pip install pandas numpy matplotlib seaborn scikit-learn torch fastapi uvicorn streamlit
en son projenin bağımlılıklarını ve kütüphane sürümlerini sabitlemek için  pip freeze > requirements.txt oluşturduk 
"""
import pandas as pd # veri işleme ve analizi
import numpy as np # matematiksel işlemler
import matplotlib.pyplot as plt # görselleştirme
import seaborn as sns # gelişmiş görselleştirme
# veriyi yukleme
df = pd.read_csv("Metro_Interstate_Traffic_Volume.csv") # csv dosyasını oku
print(df.head()) # ilk 5 satırı konsola yazdır
# veri çerçevesi hakkında genel bilgi (ka. satır, sütun, veri türleri, eksik veirleri...)
print(df.info())
#sütunlardaki eksik değerler
print(df.isnull().sum())
#sayısal değişkenler için temel istatistiksel öset (bu aşamalar aslında basit düzyede keşifsel veri analizi)
print(df.describe())
# zaman sütunu düzenle
df["date_time"] = pd.to_datetime(df["date_time"]) # string olarak bulunan date_time sütununu datetime objesine çeviriyoruz
df.set_index("date_time", inplace=True) # date_time index olur
print(df.head())

# zaman serisi görselleştirme
# trafik hacminin zamana göre çizdirilmesi
plt.figure()
plt.plot(df["traffic_volume"], label = "Trafik Hacmi", color = "steelblue")
plt.title("Trafik Hacmi Zaman Serisi")
plt.xlabel("Tarih")
plt.ylabel("Trafik Hacmi")
plt.legend()
plt.tight_layout()
plt.savefig("trafik_hacmi_grafigi.png") #codespacede olduğumuz için pltshow yerine
print("Grafik kaydedildi!")

