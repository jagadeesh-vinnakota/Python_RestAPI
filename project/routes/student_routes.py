from project import app, services
from flask import jsonify, request

# Api route for gathering all students information
@app.route("/v1/students", methods=['GET'])
def student_list():
    students_data, decider = services.all_students()
    if not decider:
        return jsonify(students_data)
    return jsonify(students_data)


# Api route for retrieving single student information. This api route is using path parameters
@app.route("/v1/students/<int:student_id>", methods=['GET'])
def single_student(student_id):
    students_data, decider = services.single_student(student_id)
    if not decider:
        return jsonify(students_data), 404
    return jsonify(students_data)

# Api route for filtering students information by gender. This api route is using query parameters
@app.route("/v1/student/gender", methods=['GET'])
def student_by_gender():
    student_gender = request.args.get('gender')
    if student_gender:
        students_data, decider = services.students_by_gender(student_gender)
        if not decider:
            return jsonify(students_data), 200
        return jsonify(students_data), 200
    else:
        return jsonify({"error": "Please Provide gender value <gender>"})