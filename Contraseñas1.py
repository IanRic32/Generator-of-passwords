# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 11:45:38 2021

@author: riosv
"""
import sqlite3
import random
listap=['in','Car','Per','futUr','iv','Co','1nd3x','@','C@H','l@m','c1','l','D3B','4r@N','N@n','1x']
contrase=[]
r=input("Ingresa el correo electronico:\t")
for i in range (1,5):
	lista=random.choice(listap)
	contrase.append(lista)
cad="ñ".join(contrase)
contrasena=[str(cad)]

conexion=sqlite3.connect('Contraseñas.db')
cursor=conexion.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS Contraseñas
               (Num_Contraseña INTEGER PRIMARY KEY AUTOINCREMENT,
               Contraseña TEXT)
               ''')
if [str(cad)]==cursor.execute('SELECT * FROM Contraseñas WHERE Contraseña=?',[str(cad)]):
    print("Esta contraseña ya la usaste\nVuelve a intentarlo")
    conexion.close()
else:
    cursor.executemany('INSERT INTO Contraseñas(Num_Contraseña,Contraseña) VALUES(NULL,?)',[contrasena]) 
    print("Tu nueva contraseña es:\t",cad,"\nSe guardo en el correo:\t%s"%r,"\nRevisa en la Tabla llamada Correos")

    cursor.execute('''
                     Create table if not exists Correos (Num_us INTEGER PRIMARY KEY AUTOINCREMENT,Correo TEXT)                    
                      ''')
    cursor.executemany('INSERT INTO Correos(Num_us,Correo) VALUES(NULL,?)',[([r])])
    conexion.commit()
    conexion.close()
