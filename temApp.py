from db import get_connection

'''try:
    connection=get_connection()
    with connection.cursor() as cursor:
        cursor.execute("CALL consultar_alumnos()")
        resutset=cursor.fetchall()
        for row in resutset:
            print(row)
except Exception as ex:
    print('ERROR')'''
'''try:
    connection=get_connection()
    with connection.cursor() as cursor:
        cursor.execute('CALL consultar_alumno(%s)',(3,))
        resutset=cursor.fetchall()
        for row in resutset:
            print(row)
except Exception as ex:
    print('ERROR')'''
try:
    connection=get_connection()
    with connection.cursor() as cursor:
        cursor.execute('CALL agrega_alumno(%s,%s,%s)',('Pancho','Varraza','cocodrilo@gmail.com'))
    connection.commit()
    connection.close()
except Exception as ex:
    print('ERROR')