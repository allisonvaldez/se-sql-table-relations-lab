# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# Connect to the database and view the data
conn = sqlite3.connect('data.sqlite')
employee_location_data = pd.read_sql("""SELECT * FROM sqlite_master""", conn)
print("\n\n--- Employee Data ---")
print(employee_location_data)

# 1. Return the first and last names and the job titles for all employees in Boston.
df_boston = pd.read_sql(""" SELECT e.firstName, e.lastName FROM employees e JOIN offices o ON e.officeCode = o.officeCode WHERE o.city = 'Boston' """, conn)
print("\n\n--- Boston Employees ---")
print(df_boston)

# 2. Are there any offices that have zero employees? Use left join for better efficiency to analyze all offices (even if no employees are returned as a match)
df_zero_emp = pd.read_sql(""" SELECT o.* FROM offices o LEFT JOIN employees e ON o.officeCode = e.officeCode WHERE e.officeCode IS NULL """, conn)
print("\n\n--- Offices with 0 employees ---")
print(df_zero_emp)

# 3. Return the employees' first name and last name, along with the city and state of the office that they work out of (if they have one). Include all employees and order them by their first name, then their last name.
df_employee = pd.read_sql(""" SELECT e.firstName, e.lastName, o.city, o.state FROM employees e LEFT JOIN offices o ON e.officeCode = o.officeCode ORDER BY e.firstName ASC, e.lastName ASC """, conn)
print("\n\n--- Employees by first name and last name with the city and state of their office ---")
print(df_employee)

# 4. Return all of the customer's contact information (first name, last name, and phone number) as well as their sales rep's employee number for any customer who has not placed an order. Sort the results alphabetically based on the contact's last name (24 customers have not placed an order).
df_contacts = pd.read_sql(""" SELECT c.contactFirstName, c.contactLastName, c.phone, c.salesRepEmployeeNumber FROM customers c LEFT JOIN orders o ON c.customerNumber = o.customerNumber WHERE o.orderNumber IS NULL ORDER BY c.contactLastName ASC """, conn)
print("\n\n--- All customer's who did not place an order ---")
print(df_contacts)

# 5. Return customer contacts (first and last names) along with details for each of the customers' payment amounts and dates of payment (results sorted in descending order by the payment amount). Confirm all customer payments are in alignment.
df_payment = pd.read_sql(""" SELECT c.contactFirstName, c.contactLastName, p.amount, p.paymentDate FROM customers c JOIN payments p ON c.customerNumber = p.customerNumber ORDER BY CAST(p.amount AS REAL) DESC """, conn)
print("\n\n--- Confirm customer payments ---")
print(df_payment)

# 6. The team wants you to identify 4 individuals. Return the employee number, first name, last name, and number of customers for employees whose customers have an average credit limit over 90k. Sort by number of customers from high to low.
df_credit = pd.read_sql(""" SELECT e.employeeNumber, e.firstName, e.lastName, COUNT(*) AS number_of_customers FROM employees e JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber GROUP BY e.employeeNumber HAVING AVG(c.creditLimit) > 90000 ORDER BY number_of_customers DESC LIMIT 4 """, conn)
print("\n\n--- Customers with average credit limit over 90k ---")
print(df_credit)

# 7. Return the product name and count the number of orders for each product as a column named numorders. Also return a new column, totalunits, that sums up the total quantity of product sold (use the quantityOrdered column). Sort the results by the totalunits column, highest to lowest, to showcase the top-selling products.
df_product_sold = pd.read_sql(""" SELECT p.productName, COUNT(*) AS numorders, SUM(od.quantityOrdered) AS totalunits FROM products p JOIN orderdetails od on p.productCode = od.productCode GROUP BY p.productCode ORDER BY totalunits DESC """, conn)
print("\n\n--- Product name and order count ---")
print(df_product_sold)

# 8. Return the product name, code, and the total number of customers who have ordered each product, aliased as numpurchasers. Sort the results by the highest number of purchasers.
df_total_customers = pd.read_sql(""" SELECT p.productName, p.productCode, COUNT(DISTINCT o.customerNumber) AS numpurchasers FROM products p JOIN orderdetails od ON p.productCode = od.productCode JOIN orders o ON od.orderNumber = o.orderNumber GROUP BY p.productCode ORDER BY numpurchasers DESC """, conn)
print("\n\n--- Product name, code, and the total number of customers who ordered each product  ---")
print(df_total_customers)

# 9. The team wants to know how many customers there are per office. Return the count as a column named n_customers.
df_customers = pd.read_sql(""" SELECT o.officeCode, o.city, COUNT(DISTINCT c.customerNumber) AS n_customers FROM offices o JOIN employees e ON o.officeCode = e.officeCode JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber GROUP BY o.officeCode """, conn)
print("\n\n--- customers there are per office  ---")
print(df_customers)

# 10. Using a subquery or common table expression (CTE), select the employee number, first name, last name, city of the office, and the office code for employees who sold products that have been ordered by fewer than 20 customers.
df_under_20 = pd.read_sql(""" SELECT DISTINCT e.employeeNumber, e.firstName, e.lastName, o.city, o.officeCode FROM employees e JOIN offices o ON e.officeCode = o.officeCode JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber JOIN orders ord ON c.customerNumber = ord.customerNumber JOIN orderdetails od ON ord.orderNumber = od.orderNumber WHERE od.productCode IN (SELECT p.productCode FROM products p JOIN orderdetails od2 ON p.productCode = od2.productCode JOIN orders o2 ON od2.orderNumber = o2.orderNumber GROUP BY p.productCode HAVING COUNT(DISTINCT o2.customerNumber) < 20) """, conn)
print("\n\n--- Employees who sold products by fewer than 20 customers ---")
print(df_under_20)

# Close the connection
conn.close()