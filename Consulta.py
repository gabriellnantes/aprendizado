import pyodbc

consulta_marca = input('Digite a marca: ')


server = 'A5679'
database = 'VEICULO'
username = 'user_app'
password = '92357955'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = cnxn.cursor()

cursor.execute(
    "select * from carro where marca = '{}'" .format(consulta_marca))
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()
