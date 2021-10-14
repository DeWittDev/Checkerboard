from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def helloWorld():
    check = 8*8
    return render_template('index.html', var = check)

@app.route('/<int:num>')
def boxes(num):
    return render_template('index.html', var = check)

@app.route('/<int:num>/<string:clr>')
def colorboxes(num, clr):
    return render_template('index.html', var = num, color = clr)

if __name__=="__main__":
    app.run(debug=True)
