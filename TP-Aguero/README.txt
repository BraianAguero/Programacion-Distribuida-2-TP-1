
## Primero construimos
docker build -t api . 

## Instanciamos un contenedor y ejecutamos
docker run --name api-cont -p 80:80 api

##Acedemos a la pagina web de fastapi
http://127.0.0.1/
