from flask import Flask, jsonify, send_file
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

BASE = os.path.dirname(__file__)
GAINERS = os.path.join(BASE, 'topGainers.csv')
LOSERS = os.path.join(BASE, 'topLosers.csv')
SCRIPTS_PY = os.path.join(BASE, 'scripts.py')


@app.route('/data/gainers')
def gainers():
    if os.path.exists(GAINERS):
        return send_file(GAINERS, mimetype='text/csv')
    return jsonify({'error': 'topGainers.csv not found'}), 404


@app.route('/data/losers')
def losers():
    if os.path.exists(LOSERS):
        return send_file(LOSERS, mimetype='text/csv')
    return jsonify({'error': 'topLosers.csv not found'}), 404


@app.route('/sync', methods=['POST'])
def sync():
    if not os.path.exists(SCRIPTS_PY):
        return jsonify({'ok': False, 'error': 'scripts.py not found'}), 500
    try:
        res = subprocess.run(['python', SCRIPTS_PY], capture_output=True, text=True, check=True)
        return jsonify({'ok': True, 'stdout': res.stdout})
    except subprocess.CalledProcessError as e:
        return jsonify({'ok': False, 'stderr': e.stderr or e.output}), 500


if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)