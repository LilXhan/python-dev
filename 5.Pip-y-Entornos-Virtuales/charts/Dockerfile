# Creamos nuestro archivo dockerfile


# Con esta instruccion le decimos a python desde que version de python va a partir este ambiente
FROM python:3.8 

# Creamos una carpeta dentro del contenedor (el espacio de trabajo)
WORKDIR /app

# Copiamos los archivos de las dependencias en este caso requirements.txt
# COPY <archivo local> <contenedor>
COPY requirements.txt /app/requirements.txt

# Instalamos las dependecias con pip (--no-cache-dir -> no aplique el cache, --upgrade -> que actualize el pip)
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Por ultimo copiamos todo nuestro codigo
COPY . /app

# Para correr este contenedor, vamos a ayudarnos y soportarnos de otro archivo que se llama docker-compose.yml


# Para poder conectarnos a un contenedor debe estar encendido continuamente
# El comando que va a mantener en ejecucion constatante este contenedor
CMD bash -c "while true; do sleep 1; done"










