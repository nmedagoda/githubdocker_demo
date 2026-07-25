from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Docker + GitHub Actions! Version 2"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
#docker build -t githubdocker_demo .
#docker run -p 5000:5000 githubdocker_demo