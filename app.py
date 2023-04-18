from flask import Flask, jsonify, request
from services.uf_service import UFService
from datetime import datetime
import json
app = Flask(__name__)
uf_service = UFService()

@app.route('/uf', methods=['GET'])
def get_uf():
    date_str = request.args.get('date', '')
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return json.dumps({'error': 'La fecha proporcionada no tiene el formato correcto (YYYY-MM-DD).'}, ensure_ascii=False), 400

    if date < datetime.strptime("2013-01-01", "%Y-%m-%d").date():
        return json.dumps({'error': 'La fecha mínima que se puede consultar es el 01-01-2013.'}, ensure_ascii=False), 400
    
    uf_value = uf_service.get_uf_value(date)
    if uf_value is None:
        return json.dumps({'error': f'No se pudo encontrar la UF para la fecha {date_str}.'}, ensure_ascii=False), 404

    return json.dumps({'date': date_str, 'uf_value': uf_value})


if __name__ == '__main__':
    app.run(debug=True)