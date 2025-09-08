import pandas
import numpy
from scipy import stats
from databaseconnect import get_connection
conn=get_connection()
cursor=conn.cursor()
cursor.execute(
                """
            select CONCAT (c.first_name, ' ', c.last_name) AS FullName, Count(r.rental_id) AS TotalRentals
            from customer c JOIN
            rental r ON r.customer_id=c.customer_id JOIN
            inventory i ON i.inventory_id=r.inventory_id JOIN
            film f ON f.film_id=i.film_id
            group by FullName
            order by TotalRentals desc
                """
)
data=cursor.fetchall()
dataFile=pandas.DataFrame(data, columns=["CustomerName", "TotalRentals"])
rentals=dataFile["TotalRentals"]
column1=["Mean", "Median", "Mode", "Variance", "Standard deviation"]
column2=[]
column2.append(numpy.mean(rentals))
column2.append(numpy.median(rentals))
column2.append(stats.mode(rentals, keepdims=True).mode[0])
column2.append(numpy.var(rentals))
column2.append(numpy.std(rentals))
resultFile=pandas.DataFrame({"Methods": column1, "Value": column2})
resultFile.to_excel(r"D:\BSIT\Python libraries\Descriptive-Statistics\reports\customerrentals.xlsx",index=False)
print(" File saved ")