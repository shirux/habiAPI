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

Si un usuario aplica un filtro invalido a los ya mencionados, el back ignora este query param y responde correctamente. Un ejemplo
```
GET /api/properties?city_name=Bogota
GET /api/properties?invalid_filter=True
```


## Segundo punto (Set Favorite on property)
Adicional, se deja documentado la posible solución del segundo punto de esta prueba tecnica y se adjunta la documentación explicando la solución implementada.
Finalmente, un último documento detalla las mejoras que se pueden implementar en la base de datos para optimizar las consultas y las posibles mejoras a futuro en el aplicativo.

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
- Python v3.7.6
- virtualenv v20.0.18 [Guia de instalacion](https://pypi.org/project/virtualenv/)

## Instalación

pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <package_name>

## Dudas
