from flask import redirect, render_template, request, Blueprint, flash
from interact_with_DB import interact_db

assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         static_url_path='/assignment10',
                         template_folder='templates')


# insertion
@assignment10.route('/insert_user', methods=['POST'])
def insert_user_func():
    name = request.form['name']
    email = request.form['email']
    query = "INSERT INTO users(name, email) VALUES ('%s', '%s');" % (name, email)
    interact_db(query=query, query_type='commit')
    flash('Insertion has been done successfully!')
    return redirect('/assignment10')


# update
@assignment10.route('/update_user', methods=['POST'])
def update_user_func():
    id = request.form['user_id']
    name = request.form['name']
    email = request.form['email']
    query = "select * FROM users WHERE user_id = '%s';" % id
    is_exist = interact_db(query=query, query_type='fetch')
    if len(is_exist) > 0:
        query = "UPDATE users SET name='%s', email='%s' WHERE user_id = '%s';" % (name, email, id)
        interact_db(query=query, query_type='commit')
        flash('Update has been done successfully!')
        return redirect('/assignment10')
    else:
        flash('No user holds this id in our database, please try to insert another id!')
        return redirect('/assignment10')


# deletion
@assignment10.route('/delete_user', methods=['POST'])
def delete_user_func():
    id = request.form['user_id']
    query = "DELETE FROM users WHERE user_id='%s'" % id
    interact_db(query=query, query_type='commit')
    flash(f"User { id } has been deleted!")
    return redirect('/assignment10')


# display
@assignment10.route('/assignment10', methods=['GET', 'POST'])
def assignment10_func():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users)

