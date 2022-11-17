import os
from flask import Flask

app = Flask(__name__)

@app.route("/run_read_serial", methods=["GET"])
def read_serial():
    response_code = os.system("~/laboratorio_virtual/LabVirtual-AgroIOT/read_serial.py")

    if response_code == 0:
        response = {
            "data": "The read_serial script is running.",
            "status_code": 200
        }
    else:
        response = {
            "data": "An error occured",
            "status_code": 500
        }
            
    return response