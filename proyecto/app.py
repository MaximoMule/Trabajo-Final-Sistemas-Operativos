from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
from juegos import Juego
import os 

app = Flask(__name__)

client = MongoClient('mongodb://maxi:123@mongodb:27017/')
db = client['juegosdb']
collection = db['juegos']

# Ruta principal 
@app.route('/')
def home():
    juegos = list(collection.find())
    return render_template('index.html', juegos=juegos)

# Ruta para agregar un nuevo juego
@app.route('/juego', methods=['POST'])
def addJuego():
     
    id = request.form['id']
    nombre = request.form['nombre']
    minJugadores = request.form['minJugadores']
    maxJugadores = request.form['maxJugadores']
    limiteEdad=request.form['limiteEdad']
    pais = request.form['pais']
    precio = request.form['precio']

    #Valido que todos los campos estén completos
    if id and nombre and minJugadores and maxJugadores and limiteEdad and pais and precio:
        # Verifico si el id ya existe en la base de datos
        if collection.find_one({'id': id}):
            return jsonify({'error': f'El id {id} ya existe. Por favor, ingrese otro id.'}), 400
        
        #Agrego a la base de datos
        juego = Juego(id, nombre, minJugadores, maxJugadores,limiteEdad,pais, precio)
        collection.insert_one(juego.toDbCollection())
        return redirect(url_for('home'))
    else:
        return notFound()

#Para eliminar libro
@app.route('/delete/<int:juego_id>')
def delete(juego_id):
    collection.delete_one({'id': str(juego_id)})  # Convertir book_id a cadena
    return redirect(url_for('home'))

#Para editar un juego
@app.route('/edit/<int:juego_id>', methods=['POST'])
def edit(juego_id):
    nombre = request.form['nombre']
    minJugadores = request.form['minJugadores']
    maxJugadores = request.form['maxJugadores']
    limiteEdad=request.form['limiteEdad']
    pais = request.form['pais']
    precio = request.form['precio']

    if nombre and minJugadores and maxJugadores and limiteEdad and pais and precio:
        collection.update_one(
            {'id': str(juego_id)}, 
            {'$set': {
                'nombre': nombre,
                'minJugadores': minJugadores,
                'maxJugadores': maxJugadores,
                'limiteEdad' : limiteEdad,
                'pais': pais,
                'precio': precio
            }}
        )
        return redirect(url_for('home'))
    else:
        return notFound()

#Manejador de error 404
@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado: ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
