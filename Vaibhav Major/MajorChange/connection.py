
import mysql.connector
from mysql.connector import Error

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(id, imgtxt, img):
    # print("Inserting BLOB into python_employee table")
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
        print("Image and file inserted successfully")

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def fetch():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='majorproject',
                                             user='root',
                                             password='root')

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM image")

        myresult = cursor.fetchall()
        for x in myresult:
            print("Data at index: ",x[0])
            print(x[1])
    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def fetchID():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='majorproject',
                                             user='root',
                                             password='root')

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM image")

        myresult = cursor.fetchall()
        count=0
        for x in myresult:
            count+=1
            # print(x)
        return count
    except mysql.connector.Error as error:
        print("Failed inserting! {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")












# Audio

def insertAudio(id, audiotxt, audiofile):
    # print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='majorproject',
                                             user='root',
                                             password='root')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO audio
                          (id, audiotxt, audiofile) VALUES (%s,%s,%s)"""

        #empPicture = convertToBinaryData(photo)
        file = convertToBinaryData(audiofile)

        # Convert data into tuple format
        insert_blob_tuple = (id, audiotxt, audiofile)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Audio file inserted successfully")

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
