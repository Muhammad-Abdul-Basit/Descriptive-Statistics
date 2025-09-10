import pandas
import numpy
from scipy import stats
from databaseconnect import get_connection
conn = get_connection()
cursor = conn.cursor()
cursor.execute("select rental_duration from film")
data = cursor.fetchall()
dataFile = pandas.DataFrame(data, columns=["Rental duration"])
rentalDuration = dataFile["Rental duration"]
# Calculations
column1 = ["Minimum", "Maximum", "Q1 (25%)", "Q3 (75%)", "Range", "IQR"]
column2 = []
minimum = numpy.min(rentalDuration)
maximum = numpy.max(rentalDuration)
q1 = numpy.percentile(rentalDuration, 25)
q3 = numpy.percentile(rentalDuration, 75)
rental_range = maximum - minimum
iqr = q3 - q1
column2.extend([minimum, maximum, q1, q3, rental_range, iqr])
resultFile = pandas.DataFrame({"Method": column1, "Value": column2})
resultFile.to_excel(r"D:\BSIT\Python libraries\Descriptive-Statistics\reports\rentalDuration.xlsx", index=False)
print("File saved")
