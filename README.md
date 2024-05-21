# Documentación del Backend

Este documento describe el backend desarrollado con Flask para gestionar experiencias AR y encuestas de satisfacción de usuarios.

## Estructura del Proyecto

El proyecto está estructurado de la siguiente manera:

```
/backend
│
├── app.py             # Archivo principal de la aplicación Flask
├── static/            # Carpeta estática para almacenar modelos y otros recursos
│   └── models/        # Carpeta donde se almacenan los modelos AR
│
├── templates/         # Plantillas HTML para las diferentes vistas
│   ├── base.html      # Plantilla base para las páginas HTML
│   ├── arjs.html      # Plantilla para visualizar una experiencia AR
│   ├── encuesta.html  # Plantilla para la encuesta de satisfacción
│   ├── experiencias.html  # Plantilla para listar las experiencias
│   ├── index.html     # Página de inicio
│   ├── login.html     # Formulario de inicio de sesión
│   ├── maps.html      # Plantilla para la vista de mapas
│   ├── register.html  # Formulario de registro
│   └── upload_experience.html  # Formulario para subir una nueva experiencia AR
│
└── util/              # Módulo con utilidades
    └── supabase_client.py  # Cliente para interactuar con Supabase
```

## Descripción de las Rutas

### `GET /`

- **Descripción**: Página de inicio.
- **Método**: `GET`
- **Plantilla asociada**: `index.html`
- **Función**: Muestra la página de inicio y verifica si el usuario está autenticado.

### `GET /login`

- **Descripción**: Página de inicio de sesión.
- **Método**: `GET`
- **Plantilla asociada**: `login.html`
- **Función**: Muestra el formulario de inicio de sesión.

- **Método**: `POST`
- **Función**: Autentica al usuario con Supabase utilizando `supabase_client.auth.sign_in_with_password`.

### `GET /register`

- **Descripción**: Página de registro de usuario.
- **Método**: `GET`
- **Plantilla asociada**: `register.html`
- **Función**: Muestra el formulario de registro de usuario.

- **Método**: `POST`
- **Función**: Registra a un nuevo usuario en Supabase utilizando `supabase_client.auth.sign_up`.

### `GET /logout`

- **Descripción**: Cierra la sesión del usuario.
- **Método**: `GET`
- **Función**: Cierra la sesión del usuario con `supabase_client.auth.sign_out`.

### `GET /arjs/<experience_id>`

- **Descripción**: Vista de una experiencia AR específica.
- **Método**: `GET`
- **Plantilla asociada**: `arjs.html`
- **Función**: Muestra una experiencia AR basada en el ID proporcionado.

### `GET /maps`

- **Descripción**: Vista de mapas (placeholder).
- **Método**: `GET`
- **Plantilla asociada**: `maps.html`
- **Función**: Muestra una vista de mapas (placeholder).

### `GET /upload_experience`

- **Descripción**: Sube una nueva experiencia AR.
- **Método**: `GET`
- **Plantilla asociada**: `upload_experience.html`
- **Función**: Muestra el formulario para subir una nueva experiencia AR.

- **Método**: `POST`
- **Función**: Sube una nueva experiencia AR y la guarda en Supabase.

### `GET /experiencias`

- **Descripción**: Lista todas las experiencias AR disponibles.
- **Método**: `GET`
- **Plantilla asociada**: `experiencias.html`
- **Función**: Lista todas las experiencias AR almacenadas en Supabase.

### `GET /encuesta`

- **Descripción**: Realiza una encuesta de satisfacción.
- **Método**: `GET`
- **Plantilla asociada**: `encuesta.html`
- **Función**: Muestra el formulario para la encuesta de satisfacción.

- **Método**: `POST`
- **Función**: Almacena la encuesta de satisfacción en Supabase.

## Uso de la Base de Datos

El backend utiliza Supabase como base de datos y autenticación. Se utilizan las siguientes tablas:

- **`experiencias`**: Almacena las experiencias AR.
- **`encuestas_satisfaccion`**: Almacena las encuestas de satisfacción de los usuarios.

## Configuración y Ejecución

Para ejecutar la aplicación:

1. Asegúrate de tener Python y Flask instalados.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Ejecuta la aplicación con `python app.py`.

```python
# app.py

from flask import Flask, render_template, redirect, request
from util import supabase_client
import os
from datetime import datetime

app = Flask(__name__)

# Rutas y lógica de la aplicación
...

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
```



# Documentación del Frontend

Este documento describe el frontend asociado al backend desarrollado con Flask para gestionar experiencias AR y encuestas de satisfacción de usuarios.

## Estructura del Proyecto

El proyecto frontend está estructurado de la siguiente manera:

```
/frontend
│
├── index.html               # Página de inicio
├── login.html               # Formulario de inicio de sesión
├── register.html            # Formulario de registro
├── experiencias.html        # Lista de experiencias AR
├── arjs.html                # Vista de una experiencia AR
├── encuesta.html            # Formulario de encuesta de satisfacción
├── maps.html                # Vista de mapas
│
└── static/                  # Archivos estáticos
    ├── css/                 # Archivos CSS
    │   └── styles.css       # Estilos personalizados
    └── js/                  # Archivos JavaScript
```

## Descripción de las Páginas

### Página de Inicio (`index.html`)

- **Descripción**: Página principal del sitio web.
- **Uso**: Muestra un menú de navegación y enlaces a otras partes del sitio.
- **Componentes Principales**: Navbar fija con enlaces a las secciones de la web.

### Formulario de Inicio de Sesión (`login.html`)

- **Descripción**: Formulario para que los usuarios inicien sesión.
- **Uso**: Permite a los usuarios autenticarse para acceder a funcionalidades protegidas.

### Formulario de Registro (`register.html`)

- **Descripción**: Formulario para que nuevos usuarios se registren.
- **Uso**: Permite a los usuarios registrarse para acceder a la plataforma.

### Lista de Experiencias AR (`experiencias.html`)

- **Descripción**: Lista todas las experiencias AR disponibles.
- **Uso**: Muestra una lista de experiencias que los usuarios pueden visualizar.

### Vista de una Experiencia AR (`arjs.html`)

- **Descripción**: Vista de una experiencia AR específica.
- **Uso**: Muestra una experiencia AR utilizando A-Frame y AR.js.

### Formulario de Encuesta de Satisfacción (`encuesta.html`)

- **Descripción**: Formulario para que los usuarios envíen una encuesta de satisfacción.
- **Uso**: Permite a los usuarios enviar comentarios y puntuaciones sobre la plataforma.

### Vista de Mapas (`maps.html`)

- **Descripción**: Vista de mapas interactivos.
- **Uso**: Permite a los usuarios explorar mapas interactivos.

## Estilos y Recursos

### Estilos CSS

Se utilizan estilos personalizados para mejorar la apariencia y la usabilidad del sitio web.

### Librerías y Frameworks

- **Bootstrap**: Se utiliza Bootstrap 5 para estilizar los componentes y el diseño general del sitio.
- **A-Frame y AR.js**: Se utilizan para crear y mostrar experiencias AR en la web.

## Configuración y Ejecución

1. Asegúrate de tener una conexión a internet para cargar los archivos CDN necesarios.
2. Abre cualquier archivo HTML en un navegador web moderno para visualizar el sitio web.

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ title }}</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

  <!-- include A-Frame obviously -->
  <script src="https://aframe.io/releases/0.6.0/aframe.min.js"></script>
  <!-- include ar.js for A-Frame -->
  <script src="https://jeromeetienne.github.io/AR.js/aframe/build/aframe-ar.js"></script>

  <style>
    /* Estilos adicionales */
    .navbar {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      z-index: 1000;
      /* Asegura que el navbar esté por encima de otros elementos */
    }

    .navbar-brand {
      font-size: 1.5rem;
      color: #fff;
    }

    .navbar-nav .nav-link {
      color: #fff;
      margin: 0 15px;
      transition: all 0.3s ease;
    }

    .navbar-nav .nav-link:hover {
      color: #ffc107;
    }

    .navbar-toggler {
      border-color: #fff;
    }

    .navbar-toggler-icon {
      background-color: #fff;
    }

    /* Agrega espacio en la parte superior del cuerpo para evitar que el contenido se solape con el navbar fijo */
    body {
      padding-top: 70px;
      /* Ajusta según la altura del navbar */
    }
  </style>
</head>

<body>
  <nav class="navbar navbar-expand-lg bg-dark">
    <div class="container">
      <a class="navbar-brand" href="#">Bazar El Very</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <a class="nav-link" aria-current="page" href="{{url_for('index')}}">Inicio</a>
          </li>
          {% if not current_user %}
          <li class="nav-item">
            <a class="nav-link" href="{{url_for('login')}}">Iniciar Sesión</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{{url_for('register')}}">Registrar</a>
          </li>
          {% else %}
          <li class="nav-item">
            <a class="nav-link" href="{{url_for('logout')}}">Cerrar Sesión</a>
          </li>
          {% endif %}
          <li class="nav-item">
            <a class="nav-link" href="{{url_for('experiencias')}}">Realidad Aumentada</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{{url_for('maps')}}">Mapa Interactivo</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <div class="container mt-4">
    {% block content %}
    {% endblock %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"
    integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r"
    crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"
    integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy"
    crossorigin="anonymous"></script>
</body>

</html>
```
