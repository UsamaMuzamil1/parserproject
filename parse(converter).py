import datetime
import mysql.connector as msql

Hexa_Code = "000000000000004b08010000017564e56e580027f9d4df0ed17380001000690f0000000f07f001150445010101b300fa01fb0106425434180000cd7255ceea0c430ff809002b02c70000390b100000aeeb000100008f1a"

# print("Slide 1 ")

ZeroBytes_hex = Hexa_Code[0:8]
#print(ZeroBytes_hex)

ZeroBytes_int = int(ZeroBytes_hex, 16)
#print(ZeroBytes_int)

DataFieldLength_hex = Hexa_Code[8:16]
#print(DataFieldLength_hex)

DataFieldLength_int = int(DataFieldLength_hex, 16)
#print(DataFieldLength_int)

CodecID_hex = Hexa_Code[16:18]
#print(CodecID_hex)

CodecID_int = int(CodecID_hex, 16)
#print(CodecID_int)

NumberofData1Records_hex = Hexa_Code[18:20]
#print(NumberofData1Records_hex)

NumberofData1Records_int = int(NumberofData1Records_hex, 16)
#print(NumberofData1Records_int)

Timestamp_hex = Hexa_Code[20:36]
#print(Timestamp_hex)

Timestamp_int = int(Timestamp_hex, 16)
#print(Timestamp_int)


date = datetime.datetime.fromtimestamp(Timestamp_int / 1e3)
#print(date)


Priority_hex = Hexa_Code[36:38]
#print(Priority_hex)

Priority_int = int(Priority_hex, 16)
#print(Priority_int)

Longitude_hex = Hexa_Code[38:46]
#print(Longitude_hex)

Longitude_int = int(Longitude_hex, 16)
#print(Longitude_int)
a = Longitude_int/10000000
#print(a)


Latitude_hex = Hexa_Code[46:54]
#print(Latitude_hex)

Latitude_int = int(Latitude_hex, 16)
#print(Latitude_int)
b = Latitude_int/10000000
#print(b)


Altitude_hex = Hexa_Code[54:58]
#print(Altitude_hex)

Altitude_int = int(Altitude_hex, 16)
#print(Altitude_int)

Angle_hex = Hexa_Code[58:62]
#print(Angle_hex)

Angle_int = int(Angle_hex, 16)
#print(Angle_int)

Satellites_hex = Hexa_Code[62:64]
#print(Satellites_hex)

Satellites_int = int(Satellites_hex, 16)
#print(Satellites_int)

Speed_hex = Hexa_Code[64:68]
#print(Speed_hex)

Speed_int = int(Speed_hex, 16)
#print(Speed_int)

#print('\n')

Event_IO_ID_hex = Hexa_Code[68:70]
#print(Event_IO_ID_hex)

Event_IO_ID_int = int(Event_IO_ID_hex, 16)
#print(Event_IO_ID_int)

NofTotalID_hex = Hexa_Code[70:72]
#print(NofTotalID_hex)

NofTotalID_int = int(NofTotalID_hex, 16)
#print(NofTotalID_int)

N1ofOneByteIO_hex = Hexa_Code[72:74]
#print(N1ofOneByteIO_hex)

N1ofOneByteIO_int = int(N1ofOneByteIO_hex, 16)
#print(N1ofOneByteIO_int)

FirsttIOID_hex = Hexa_Code[74:78]
#print(FirsttIOID_hex)

FirsttIOID_int = int(FirsttIOID_hex, 16)
#print(FirsttIOID_int)

FirstIOValue_hex = Hexa_Code[78:80]
#print(FirstIOValue_hex)

FirstIOValue_int = int(FirstIOValue_hex, 16)
#print(FirstIOValue_int)

SecondIOID_hex = Hexa_Code[80:82]
#print(SecondIOID_hex)

SecondIOID_int = int(SecondIOID_hex, 16)
#print(SecondIOID_int)

SecondIOValue_hex = Hexa_Code[82:84]
#print(SecondIOValue_hex)

SecondIOValue_int = int(SecondIOValue_hex, 16)
#print(SecondIOValue_int)

ThirdIOID_hex = Hexa_Code[84:86]
#print(ThirdIOID_hex)

ThirdIOID_int = int(ThirdIOID_hex, 16)
#print(ThirdIOID_int)

ThirdIOValue_hex = Hexa_Code[86:88]
#print(ThirdIOValue_hex)

ThirdIOValue_int = int(ThirdIOValue_hex, 16)
#print(ThirdIOValue_int)


FourthIOID_hex = Hexa_Code[88:90]
#print(FourthIOID_hex)

FourthIOID_int = int(FourthIOID_hex, 16)
#print(FourthIOID_int)

FourthIOValue_hex = Hexa_Code[90:92]
#print(FourthIOValue_hex)

FourthIOValue_int = int(FourthIOValue_hex, 16)
#print(FourthIOValue_int)

#print('\n')

FifthIOID_hex = Hexa_Code[92:94]
#print(FifthIOID_hex)

FifthIOID_int = int(FifthIOID_hex, 16)
#print(FifthIOID_int)

FifthIOValue_hex = Hexa_Code[94:96]
#print(FifthIOValue_hex)

FifthIOValue_int = int(FifthIOValue_hex, 16)
#print(FifthIOValue_int)

SixthIOID_hex = Hexa_Code[96:98]
#print(SixthIOID_hex)

SixthIOID_int = int(SixthIOID_hex, 16)
#print(SixthIOID_int)

SixthIOValue_hex = Hexa_Code[98:100]
#print(SixthIOValue_hex)

SixthIOValue_int = int(SixthIOValue_hex, 16)
#print(SixthIOValue_int)

SeventhIOID_hex = Hexa_Code[100:102]
#print(SeventhIOID_hex)

SeventhIOID_int = int(SeventhIOID_hex, 16)
#print(SeventhIOID_int)

SeventhIOValue_hex = Hexa_Code[102:104]
#print(SeventhIOValue_hex)

SeventhIOValue_int = int(SeventhIOValue_hex, 16)
#print(SeventhIOValue_int)

N2ofTwoBytesIO_hex = Hexa_Code[104:106]
#print(N2ofTwoBytesIO_hex)

N2ofTwoBytesIO_int = int(N2ofTwoBytesIO_hex, 16)
#print(N2ofTwoBytesIO_int)

First_IOID_hex = Hexa_Code[106:108]
#print(First_IOID_hex)

First_IOID_int = int(First_IOID_hex, 16)
#print(First_IOID_int)

First_IOValue_hex = Hexa_Code[108:112]
#print(First_IOValue_hex)

First_IOValue_int = int(First_IOValue_hex, 16)
#print(First_IOValue_int)

Second_IOID_hex = Hexa_Code[112:114]
#print(Second_IOID_hex)

Second_IOID_int = int(Second_IOID_hex, 16)
#print(Second_IOID_int)

Second_IOValue_hex = Hexa_Code[114:118]
#print(Second_IOValue_hex)

Second_IOValue_int = int(Second_IOValue_hex, 16)
#print(Second_IOValue_int)

#print('\n')

ThirdIOID_hex = Hexa_Code[118:120]
#print(ThirdIOID_hex)

ThirdIOID_int = int(ThirdIOID_hex, 16)
#print(ThirdIOID_int)

ThirdIOValue_hex = Hexa_Code[120:124]
#print(ThirdIOValue_hex)

ThirdIOValue_int = int(ThirdIOValue_hex, 16)
#print(ThirdIOValue_int)


FourthIOID_hex = Hexa_Code[124:126]
#print(FourthIOID_hex)

FourthIOID_int = int(FourthIOID_hex, 16)
#print(FourthIOID_int)

FourthIOValue_hex = Hexa_Code[126:130]
#print(FourthIOValue_hex)

FourthIOValue_int = int(FourthIOValue_hex, 16)
#print(FourthIOValue_int)

FifthIOID_hex = Hexa_Code[130:132]
#print(FifthIOID_hex)

FifthIOID_int = int(FifthIOID_hex, 16)
#print(FifthIOID_int)

FifthIOValue_hex = Hexa_Code[132:136]
#print(FifthIOValue_hex)

FifthIOValue_int = int(FifthIOValue_hex, 16)
#print(FifthIOValue_int)

SixthIOID_hex = Hexa_Code[136:138]
#print(SixthIOID_hex)

SixthIOID_int = int(SixthIOID_hex, 16)
#print(SixthIOID_int)

SixthIOValue_hex = Hexa_Code[138:142]
#print(SixthIOValue_hex)

SixthIOValue_int = int(SixthIOValue_hex, 16)
#print(SixthIOValue_int)

N4ofFourBytesIO_hex = Hexa_Code[142:146]
#print(N4ofFourBytesIO_hex)

N4ofFourBytesIO_int = int(N4ofFourBytesIO_hex, 16)
#print(N4ofFourBytesIO_int)

First__IOID_hex = Hexa_Code[146:148]
#print(First__IOID_hex)

First__IOID_int = int(First__IOID_hex, 16)
#print(First__IOID_int)

First__IOValue_hex = Hexa_Code[148:156]
#print(First__IOValue_hex)

First__IOValue_int = int(First__IOValue_hex, 16)
#print(First__IOValue_int)

#print('\n')

Second__IOID_hex = Hexa_Code[156:158]
#print(Second__IOID_hex)

Second__IOID_int = int(Second__IOID_hex, 16)
#print(Second__IOID_int)

Second__IOValue_hex = Hexa_Code[158:166]
#print(Second__IOValue_hex)

Second__IOValue_int = int(Second__IOValue_hex, 16)
#print(Second__IOValue_int)

N8ofEightBytesIO_hex = Hexa_Code[166:168]
#print(N8ofEightBytesIO_hex)

N8ofEightBytesIO_int = int(N8ofEightBytesIO_hex, 16)
#print(N8ofEightBytesIO_int)

NumberofData2NumberofTotalRecords_hex = Hexa_Code[168:170]
#print(NumberofData2NumberofTotalRecords_hex)

NumberofData2NumberofTotalRecords_int = int(NumberofData2NumberofTotalRecords_hex, 16)
#print(NumberofData2NumberofTotalRecords_int)

CRC_16_hex = Hexa_Code[170:178]
#print(CRC_16_hex)

CRC_16_int = int(CRC_16_hex, 16)
#print(CRC_16_int)


# conn = msql.connect(host='localhost', user='root', password='password')  # give ur username, password
# cursor = conn.cursor()
# cursor.execute("CREATE DATABASE parsingdata")

conn = msql.connect(host='localhost', user='root', password='password', database='parsingdata')
cursor = conn.cursor()


import mysql.connector


'''cursor.execute("CREATE TABLE ParsingDetail (Zero_Bytes VARCHAR(255),"
                                      "Data_Field_Length VARCHAR(255),"
                                      "Codec_ID VARCHAR(255),"
                                      "Number_of_Data1_Records VARCHAR(255),"
                                      "Timestamp VARCHAR(255),"
                                      "Priority VARCHAR(255),"
                                      "Longitude VARCHAR(255),"
                                      "Latitude VARCHAR(255),"
                                      "Altitude VARCHAR(255),"
                                      "Angle VARCHAR(255),"
                                      "Satellites VARCHAR(255),"
                                      "Speed VARCHAR(255),"
              "Event_IO_ID VARCHAR(255),"
              "N_of_Total_ID VARCHAR(255),"
              "N1_of_One_Byte VARCHAR(255),"
              "first_IO_ID VARCHAR(255),"
              "first_IO_Value VARCHAR(255),"
              "second_IO_ID VARCHAR(255),"
              "second_IO_Value VARCHAR(255),"
              "third_IO_ID VARCHAR(255),"
              "third_IO_Value VARCHAR(255),"
              "fourth_IO_ID VARCHAR(255),"
              "fourth_IO_Value VARCHAR(255),"
              "fifth_IO_ID VARCHAR(255),"
              "fifth_IO_Value VARCHAR(255),"
              "sixth_IO_ID VARCHAR(255),"
              "sixth_IO_Value VARCHAR(255),"
              "seventh_IO_ID VARCHAR(255),"
              "seventh_IO_Value VARCHAR(255),"
              "N2_of_Two_Byte VARCHAR(255),"
              "first__IO_ID VARCHAR(255),"
              "first__IO_Value VARCHAR(255),"
              "second__IO_ID VARCHAR(255),"
              "second__IO_Value VARCHAR(255),"
              "third__IO_ID VARCHAR(255),"
              "third__IO_Value VARCHAR(255),"
              "fourth__IO_ID VARCHAR(255),"
              "fourth__IO_Value VARCHAR(255),"
              "fifth__IO_ID VARCHAR(255),"
              "fifth__IO_Value VARCHAR(255),"
              "sixth__IO_ID VARCHAR(255),"
              "sixth__IO_Value VARCHAR(255),"
              "N4_of_Four_Byte VARCHAR(255),"
              "first_IO__ID VARCHAR(255),"
              "first_IO__Value VARCHAR(255),"
              "second_IO__ID VARCHAR(255),"
              "second_IO__Value VARCHAR(255),"
              "N8_of_Eight_Byte VARCHAR(255),"
              "Number_of_Data_2_Number_of_Total_Records VARCHAR(255),"
              "CRC_16 VARCHAR(255))")



print("parsing code")
def insert_varibles_into_table(Zero_Bytes,Data_Field_Length,Codec_ID,Number_of_Data1_Records,Timestamp,Priority,Longitude,Latitude,Altitude,Angle,Satellites,Speed,Event_IO_ID,N_of_Total_ID,N1_of_One_Byte,first_IO_ID,first_IO_Value,second_IO_ID,second_IO_Value,third_IO_ID,third_IO_Value,fourth_IO_ID,fourth_IO_Value,fifth_IO_ID,fifth_IO_Value,sixth_IO_ID,sixth_IO_Value,seventh_IO_ID,seventh_IO_Value,N2_of_Two_Byte,first__IO_ID,first__IO_Value,second__IO_ID,second__IO_Value,third__IO_ID,third__IO_Value,fourth__IO_ID,fourth__IO_Value,fifth__IO_ID,fifth__IO_Value,sixth__IO_ID,sixth__IO_Value,N4_of_Four_Byte,first_IO__ID,first_IO__Value,second_IO__ID,second_IO__Value,N8_of_Eight_Byte,Number_of_Data_2_Number_of_Total_Records,CRC_16):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='parsingdata',
                                             user='root',
                                             password='password')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO ParsingDetail(Zero_Bytes,Data_Field_Length,Codec_ID,Number_of_Data1_Records,Timestamp,Priority,Longitude,Latitude,Altitude,Angle,Satellites,Speed,Event_IO_ID,N_of_Total_ID,N1_of_One_Byte,first_IO_ID,first_IO_Value,second_IO_ID,second_IO_Value,third_IO_ID,third_IO_Value,fourth_IO_ID,fourth_IO_Value,fifth_IO_ID,fifth_IO_Value,sixth_IO_ID,sixth_IO_Value,seventh_IO_ID,seventh_IO_Value,N2_of_Two_Byte,first__IO_ID,first__IO_Value,second__IO_ID,second__IO_Value,third__IO_ID,third__IO_Value,fourth__IO_ID,fourth__IO_Value,fifth__IO_ID,fifth__IO_Value,sixth__IO_ID,sixth__IO_Value,N4_of_Four_Byte,first_IO__ID,first_IO__Value,second_IO__ID,second_IO__Value,N8_of_Eight_Byte,Number_of_Data_2_Number_of_Total_Records,CRC_16) 
                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """

        record = (Zero_Bytes,Data_Field_Length,Codec_ID,Number_of_Data1_Records,Timestamp,Priority,Longitude,Latitude,Altitude,Angle,Satellites,Speed,Event_IO_ID,N_of_Total_ID,N1_of_One_Byte,first_IO_ID,first_IO_Value,second_IO_ID,second_IO_Value,third_IO_ID,third_IO_Value,fourth_IO_ID,fourth_IO_Value,fifth_IO_ID,fifth_IO_Value,sixth_IO_ID,sixth_IO_Value,seventh_IO_ID,seventh_IO_Value,N2_of_Two_Byte,first__IO_ID,first__IO_Value,second__IO_ID,second__IO_Value,third__IO_ID,third__IO_Value,fourth__IO_ID,fourth__IO_Value,fifth__IO_ID,fifth__IO_Value,sixth__IO_ID,sixth__IO_Value,N4_of_Four_Byte,first_IO__ID,first_IO__Value,second_IO__ID,second_IO__Value,N8_of_Eight_Byte,Number_of_Data_2_Number_of_Total_Records,CRC_16)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into ParsingDetail table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


insert_varibles_into_table(ZeroBytes_int, DataFieldLength_int, CodecID_int, NumberofData1Records_int, date, Priority_int, a, b, Altitude_int, Angle_int ,Satellites_int,Speed_int,Event_IO_ID_int,NofTotalID_int,N1ofOneByteIO_int,FirsttIOID_int,FirstIOValue_int,SecondIOID_int,SecondIOValue_int,ThirdIOID_int,ThirdIOValue_int,FourthIOID_int,FourthIOValue_int,FifthIOID_int,FifthIOValue_int,SixthIOID_int,SixthIOValue_int,SeventhIOID_int,SeventhIOValue_int,N2ofTwoBytesIO_int,First_IOID_int,First_IOValue_int,Second_IOID_int,Second_IOValue_int,ThirdIOID_int,ThirdIOValue_int,FourthIOID_int,FourthIOValue_int,FifthIOID_int,FifthIOValue_int,SixthIOID_int,SixthIOValue_int,N4ofFourBytesIO_int,First__IOID_int,First__IOValue_int,Second__IOID_int,Second__IOValue_int,N8ofEightBytesIO_int,NumberofData2NumberofTotalRecords_int,CRC_16_int)




# i am adding extra row by inserting hardcore values to check in table form

VALUES = ("20", "715", "78", "12", "2022-06-26 18:12:39", "0", "55.0684383", "74.8607616", "106", "15","5", "0","10", "75", "28", "2", "2022", "0", "5506", "7616", "16", "115","25", "0","2", "7151", "278", "712", "202", "10", "55843", "2472", "06", "5","544", "10","220", "785", "38", "312", "29", "0", "5383", "7506", "1", "15277","7472", "41","0", "70457")
query = "INSERT INTO ParsingDetail(Zero_Bytes,Data_Field_Length,Codec_ID,Number_of_Data1_Records,Timestamp,Priority,Longitude,Latitude,Altitude,Angle,Satellites,Speed,Event_IO_ID,N_of_Total_ID,N1_of_One_Byte,first_IO_ID,first_IO_Value,second_IO_ID,second_IO_Value,third_IO_ID,third_IO_Value,fourth_IO_ID,fourth_IO_Value,fifth_IO_ID,fifth_IO_Value,sixth_IO_ID,sixth_IO_Value,seventh_IO_ID,seventh_IO_Value,N2_of_Two_Byte,first__IO_ID,first__IO_Value,second__IO_ID,second__IO_Value,third__IO_ID,third__IO_Value,fourth__IO_ID,fourth__IO_Value,fifth__IO_ID,fifth__IO_Value,sixth__IO_ID,sixth__IO_Value,N4_of_Four_Byte,first_IO__ID,first_IO__Value,second_IO__ID,second_IO__Value,N8_of_Eight_Byte,Number_of_Data_2_Number_of_Total_Records,CRC_16) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
cursor.execute(query, VALUES)
conn.commit()'''


cursor.execute("SELECT * FROM ParsingDetail")
record1 = cursor.fetchone()

record2 = cursor.fetchone()



from tabulate import tabulate

fetchrecord = [record1,record2]

print(tabulate(fetchrecord, headers=["Zero_Bytes","Data_Field_Length","Codec_ID","Number_of_Data1_Records","Timestamp","Priority","Longitude","Latitude","Altitude","Angle","Satellites","Speed","Event_IO_ID","N_of_Total_ID","N1_of_One_Byte","first_IO_ID","first_IO_Value","second_IO_ID","second_IO_Value","third_IO_ID","third_IO_Value","fourth_IO_ID","fourth_IO_Value","fifth_IO_ID","fifth_IO_Value","sixth_IO_ID","sixth_IO_Value","seventh_IO_ID","seventh_IO_Value","N2_of_Two_Byte","first__IO_ID","first__IO_Value","second__IO_ID","second__IO_Value","third__IO_ID","third__IO_Value","fourth__IO_ID","fourth__IO_Value","fifth__IO_ID","fifth__IO_Value","sixth__IO_ID","sixth__IO_Value","N4_of_Four_Byte","first_IO__ID","first_IO__Value","second_IO__ID","second_IO__Value","N8_of_Eight_Byte","Number_of_Data_2_Number_of_Total_Records","CRC_16"]))

