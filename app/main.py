from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the form page
@app.route('/')
def form():
    return render_template('index.html')

# Route for handling form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    # Additional logic to evaluate criteria
    # Example: if name and email meet conditions, accept or reject
    if name and email:  # Dummy condition
        return f"Hello {name}, your application is being reviewed!"
    else:
        return "Error: All form fields are required."

if __name__ == '__main__':
    app.run(debug=True)

