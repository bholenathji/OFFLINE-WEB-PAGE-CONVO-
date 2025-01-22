from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Options Menu</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    background-color: #f4f4f9;
                    margin: 0;
                    padding: 0;
                }
                .container {
                    margin-top: 100px;
                }
                button {
                    display: inline-block;
                    margin: 10px;
                    padding: 15px 30px;
                    font-size: 18px;
                    border: none;
                    border-radius: 5px;
                    background-color: #4CAF50;
                    color: white;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #45a049;
                }
                .back {
                    background-color: #ff4d4d;
                }
                .back:hover {
                    background-color: #e60000;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to the Options Menu</h1>
                <button onclick="location.href='/option1'">Option 1</button>
                <button onclick="location.href='/option2'">Option 2</button>
                <button onclick="location.href='/option3'">Option 3</button>
                <button onclick="location.href='/option4'">Option 4</button>
                <br><br>
                <button class="back" onclick="location.href='/back'">Go Back</button>
            </div>
        </body>
        </html>
    '''

@app.route('/option1')
def option1():
    return '''
        <h1>Option 1 Selected</h1>
        <p>This is Option 1 functionality.</p>
        <a href="/">Go Back</a>
    '''

@app.route('/option2')
def option2():
    return '''
        <h1>Option 2 Selected</h1>
        <p>This is Option 2 functionality.</p>
        <a href="/">Go Back</a>
    '''

@app.route('/option3')
def option3():
    return '''
        <h1>Option 3 Selected</h1>
        <p>This is Option 3 functionality.</p>
        <a href="/">Go Back</a>
    '''

@app.route('/option4')
def option4():
    return '''
        <h1>Option 4 Selected</h1>
        <p>This is Option 4 functionality.</p>
        <a href="/">Go Back</a>
    '''

@app.route('/back')
def back():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
