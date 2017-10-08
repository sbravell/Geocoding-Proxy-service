from flask import Flask, jsonify, make_response, request, abort
from app.geocoding import GeocodeProxyAPI

app = Flask(__name__)

def response_with_status_code(response, code = None):
    """Create a response object with an error code

    """
    if code is None:
        code = 200
    if response and isinstance(response, dict):
        response.update({'status' : code})
    return response

def error_message(message, code):
    response = response_with_status_code({'error': message}, code)
    return make_response(jsonify(response), code)

"""
Geocode routes ( GET/POST )
"""
@app.route('/api/v1.0/geocode', methods=['GET'])
@app.route('/api/v1.0/geocode/<string:address>', methods=['GET'])
def get_geocode(address=None):
    args = request.args
    if address is None and (len(args) == 0 or 'address' not in args):
        abort(400)
    if len(args) > 0 and 'address' in args:
        address = args['address']
    response = response_with_status_code(GeocodeProxyAPI().get(address))
    return jsonify(response)

"""
POST, PUT, PATCH, DELETE Methods not allowed
"""
@app.route('/api/v1.0/geocode', methods=['POST', 'PUT', 'PATCH', 'DELETE'])
def method_not_allowed():
    return error_message('Method not allowed. Allow: GET, POST', 405)

"""
Error handling ( 404, 400, 500 )
"""
@app.errorhandler(404)
def not_found(error):
    return error_message('Not Found', error.code)

@app.errorhandler(400)
def bad_request(error):
    return error_message('Bad Request', error.code)

@app.errorhandler(Exception)
def exception_handler(error):
    return error_message('Service Unavailable', error.code)

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()