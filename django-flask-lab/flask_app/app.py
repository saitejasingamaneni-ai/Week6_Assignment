from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Flask!</h1>"

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/greet', methods=['GET', 'POST'])
def greet_form():
    if request.method == 'POST':
        name = request.form.get('name') or 'World'
        # redirect to the dynamic route to show the greeting
        return redirect(url_for('hello', name=name))
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
