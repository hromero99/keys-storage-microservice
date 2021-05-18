# keys-storage-microservice
Simple microservice written in flask for RSA keys storage

## Endpoints

### /generate/ 
POST Necesita un pasarse el argumento _device\_id_ que sera el identificador unico del dipositivo

`` 
{"device_id": "demo"}
``

### /query/device_id/
GET Obtenemos la clave pública del dispositivo
_device\_id_ será el identificador del dispositivo

### /query/private/device_id/
GET Obtenemos la clave privada del dispositivo
_device\_id_ será el identificador del dispositivo