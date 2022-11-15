from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
  return '<h1>Hello, World!</h1>'

if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="localhost", port=8080, debug=True)