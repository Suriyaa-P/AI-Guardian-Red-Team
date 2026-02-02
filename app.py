import os
import glob
import asyncio
from flask import Flask, render_template, jsonify, send_from_directory
from ai_guardian_orchestrator import run_security_audit
from flask import send_file

app = Flask(__name__, static_folder='screenshots')

# --- ROUTES ---

@app.route('/')
def landing_page():
    # Serves your Tech-Forward Landing Page
    return render_template('index.html')

@app.route('/dashboard')
def audit_ui():
    # Serves the Live Audit Command Center
    return render_template('run_audit.html')

@app.route('/run-audit', methods=['POST'])
def trigger_audit():
    try:
        # Executes the multi-agent Playwright loop
        asyncio.run(run_security_audit())
        return jsonify({"status": "success", "message": "Audit completed."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/get-latest-screenshots')
def get_screenshots():
    screenshot_dir = 'screenshots'
    if not os.path.exists(screenshot_dir):
        return jsonify([])
    
    files = glob.glob(os.path.join(screenshot_dir, "*.png"))
    files.sort(key=os.path.getmtime, reverse=True)
    
    # Returns the path for the frontend to consume
    names = [os.path.basename(f) for f in files[:4]]
    return jsonify([f"/screenshots/{name}" for name in names])

# Serve actual image files to the browser
@app.route('/screenshots/<path:filename>')
def serve_screenshot(filename):
    return send_from_directory('screenshots', filename)


import glob

@app.route('/download-report')
def download_report():
    # Find the most recently created markdown file in the report folder
    list_of_files = glob.glob('report/*.md')
    if not list_of_files:
        return "No report found", 404
    latest_file = max(list_of_files, key=os.path.getctime)
    return send_file(latest_file, as_attachment=True)

if __name__ == '__main__':
    # Ensure folders exist before starting
    os.makedirs('screenshots', exist_ok=True)
    os.makedirs('report', exist_ok=True)
    app.run(debug=True, port=5000)