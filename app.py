from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Welcome to the Vulnerable Web App!</h1>
    <p>Try to access the <a href="/secret">secret page</a> and see if you get a 403 Forbidden error.</p>
    '''

@app.route('/secret')
def secret():
    path = request.path

    # Header bypass
    if request.headers.get('X-Custom-IP-Authorization') == "127.0.0.1":
        return "Bypassed using X-Custom-IP-Authorization header"

    if request.headers.get('X-Forwarded-Host') == "localhost":
        return "Bypassed using X-Forwarded-Host header"

    if request.headers.get('X-Forwarded-For') == "127.0.0.1":
        return "Bypassed using X-Forwarded-For header"

    # 403
    abort(403)

if __name__ == '__main__':
    app.run(debug=True)
