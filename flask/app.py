#Importing flask module
from flask import Flask, render_template, request
# Create Flask app
app = Flask(__name__, template_folder='template') # Specifying custom template folder name because the directory is named 'template', not 'templates'

# Route for register page
@app.route('/register')




def register():
    return render_template('register.html')
@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

# FIX: Renamed function from 'register' to 'register_post' to avoid duplicate function name error.
# Python does not allow two functions with the same name - the second definition would overwrite the first.
@app.route('/register', methods=['POST'])
def register_post():
    username = request.form['username']
    city = request.form['city']
    phone = request.form['phone']
    password = request.form['password']
    # Pass the form data to the confirmation template to display it
    return render_template('confirmation.html', username=username, city=city, phone=phone, password=password)


# Run the app
if __name__ == '__main__':
    app.run(debug=True) #Running the app