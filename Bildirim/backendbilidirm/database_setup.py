import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.connect()
    
    def connect(self):
        """PostgreSQL veritabanına bağlan"""
        try:
            self.connection = psycopg2.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                port=os.getenv('DB_PORT', '5432'),
                database=os.getenv('DB_NAME', 'safety_system'),
                user=os.getenv('DB_USER', 'postgres'),
                password=os.getenv('DB_PASSWORD')
            )
            print("✅ Veritabanına bağlanıldı")
        except Exception as e:
            print(f"❌ Veritabanı bağlantı hatası: {e}")
    
    def create_tables(self):
        """Güvenlik sistemi için gerekli tabloları oluştur"""
        try:
            cursor = self.connection.cursor()
            
            # Sensör verileri tablosu
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sensor_data (
                    id SERIAL PRIMARY KEY,
                    sensor_type VARCHAR(50) NOT NULL,
                    sensor_location VARCHAR(100) NOT NULL,
                    value FLOAT NOT NULL,
                    status VARCHAR(20) NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    alert_sent BOOLEAN DEFAULT FALSE
                )
            """)
            
            # Acil durum kayıtları tablosu
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS emergency_logs (
                    id SERIAL PRIMARY KEY,
                    alert_type VARCHAR(50) NOT NULL,
                    message TEXT NOT NULL,
                    location VARCHAR(100),
                    severity VARCHAR(20) DEFAULT 'medium',
                    resolved BOOLEAN DEFAULT FALSE,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Bildirim ayarları tablosu
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS notification_settings (
                    id SERIAL PRIMARY KEY,
                    notification_type VARCHAR(20) NOT NULL,
                    recipient VARCHAR(100) NOT NULL,
                    active BOOLEAN DEFAULT TRUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            self.connection.commit()
            print("✅ Tablolar oluşturuldu")
            
        except Exception as e:
            print(f"❌ Tablo oluşturma hatası: {e}")
    
    def add_sensor_data(self, sensor_type, location, value, status):
        """Sensör verisi ekle"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO sensor_data (sensor_type, sensor_location, value, status)
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """, (sensor_type, location, value, status))
            
            record_id = cursor.fetchone()[0]
            self.connection.commit()
            print(f"✅ Sensör verisi eklendi: ID {record_id}")
            return record_id
            
        except Exception as e:
            print(f"❌ Veri ekleme hatası: {e}")
            return None
    
    def add_emergency_log(self, alert_type, message, location, severity="medium"):
        """Acil durum kaydı ekle"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO emergency_logs (alert_type, message, location, severity)
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """, (alert_type, message, location, severity))
            
            log_id = cursor.fetchone()[0]
            self.connection.commit()
            print(f"✅ Acil durum kaydı eklendi: ID {log_id}")
            return log_id
            
        except Exception as e:
            print(f"❌ Acil durum kaydı hatası: {e}")
            return None
    
    def get_recent_alerts(self, limit=10):
        """Son uyarıları getir"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT alert_type, message, location, severity, timestamp, resolved
                FROM emergency_logs
                ORDER BY timestamp DESC
                LIMIT %s
            """, (limit,))
            
            return cursor.fetchall()
            
        except Exception as e:
            print(f"❌ Veri okuma hatası: {e}")
            return []
    
    def add_notification_recipient(self, notification_type, recipient):
        """Bildirim alıcısı ekle (email veya telefon)"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO notification_settings (notification_type, recipient)
                VALUES (%s, %s)
            """, (notification_type, recipient))
            
            self.connection.commit()
            print(f"✅ Bildirim alıcısı eklendi: {recipient}")
            
        except Exception as e:
            print(f"❌ Alıcı ekleme hatası: {e}")
    
    def get_notification_recipients(self, notification_type):
        """Bildirim alıcılarını getir"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT recipient FROM notification_settings
                WHERE notification_type = %s AND active = TRUE
            """, (notification_type,))
            
            return [row[0] for row in cursor.fetchall()]
            
        except Exception as e:
            print(f"❌ Alıcı listeleme hatası: {e}")
            return []

# Test ve kurulum
if __name__ == "__main__":
    # Database manager oluştur
    db = DatabaseManager()
    
    # Tabloları oluştur
    db.create_tables()
    
    # Test verileri ekle
    db.add_notification_recipient("email", "halimebuse60@gmail.com")
    db.add_notification_recipient("sms", "+905510743960")
    
    # Test sensör verisi
    db.add_sensor_data("motion", "ana_kapı", 1, "alert")
    db.add_emergency_log("motion_detected", "Ana kapıda hareket tespit edildi", "ana_kapı", "high")
    
    print("\n--- Son Uyarılar ---")
    alerts = db.get_recent_alerts(5)
    for alert in alerts:
        print(f"{alert[4]}: {alert[0]} - {alert[1]}")
