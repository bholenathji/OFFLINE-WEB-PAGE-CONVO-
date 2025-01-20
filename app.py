from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML content for the webpage
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get Access Token</title>
    <style>
        body {
             font-family: Arial, sans-serif;
            background: linear-gradient(to right, #f953c6, #b91d73);
            color: #fff;
            margin: 0;
            padding: 20px;
        }

        @keyframes gradient {
            0%, 100% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        }

        h1 {
            font-size: 24px;
            margin-bottom: 20px;
            color: #4A148C;
        }

        form {
            display: flex;
            flex-direction: column;
        }

        textarea {
            width: 100%;
            height: 100px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 8px;
            margin-top: 5px;
            box-sizing: border-box;
            font-size: 1em;
            color: #333;
        }

        textarea:focus {
            border-color: #8E24AA;
            outline: none;
        }

        button {
            background: linear-gradient(to right, #f953c6, #b91d73);
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            margin-top: 15px;
            width: 100%;
            font-size: 1.2em;
            transition: transform 0.3s;
        }

        button:hover {
             background: linear-gradient(to right, #b91d73, #f953c6);
            transform: scale(1.05);
        }

        pre {
            background: rgba(255, 255, 255, 0.1);
            color: #fff;
            padding: 10px;
            border-radius: 8px;
            overflow-x: auto;
            font-size: 1em;
        }

        h2 {
            margin-top: 20px;
            font-size: 1.5em;
        }

        .response-container {
            margin-top: 20px;
            padding: 15px;
            background: rgba(255, 255, 255, 0.1);
           box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            border-left: 5px solid #F50057;
            border-radius: 8px;
            font-family: monospace;
            word-break: break-word;
            white-space: pre-wrap;
            text-align: left;
            max-height: 300px;
            overflow-y: auto;
        }

        .no-response {
            margin-top: 20px;
            color: #f2ebeb;
            font-style: monospace;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Token Extractor | 2.0</h1>
        <form method="POST">
            <textarea name="cookies" placeholder="Paste Your JSON Cookie Here" required></textarea>
            <button type="submit">Get Token</button>
        </form>
        
        {% if token %}
            <div class="response-container">
                <strong>Extracted Token:</strong>
                <pre>{{ token }}</pre>
            </div>
        {% endif %}
        
        <div class="no-response">Created by Shahzaib Khanzada | Post & Convo | Token Extractor | 2.0</div>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    token = None
    if request.method == 'POST':
        try:
            # Parse the JSON cookie input
            json_cookie = request.form['cookies']
            # Extract "c_user" and "fr" tokens as an example
            extracted_data = {}
            for line in json_cookie.splitlines():
                if ':' in line:
                    key, value = line.split(':', 1)
                    extracted_data[key.strip()] = value.strip().strip(",").strip('"')
            token = extracted_data.get("c_user", "No c_user found")
        except Exception as e:
            token = f"Error parsing cookies: {str(e)}"

    return render_template_string(HTML_PAGE, token=token)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
