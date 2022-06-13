import mysql
import mysql.connector as msql

# conn = msql.connect(host='localhost', user='root', password='password')  # give ur username, password
# cursor = conn.cursor()
# cursor.execute("CREATE DATABASE parsingdata")

conn = msql.connect(host='localhost', user='root', password='password', database='parsingdata')
cursor = conn.cursor()


cursor.execute("SELECT * FROM ParsingDetail")
record1 = cursor.fetchone()

record2 = cursor.fetchone()



from tabulate import tabulate

fetchrecord = [record1,record2]

print(tabulate(fetchrecord, headers=["Zero_Bytes","Data_Field_Length","Codec_ID","Number_of_Data1_Records","Timestamp","Priority","Longitude","Latitude","Altitude","Angle","Satellites","Speed","Event_IO_ID","N_of_Total_ID","N1_of_One_Byte","first_IO_ID","first_IO_Value","second_IO_ID","second_IO_Value","third_IO_ID","third_IO_Value","fourth_IO_ID","fourth_IO_Value","fifth_IO_ID","fifth_IO_Value","sixth_IO_ID","sixth_IO_Value","seventh_IO_ID","seventh_IO_Value","N2_of_Two_Byte","first__IO_ID","first__IO_Value","second__IO_ID","second__IO_Value","third__IO_ID","third__IO_Value","fourth__IO_ID","fourth__IO_Value","fifth__IO_ID","fifth__IO_Value","sixth__IO_ID","sixth__IO_Value","N4_of_Four_Byte","first_IO__ID","first_IO__Value","second_IO__ID","second_IO__Value","N8_of_Eight_Byte","Number_of_Data_2_Number_of_Total_Records","CRC_16"]))



