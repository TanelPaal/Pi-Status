from flask import Flask, render_template, jsonify
import psutil
import subprocess
import os

app = Flask(__name__)

def get_cpu_temperature():
    try:
        # Try reading from thermal zone first (more compatible method)
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
            temp = float(f.read().strip()) / 1000.0
            return temp
    except:
        try:
            # Fallback to vcgencmd
            temp = subprocess.check_output(['vcgencmd', 'measure_temp']).decode()
            return float(temp.replace('temp=', '').replace('\'C\n', ''))
        except Exception as e:
            print(f"Error getting temperature: {str(e)}")  # Debug print
            return 0

def get_system_stats():
    return {
        'cpu_percent': psutil.cpu_percent(),
        'cpu_temp': get_cpu_temperature(),
        'memory': {
            'total': round(psutil.virtual_memory().total / (1024.0 ** 3), 1),
            'used': round(psutil.virtual_memory().used / (1024.0 ** 3), 1),
            'percent': psutil.virtual_memory().percent
        },
        'disk': {
            'total': round(psutil.disk_usage('/').total / (1024.0 ** 3), 1),
            'used': round(psutil.disk_usage('/').used / (1024.0 ** 3), 1),
            'percent': psutil.disk_usage('/').percent
        }
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stats')
def stats():
    return jsonify(get_system_stats())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
