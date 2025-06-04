import sendgrid
import os
import json
from dotenv import load_dotenv
from sendgrid.helpers.mail import Mail

load_dotenv()

def detailed_sendgrid_test():
    api_key = os.getenv('SENDGRID_API_KEY')
    from_email = os.getenv('SENDGRID_FROM_EMAIL')
    
    print("=== SendGrid Detaylı Test ===")
    print(f"API Key: {api_key[:10]}...{api_key[-10:] if len(api_key) > 20 else ''}")
    print(f"From Email: {from_email}")
    
    try:
        sg = sendgrid.SendGridAPIClient(api_key=api_key)
        
        # 1. API Key geçerliliğini test et
        print("\n1. API Key testi...")
        
        # 2. Basit email gönderimi
        print("\n2. Email gönderimi testi...")
        message = Mail(
            from_email=from_email,
            to_emails='halimebuse60@gmail.com',
            subject='SendGrid Test - Detaylı',
            html_content='<p>Bu detaylı bir test emailidir.</p>'
        )
        
        response = sg.send(message)
        
        print(f"✅ Başarılı!")
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.body}")
        print(f"Response Headers: {dict(response.headers)}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ HATA DETAYI:")
        print(f"Hata Tipi: {type(e).__name__}")
        print(f"Hata Mesajı: {str(e)}")
        
        # Eğer HTTP hatası ise daha detaylı bilgi
        if hasattr(e, 'body'):
            try:
                error_body = json.loads(e.body)
                print(f"Hata Detayları: {json.dumps(error_body, indent=2)}")
            except:
                print(f"Ham Hata Body: {e.body}")
        
        if hasattr(e, 'status_code'):
            print(f"HTTP Status: {e.status_code}")
            
        return False

def check_sender_verification():
    """Sender doğrulaması kontrolü için tavsiyeler"""
    print("\n=== Sender Verification Kontrol Listesi ===")
    print("□ SendGrid → Settings → Sender Authentication")
    print("□ Single Sender Verification seçili")
    print("□ yalcinhalimebuse@gmail.com eklendi")
    print("□ Gmail'den doğrulama emaili onaylandı")
    print("□ Status: Verified olarak görünüyor")

if __name__ == "__main__":
    detailed_sendgrid_test()
    check_sender_verification()