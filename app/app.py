import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    """Estabelece a conexão com o banco de dados usando variáveis de ambiente."""
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST'),
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        port=os.environ.get('DB_PORT', '5432')
    )
    return conn

@app.route('/db_version')
def get_db_version():
    """Endpoint que retorna a versão do banco de dados PostgreSQL."""
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT version();')
                db_version = cur.fetchone()[0]
                return jsonify({'status': 'success', 'db_version': db_version})
    except (Exception, psycopg2.Error) as error:
        return jsonify({'status': 'error', 'message': str(error)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
