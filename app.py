from flask import Flask, jsonify
import threading
from sftp_config import sftp_server

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "SFTP Server is Running"})


if __name__ == "__main__":
    threading.Thread(target=sftp_server).start()
    app.run(debug=True, host="0.0.0.0", port=5000)
