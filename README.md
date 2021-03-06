# Prueba técnica Habi.co
En este repositorio se puede encontrar el proyecto que responde a la solicitud de la prueba tecnica enviada por habi.co.
Adicional, en este documento encontrará las descripciones de ambos puntos de la solución, su detalle tecnico, requerimientos, una guia de instalación y finalmente las dudas que se pueden resolver durante el desarrollo.

Para el desarrollo de esta prueba se le entrega al desarrollador una base de datos Dummy sobre la cual se deben hacer las consultas (Al igual que los testings, pues no existe una base de datos de prueba, ni tampoco existen permisos para generar una)

## Primer punto (Endpoint de consulta)

### Descripción
Los usuarios pueden consultar varios inmuebles con cierto tipo de estado, aplicando filtros a esta consulta como lo son:
- Ciudad
- Estado
- Año de construcción

Los resultados detallan cada inmueble con la siguiente información:
- Dirección
- Ciudad
- Estado
- Precio de venta
- Descripción

Adicional, la consulta debe traer siempre el último estado de cada inmueble.

### Solución
El codigo habilitado en el repositorio responde en su totalidad al primer requerimiento.

Se genera el siguiente endpoint sobre el cual el usuario puede hacer las consultas y filtros correspondientes:
```
GET /api/properties
```

Los filtros deben ser enviados como query parameters y no en el body del request. Se detalla a continuación se detallan los filtros y como se deben aplicar sobre el endpoint:
- **city:** Nombre de la ciudad que el usuario desea filtrar
- **state:** Nombre del estado o departamento que el usuario se desea filtrar
- **min_year:** Año minimo de construcción que el usuario desea filtrar
- **max_year:** Año maximo de construcción que el usuario desea filtrar

Ejemplos (Puede aplicar uno, varios, todos o ningun filtro)
```
GET /api/properties
GET /api/properties?city=Bogota
GET /api/properties?state=Antioquia
GET /api/properties?min_year=2010
GET /api/properties?max_year=2010
GET /api/properties?city=Bogota&max_year=2010
GET /api/properties?city=Bogota&state=Bogota&min_year=2000&max_year=2010
```

Si un usuario aplica un filtro invalido a los ya mencionados, el back ignora este query param y responde correctamente. Un ejemplo:
```
GET /api/properties?city_name=Bogota
GET /api/properties?invalid_filter=True
```

Dentro del codigo se puede encontrar un aplicativo (Properties), que es la encargada de manejar cualquier transacción referente a una propiedad.
En esta app encuentra los archivos basicos generados por Django (admin, apps, models, tests, urls, views) y algunos archivos adicionales agregados para el correcto funcionamiento del endpoint (entities, serializers).

Se explica la responsabilidad de cada archivo en la solución propuesta (Cabe resaltar que todos los endpoints funcionarian asi):
- **entities:** Clase encargada de realizar las consultas|queries hacia la Base de datos. Se dejan en un archivo separado, pues varias consultas se pueden reutilizar en diferentes endpoints, ya sea para dar una respuesta fija o usar la data para realizar otro tipo de operaciones
- **models:** Representación del modelo en el ORM de Django (Para esta prueba no se usa)
- **serializers:** Clase encargada de convertir los QuerySets en Dictionaries siguiendo unos modelos. Adicional puede hacer validaciones antes de crear o actualizar una columna en la base de datos (También siguiendo unos modelos o campos personalizados)
- **tests:** Pruebas unitarias
- **urls:** Define que vista llamar dependiendo del match que hace con la URL.
- **views:** Encargado de resolver cada acción del request (GET, PUT, POST, DELETE, etc), se encarga de entender un request y de orquestar las demas clases para poder armar un response

### Adicionales
Al momento de realizar la prueba el campo de state no existia en la base de datos, asi que todo lo referente a este campo en la solución ha sido documentado.

## Segundo punto (Give Like on property)

### Descripcion
El usuario es capaz de darle Like a una propiedad, y esta debe registrarse en la base de datos.

### Solución
Para la solución de este segundo requerimiento se adjunta el código (Pseudocodigo documentado en su mayoria).
En este se puede encontrar el siguiente endpoint (donde id es el identificador de la propiedad):
```
PUT /api/properties/likes/:id
```

Este endpoint maneja diferentes excepciones, como las siguientes:
- No se provee un auth token o este caduco (403 Forbidden)
- La propiedad no existe (404 Not Found)
- Falta de conexión a BD (500 Server Error)
- Error transaccional hacia la BD (500 Server Error)

Al igual que el primer punto, cuenta con las mismas capas y mismas responsabilidades. Se mantiene el orden y se manejan los estandares para las respuestas por parte del servidor.

### Adicionales
Para la parte de las respuestas se maneja un serializador NoNullSerializer (Serializador que utiliza el metodo ***to_representation*** para remover todos los valores que son NULOS y no enviar estos como respuesta). Personalmente no me gusta enviar valores nulos (pero si vacios) en los request y responses y siento que es muy mala practica hacer esto.

Dentro del repositorio encontrará unos documentos detallando el modelo propuesto para la solución del segundo punto, asi como una pequeña propuesta en la arquitectura para manejar tanto la parte transaccional (Que propiedades son favoritas de que usuario, teniendo fecha de registro de la acción), asi como el historico de cada acción de seleccionar/deseleccionar la propiedad como favorito.

## Detalle Técnico
Esta prueba se encuentra desarrollada en el siguiente lenguaje:
- Python 3.7.6

Las librerias que se utilizan son las siguientes:
- django v3.2
- djangorestframework v3.12.4
- mysqlclient v1.4.1
- pymysql v1.0.2
- django-environ v0.4.5
- django-mysql v3.12

## Requerimientos
Para poder hacer el despliegue de este repositorio, el ambiente local debe tener como minimo las siguientes dependencias:
- Python v3.7.6 [Windows](https://www.python.org/downloads/) [Linux](https://docs.python-guide.org/starting/install3/linux/)
- virtualenv v20.0.18 [Guia de instalación](https://pypi.org/project/virtualenv/)
- Git [Windows](https://git-scm.com/downloads) [Linux](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Instalación
Con los requerimientos ya instalados lo primero es proceder a clonar el repositorio. Para esto ejecutar el siguiente comando
```
git clone https://github.com/shirux/habiAPI
```

Una vez se clone el repositorio, nos ubicamos dentro del nuevo directorio para proseguir con los siguientes pasos de la instalación.
Se debe ahora instalar un ambiente virtual en el cual se instalaran las dependencias del proyecto.
Para esto ejecutamos el siguiente comando (Se sugiere mantener el nombre del ambiente virtual por temas de versionamiento)
```
virtualenv venv
```

Para activar el ambiente virtual, ejecutamos el siguiente comando:
```
venv/Scripts/Activate
```

Si está en windows(GitBash) puede usar el siguiente comando:
```
source venv/Scripts/Activate
```

Una vez activado el ambiente virtual, se procede a instalar las dependencias, para esto ejecute el siguiente comando (Este ignora cualquier advertencia de SSL):
```
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

Procedemos a hacer la configuración del ambiente. 
En el repositorio se deja un archivo de variables de entorno con ejemplos (.env-example). Copielo, peguelo y cambiele el nombre a .env
Dentro del nuevo archivo deje las configuraciones necesarias para el correcto funcionamiento del aplicativo. (No omita ninguna variable, asi existan algunas por defecto).

Con los pasos anteriores ya ejecutados se puede dar la inicialización del servidor. Para esto ejecute el siguiente comando:
```
python manage.py runserver
```

Este útlimo dara ejecución al servidor y se puede acceder por la siguiente url (Por defecto, si tiene otra configuración de inicialización, omita esta información):
```
http://127.0.0.1:8000
```

## Adicionales
Adjunto en el repositorio se puede encontrar un documento en el cual se hacen varias propuestas para la optimización en la base de datos, así como otras propuestas a nivel de arquitectura para conseguir este objetivo.

En el repositorio encontará un archivo JSON de postman, en el cual se detallan los dos endpoints implementados con sus respectivos ejemplos y escenarios. En ellos puede encontrar que parametros se usan, ya sea URL parameters o query parameters. También se puede visualizar si utilizan o no un BODY, que respuesta deben generar en cada escenario y si deben o no llevar autenticación.

Finalmente, en el repositorio encontrará un archivo documentando la estructura que se debe implementar en el front para poder realizar los llamados (Un pequeño Backup si el postman no logra importar los ejemplos), con el objetivo de tener una clara comunicación con el posible equipo de trabajo

## Dudas

**En el requerimiento se habla de un filtro (state) pero en la base de datos no está habilitado. ¿Qué debo hacer en este caso?**
El servidor entiende el filtro y es capaz de procesarlo. Sin embargo cuando se arma la consulta y se procesa la información a un dict, este pedazo de codigo se encuentra documentado para no generar errores en la transacción

**En el requerimiento se habla de poder manejar las excepciones. ¿Qué debo hacer para esto?**
Con el diseño propuesto para el endpoint habilitado se manejan los escenarios de error, los cuales son:
- Perdida de conexión a la base de datos
- Mala estructuración en la query
- El modelo no corresponde con la respuesta al usuario que define el negocio

En cualquier escenario el servidor responde con un 500, pues no entiende el request o pierde conexión y le envia al FrontEnd con este status.
Las validaciones, ya sea en la estructura y ejecución de la query o con los datos del resultado se manejan en las clases entities y serializers respectivamente.
Estas excepciones todas son levantadas (raise) y llegan hasta la vista, la cual se encarga de generar una respuesta generica en caso de error.
Finalmente, el serializer entiende que algunos campos en la respuesta pueden ser nulos o pueden retornar un string vacio. Todo esto se maneja en los campos definidos en el mismo serializer.

**¿Puedo modificar la base de datos para el primer requerimiento?**
En el documento entregado dice que **NO**

**Para el segundo requerimiento que es conceptual, ¿Puedo usar el ORM para poder realizar el desarrollo?**
Haciendo el analisis en la base de datos, se puede ver que se usan librerias y migraciones generadas por Django para el manejo de usuarios y la autenticación de estos.
Teniendo en cuenta esto, se asume que utilizan las librerias de rest-framework-jwt y se plantea el desarrollo con esto en mente.

