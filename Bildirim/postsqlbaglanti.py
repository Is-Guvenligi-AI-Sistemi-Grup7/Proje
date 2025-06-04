# requirements.txt
psycopg2-binary==2.9.7  # PostgreSQL için
# veya
pymysql==1.1.0  # MySQL için

import psycopg2
# Veritabanı bağlantısı
conn = psycopg2.connect(
    host="arkadaşının_ip_adresi",  # örn: 192.168.1.100
    database="veritabani_adi",
    user="kullanici_adi", 
    password="sifre",
    port="5432"  # PostgreSQL default port
)