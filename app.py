from flask import Flask, render_template_string

app = Flask(__name__)

# Main page with options
@app.route('/')
def index():
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>YK TRICKS INDIA</title>
        <style>
            body {
                background-color: #f0f8ff;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
            }

            .container {
                max-width: 500px;
                margin: auto;
            }

            .btn {
                display: block;
                width: 200px;
                padding: 15px;
                margin: 20px auto;
                text-decoration: none;
                color: white;
                background-color: #abaf4c;
                border: none;
                border-radius: 10px;
                font-size: 18px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
                cursor: pointer;
                transition: all 0.3s ease;
                text-align: center;
            }

            .btn:hover {
                background-color: #7c7f7c;
                box-shadow: 0 6px 8px rgba(0, 0, 0, 0.3);
                transform: translateY(-2px);
            }

            .btn:active {
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
                transform: translateY(2px);
            }

            .back-btn {
                background-color: #f3e721;
            }

            .back-btn:hover {
                background-color: #f37e21;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Choose an Option</h1>
            <a href="/http://104.168.76.139:27003/" class="btn">GET TOKEN</a>
            <a href="/option2" class="btn">Option 2</a>
            <a href="/option3" class="btn">Option 3</a>
            <a href="/option4" class="btn">Option 4</a>
            <a href="/" class="btn back-btn">Go to Back</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

# Route for Option 1
@app.route('/option1')
def option1():
    return '''
    <h1>Option 1 Selected</h1>
    <a href="/">Go Back</a>
    '''

# Route for Option 2
@app.route('/option2')
def option2():
    return '''
    <h1>Option 2 Selected</h1>
    <a href="/">Go Back</a>
    '''

# Route for Option 3
@app.route('/option3')
def option3():
    return '''
    <h1>Option 3 Selected</h1>
    <a href="/">Go Back</a>
    '''

# Route for Option 4
@app.route('/option4')
def option4():
    return '''
    <h1>Option 4 Selected</h1>
    <a href="/">Go Back</a>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
