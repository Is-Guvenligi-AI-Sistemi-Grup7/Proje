import time
import threading
from datetime import datetime
import os
from dotenv import load_dotenv

# Kendi modüllerimizi import et
from database_setup import DatabaseManager
from email_sender import send_alert_email, send_email
# from twilio_sender import send_sms  # SMS için ayrı dosya oluşturacağız

load_dotenv()

class SecuritySystem:
    def __init__(self):
        self.db = DatabaseManager()
        self.is_running = False
        self.monitoring_thread = None
        
        print("🛡️ Güvenlik Sistemi başlatılıyor...")
        
    def start_monitoring(self):
        """Sistem izleme başlat"""
        self.is_running = True
        self.monitoring_thread = threading.Thread(target=self._monitor_loop)
        self.monitoring_thread.start()
        print("✅ İzleme sistemi başlatıldı")
    
    def stop_monitoring(self):
        """Sistem izleme durdur"""
        self.is_running = False
        if self.monitoring_thread:
            self.monitoring_thread.join()
        print("⏹️ İzleme sistemi durduruldu")
    
    def _monitor_loop(self):
        """Ana izleme döngüsü - arka planda sürekli çalışır"""
        while self.is_running:
            try:
                # Burada sensör verilerini kontrol ederiz
                # Arduino'dan veri gelirse bu fonksiyon tetiklenir
                self._check_for_new_alerts()
                time.sleep(1)  # 1 saniye bekle
                
            except Exception as e:
                print(f"⚠️ İzleme hatası: {e}")
                time.sleep(5)
    
    def _check_for_new_alerts(self):
        """Yeni uyarıları kontrol et ve bildirim gönder"""
        # Database'de bildirim gönderilmemiş kayıtları bul
        # Bu fonksiyon gerçek sensör verilerini kontrol edecek
        pass
    
    def process_sensor_data(self, sensor_type, location, value):
        """Sensör verisini işle ve gerekirse uyarı gönder"""
        print(f"📊 Sensör verisi: {sensor_type} - {location} - {value}")
        
        # Sensör değerini analiz et
        alert_needed = self._analyze_sensor_data(sensor_type, value)
        
        if alert_needed:
            # Database'e kaydet
            sensor_id = self.db.add_sensor_data(sensor_type, location, value, "alert")
            
            # Acil durum kaydı oluştur
            message = self._create_alert_message(sensor_type, location, value)
            log_id = self.db.add_emergency_log(sensor_type, message, location, "high")
            
            # Bildirimleri gönder
            self._send_notifications(message, sensor_type)
            
        else:
            # Normal veri kaydet
            self.db.add_sensor_data(sensor_type, location, value, "normal")
    
    def _analyze_sensor_data(self, sensor_type, value):
        """Sensör verisini analiz et, uyarı gerekip gerekmediğini belirle"""
        alert_thresholds = {
            "motion": 0.5,      # Hareket sensörü eşiği
            "door": 0.5,        # Kapı sensörü eşiği  
            "temperature": 35,   # Sıcaklık eşiği
            "smoke": 0.3,       # Duman sensörü eşiği
            "sound": 0.7        # Ses sensörü eşiği
        }
        
        threshold = alert_thresholds.get(sensor_type, 0.5)
        return value > threshold
    
    def _create_alert_message(self, sensor_type, location, value):
        """Uyarı mesajı oluştur"""
        messages = {
            "motion": f"🚶 {location} konumunda hareket tespit edildi! Değer: {value}",
            "door": f"🚪 {location} kapısı açıldı! Değer: {value}",
            "temperature": f"🌡️ {location} konumunda yüksek sıcaklık! {value}°C",
            "smoke": f"🔥 {location} konumunda duman tespit edildi! Değer: {value}",
            "sound": f"🔊 {location} konumunda yüksek ses tespit edildi! Değer: {value}"
        }
        
        return messages.get(sensor_type, f"⚠️ {location} konumunda {sensor_type} sensörü tetiklendi!")
    
    def _send_notifications(self, message, alert_type):
        """Tüm bildirimleri gönder"""
        print(f"📢 Bildirim gönderiliyor: {message}")
        
        # Email bildirimleri
        email_recipients = self.db.get_notification_recipients("email")
        for email in email_recipients:
            try:
                send_alert_email(email, message)
                print(f"✅ Email gönderildi: {email}")
            except Exception as e:
                print(f"❌ Email hatası {email}: {e}")
        
        # SMS bildirimleri (ileride eklenecek)
        # sms_recipients = self.db.get_notification_recipients("sms")
        # for phone in sms_recipients:
        #     send_sms(phone, message)
    
    def add_notification_recipient(self, type, recipient):
        """Yeni bildirim alıcısı ekle"""
        self.db.add_notification_recipient(type, recipient)
    
    def get_system_status(self):
        """Sistem durumunu getir"""
        recent_alerts = self.db.get_recent_alerts(5)
        return {
            "system_running": self.is_running,
            "recent_alerts": recent_alerts,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def simulate_sensor_trigger(self, sensor_type="motion", location="test_kapı", value=1.0):
        """Test için sensör tetikleme simülasyonu"""
        print(f"🧪 Sensör simülasyonu: {sensor_type}")
        self.process_sensor_data(sensor_type, location, value)

# Ana çalıştırma
if __name__ == "__main__":
    # Güvenlik sistemini başlat
    security = SecuritySystem()
    
    # Bildirim alıcıları ekle
    security.add_notification_recipient("email", "halimebuse60@gmail.com")
    
    # Sistem izlemeyi başlat
    security.start_monitoring()
    
    try:
        print("🛡️ Güvenlik sistemi aktif - Testler başlıyor...")
        
        # Test 1: Hareket sensörü
        time.sleep(2)
        security.simulate_sensor_trigger("motion", "ana_kapı", 1.0)
        
        # Test 2: Kapı sensörü  
        time.sleep(3)
        security.simulate_sensor_trigger("door", "arka_kapı", 0.8)
        
        # Test 3: Normal veri (uyarı yok)
        time.sleep(3)
        security.simulate_sensor_trigger("temperature", "salon", 25.0)
        
        # Sistem durumunu göster
        time.sleep(2)
        status = security.get_system_status()
        print(f"\n📊 Sistem Durumu: {status}")
        
        # Sistemi çalışır durumda tut
        print("\n✋ Sistemi durdurmak için Ctrl+C basın...")
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Sistem kapatılıyor...")
        security.stop_monitoring()
        print("✅ Güvenlik sistemi kapatıldı")
