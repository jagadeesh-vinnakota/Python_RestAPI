import pymysql
import json


def database_connection():
    return pymysql.connect(host='localhost', user='root', password='root', db='college')


def retrieve_data(sql_query, parameters):
    table_columns = []
    try:
        connection = database_connection()
        with connection.cursor() as cursor:
            cursor.execute(sql_query, parameters)
            for data in cursor.description:
                table_columns.append(data[0])
            result = cursor.fetchall()
        connection.close()
    except Exception as e:
        return {"error": f"Something went wrong while retrieving data from data base. Please check query. {e.__str__()}"}, False
    return result, table_columns


# Function for retrieving all the students info from data base
def all_students():
    student_list = []
    sql_query = "select * from students"
    result, table_columns = retrieve_data(sql_query, [])
    for data in result:
        student_list.append(dict(zip(tuple(table_columns), data)))
    return student_list, True


# Function for retrieving single student information based on ID of the student
def single_student(student_id):
    student_list = {}
    params_list = []
    params_list.append(int(student_id))
    sql_query = "SELECT * FROM `students` WHERE `id`=%s"
    result, table_columns = retrieve_data(sql_query, params_list)
    for data in result:
        student_list = dict(zip(tuple(table_columns), data))
        break
    if student_list:
        return student_list, True
    else:
        return {}, False


# Function for filtering students information based on gender
def students_by_gender(gender):
    student_list = []
    params_list = []
    params_list.append(gender)
    sql_query = "SELECT * FROM `students` WHERE `gender`=%s"
    result, table_columns = retrieve_data(sql_query, params_list)
    for data in result:
        student_list.append(dict(zip(tuple(table_columns), data)))
    if student_list:
        return student_list, True
    else:
        return [], False
