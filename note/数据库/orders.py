import pymysql

cnne = pymysql.Connect(

)

cursor = cnne.cursor()
sql = ""
cursor.execute(sql)
cnne.commit()
cursor.close()
cnne.close()