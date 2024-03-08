from flask import Flask, render_template, request, redirect

app = Flask(_name_)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle the login form submission
        username = request.form['username']
        password = request.form['password']
        # Perform authentication logic here
        
        # Redirect to a different page after successful login
        return redirect('/dashboard')
    else:
        return render_template('login.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle the registration form submission
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Perform registration logic here
        
        # Redirect to a different page after successful registration
        return redirect('/dashboard')
    else:
        return render_template('register.html')

if _name_ == '_main_':
    app.run()