import pymysql
def database_connection():
    return pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='college')
def all_students():
    student_list = []
    table_columns = []
    sql_query = "select * from students"
    try:
        connection = database_connection()
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            for data in cursor.description:
                table_columns.append(data[0])
            result = cursor.fetchall()
    finally:
        connection.close()
    for data in result:
        student_list.append(dict(zip(tuple(table_columns), data)))
    return student_list