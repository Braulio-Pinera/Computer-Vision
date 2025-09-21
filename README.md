# Sistema de Login Facial con DeepFace

## Descripción
Este proyecto implementa un sistema de inicio de sesión seguro utilizando **reconocimiento facial**. Los usuarios pueden registrarse con su rostro y posteriormente iniciar sesión simplemente comparando su cara con la imagen registrada, eliminando la necesidad de contraseñas.

## Requisitos
- Python 3.10+
- pip

## Instalación y configuración

1. **Clonar el repositorio**  
```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
````

2. **Crear entorno virtual**

```bash
python -m venv venv
```

3. **Activar entorno virtual**

* Windows:

```bash
venv\Scripts\activate
```

* Linux / MacOS / WSL:

```bash
source venv/bin/activate
```

4. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

Si no existe `requirements.txt`, instalar manualmente:

```bash
pip install flask deepface opencv-python tf-keras
```

## Uso

### Ejecutar la aplicación

```bash
python app.py
```

### Registro de usuario

1. Abrir navegador y entrar a:

```
http://127.0.0.1:5000/register/<usuario>
```

2. Subir la imagen de tu rostro (si estás en WSL) o capturar desde la webcam (si estás en Windows nativo).
3. Se guardará la imagen como referencia para login.

### Inicio de sesión

1. Abrir navegador y entrar a:

```
http://127.0.0.1:5000/login/<usuario>
```

2. Subir la imagen de tu rostro (o capturar desde webcam).
3. El sistema verificará si coincide con la foto registrada y mostrará `Acceso concedido` o `Acceso denegado`.

## Estructura del proyecto

```
app.py              # Código principal del servidor Flask
users_faces/        # Carpeta donde se guardan las fotos de los usuarios
requirements.txt    # Dependencias del proyecto
README.md           # Documentación
```

## Notas

* En WSL no es posible usar webcam directamente; subir fotos manualmente.
* Se recomienda ejecutar en Windows nativo para capturas automáticas desde la cámara.

```

Si quieres, puedo generarte **una versión más completa con screenshots, formularios web para subir imágenes y endpoints listos**, para que el README quede listo para compartir en GitHub. ¿Quieres que haga eso?
```
