from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "🚀 Hello from Flask App deployed via Ansible on MicroK8s!"

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="0.0.0.0", port=80)
=======
    app.run(host="0.0.0.0", port=5000)
>>>>>>> 7ecc758 (updated)
