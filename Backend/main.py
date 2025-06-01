from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (frontend'e izin vermek için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Geliştirme ortamında bu şekilde bırakabilirsin
    allow_methods=["*"],
    allow_headers=["*"],
)

# Giriş formunu karşılayan POST endpoint
@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...), role: str = Form(...)):
    # Örnek kullanıcılar (veritabanı yoksa bu şekilde kontrol edilir)
    users = {
        "ahmet.yilmaz": {"password": "123456", "role": "calisan"},
        "fatma.kaya": {"password": "123456", "role": "calisan"},
        "mehmet.demir": {"password": "admin123", "role": "yonetici"},
        "ayse.ozkan": {"password": "admin123", "role": "yonetici"},
    }

    user = users.get(username)
    if user and user["password"] == password and user["role"] == role:
        # Giriş başarılıysa dashboard sayfasına yönlendir
        response = RedirectResponse(url="/dashboard", status_code=303)
        return response
    else:
        # Giriş başarısızsa tekrar index'e yönlendir (ya da hata mesajı göster)
        return RedirectResponse(url="/?error=Gecersiz%20giris", status_code=303)

# Dashboard sayfası
@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    return "<h1>Dashboard Sayfası</h1><p>Giriş başarılı.</p>"
