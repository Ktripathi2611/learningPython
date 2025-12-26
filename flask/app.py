# =============================================================================
# TOPIC 1: INTRODUCTION TO FLASK
# =============================================================================
# Flask is a micro web framework written in Python. It is classified as a
# microframework because it does not require particular tools or libraries.
# 
# Key Features of Flask:
# - Lightweight and modular design
# - Built-in development server and debugger
# - RESTful request dispatching
# - Jinja2 templating engine
# - Support for secure cookies (client-side sessions)
# - WSGI 1.0 compliant
# - Unicode-based
# - Extensive documentation
# =============================================================================

# =============================================================================
# TOPIC 2: IMPORTING FLASK MODULES
# =============================================================================
# Flask provides several key modules that we need to import:
# - Flask: The main application class
# - render_template: Function to render HTML templates using Jinja2
# - request: Object containing incoming request data (form data, files, etc.)
# - redirect: Function to redirect users to a different URL
# - url_for: Function to build URLs for functions (prevents hardcoding URLs)
# =============================================================================

from flask import Flask, render_template, request, redirect, url_for
import os

# =============================================================================
# TOPIC 1 (continued): CREATING A FLASK APPLICATION
# =============================================================================
# Create an instance of the Flask class.
# __name__ is a special Python variable that represents the name of the module.
# Flask uses this to determine the root path of the application.
# 
# template_folder: Specifies where Flask should look for HTML templates.
# By default, Flask looks in a folder named 'templates' (plural).
# Here we specify 'template' (singular) as our folder name.
# =============================================================================

app = Flask(__name__, template_folder='template')

# =============================================================================
# TOPIC 11: CONFIGURATION FOR IMAGE/FILE UPLOADS
# =============================================================================
# Flask needs to know where to store uploaded files.
# We create a folder path using os.path.join for cross-platform compatibility.
# app.config is a dictionary that holds all configuration values.
# 
# UPLOAD_FOLDER: Specifies the directory where uploaded files will be saved.
# =============================================================================

# Define the folder path for storing uploaded images
UPLOAD_FOLDER = os.path.join('static', 'images')

# Create the images folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Configure the app with the upload folder path
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# =============================================================================
# TOPIC 3: BASIC WEBPAGE 1 - HOME PAGE (Root Route)
# =============================================================================
# The @app.route() decorator tells Flask what URL should trigger our function.
# '/' represents the root URL (homepage) of our website.
# 
# When a user visits http://127.0.0.1:5000/, the home() function is called,
# which renders and returns the home.html template.
# 
# render_template() loads the HTML file from the template folder and
# processes any Jinja2 template syntax before sending it to the browser.
# =============================================================================

@app.route('/')
def home():
    """
    Home page route - This is the landing page of our Flask application.
    Renders the home.html template which contains navigation links.
    """
    return render_template('home.html')


# =============================================================================
# TOPIC 4: BASIC WEBPAGE 2 - SECOND PAGE
# =============================================================================
# You can create multiple routes for different pages in your application.
# Each route maps a URL to a Python function (called a view function).
# 
# The URL '/second' will trigger the second() function.
# =============================================================================

@app.route('/second')
def second():
    """
    Second page route - Demonstrates creating multiple pages.
    Shows how to navigate between different pages using hyperlinks.
    """
    return render_template('second.html')


# =============================================================================
# TOPIC 5: IMPORTING HTML FILES USING FLASK
# =============================================================================
# Flask uses the render_template() function to load and render HTML files.
# The HTML files must be placed in the template folder (configured above).
# 
# Jinja2 templating engine processes the HTML before sending to browser:
# - {{ variable }}: Outputs the value of a variable
# - {% statement %}: Executes Python-like statements (if, for, block, etc.)
# - {# comment #}: Adds comments that won't appear in the output
# =============================================================================

@app.route('/index')
def index():
    """
    Index page route - Demonstrates template inheritance.
    This page extends base.html and overrides specific blocks.
    """
    return render_template('index.html')


# =============================================================================
# TOPICS 6, 7, 8: BASIC REGISTRATION FORM (GET and POST methods)
# =============================================================================
# Web forms use HTTP methods to send data:
# - GET: Retrieves data (default method, data visible in URL)
# - POST: Sends data to server (data hidden, used for sensitive information)
# 
# We create two routes for the registration form:
# 1. GET route (/register): Displays the empty form
# 2. POST route (/register): Processes the submitted form data
# 
# request.form is a dictionary containing all form field values.
# The keys are the 'name' attributes from the HTML form input fields.
# =============================================================================

@app.route('/register')
def register():
    """
    Registration form page (GET request).
    Displays the registration form to the user.
    """
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register_post():
    """
    Registration form submission handler (POST request).
    
    This function is called when the user submits the registration form.
    It extracts form data and passes it to the confirmation template.
    
    Note: We use a different function name (register_post) to avoid
    conflicts with the register() function above, even though they
    share the same URL route but different HTTP methods.
    """
    # Extract form data using request.form dictionary
    # The keys ('username', 'city', etc.) must match the 'name' attributes in HTML
    username = request.form['username']
    city = request.form['city']
    phone = request.form['phone']
    password = request.form['password']
    
    # Pass the form data to the confirmation template for display
    # The variable names become available in the Jinja2 template
    return render_template(
        'confirmation.html',
        username=username,
        city=city,
        phone=phone,
        password=password
    )


# =============================================================================
# BASIC LOGIN FORM
# =============================================================================
# Similar to registration, login requires both GET and POST methods.
# GET: Display the login form
# POST: Process login credentials
# =============================================================================

@app.route('/login')
def login():
    """
    Login page route (GET request).
    Displays the login form to the user.
    """
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    """
    Login form submission handler (POST request).
    Processes login credentials and redirects to home or shows error.
    """
    username = request.form['username']
    password = request.form['password']
    
    # In a real application, you would validate credentials against a database
    # For this demo, we just pass the data to a welcome page
    return render_template('login_success.html', username=username)


# =============================================================================
# TOPIC 9 & 10: REDIRECTING USING HYPERLINKS
# =============================================================================
# Flask provides two ways to handle redirects:
# 
# 1. redirect(): Sends the user to a different URL
# 2. url_for(): Generates a URL for a given function name
# 
# Using url_for() is preferred over hardcoding URLs because:
# - If you change a route URL, you only need to update it in one place
# - It automatically handles URL encoding
# - It works correctly regardless of where your app is mounted
# =============================================================================

@app.route('/confirmation')
def confirmation():
    """
    Confirmation page route.
    Can be accessed directly or after form submission.
    """
    return render_template('confirmation.html')


@app.route('/go-home')
def go_home():
    """
    Redirect example - Demonstrates programmatic redirection.
    Redirects the user to the home page using redirect() and url_for().
    """
    # url_for('home') generates the URL for the home() function
    # redirect() sends the user to that URL
    return redirect(url_for('home'))


@app.route('/go-register')
def go_register():
    """
    Another redirect example - Redirects to the registration page.
    """
    return redirect(url_for('register'))


# =============================================================================
# TOPIC 11: ADDING IMAGES TO FLASK
# =============================================================================
# Static files (images, CSS, JavaScript) are served from the 'static' folder.
# Flask automatically creates a route for static files at /static/<filename>
# 
# In templates, use url_for('static', filename='path/to/file') to reference
# static files, which ensures proper URL generation.
# =============================================================================

@app.route('/upload_page')
def upload_page():
    """
    Upload page route - Displays the file upload form.
    """
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload():
    """
    File upload handler - Processes uploaded files.
    
    request.files is a dictionary containing uploaded files.
    The key ('file') must match the 'name' attribute in the HTML form.
    
    The file is saved to the configured UPLOAD_FOLDER.
    """
    # Check if a file was uploaded
    if 'file' not in request.files:
        return 'No file uploaded', 400
    
    file = request.files['file']
    
    # Check if a file was selected
    if file.filename == '':
        return 'No file selected', 400
    
    # Save the file to the upload folder
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    
    # Redirect to the gallery page to see the uploaded image
    return redirect(url_for('gallery'))


@app.route('/gallery')
def gallery():
    """
    Gallery page route - Displays all uploaded images.
    
    Lists all image files in the upload folder and passes them to the template.
    """
    # Get list of all files in the images folder
    image_folder = app.config['UPLOAD_FOLDER']
    
    # Only include image files (common image extensions)
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp'}
    images = []
    
    if os.path.exists(image_folder):
        for filename in os.listdir(image_folder):
            # Check if the file has an image extension
            ext = os.path.splitext(filename)[1].lower()
            if ext in image_extensions:
                images.append(filename)
    
    return render_template('gallery.html', images=images)


# =============================================================================
# RUNNING THE APPLICATION
# =============================================================================
# The if __name__ == '__main__' block ensures this code only runs when
# the script is executed directly (not when imported as a module).
# 
# app.run() starts the Flask development server:
# - debug=True: Enables the debugger and auto-reloader
#   - Debugger: Shows detailed error messages in the browser
#   - Auto-reloader: Automatically restarts the server when code changes
# 
# WARNING: Never use debug=True in production! It's a security risk.
# 
# Default server settings:
# - Host: 127.0.0.1 (localhost only)
# - Port: 5000
# - URL: http://127.0.0.1:5000/
# =============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("FLASK TUTORIAL APPLICATION")
    print("=" * 60)
    print("Starting Flask development server...")
    print("Open your browser and navigate to: http://127.0.0.1:5000/")
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    
    # Run the Flask application with debug mode enabled
    app.run(debug=True)