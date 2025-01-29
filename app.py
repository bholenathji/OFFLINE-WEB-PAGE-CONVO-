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
    <title>Flask AI Webpage</title>
    <style>
        body {
            {% if theme == 'dark' %}
                background-color: #121212;
                color: white;
            {% else %}
                background-color: white;
                color: black;
            {% endif %}
            font-family: Arial, sans-serif;
            text-align: center;
            transition: 0.3s;
        }

        .container {
            margin-top: 50px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
            padding: 20px;
            border-radius: 10px;
            display: inline-block;
            background: {% if theme == 'dark' %}#333{% else %}#f9f9f9{% endif %};
        }

        nav {
            display: flex;
            justify-content: center;
            gap: 20px;
            padding: 15px;
            background: {% if theme == 'dark' %}#222{% else %}#ddd{% endif %};
            border-radius: 10px;
        }

        nav a {
            text-decoration: none;
            font-size: 18px;
            font-weight: bold;
            color: {% if theme == 'dark' %}white{% else %}black{% endif %};
            padding: 5px 10px;
            border-radius: 5px;
        }

        nav a:hover {
            background: gray;
            color: white;
        }

        .theme-toggle {
            margin-top: 20px;
        }

        button {
            padding: 10px;
            border: none;
            cursor: pointer;
            font-size: 16px;
            border-radius: 5px;
        }

        .dark-btn {
            background: black;
            color: white;
        }

        .light-btn {
            background: white;
            color: black;
            border: 1px solid black;
        }
    </style>
</head>
<body>

    <nav>
        <a href="/">Home</a>
        <a href="/contact">Contact</a>
        <a href="/mobile">Mobile</a>
        <a href="/facebook">Facebook</a>
        <a href="/instagram">Instagram</a>
        <a href="/about">About</a>
        <a href="/services">Services</a>
    </nav>

    <div class="container">
        <h1>Welcome to Flask AI Webpage</h1>
        <p>Choose your favorite theme:</p>
        <div class="theme-toggle">
            <a href="/set_theme/dark"><button class="dark-btn">Dark Mode</button></a>
            <a href="/set_theme/light"><button class="light-btn">Light Mode</button></a>
        </div>
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
    
