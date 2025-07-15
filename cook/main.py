from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/kartoplyani-zrazy")
def kartoplyani_zrazy():
    return render_template('end.html')

@app.route("/top")
def top():
    return render_template('top.html')

@app.route("/mlinci")
def mlinci():
    return render_template('Mlinci.html')

@app.route("/ponchiki")
def ponhiki():
    return render_template('ponhiki.html')

@app.route("/solyanka")
def solanka():
    return render_template('solanka.html')

@app.route("/soup")
def soup():
    return render_template('soup.html')

@app.route("/potato-casserole")
def potato_casserole():
    return render_template('potato_casserole.html')

@app.route("/milkshake")
def milkshake():
    return render_template('milkshake.html')

@app.route("/egg-nog")
def egg_nog():
    return render_template('egg_nog.html')

@app.route("/cherry-compote")
def cherry_compote():
    return render_template('cherry_compote.html')

@app.route("/pie")
def pie():
    return render_template('pie.html')

@app.route("/napoleon")
def napoleon():
    return render_template('napoleon.html')

@app.route("/kyiv-tort")
def kyiv_tort():
    return render_template('kyiv_tort.html')

@app.route("/raspberry-cake")
def raspberry_cake():
    return render_template('raspberry_cake.html')

@app.route("/soup2")
def soup2():
    return render_template('soup2.html')

@app.route("/strudel")
def strudel():
    return render_template('strudel.html')

@app.route("/apple-crumble")
def apple_crumble():
    return render_template('apple_crumble.html')

@app.route("/panna-cotta")
def panna_cotta():
    return render_template('panna_cotta.html')

@app.route("/chiken-thomas")
def chiken_thomas():
    return render_template('chiken_thomas.html')

app.run(debug=True)
