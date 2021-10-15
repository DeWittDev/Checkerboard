from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def eights():
    num = 4
    return render_template('index.html', num = num)

@app.route('/<int:row>')
def columnVar(row):
    column = 4
    return render_template('index.html', column = column, row = row)

@app.route('/<int:row>/<int:column>')
def sizeVar(row, column):
    return render_template('index.html', column = column, row = row)

if __name__=="__main__":
    app.run(debug=True)
