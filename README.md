# High-availability-ethereum-like-node-proxy

## Problemática
Generalmente las DApps dependen de un único nodo de blockchain para realizar todas las transacciones, por lo que sería interesante tener un sistema que puedas configurar un listado de nodos, que tengan un healthcheck para ir viendo qué nodos son más rápidos, que nodos están funcionando, etc.. Y que el sistema sea capaz de recibir una llamada y redirigirla al mejor nodo disponible. Hay que tener en cuenta que cada nodo tendrá una autenticación diferente.

## Solución
Crear una aplicación en Python para monitorear diferentes nodos ethereum json-rpc y equilibrar el tráfico entre ellos.

## Despliegue del Entorno Virtual de Python
Primero de todo para poder desplegar la API se necesitan descargar FastAPI en un entorno virtual de Python:

```
python3 -m venv env
source env//bin/activate
pip install fastapi
pip install uvicorn
```

### Ejecutar la API
Una vez creado el entorno virtual, se puede desplegar la API de forma:

```
uvicorn main:app --reload
```

## Manual de implementación
* Definir el diccionario 'nodes' del archivo [/nodes/node_list.py]
* Crear el archivo vacio '/nodes/results.json' si no existe
