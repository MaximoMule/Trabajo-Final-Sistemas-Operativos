----Python-Flask-Docker-MongoDB-Apache HTTP Server:Trabajo final SO----
----Alumno:Maximo Mule

El trabajo consiste en una interfaz web en Python servida por Apache HTTP Server,y una base de datos MongoDB para almacenar informacion 
sobre juegos de mesa.

Requisitos:
-Docker y Docker Compose instalados.
-MongoDB,y MongoDBCompass(Si es que quisieramos visualizar los datos)
-Algun editor de texto

Para poder probar la aplicacion primero debemos construir los contenedores
Ejecutando este comando:
docker-compose build

Luego debemos levantar los contenedores 
docker-compose run

En esta direccion vamos a poder ver la interfaz y realizar las operaciones que queramos.
http://localhost:5000/

Para detener los contenedores se puede realizar de esta forma
docker-compose down

AVISO:
Si utilizas MongoDBCompass podes conectarte a la bases de datos con los siguientes datos
Host: localhost
Puerto: 27017
Usuario: maxi
Contraseña: 123