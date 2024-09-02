import mysql.connector

conection_mysql = mysql.connector.connect(
    host='localhost',
    user='local_user',
    password='local_password',
    database='seu_database',
)

cursor = conection_mysql.cursor()

# CREATOR
nome_produto = "Todynho" # NOQA
valor = 10
inserir = f'INSERT INTO Vendas (nome_produto, valor) VALUES("{nome_produto}", {valor})' # NOQA
cursor.execute(inserir)
conection_mysql.commit()
# - fim creator

# READ
selecionar = (f'SELECT nome_produto as "Nome do Produto",' # NOQA
           f'valor as "Preço"' 
           f'FROM vendas') # NOQA
cursor.execute(selecionar)
result = cursor.fetchall()
print(result)
# - fim read

# UPDATE
update = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(update)
conection_mysql.commit()

# DELETE

delete = f'DELETE FROM vendas WHERE id = 4'# delete por ID # NOQA
cursor.execute(delete)
conection_mysql.commit()


cursor.close()
conection_mysql.close()
