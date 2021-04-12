from flask import Flask, request, abort

from producer import generate_discount_codes_producer
from logger import log

app = Flask(__name__)
log.msg("Server is just started")


@app.route('/generate_discount_codes', methods=['POST'])
def generate_discount_codes_view():
    try:
        user_id = request.json['user_id']
        number_of_codes = request.json['number_of_codes']
        code_length = request.json['code_length']
    except KeyError as e:
        log.msg(f'Validation Failed: {e}')
        abort(400)
    return {'message': f'Creation of {number_of_codes} codes was initiated'}, 202
