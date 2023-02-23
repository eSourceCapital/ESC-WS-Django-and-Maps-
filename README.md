# ESC-WS-Django-and-Maps

Repositorio de ejemplo para el workshop de Django y Google Maps.

## Requisitos

- Tener instalado Python 
- Tener instalado Django

### Instalación de Python

- [Windows (https://www.python.org/downloads/windows/)](https://www.python.org/downloads/windows/)
- [Mac (https://www.python.org/downloads/mac-osx/)](https://www.python.org/downloads/mac-osx/)
- [Linux (https://www.python.org/downloads/source/)](https://www.python.org/downloads/source/)

Comprobar la instalación ejecutando el comando `python --version` en la consola.

### Instalación de Django

Para instalar Django, ejecutar el comando `pip install django` en la consola.

## Creación de las API Keys

### Google Maps

Entrara a la consola de GCP [Google](https://console.cloud.google.com/).

Para crear una API Key, se debe ir a la sección de [APIs y Servicios](https://console.cloud.google.com/apis/dashboard) y seleccionar la opción de [Credenciales](https://console.cloud.google.com/apis/credentials).

Tambien activar la API de [Maps JavaScript API](https://console.cloud.google.com/apis/library/maps-backend.googleapis.com).

Es nesesario contar con un proyecto creado en GCP, si no se tiene, se debe crear uno nuevo. Y tener una cuenta de facturación asociada a la cuenta de GCP.

### Cambiar la API Key

¿Descargaste el código ya terminado? Recuerda que para poder utilizar las API de Google Maps, es necesario crear una API Key, ya que este repositorio no contiene la API Key.

Recordar cambiar la API Key en: 
`<script src="https://maps.googleapis.com/maps/api/js?key=[CAMBIAR API KEY]&callback=initMap"></script>`

Por la generada en la consola de [Google](https://console.cloud.google.com/).

[Leer las mejores practicas para el uso de las API Keys](https://cloud.google.com/docs/authentication/api-keys)


## Creación del proyecto
Para crear un proyecto en Django, ejecutar el comando `django-admin startproject [nombre del proyecto]` en la consola.

El comando utilizado fue: `django-admin startproject maps-example`

Estructura del proyecto:

```
maps-example
├── manage.py
└── maps-example
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Levantar el servidor de desarrollo

Para levantar el servidor de desarrollo, ejecutar el comando `python manage.py runserver` en la consola.

Abrir el navegador y navegar a `http://localhost:8000/`. Puerta por defecto de Django. 

## Apps en Django

Las apps en Django son como los módulos de un proyecto. Cada app tiene su propia funcionalidad y se puede reutilizar en otros proyectos.

Para crear una app, ejecutar el comando `python manage.py startapp [nombre de la app]` en la consola.

El comando utilizado fue: `python manage.py startapp maps`

Estructura de la app (Contenida dentro del proyecto):

```
maps
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

## Views

Las views son las encargadas de procesar la información que se envía al servidor y de generar la respuesta que se envía al cliente.

Para crear una view, se debe crear una función en el archivo `views.py` de la app.

```python
from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world! ")
```

Si abrimos el navegador y navegamos a `http://localhost:8000`, no se mostrará nada. Esto es porque no se ha creado una ruta para la view.

## URLs

Las URLs son las encargadas de manejar las peticiones que se hacen al servidor.

Para crear una URL, se debe crear una ruta en el archivo `urls.py` del proyecto.

```python
# urls.py
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),

    # Add this line:
    path('maps/', include('maps.urls')),
]

```

Ahora deberíamos poder navegar a `http://localhost:8000/maps/` y ver el mensaje `Hello world! `. En caso de que no se muestre el mensaje, saltar a los settings para indicarle a Django que la app `maps` ha sido creada.

## Settings

Los settings son los encargados de configurar el proyecto.

Para indicarle a Django que la app `maps` ha sido creada, en la sección `INSTALLED_APPS` del archivo `settings.py` del proyecto, se debe agregar la app.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add this line:
    'maps'
]
```

## Templates

Los templates son los encargados de mostrar la información al usuario.

Para crear un template, se debe crear un archivo `.html` en la carpeta `templates` de la app.

```html
<!-- /templates/home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maps</title>
</head>
<body>
    <h1>Hello World</h1>
</body>
</html>
```

Para poder utilizar el template, modificamos la view para que renderice el template.

```python
# views.py
from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

```

## Templates dinámicos

Los templates dinámicos son los encargados de mostrar la información al usuario de forma dinámica.

Modificamos el template para que muestre la información que se envía desde la view.

```html
<!-- /templates/home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maps</title>
</head>
<body>
    <h1>Workshop Django + Google Maps - eSource</h1>
    <p>
      Api Key: {{apiKey}}
      My first name is {{ first_name }}. My last name is {{ last_name }}.
    </p>
</body>
</html>
```

Hay que notar que en el template se utilizan las variables `{{apiKey}}` y `{{ first_name }}` y `{{ last_name }}`. Estas variables se envían desde la view.

Modificamos la view para que envíe la información al template.

```python
# views.py
from django.http import HttpResponse
from django.template import loader

def index(request):
    first_name = 'Tu nombre'
    last_name = 'Tu apellido'
    apiKey = 'sustituir por la api key'
    template = loader.get_template('home.html')
    context = {
        'first_name': first_name,
        'last_name': last_name,
        'apiKey': apiKey
    }
    return HttpResponse(template.render(context, request))

```
Verificar que se muestre la información en el navegador. En caso de que no se muestre, verificar que la ruta sea correcta. Así mismo, verificar que el template se encuentre en la carpeta `templates` de la app. Y los nombres de las variables sean correctos.

## Agregando un mapa

Para agregar un mapa, se debe agregar el siguiente código en el template.

```html
<!-- /templates/home.html -->
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <title>Mi primer mapa</title>
    <style>
      #map {
        width: 600px;
        height: 400px;
      }
    </style>
  </head>
  <body>
    
    <h1>Workshop Django + Google Maps - eSource</h1>
    <p>
      Api Key: {{apiKey}}
      My first name is {{ first_name }}. My last name is {{ last_name }}.
    </p>
    <div id="map"></div>
    <script>


        // coordenadas ciudad de mexico
        var location = { lat: 19.432608, lng: -99.133209 };

      function initMap() {
        var mapa = new google.maps.Map(document.getElementById("map"), {
          center: location,
          zoom: 6,
          // estilos opcionales
        });
      }

      window.initMap = initMap;
    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key={{apiKey}}&callback=initMap"></script>
    
  </body>
</html>

```

Verificar que se muestre el mapa en el navegador. En caso de que no se muestre, verificar que la ruta sea correcta. Así mismo, verificar que el template se encuentre en la carpeta `templates` de la app. Y los nombres de las variables sean correctos.

## Agregando marcadores

Para agregar marcadores, se debe agregar el siguiente código en el template.

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <title>Mi primer mapa</title>
    <style>
      #map {
        width: 600px;
        height: 400px;
      }
    </style>
  </head>
  <body>
    
    <h1>Workshop Django + Google Maps - eSource</h1>
    <p>
      Api Key: {{apiKey}}
      My first name is {{ first_name }}. My last name is {{ last_name }}.
    </p>
    <div id="map"></div>
    <script>

      // The escapejs filter escapes text to be used in JavaScript strings.
      var list = "{{list | escapejs}}"

      list = JSON.parse(list)

      console.log(list)

      function initMap() {
        var mapa = new google.maps.Map(document.getElementById("map"), {
          center: list[0],
          zoom: 6,
         // estilos opcionales
        });

        // add markers from the list
        for (var i = 0; i < list.length; i++) {
          addMarker(list[i], mapa);
        }
      }

      function addMarker(location, mapa) {
        var marker = new google.maps.Marker({
          position: location,
          map: mapa,
        });

        var infoWindow = new google.maps.InfoWindow({
          content:
            "Esta es la sucursal con coords: " +
            location.lat +
            ", " +
            location.lng,
        });

        marker.addListener("click", function () {
          infoWindow.open(mapa, marker);
        });
      }

      window.initMap = initMap;
    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key={{apiKey}}&callback=initMap"></script>
    
  </body>
</html>

```
Finalmente, hemos agregado marcadores a nuestro mapa. Para poder agregar marcadores, se debe enviar una lista de coordenadas desde la view.

```python
# views.py
from django.http import HttpResponse
from django.template import loader
import json

def index(request):
    mexico_city = { 'lat': 19.432608, 'lng': -99.133209 }
    colombia = { 'lat': 4.570868, 'lng': -74.297333 }
    list = [mexico_city, colombia]
    list_json = json.dumps(list)
    first_name = 'Tu nombre'
    last_name = 'Tu apellido'
    apiKey = 'sustituir por la api key'
    template = loader.get_template('home.html')
    context = {
        'first_name': first_name,
        'last_name': last_name,
        'apiKey': apiKey,
        'list': list_json
    }
    return HttpResponse(template.render(context, request))

```

## Documentación

- [Django](https://docs.djangoproject.com/en/3.1/)
- [Google Maps](https://developers.google.com/maps/documentation/javascript/overview)
- [Google Maps API Key](https://developers.google.com/maps/documentation/javascript/get-api-key)
- [Python](https://docs.python.org/3/)

Sigue aprendiendo con nosotros.
Conocemas sobre eSource Capital y las soluciones con Google Cloud Platform. [https://esourcecapital.com/maps](https://esourcecapital.com/maps)

[eSource](https://esourcecapital.com/) - 2023

### Recomentaciones

El código de este repositorio es solo para fines demosntrativos. Se recomienda revisar la documentación oficial de Django y Google Maps para conocer más sobre el uso de estas herramientas, sus mejores prácticas y las ultimas actualizaciones.