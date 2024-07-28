from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Sample in-memory database for devices
devices = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/devices', methods=['GET'])
def get_devices():
    return jsonify(devices)

@app.route('/api/add_device', methods=['POST'])
def add_device():
    device_data = request.json
    devices.append({
        "name": device_data.get("name"),
        "local_ip": device_data.get("local_ip"),
        "public_ip": device_data.get("public_ip"),
        "cloudflared_tunnel": device_data.get("cloudflared_tunnel"),
        "use_case": device_data.get("use_case"),
        "existing_since": device_data.get("existing_since"),
        "location": device_data.get("location"),
        "owner": device_data.get("owner")
    })
    return jsonify({"status": "success"}), 201

@app.route('/api/delete_device', methods=['DELETE'])
def delete_device():
    name = request.args.get('name')
    global devices
    devices = [device for device in devices if device["name"] != name]
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
