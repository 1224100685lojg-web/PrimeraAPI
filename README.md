# 🐍 API REST con Flask y PostgreSQL

## 📚 Descripción

Este proyecto consiste en el desarrollo de una API REST utilizando **Python (Flask)** y **PostgreSQL**, como parte de la Unidad 3 de la materia *Aplicaciones Web Orientadas a Servicios*.

La API permite gestionar estudiantes mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar), además de demostrar la conexión con base de datos y pruebas mediante Postman.

---

## 🛠️ Tecnologías utilizadas

* Python 3.x
* Flask
* Flask-SQLAlchemy
* PostgreSQL
* Postman
* JWT (autenticación)
* Swagger (documentación)

---

## ⚙️ Configuración del proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO
```

---

### 2. Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno:

```bash
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
```

---

### 3. Instalar dependencias

```bash
pip install flask flask-sqlalchemy psycopg2-binary flask-marshmallow
pip install marshmallow-sqlalchemy flask-jwt-extended python-dotenv
pip install flasgger flask-cors
```

---

### 4. Configurar variables de entorno

Crear archivo `.env`:

```env
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=clave-secreta

DATABASE_URL=postgresql://flask_user:password123@localhost:5432/mi_api_db
```

---

### 5. Ejecutar el proyecto

```bash
python run.py
```

Servidor disponible en:

```
http://localhost:5000/
```

---

## 🧪 Pruebas de la API (Evidencias)

Las pruebas se realizaron utilizando Postman.

---

### 🔹 1. Endpoint raíz

**GET /**

* Verifica que la API está funcionando

📸 Evidencia:
![Root](root.png)

---

### 🔹 2. CREATE - Crear estudiante

**POST /api/estudiantes/**

Body:

```json
{
  "matricula": "ITIC001",
  "nombre": "Owen",
  "apellido": "Jaramillo",
  "email": "owen@test.com",
  "carrera": "ITIC",
  "semestre": 5
}
```

📸 Evidencia:
![Create](create.png)

**Resultado:** Estudiante creado correctamente
**Código:** 201 Created

---

### 🔹 3. READ ALL - Obtener estudiantes

**GET /api/estudiantes/**

📸 Evidencia:
![ReadAll](readall.png)

**Resultado:** Lista de estudiantes obtenida
**Código:** 200 OK

---

### 🔹 4. READ ONE - Obtener por ID

**GET /api/estudiantes/{id}**

📸 Evidencia:
![ReadOne](readone.png)

**Resultado:** Estudiante encontrado
**Código:** 200 OK

---

### 🔹 5. UPDATE - Actualizar estudiante

**PUT /api/estudiantes/{id}**

Body:

```json
{
  "semestre": 6
}
```

📸 Evidencia:
![Update](update.png)

**Resultado:** Datos actualizados correctamente
**Código:** 200 OK

---

### 🔹 6. DELETE - Eliminar estudiante

**DELETE /api/estudiantes/{id}**

📸 Evidencia:
![Delete](delete.png)

**Resultado:** Eliminación lógica realizada
**Código:** 200 OK

---

## 🗄️ Base de datos

Se utilizó PostgreSQL para el almacenamiento de datos.

📸 Evidencia:

* Tabla estudiantes
* Registros almacenados

---

## 🔐 Autenticación

Se implementó autenticación mediante JWT para proteger endpoints.

---

## 📖 Documentación

La API cuenta con documentación Swagger accesible en:

```
http://localhost:5000/docs/
```

---

## ✅ Conclusiones

* Se desarrolló una API REST funcional con Flask
* Se implementaron operaciones CRUD completas
* Se logró la conexión con PostgreSQL
* Se validaron endpoints mediante Postman
* Se documentó el funcionamiento de la API

---

## 👨‍💻 Autor

Luis Owen Jaramillo Guerrero
Ingeniería en Tecnologías de la Información
UTNG

---
