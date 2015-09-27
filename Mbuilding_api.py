from flask import Flask, jsonify, g, request
import sqlite3 as sql
from Model import Course

app = Flask(__name__)

DB_path = r'C:\Users\yuhui\PycharmProjects\Mbuilding_api\static\class.db'

@app.teardown_appcontext
def close_conn(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        conn = sql.connect(DB_path)
        conn.row_factory = sql.Row
        db = g._database = conn.cursor()
    return db

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/1.0/course/<int:class_nbr>')
def search_course_by_class_nbr(class_nbr):
    term = request.args.get('term')
    if term:
        query = 'select * from courses where class_nbr=? and term=?'
        res = get_db().execute(query, (class_nbr,term))
    else:
        query = 'select * from courses where class_nbr=?'
        res = get_db().execute(query, (class_nbr,))

    # create sql connection
    course_list = [Course(row) for row in res.fetchall()]

    print course_list
    return jsonify(courses=[course.serialize() for course in course_list])

if __name__ == '__main__':
    app.run(debug=True)
