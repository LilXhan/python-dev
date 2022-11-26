# Game Project

Para correr el juego debes seguir las siguientes instrucciones:

```sh
cd game
python3 main.py 
```

# Docker

Para crear nuestro contenedor de docker usaremos:

```sh
docker-compose build
```

Y para lanzarlo usaremos:

```sh
docker-compose up -d
```

Para comprobar el estado de funcionamiento del contenedor usaremos el siguiente comando:

```sh
docker-compose ps
```

Y como ingresamos a el, como empezamos a desarrollar en ¿el?
Con el siguiente comando:

```sh
docker-compose exec my-app bash
```

en este caso my-app es el nombre del servicio que usamos en docker-compose.yml

Para salir de un contenedor usaremos el comando:

```sh
exit
```

Para bajarnos o parar un contenedor usaremos:

```sh
docker-compose down
```

Para obtener una experiencia al 100 desarrollando o pogramando, podemos activar el live reloading entre
tu sistema de archivos y tu contenedo, sera añadiendo al archivo docker-compose.yml la siguiente a la misma linea de build:

```sh
    .
    .
    .
    volumes:
      - .:/app
```