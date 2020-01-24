from flask import request, Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])


def plus():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        plus = float(num1) + float(num2)
        return '''<h1>The sum is: {}</h1>'''.format(plus)


    return '''<form method="POST">
                  num1: <input type="text" name="num1"><br>
                  num2: <input type="text" name="num2"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

