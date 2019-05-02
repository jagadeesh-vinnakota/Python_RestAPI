import pymysql


def database_connection():
    return pymysql.connect(host='localhost', user='root', password='root', db='college')

# data base function for retrieving data from data base
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


# Data base function for inserting into data base.
def insert_or_delete_data(sql_query, parameters):
    try:
        connection = database_connection()
        with connection.cursor() as cursor:
            result = cursor.execute(sql_query, parameters)
            connection.commit()
            print(f"Done Execution query and created {str(result)}")
        connection.close()
    except Exception as e:
        return {"error": f"Something went wrong while inserting data into data base. Please check query. {e.__str__()}"}, False
    return result


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
    sql_query = "insert into `students` WHERE `gender`=%s"
    result, table_columns = retrieve_data(sql_query, params_list)
    for data in result:
        student_list.append(dict(zip(tuple(table_columns), data)))
    if student_list:
        return student_list, True
    else:
        return [], False


def student_creation(data):
    sql_query = "INSERT INTO `students` (`fname`, `lname`, `age`, `gender`) VALUES (%s, %s, %s, %s)"
    parameters = []
    parameters.append(data['first_name'])
    parameters.append(data['last_name'])
    parameters.append(data['age'])
    parameters.append(data['gender'])

    result = insert_or_delete_data(sql_query, parameters)
    if result > 0:
        return {"message": "Student created with the provided data"}, True
    else:
        return {}, False


def student_removal(student_id):
    sql_query = "DELETE FROM `students` WHERE `id` =%s"
    result = insert_or_delete_data(sql_query, [student_id])
    if result > 0:
        return {"message": "Student deleted with the provided student id"}, True
    else:
        return {}, False


def student_updation(data):
    pass
