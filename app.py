from flask import Flask, redirect
from flask import url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify

app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=40)

@app.route('/')
def homePage_func():  # put application's code here
    return render_template('homePage.html')

@app.route('/google')
def google_func():  # put application's code here
    return redirect("https://www.google.com/")


@app.route('/leave_details')
def leave_details_func():  # put application's code here
    return render_template('leave_details.html')

@app.route('/assignment3_1')
def about_page():
    user_info = {'first name': ' Inbar', 'last_name': ' Duvdevani', 'age': ' 27' , 'home town': ' Hayogev'}
    sports = ['Running', 'Frisbee', 'Basketball']
    movies = ['kill bill', 'pirates of the caribbean', 'space jam', 'treasure planet']
   # session['CHECK'] = 'about'
    return render_template('assignment3_1.html',
                           user_info=user_info,
                           sports=sports,
                           movies=movies)


user_dict = {
    'Inbar': ['Inbar@gmail.com', 'Duvdevani', '27', 'Inbi'],
    'Reut': ['Reut@gmail.com', 'Hochwald', '26', 'Widad'],
    'Rinat': ['Rinat@gmail.com', 'Rozenblum', '25', 'Rino'],
    'Hadar': ['Hadar@gmail.com', 'Malki', '25', 'Hadari'],
    'Shahar': ['Shahar@gmail.com', 'Dumani', '25', 'Shuchi'],
    'Tal': ['Tal@gmail.com', 'Kashi', '27', 'Taltul'],
    'Yael': ['Yael@gmail.com', 'Kachanski', '25', 'Yaeli']
}


@app.route('/assignment3_2', methods=['GET', 'POST'])
def go_to_assignment3_2():
    # Get Case
    if request.method == 'GET':
        if 'user_name' in request.args:
            user_name = request.args['user_name']
            if user_name in user_dict:
                return render_template('assignment3_2.html',
                                       user_username=user_name,
                                       user_lastname=user_dict[user_name][1],
                                       user_email=user_dict[user_name][0],
                                       user_age=user_dict[user_name][2],
                                       nickname=user_dict[user_name][3])
            if len(user_name) == 0:
                return render_template('assignment3_2.html',
                                       user_dict=user_dict)
            else:
                return render_template('assignment3_2.html', message='User is not found in the system!')
    # Post Case
    if request.method == 'POST':
        reg_username = request.form['username']
        reg_lastname = request.form['user_lastname']
        reg_email = request.form['email']
        reg_age = request.form['age']
        reg_nickname = request.form['nickname']
        session['username'] = reg_username
        session['user_lastname'] = reg_lastname
        session['email'] = reg_email
        session['age'] = reg_age
        session['nickname'] = reg_nickname
        session['Registered'] = True
        if reg_username in user_dict:
            return render_template('assignment3_2.html', message2='user is already exist!!')
        else:
            new_user = {reg_username: [reg_email, reg_lastname, reg_age, reg_nickname]}
            user_dict.update(new_user)
            return render_template('assignment3_2.html', message2='registration succeeded')

        return render_template('assignment3_2.html')

    return render_template('assignment3_2.html')


@app.route('/session')
def session_func():
    # print(session['CHECK'])
    return jsonify(dict(session))

@app.route('/log_out')
def logout():
    session['Registered'] = False
    session.clear()
    return redirect(url_for('go_to_assignment3_2'))


if __name__ == '__main__':
    app.run(debug=True)
