from flask import *
import os
import socket
from ddtrace import tracer

tracer.configure(
    hostname='datadog-agent',
    port=8126,
)

app = Flask(__name__)

# app.config["Debug"] = True
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

    
if __name__ == '__main__':
    app.run()


# PORT = int(os.environ.get("PORT", 9090))
if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=9090)

# if __name__ == "__main__":
#   app.run(host='0.0.0.0', port=9090)