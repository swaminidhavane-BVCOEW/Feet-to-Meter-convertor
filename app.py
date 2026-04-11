from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Feet to Meter Converter</title>
    <style>
        body { background-color: #f0f2f5; font-family: sans-serif; display: flex; justify-content: center; padding-top: 50px; }
        .card { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); width: 300px; text-align: center; }
        input { width: 90%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 6px; }
        .btn { padding: 10px 20px; border: none; border-radius: 6px; cursor: pointer; font-weight: bold; width: 100%; margin: 5px 0; }
        .convert-btn { background-color: #007bff; color: white; }
        .clear-btn { background-color: #6c757d; color: white; }
        .result-box { margin-top: 20px; padding: 15px; background: #e9ecef; border-radius: 6px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Feet to Meter</h2>
        <form method="POST">
            <input type="number" step="any" name="feet" placeholder="Enter Feet" value="{{ feet }}" required>
            <button type="submit" name="action" value="convert" class="btn convert-btn">Convert</button>
            <button type="submit" name="action" value="clear" class="btn clear-btn">Clear</button>
        </form>
        {% if meters %}
        <div class="result-box">
            {{ feet }} ft = {{ meters }} m
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    feet = ""
    meters = ""
    if request.method == 'POST':
        if request.form.get('action') == 'convert':
            try:
                feet = request.form.get('feet')
                # Calculation: 1 Foot = 0.3048 Meters
                meters = round(float(feet) * 0.3048, 4)
            except ValueError:
                pass
    return render_template_string(HTML_TEMPLATE, feet=feet, meters=meters)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

