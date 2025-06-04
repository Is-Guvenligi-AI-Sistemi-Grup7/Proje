# app.py - Arkadaşınızın frontend'i için API'ler

@app.route('/api/send-notification', methods=['POST'])
def send_notification_to_frontend():
    """Arkadaşının arayüzüne bildirim gönder"""
    data = request.json
    
    # WebSocket ile frontend'e bildirim gönder
    socketio.emit('new_violation', {
        'employee_id': data['employee_id'],
        'violation_type': data['violation_type'],
        'severity': data['severity'],
        'location': data['location'],
        'timestamp': datetime.now().isoformat(),
        'message': f"⚠️ {data['employee_id']} - {data['violation_type']} ihlali tespit edildi!"
    })
    
    return jsonify({"success": True})

@app.route('/api/get-alerts')
def get_current_alerts():
    """Aktif uyarıları frontend için getir"""
    alerts = analytics.get_critical_alerts()
    return jsonify(alerts)

@app.route('/api/analytics/dashboard-data')
def get_dashboard_data():
    """Dashboard için tüm verileri getir"""
    return jsonify({
        "total_violations_today": get_today_violations_count(),
        "critical_alerts": len(analytics.get_critical_alerts()),
        "violation_types": analytics.violation_type_analysis(7),  # Son 7 gün
        "departments": analytics.department_analysis()
    })