📅 Proyecto Reserva de Citas 2025-1
¡Bienvenido al proyecto de citas! Este README te guiará a través de la configuración y ejecución de las partes frontend (Angular) y backend (Django).

🌐 Configuración del Frontend (Angular)Sigue estos pasos para poner en marcha el frontend de tu aplicación:📁 1. Entrar a la carpeta del frontendAbre tu terminal y navega hasta el directorio del frontend del proyecto:Bashcd citas-frontend
📥 2. Instalar las dependencias del proyectoUna vez dentro de la carpeta citas-frontend, instala todas las dependencias necesarias con el siguiente comando:Bashnpm install
🧪 3. Ejecutar el servidor de desarrolloDespués de instalar las dependencias, puedes iniciar el servidor de desarrollo de Angular:Bashng serve
🧪 Nota de Desarrollo: Si necesitas que los cambios del frontend se actualicen en el servicio mientras desarrollas (por ejemplo, en un entorno con Docker), utiliza el comando npm run watch dentro de la carpeta /client si tu estructura lo requiere. Ten en cuenta que es posible que debas recargar la página en el navegador para ver los cambios.⚙️ Configuración del Backend (Django)Aquí te explicamos cómo configurar y ejecutar el backend de Django:🚨 ¡Importante!No olvides que debes tener corriendo tus servicios de PostgreSQL y Redis (ya sea con Docker o de forma local) antes de iniciar el backend.📁 1. Entrar a la carpeta del backendNavega a la carpeta del backend en tu terminal:Bashcd backend
🐍 2. Crear y activar un entorno virtual (recomendado)Es una buena práctica usar un entorno virtual para las dependencias de Python.Para Windows (CMD):Bashpy -m venv venv
.\venv\Scripts\activate
Para Linux/macOS:Bashpython -m venv venv
source venv/bin/activate
📥 3. Instalar las dependencias y navegar a la aplicaciónCon el entorno virtual activado, instala las dependencias y luego navega a la carpeta principal de la aplicación (server_django/):Bashpip install -r requirements.txt
cd server_django/
🚀 4. Ejecutar el servidor de desarrolloFinalmente, inicia el servidor de desarrollo de Django:Bashpython manage.py runserver
🔑 Credenciales de Acceso (para pruebas)Para iniciar sesión en la aplicación, puedes usar las siguientes credenciales:RolUsuarioContraseñaAdministradoradminadmin123Pacientemgomezadmin123¡Esperamos que disfrutes desarrollando con este proyecto! Si tienes alguna pregunta o encuentras algún problema, no dudes en consultar la documentación específica de Angular y Django.
