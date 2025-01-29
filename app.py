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
    <title>{{ title }} | Flask Web App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

    <nav class="navbar">
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
            <li><a href="/contact">Contact</a></li>
            <li><a href="/services">Services</a></li>
        </ul>
    </nav>

    <header>
        <h1>Welcome to {{ title }}</h1>
        <p>Explore our services and learn more about us.</p>
    </header>

    <section class="content">
        <p>This is the {{ title }} page.</p>
    </section>

    <footer>
        <p>© 2025 Flask Web App | Developed with ❤️</p>
    </footer>

    <button class="theme-toggle" onclick="toggleTheme()">Switch Theme</button>

    <script>
        function toggleTheme() {
            document.body.classList.toggle("dark-mode");
        }
    </script>

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
    
