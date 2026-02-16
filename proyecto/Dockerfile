#Uso la imagen ubuntu
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    apache2 \
    apache2-dev \
    libapache2-mod-wsgi-py3 \
    && apt-get clean


    RUN a2enmod proxy
    RUN a2enmod proxy_http
    RUN a2enmod headers
    
#Establezco el directorio de trabajo en el contenedor
WORKDIR /app

#Copio los archivos de la aplicacion al contenedor
COPY . /app/


RUN pip3 install --no-cache-dir -r requirements.txt

#Copio el archivo de configuración de Apache
COPY apache.conf /etc/apache2/sites-available/000-default.conf

#Copio el script de inicio
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

#Exponer el puerto 80 (el puerto de Apache)
EXPOSE 80


CMD ["/app/run.sh"]
