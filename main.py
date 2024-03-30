
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)



@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/print_result/<string:result>/<int:marks>')
def print_result(result, marks):
    return render_template('results.html', result=result, marks=marks)


@app.route('/check_result/<int:marks>')
def check_result(marks):
    result = ''
    if marks > 35:
        result = 'success'
    else:
        result = 'fail'
    return redirect(url_for('print_result', result=result, marks=marks))


@app.route('/submit_marks', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method=='POST':
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
        biology = float(request.form['biology'])
        total_score = (maths+science+history+biology)/4
    return redirect(url_for('check_result', marks=total_score))



if __name__ == '__main__':
    app.run(debug=True)