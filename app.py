from flask import Flask, request, render_template
import subprocess as sp
import os
app = Flask("app")
global cmd


@app.route("/menu")
def menuform():
    form = render_template("index.html")
    return form


@app.route("/cmd_output")
def cmd_output():
    cmd = request.args.get("input_query")
    b = sp.getoutput(cmd)
    a = render_template('new.html', value=b)
    print(cmd)
    return a


app.run(debug=True)