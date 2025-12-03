from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hola Mundo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            .container {
                text-align: center;
                background: white;
                padding: 50px;
                border-radius: 10px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            }
            h1 {
                color: #667eea;
                margin: 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hola mundo</h1>
            <p>Vielka Sanchez 2023-1754</p>
        </div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)