## Ubicarse en el path donde clonara el repositorio.
 cd PathDestino\API

##Clonar el repositorio git.Escribir en el CMD:
git clone https://github.com/BraianAguero/Programacion-Distribuida-2-TP-1.git

## Levantar el servicio. Escribir en el CMD:
docker compose up

##Acedemos a la pagina web de fastapi para verificar que se levanto correctamente.
http://127.0.0.1/

##Las timezone que podra consultar deben tener dos parametros, Continente  y zone.
http://127.0.0.1/Localizacion/{Continente}/{zone}

##Continente (America,Europe,etc..) y Zone por una ubicacion(Provincia/Capital/Localidad) 
http://127.0.0.1/Localizacion/America/Buenos_Aires

##Continente por Eastern Standard Time (EST) y zona por Greenwich Mean Time (GMT+N o GMT-N).
##El rango de numeros en el tiempo medio de Greenwich es desde -14 hasta +12
http://127.0.0.1/Localizacion/Etc/GMT-11

##Ejecucion en postman:
#Importamos la coleccion desde File->Import...->Chose File->API_Aguero_Test.postman_collection.json

1.Clic derecho sobre la Coleccion API
2.Run Collection
3.Run API

##Bajar el servicio:
docker compose down

##Eliminar imagenes del servicio
docker rmi api-client api-server