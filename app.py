from flask import Flask, render_template, request

app = Flask(__name__)
import demo as d


@app.route("/",methods=['GET','POST'])
def hello():
    # global ab
    lis1 =[]
    # dic2 = {}
    # global list
    if request.method == 'POST':
        movie = request.form["Movie"]
        amey = d.MoviePre(movie)
        # print(amey)
        # dic2 = amey
        lis1.append(amey)
        # list = list(dic2.items())
    # print(dic2)
    # for printing the value
    # print(lis1)


    return render_template("index.html",amey2 = lis1)



if __name__ == '__main__':
    app.run()
