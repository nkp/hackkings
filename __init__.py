from flask import Flask

def configure(app):
    app.debug = True


app = Flask(__name__)

configure(app)

if __name__ == '__main__':
    app.run()
