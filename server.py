from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def eights():
    num = 4
    return render_template('index.html', column=num)

@app.route('/<int:num>')
def columnVar(num):
    return render_template('index.html', column=num/2)


if __name__=="__main__":
    app.run(debug=True)
