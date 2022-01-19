from flask import Flask, render_template, request, session, json, jsonify
from interact_with_DB import query_to_json, interact_db
import requests
from components.assignment10.assignment10 import assignment10
app = Flask(__name__)
app.secret_key = '123'

# creating users' dictionary
users = {'user1': {'name': 'Or', 'email': 'or@gmail.com'},
         'user2': {'name': 'Hila', 'email': 'hila@gmail.com'},
         'user3': {'name': 'Daniel', 'email': 'daniel@gmail.com'},
         'user4': {'name': 'Ofir', 'email': 'ofir@gmail.com'},
         'user5': {'name': 'Gil', 'email': 'gil@gmail.com'},
         'user6': {'name': 'Anat', 'email': 'anat@gmail.com'}
         }


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment_9():
    if 'mail' in request.args:
        email = request.args['mail']
        if email == '':
            return render_template('assignment9.html', users_list=users)
        else:
            for key, value in users.items():
                if value.get('email') == email:
                    return render_template('assignment9.html', p_name=value.get('name'), p_mail=value.get('email'))
        return render_template('assignment9.html', users_list=users)
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        return render_template('assignment9.html', p_username=username, p_password=password)
    return render_template('assignment9.html')


@app.route("/logout", methods=['GET', 'POST'])
def logout_func():
    session['username'] = ''
    return render_template('assignment9.html')


@app.route('/home')
@app.route('/')
def home_func():
    return render_template('home.html')


app.register_blueprint(assignment10)


@app.route('/assignment11/users')
def ass11_users_func():
    query = "select * from users"
    query_result = query_to_json(query=query)
    return json.dumps(query_result)


@app.route("/assignment11/outer_source", methods=['GET'])
def ass11_outer_source_func():
    if 'number' in request.args:
        number = request.args['number']
        result = requests.get(f'https://reqres.in/api/users/{number}')
        result = result.json()
        return render_template('assignment_11_outer_source.html', user=result['data'])
    return render_template('assignment_11_outer_source.html')


@app.route("/assignment12/restapi_users/<int:user_id>")
@app.route('/assignment12/restapi_users', defaults={'user_id': 6})
def get_user_by_id_func(user_id):
    query = 'select * from users where user_id=%s;' % user_id
    user = query_to_json(query=query)
    if len(user) == 0:
        user = {
            'status': 'failed', 'message': 'user not found'
        }
    else:
        user = user[0]
    return json.dumps(user)


if __name__ == '__main__':
    app.run(debug=True)

