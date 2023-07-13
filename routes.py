from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome():
    print('welcome to basic flask app')

@app.route('/greet/<username>') 
def greet(username):
    print(f'hello! ${username}')

    

if __name__ == '__main__':
    app.run()