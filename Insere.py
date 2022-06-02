import pyodbc

modelo_carro = input('Digite o Modelo do carro ')
cor_carro = input('Digite a cor do carro ')
marca_carro = input('Digite a marca do carro ')


server = 'A5679'
database = 'VEICULO'
username = 'user_app'
password = '92357955'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = cnxn.cursor()

count = cursor.execute("""
INSERT INTO carro (modelo, cor, marca) 
VALUES (?,?,?)""",
                       modelo_carro, cor_carro, marca_carro,).rowcount
cnxn.commit()
print('Inserido com exito!')
print('Rows inserted: ' + str(count))
