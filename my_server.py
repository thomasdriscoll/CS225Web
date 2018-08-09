from flask import Flask, flash, redirect, render_template, request, session, abort
import random

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def home():

    quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
               "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
               "'To understand recursion you must first understand recursion..' -- Unknown",
               "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
               "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
    randomNumber = random.randint(0,len(quotes)-1)
    quote = quotes[randomNumber]
    return render_template(
    '/index.html', index = True, **locals()
    )

@app.route('/cplusplus.html')
def cpp():
    return render_template(
    '/cplusplus.html', cpp=True
    )

@app.route('/lists.html')
def lists():
    return render_template(
    '/lists.html', lists=True
    )

@app.route('/stack.html')
def stack():
    return render_template(
    '/stack.html', stack=True
    )

@app.route('/trees.html')
def trees():
    return render_template(
    '/trees.html', trees=True
    )

@app.route('/btrees.html')
def btrees():
    return render_template(
    '/btrees.html', btrees=True
    )

@app.route('/hash_tab.html')
def hash_tab():
    return render_template(
    '/hash_tab.html', hash_tab=True
    )

@app.route('/graphs.html')
def graphs():
    return render_template(
    '/graphs.html', graphs=True
    )

@app.route('/algorithms.html')
def algorithms(name=None):
    return render_template(
    '/algorithms.html', algorithms=True
    )
if __name__ == '__main__':
    app.run(host='0.0.0.0')
