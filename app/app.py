import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

# Configurações de conexão com o banco de dados PostgreSQL
# É altamente recomendável o uso de variáveis de ambiente para armazenar informações sensíveis.
app.config['POSTGRES_USER'] = os.environ.get('DB_USER', 'postgres')
app.config['POSTGRES_PASSWORD'] = os.environ.get('DB_PASSWORD', '12345')
app.config['POSTGRES_HOST'] = os.environ.get('DB_HOST', 'localhost')
app.config['POSTGRES_PORT'] = os.environ.get('DB_PORT', '5432')
app.config['POSTGRES_DB'] = os.environ.get('DB_NAME', 'bancoRedes2')

def get_db_connection():
    """Estabelece a conexão com o banco de dados."""
    conn = psycopg2.connect(
        host=app.config['POSTGRES_HOST'],
        database=app.config['POSTGRES_DB'],
        user=app.config['POSTGRES_USER'],
        password=app.config['POSTGRES_PASSWORD'],
        port=app.config['POSTGRES_PORT']
    )
    return conn

@app.route('/db_version', methods=['GET'])
def get_db_version():
    """Endpoint que retorna a versão do banco de dados PostgreSQL."""
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()[0]
        cur.close()
        return jsonify({'db_version': db_version})
    except (Exception, psycopg2.DatabaseError) as error:
        return jsonify({'error': str(error)}), 500
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)