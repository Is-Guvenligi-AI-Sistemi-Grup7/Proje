from dataclasses import dataclass
from datetime import datetime

@dataclass
class Notification:
    notification_id: int
    target_type: str          #hedef turu
    user_id: int              # İhlal yapan kullanıcı
    violation_type_id: int 
    target_department: str    # hedef departman
    target_user: int          # hedef kullanıcı
    camera_id: int            # İhlalin tespit edildiği kamera
    notification_date: datetime
    is_read: bool = False     # Yöneticinin bildirimi okuduğu bilgisi
    # admin_chat_id nedir?
