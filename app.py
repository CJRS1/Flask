from flask import Flask, render_template #Importando Flask
from flask_mysqldb import MySQL
from os import environ
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

mysql = MySQL(app) #Para usar MySQL

#Para  usar las variables de entorno 
app.config['MYSQL_HOST']=environ.get('MYSQL_HOST')
app.config['MYSQL_USER']=environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD']=environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB']=environ.get('MYSQL_DB')
app.config['MYSQL_PORT']=int(environ.get('MYSQL_PORT'))


#Argegando decoradores
@app.route('/',methods=['GET'])
def funcionando():
    return {
        'message':'Está funcionando correctamente'
    }

@app.route('/inicio',methods=['GET'])
def obtener_datos():
    cursor = mysql.connection.cursor()
    cursor.execute(" SELECT * FROM alumnos")
    resultado = cursor.fetchall() #Devuelve una tupla
    print(resultado)
    resultado_final=[]
    for alumno in resultado:
        alumno_diccionario = {
            'id':alumno[0],
            'nombre':alumno[1],
            'ape_materno':alumno[2],
            'ape_paterno':alumno[3],
            'correo':alumno[4],
            'num_emergencia':alumno[5],
            'curso_id':alumno[6],
        }
    resultado_final.append(alumno_diccionario)
    
    return render_template('inicio.html',alumnos=resultado_final)




app.run(debug = True) #Debug True para que se ejecute el codigo de nuevo