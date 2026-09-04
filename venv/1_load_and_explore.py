"""
GRU ile trafik hacmi tahmini


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
