
import sqlite3
import random

listap = ['in', 'Car', 'Per', 'futUr', 'iv', 'Co', '1nd3x', '@', 'C@H', 'l@m', 'c1', 'l', 'D3B', '4r@N', 'N@n', '1x']
correo_electronico = input("Ingresa el correo electronico:\t")

contrasena = [str("ñ".join([random.choice(listap) for _ in range(1, 5)]))]
conexion = sqlite3.connect('Contraseñas.db')
cursor = conexion.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS Contraseñas
               (Contraseña TEXT)
               ''')

cursor.execute('SELECT * FROM Contraseñas WHERE Contraseña=?', contrasena)
result = cursor.fetchone()

if result:
    print("Esta contraseña ya la usaste\nVuelve a intentarlo")
    conexion.close()
else:
    cursor.execute('INSERT INTO Contraseñas(Contraseña) VALUES(?)', contrasena)
    print("Tu nueva contraseña es:\t", contrasena, "\nSe guardo en el correo:\t%s" % correo_electronico, "\nRevisa en la Tabla llamada Correos")

    cursor.execute('''
                     CREATE TABLE IF NOT EXISTS Correos (Correo TEXT)                    
                      ''')
    cursor.execute('INSERT INTO Correos(Correo) VALUES(?)', ([correo_electronico]))
    conexion.commit()
    conexion.close()