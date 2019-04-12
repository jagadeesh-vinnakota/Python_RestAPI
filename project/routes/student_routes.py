from project import app, services
from flask import jsonify

@app.route("/v1/students", methods=['GET'])
def student_list():
    return jsonify(services.all_students())