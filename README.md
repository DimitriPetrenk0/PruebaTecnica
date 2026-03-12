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

### Render, con listados de ejemplos de body JSON

- Dirigir peticiones a la URL: https://pruebatecnica-dxsn.onrender.com
-   Estatus: https://pruebatecnica-dxsn.onrender.com/health/

- POST https://pruebatecnica-dxsn.onrender.com/signup/ 
  ```c
  {
    "username": "matiastest",
    "email": "matiastest@gmail.com",
    "password": "Contra1234",
    "confirm_password": "Contra1234"
  }
  ```

- POST https://pruebatecnica-dxsn.onrender.com/signin/ 
  ```c
  {
    "username": "matiastest",
    "password": "Contra1234"
  }
  La respuesta de esta petición entregará dos valores,"refresh"
   y "access", el valor de access corresponde al token de 
  acceso necesario para autenticar las siguientes peticiones. 
  Por ejemplo, dentro de Postman, el valor "access" debe ser ubicado 
  dentro de la variable de entorno "Bearer Token", esto 
  automatizará el token para todas las peticiones de la 
  colección que lo requieran.
  ```
- POST https://pruebatecnica-dxsn.onrender.com/tasks/ 
  ```c
  {
    "task_title": "Test backend",
    "task_description": "Terminar backend Wizz",
    "task_status": "pending",
    "task_due_date": "2026-03-16T18:00:00Z"
  }
  ```
- GET https://pruebatecnica-dxsn.onrender.com/tasks/ 
  ```c
  Obtiene las tareas creadas por el usuario autenticado
  ```
- GET https://pruebatecnica-dxsn.onrender.com/tasks/?task_status=pending
  ```c
    Entrega las tareas en estado pendiente
  ```
- GET https://pruebatecnica-dxsn.onrender.com/tasks/?ordering=-task_created_at
  ```c
    Ordena tareas por fecha de creación
  ```
- GET https://pruebatecnica-dxsn.onrender.com/tasks/?page=1&page_size=1
  ```c
    Entrega tareas con paginación dependiendo del page_size
  ```
- GET https://pruebatecnica-dxsn.onrender.com/tasks/1/
  ```c
  Entrega la tarea con id=1, el usuario debe ser dueño de la tarea 
  para poder verlas
  ```


- UPDATE https://pruebatecnica-dxsn.onrender.com/tasks/1/
  ```c
  Modifica campo de la tarea
  {
    "task_status": "completed"
  }
  ```

- DELETE https://pruebatecnica-dxsn.onrender.com/tasks/1/
  ```c
  Elimina una tarea
  ```
## Dudas y consultas

matias.herrerac@sansano.usm.cl