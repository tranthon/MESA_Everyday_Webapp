# MIT License
# MESA © 2019
# PSU Capstone 2018-2019
from MESAeveryday import app
import os

if __name__ == '__main__':
    app.run(debug=True, 
            host='127.0.0.1', 
            port=8080,)
            #ssl_context=(os.environ['MESAsslcert'],os.environ['MESAsslkey']))
