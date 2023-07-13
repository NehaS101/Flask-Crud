from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome():
    return ('welcome to basic flask app')

@app.route('/greet/<username>') 
def greet(username):
    return (f'hello! {username}')

@app.route('/farewell/<username>')
def farewell(username):
    return (f'goodbye! {username}')    

if __name__ == '__main__':
    app.run()