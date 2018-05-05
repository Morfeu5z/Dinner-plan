from flask import Flask, render_template
from my_app import app

app.run(debug=True, host="127.0.0.1", port=5000)


