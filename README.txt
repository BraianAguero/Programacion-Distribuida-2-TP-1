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

-----RESPUESTA-----
1.Para la conexión entre contenedores consiste de la siguiente configuración. 
Por un lado se generó un contenedor el cual contenía la API RES y un Client generado por código proto (gRPC). Por otro lado un Server generado por código proto (gRPC).
Ambos contenedores se levantan en una misma red debido a que se usa  docker compose. Esto genera que tengan visibilidad entre ellos y por ende comunicarse entre sí. 
Se configuró a los contenedores de la siguiente forma: El contenedor Cliente apunta al contenedor Servidor y enviará en el canal 50051 los mensajes. El contenedor Servido expondría su puerto 50051 y escucharía lo que se envíe en este.
	
2.Ambas tecnologías se basan en HTML, la diferencia es que API REST no enfrenta los mismos problemas/limitaciones que gRPC. 
Del lado de REST sigue un modelo de comunicación request-response y es totalmente compatible con todos los navegadores, pero no soporta recibir grandes cantidades de request por su modelo de comunicación.  
Por otro lado, gRPC sigue un modelo de comunicación client-response la cual le permite  manejar una comunicación bidireccional,recibir múltiples solicitudes de varios clientes y manejar esas solicitudes simultáneamente mediante la transmisión constante de información.

COMPARACIÓN:
REST es totalmente compatible con todos los navegadores. RPC está limitado en lo que respecta a la compatibilidad con navegadores y requiere gRPC-web y una capa de proxy para realizar conversiones entre HTTP 1.1 y HTTP 2.
gRPC usa Protocol Buffer, lo cual es una ventaja ya que permite normalizar o traducir los datos. Esta solución es más ligera ya que permite un formato muy comprimido y reduce el tamaño de los mensajes. Además, Protobuf es binario por lo que permite convertir los mensajes automáticamente de un formato Protobuf al lenguaje de programación del cliente y del servidor.
 En REST los mensajes son en formatos JSON o XML. Si bien JSON es más legible que Protobuf, no es más ligero o rápido en la transmisión de datos a comparación de gRPC, ya que se debe convertir serializarse los mensajes y convertirlos de programación adicionando un paso más.
REST no proporciona funciones para generación de código integrado por lo que se debe usar herramientas cómo POSTMAN producir código para realizar las solicitudes a la API. 
gRPC tiene funciones para generar código integrado compatible con varios lenguajes de programación.
gRPC ofrece una gran cantidad de ventajas para sistemas internos/privados, sistemas multilenguaje y transmisión en tiempo real.
API REST tiene un soporte universal con navegadores y es más conocido por lo que es conveniente usarlo para desarrollo de servicios web y la integración de aplicaciones y microservicio
