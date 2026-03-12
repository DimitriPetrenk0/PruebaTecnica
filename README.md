# README

API desarrollada utilizando Django REST Framework y PostgreSQL

- Permite ejecutarse localmente, utilizando Docker o directamente desde una URL del servicio desplegado en Render.
 
## Decisiones Técnicas
- Utilización de Django REST Framework para la API.
- PostgreSQL como motor de base de datos.
- Autenticación de usuarios utiliza JWT.
- Variables de entorno no se suben al repositorio.
- En el despliegue de Render, las variables de entorno estan configuradas en el Dashboard.
- Al utilizar versión gratuita de Render, pasados 15 minutos de inactividad el Web Service entra en modo Sleep, lo que puede generar un retraso de cerca de 1 minuto en la primera petición, mientras vuelve a estar activo.

## Enlace importante

- URL deploy en Render: https://pruebatecnica-dxsn.onrender.com


## Modos de ejecución
### Localmente

1. Clonar repositorio.
  
2. Crear entorno virtual e instalar dependencias.
  *     python -m venv .venv 
        .venv\Scripts\activate
        pip install -r requirements.txt
3. Creación de archivo ".env" en la raíz del proyecto, utilizando el contenido del archivo ".env.example".

4. Ejecutar migraciones y levantar servidor.
  *     python manage.py migrate
        python manage.py runserver
5. Base URL : http://localhost:8000 

### Docker

1. Clonar repositorio.
  
2. Creación de archivo ".env" en la raíz del proyecto, utilizando el contenido del archivo ".env.example".

3. Buildear en la raíz del proyecto.
  *     docker compose up --build
        
4. Base URL : http://localhost:8000 

### Render

- Dirigir peticiones a la URL: https://pruebatecnica-dxsn.onrender.com
*   Ejemplo: 
        https://pruebatecnica-dxsn.onrender.com/health/




## Dudas y consultas

matias.herrerac@sansano.usm.cl