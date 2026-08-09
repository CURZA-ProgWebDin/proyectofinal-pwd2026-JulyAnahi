from itsdangerous import URLSafeTimedSerializer
from flask import current_app

def generar_url_qr_dinamico(numero_mesa):

    serializador:URLSafeTimedSerializer(current_app.config['SECRET_KEY'])

    token_tiempo: serializador.dumps({'table_number':numero_mesa})

    base_url = current_app.config['BASE_URL_APP']
    url_dinamica = f'{base_url}/api/orders?token={token_tiempo}'
    return url_dinamica