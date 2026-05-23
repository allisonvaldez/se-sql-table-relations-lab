# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

# View the data
pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# 1. Return the first and last names and the job titles for all employees in Boston.
df_boston = None

# 2. Are there any offices that have zero employees?
df_zero_emp = None

# 3. Return the employees' first name and last name, along with the city and state of the office that they work out of (if they have one). Include all employees and order them by their first name, then their last name.
df_employee = None

# 4. Return all of the customer's contact information (first name, last name, and phone number) as well as their sales rep's employee number for any customer who has not placed an order. Sort the results alphabetically based on the contact's last name. There are several approaches you could take here, including a left join and filtering on null values or using a subquery to filter out customers who do have orders. In total, 24 customers have not placed an order.
df_contacts = None

# 5. Return the employee number, first name, last name, and number of customers for employees whose customers have an average credit limit over 90k. Sort by number of customers from high to low.
Sort by number of customers from high to low.
df_payment = None

# 6. The team wants you to identify these 4 individuals. Return the employee number, first name, last name, and number of customers for employees whose customers have an average credit limit over 90k. Sort by number of customers from high to low.
df_credit = None

# 7. Return the product name and count the number of orders for each product as a column named numorders. Also return a new column, totalunits, that sums up the total quantity of product sold (use the quantityOrdered column). Sort the results by the totalunits column, highest to lowest, to showcase the top-selling products.
df_product_sold = None

# 8. Return the product name, code, and the total number of customers who have ordered each product, aliased as numpurchasers. Sort the results by the highest number of purchasers.
df_total_customers = None

# 9. The team wants to know how many customers there are per office. Return the count as a column named n_customers.
df_customers = None

# 10. Using a subquery or common table expression (CTE), select the employee number, first name, last name, city of the office, and the office code for employees who sold products that have been ordered by fewer than 20 customers.
df_under_20 = None

# Close the connection
conn.close()