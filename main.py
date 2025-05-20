from flask import Flask
app = Flask(__name__)

@app.route('/')
def mensajeWeb():
    return 'Me encanta este curso...'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
