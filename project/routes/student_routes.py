from project import app, services
from flask import jsonify, request
import json

# Api route for gathering all students information
@app.route("/v1/students", methods=['GET'])
def student_list():
    students_data, decider = services.all_students()
    if not decider:
        return jsonify(students_data)
    return jsonify(students_data)


# Api route for retrieving single student information. This api route is using path parameters
@app.route("/v1/student/<int:student_id>", methods=['GET'])
def single_student(student_id):
    students_data, decider = services.single_student(student_id)
    if not decider:
        return jsonify(students_data), 404
    return jsonify(students_data)

# Api route for filtering students information by gender. This api route is using query parameters
@app.route("/v1/students/gender", methods=['GET'])
def student_by_gender():
    student_gender = request.args.get('gender')
    if student_gender:
        students_data, decider = services.students_by_gender(student_gender)
        if not decider:
            return jsonify(students_data), 200
        return jsonify(students_data), 200
    else:
        return jsonify({"error": "Please Provide gender value <gender>"})


# Api route for creating a new student
@app.route("/v1/student", methods=['POST'])
def create_student():
    if 'first_name' in request.json and 'last_name' in request.json and 'age' in request.json and \
            'gender' in request.json:
        result, decider = services.student_creation(request.json)
        if decider:
            return jsonify(result), 201
        else:
            return jsonify({"Message": "Problem creating student"})
    else:
        return jsonify({"Error": "first_name, last_name, age, gender values are required! "})


@app.route("/v1/student/<int:student_id>", methods=['DELETE'])
def remove_student(student_id):
    result, decider = services.student_removal(student_id)
    if decider:
        return jsonify(result), 201
    else:
        return jsonify({"Message": "Problem deleting student"})

