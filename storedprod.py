Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pyodbc as po
 
# Connection variables
server = 'ADMIN\SQLEXPRESS'
database = 'JANAMMIS'
username = 'sa'
password = ''
 
try:
    # Connection string
    cnxn = po.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
            server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    cursor = cnxn.cursor()
 
    # Prepare the stored procedure execution script and parameter values
    storedProc = "Exec [dbo].[Display_Client_Category_Analysis] @FinYear = 2022, @FromDate = '01-apr-2022',@ToDate= '31-mar-2023'"
    #params = ("And", 10)
 
    # Execute Stored Procedure With Parameters
    cursor.execute( storedProc )
 
    # Iterate the cursor
    row = cursor.fetchone()
    while row:
        # Print the row
        print(str(row[0]) + " : " + str(row[1] or '') )
        row = cursor.fetchone()
 
    # Close the cursor and delete it
    cursor.close()
    del cursor
 
    # Close the database connection
    cnxn.close()
 
except Exception as e:
    print("Error: %s" % e)