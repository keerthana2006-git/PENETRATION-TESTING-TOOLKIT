from flask import Flask, request, render_template_string

app = Flask(__name__)

VALID_USERNAME = "admin"
VALID_PASSWORD = "toor"

LOGIN_HTML = """
<!doctype html>
<title>Login</title>
<h2>Login Page</h2>
<form method="post">
  Username: <input name="username"><br>
  Password: <input name="password"><br>
  <input type="submit" value="Login">
</form>
{% if error %}<p style="color:red">{{ error }}</p>{% endif %}
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == VALID_USERNAME and request.form['password'] == VALID_PASSWORD:
            return "Welcome, admin!"
        else:
            error = "Invalid credentials"
    return render_template_string(LOGIN_HTML, error=error)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
