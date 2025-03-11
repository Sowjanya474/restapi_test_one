from flask import Flask, jsonify


todo = Flask('_name_')


@todo.route('/students-list')
def students_list():
    students = [
        {
            'id':1,
            'student_name': 'std1',
            'age' : 21,
            'email':'hello@gmail.com'
        },
        {
            'id':2,
            'student_name': 'std2',
            'age' : 21,
            'email':'hello@gmail.com'
        },
        {
            'id':3,
            'student_name': 'std3',
            'age' : 21,
            'email':'hello@gmail.com'
        },
    ]
    return jsonify(students)


# @todo.route('/student/get/<id:int>')
# def students_list():
    return "students list"

if _name_ == '_main_':
    todo.run(
        host="127.0.0.1",
        port=5010,
        debug=True,
    )