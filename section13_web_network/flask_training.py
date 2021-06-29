import sqlite3
from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response

app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('flask_sqlite.db')
    return db


@app.teardown_appcontext
def close_connection(exception):
    """
        @app.teardown_appcontextでアプリ開始時にDB接続,終了時にDB接続を切る
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/employee', methods=['POST', 'PUT', 'DELETE'])
@app.route('/employee/<name>', methods=['GET'])
def employee(name=None):
    db = get_db()
    curs = db.cursor()

    curs.execute(
        'CREATE TABLE IF NOT EXISTS persons('
        'id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
    )
    db.commit()

    name = request.values.get('name', name)
    if request.method == 'GET':
        curs.execute(f'SELECT * FROM persons WHERE name = "{name}"')
        person = curs.fetchone()
        if not person:
            return "No", 404
        user_id, name = person
        print(person)
        return f'{user_id}: {name}', 200

    if request.method == 'POST':
        curs.execute(f'INSERT INTO persons(name) values("{name}")')
        db.commit()
        return f'Created: {name}', 201

    if request.method == 'PUT':
        new_name = request.values['new_name']
        curs.execute(f'UPDATE persons set name = "{new_name}" WHERE name = "{name}"')
        db.commit()
        return f'Updated: {name} -> {new_name}', 200

    if request.method == 'DELETE':
        curs.execute(f'DELETE FROM persons WHERE name = "{name}"')
        db.commit()
        return f'Deleted: {name}', 200

    curs.close()


@app.route('/')
def hello_world():
    return 'top page'


@app.route('/hello')
@app.route('/hello/<username>')
def hello_world2(username=None):
    # if username is None:
    #     return 'hello world!!!'
    # else:
    #     return f'hello world!!!{username}'
    return render_template('hello.html', username=username)


@app.route('/post', methods=['POST'])
def show_post():
    return str(request.values)


def main():
    app.debug = True
    app.run()
    # app.run(host='127.0.0.1', port=5000)


if __name__ == '__main__':
    main()
