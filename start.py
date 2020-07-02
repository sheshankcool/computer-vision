from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("demo.html")
'''
@app.route("/calculate",methods=["POST","get"])
def calculate():
    #result=request.form
    values=[int(f) for f in request.form.values()]
    values=sum(values)
    return render_template("demo.html",values="Total marks secured:{}".format(values))
'''
@app.route("/calculate",methods=["POST","get"])
def calculate():
    #result=request.form
    values=[int(f) for f in request.form.values()]
    values=sum(values)
    return render_template("demo2.html",values="Total marks secured:{}".format(values))

if __name__== "__main__":
    app.run(debug=True)
