# SDK Python


### Requerimientos

**MacOS:**

Instalar [Docker](https://docs.docker.com/docker-for-mac/install/), [Docker-compose](https://docs.docker.com/compose/install/#install-compose)

**Windows:**

Instalar [Docker](https://docs.docker.com/docker-for-windows/install/), [Docker-compose](https://docs.docker.com/compose/install/#install-compose)

**Linux:**

Instalar [Docker](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/) y [Docker-compose](https://docs.docker.com/compose/install/#install-compose).

### Como usar

Esta imagin de docker sirve para correr y comprobar la compatibilidad del sdk con distintas versiones de python

**NOTA:** La primera vez que se ejecuta ./build.sh demorará en instalar todo, esperar al menos unos 5 minutos.

### Construir el contenedor desde cero

Para construir la imagen se debe ejecutar el archivo build.sh y se puede pasar opcionalmente
la version de python, sino se pasa la version como parametro usara la version 3.7.4-stretch por defecto

```

./build.sh 3.5.6
```

### Iniciar el contenedor construido anteriormente

```
./run.sh
```


