from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/messege", methods=['POST'])
def messege():
    acctName = request.values['acctName']
    pwd = request.values['pwd']
    return render_template('messege.html',**locals())

if __name__ == '__main__':
	app.run(host='127.0.0.1',port='3000',debug=True)