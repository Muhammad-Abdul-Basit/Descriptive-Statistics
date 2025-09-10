import pandas
import numpy
from scipy import stats
from databaseconnect import get_connection
conn=get_connection()
cursor=conn.cursor()
cursor.execute("select amount from payment")
data=cursor.fetchall()
dataFile=pandas.DataFrame(data, columns=["Amount"])
amount=dataFile["Amount"]
amount=[float(x) for x in amount]
column1=["Average", "Minimum", "Maximum", "1st Quartiles", "2nd Quartile", "3rd Quartile"]
column2=[]
column2.append(numpy.mean(amount))
column2.append(numpy.min(amount))
column2.append(numpy.max(amount))
column2.append(numpy.percentile(amount, 25))
column2.append(numpy.percentile(amount, 50))
column2.append(numpy.percentile(amount, 75))
resultFile=pandas.DataFrame({"Methods ": column1, "Value": column2})
resultFile.to_excel(r"D:\BSIT\Python libraries\Descriptive-Statistics\reports\paymentAounts.xlsx",index=False)
print(" File saved")