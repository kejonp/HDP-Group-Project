from flask import Flask, render_template, request
from final_result import ProvideResult

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test')
def test():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/result', methods=['GET', 'POST'])
def final_result():
    input_dict = request.form.to_dict()
    print(input_dict)
    provide_result = ProvideResult()
    output = provide_result.get_final_result(input_dict=input_dict)
    return render_template('result.html', output=output)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8448, debug=True)
