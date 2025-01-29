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
    <title>Flask Web App - Dark Theme</title>
    <style>
        /* Global Styles */
        body {
            font-family: Arial, sans-serif;
            background-image: url('https://i.ibb.co/gvxrWhg/IMG-20240727-001613.jpg'); /* Change the wallpaper */
            background-size: cover;
            background-repeat: no-repeat;
            color: white;
            margin: 0;
            padding: 0;
        }

        /* Navigation Menu */
        .navbar {
            background: linear-gradient(to right, #2c3e50, #4c5d6c); /* Dark theme gradient */
            padding: 15px;
            text-align: center;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5);
        }

        .navbar a {
            color: white;
            text-decoration: none;
            margin: 10px;
            font-weight: bold;
            padding: 10px 15px;
            transition: 0.3s;
        }

        .navbar a:hover {
            background: rgba(255, 255, 255, 0.2);
            border-radius: 5px;
        }

        /* Content Section */
        .container {
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: rgba(0, 0, 0, 0.7);
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            text-align: center;
        }

        h1 {
            font-size: 28px;
        }

        p {
            font-size: 16px;
        }

        /* Theme Buttons */
        .theme-buttons {
            margin-top: 20px;
        }

        .theme-btn {
            border: none;
            padding: 10px 15px;
            margin: 5px;
            cursor: pointer;
            border-radius: 5px;
            font-weight: bold;
            color: white;
            transition: 0.3s;
        }

        .theme-dark { background: #2c3e50; }
        .theme-red { background: #e74c3c; }
        .theme-blue { background: #3498db; }
        .theme-green { background: #2ecc71; }

        .theme-btn:hover {
            opacity: 0.8;
        }
    </style>
</head>
<body>

    <!-- Navigation Bar -->
    <div class="navbar">
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Services</a>
        <a href="#">Contact</a>
    </div>

    <!-- Main Content -->
    <div class="container">
        <h1>Welcome to My Flask Web App</h1>
        <p>Choose a theme:</p>

        <!-- Theme Selection Buttons -->
        <div class="theme-buttons">
            <button class="theme-btn theme-dark">Dark</button>
            <button class="theme-btn theme-red">Red</button>
            <button class="theme-btn theme-blue">Blue</button>
            <button class="theme-btn theme-green">Green</button>
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
    
