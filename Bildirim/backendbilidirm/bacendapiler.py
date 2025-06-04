# app.py - Sizin backend kodunuz
from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Arkadaşının frontend'i için API'ler
@app.route('/api/get-alerts')
def get_alerts():
    """Kritik uyarıları döndür"""
    alerts = analytics.get_critical_alerts()
    return jsonify(alerts)

@app.route('/api/analytics/dashboard-data')
def dashboard_data():
    """Dashboard verileri"""
    return jsonify({
        "total_violations": get_total_violations(),
        "critical_count": get_critical_count(),
        "violation_types": analytics.violation_type_analysis()
    })

##🔗 API Endpoints (Arkadaşının kullanacağı):
##- http://localhost:5000/api/get-alerts
##- http://localhost:5000/api/analytics/dashboard-data
##- WebSocket: ws://localhost:5000 (real-time bildirimler için)
