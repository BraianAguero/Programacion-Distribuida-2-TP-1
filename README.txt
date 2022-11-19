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

--------------------Devolucion---------------------------

HTML es un lenguaje de marcado

Así es, me confundí de palabra. Quise decir HTTP.

- ¿Por qué el modelo de comunicación no deja que reciba grandes cantidades de comunicaciones?

Es debido a que REST está principalmente basado en HTTP1 la cual tiene un modelo de comunicación request-response, limitando la gestión de las solicitudes llegan al servidor, está obligado a manejar cada una de ellas, una a la vez. Por el contrario, grpc sigue un modelo de comunicación que se basa en HTTP/2 . Por lo tanto, le permite la transmisión de mensajes y atender las múltiples solicitudes simultáneamente. Además de que grpc también admite comunicación unaria igual que REST.

Si bien REST puede adaptarse para que funcione con HTTP2, pero procesa los mensajes de a uno.

- client/response, estimo que es client/server que sigue el patrón request/reply.

Así es, cliente/servidor. Lo que quise decir es que la grpc maneja una arquitectura Clientes/servidor en el cual el cliente solicita un mensaje que es serializado por el RPC y respondido por el servidor.

- REST sobre HTTP no es client-server?

REST sobre HTTP es cliente-servidor. 

Un cliente (una pc o host) envía un  request  por un servicio o dato a un servidor a través del protocolo  HTTP.

El servidor acepta la request, lo procesa y envía una respuesta a traves del protocolo HTTP

- Los browsers también hablan HTTP 2, no entiendo para qué sirve el proxy, qué a qué convertirían y si el proxy es un proxy o un proxy-reverso.

Para que grpc sea compatible con navegadores es necesario una capa llamada gRPC-Web que actúa como una capa de traducción entre gRPC.  Todo esto es necesario porque el codigo javascript que se ejecuta en el navegador no proporciona un control total sobre HTTP2 .

- XML y JSON? Dónde está esa restricción? YML no se puede?

JSON y XML son los formatos más populares y usados debido a su flexibilidad y capacidad para enviar datos dinámicos sin seguir necesariamente una estructura estricta.

YML también puede ser utilizado. Cómo mencione anteriormente, REST no está definido en una estructura estricta, pero la desventaja de usar YML es que no siempre se incluye en las bibliotecas estándar como suele ser JSON. Por lo que se podría depender de una biblioteca adicional. Además, si el cliente es un navegador, el análisis será más lento, ya que se tendrá que usar una librería externa no nativa.
