
import mysql.connector
from mysql.connector import Error

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(id, imgtxt, img):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='majorproject',
                                             user='root',
                                             password='root')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO image
                          (id, imgtxt, img) VALUES (%s,%s,%s)"""

        #empPicture = convertToBinaryData(photo)
        file = convertToBinaryData(img)

        # Convert data into tuple format
        insert_blob_tuple = (id, imgtxt, file)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB(1, "trying to concentrate on my  work but all I've been doing is.  daydreaming about having you  bent over my desk with your  jeans around your ankles", "U:\\MAJOR\\2.jpg")
