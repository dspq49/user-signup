from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    template = jinja_env.get_template('base.html')
    return template.render()




@app.route('/validate-signup', methods=['POST'])
def valid_signup():

    username = request.form['username']
    password_input = request.form['password_input']
    password_verify = request.form['password_verify']
    email = request.form['email']

    
    password_error = ''
    username_error = ''
    password_verify_error = ''
    email_error = ''

    if username == '':
        username_error = 'Enter Username'

    else:
         if len(username) < 3 or len(username) > 20:
            username_error = 'Invaild username'


    if password_input == '':
        password_error = 'Enter password'

    else:
        
         if len(password_input) < 3 or len(password_input) > 20:
            password_error = 'Invaild password'
            

    if password_input != password_verify:
        password_verify_error = 'Please make passwords match'
    

    if email == '':
        email = email
    else:
        if len(email) < 3 or len(email) > 20:
         email_error = 'invaild email'
    
    if not username_error and not password_error:
        username = username
        return redirect('/vaild-signup?username={0}'.format(username))
    else:
        template = jinja_env.get_template('base.html')
        return template.render( username=username, password_error=password_error, username_error=username_error, password_input=password_input, password_verify_error=password_verify_error,email_error=email_error) 
        


@app.route('/vaild-signup')
def vaild_signup():
    username = request.args.get('username')
    return render_template('enter.html', username=username)

app.run()

