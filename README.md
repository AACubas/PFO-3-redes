# PFO 3: Rediseño como Sistema Distribuido (Cliente-Servidor)

**Práctica Formativa Obligatoria N° 3**

---

## ⚙️ Descripción General

El sistema está compuesto por:

- **Clientes (Web / CLI)**  
  Los usuarios interactúan con el sistema mediante una interfaz web (HTML + JS).  
  Envían textos para analizar y visualizan los resultados.

- **Balanceador (Nginx / HAProxy)**  
  Simulado en el diseño arquitectónico: representa la distribución de carga entre múltiples servidores Flask.

- **Servidor / Socket (Flask)**  
  Recibe las solicitudes de análisis, las almacena en la base de datos y las envía a la cola de tareas.

- **Cola de Tareas (Queue)**  
  Administra las tareas pendientes y garantiza un procesamiento seguro y ordenado entre los hilos de los workers.

- **Workers (threading)**  
  Ejecutan los análisis de texto de forma paralela.  
  Cada worker toma una tarea de la cola, la procesa (conteo, análisis semántico básico) y actualiza el resultado en la base de datos.

- **Almacenamiento**  
  La base SQLite registra usuarios, textos y resultados.  
  

---

## 🧩 Estructura del Proyecto

```
project/
│
├── app.py             # Punto de inicio del servidor Flask
├── auth.py            # Módulo de registro e inicio de sesión
├── db.py              # Inicialización y conexión a SQLite
├── routes.py          # Definición de rutas y API REST
├── tasks.py           # Cola de tareas y workers concurrentes
│
├── templates/         # Interfaz web (frontend)
│   ├── login.html
│   ├── register.html
│   └── analyze.html
│
├── static/            # Archivos estáticos
│   └── style.css
│
└── app.db             # Base de datos local (autogenerada)
```

---

## 🔄 Flujo de Funcionamiento

1. El usuario **se registra o inicia sesión**.  
2. Envía un **texto** para analizar.  
3. El servidor guarda la tarea en la base y la coloca en la **cola (`Queue`)**.  
4. Los **workers** (hilos) toman tareas de la cola y las procesan:  
   - Cuentan palabras.  
   - Calculan la longitud del texto.  
   - Detectan un sentimiento básico (“positivo” si contiene “feliz”).  
5. El resultado se guarda en la base y se muestra automáticamente en la interfaz web.

---

**Componentes representados:**
- Clientes (Web / CLI)  
- Balanceador (Nginx / HAProxy)  
- Servidor / Socket (Flask)  
- Cola de tareas (Queue)  
- Workers (3 hilos concurrentes)  
- Almacenamiento distribuido (SQLite + JSON/S3 simulado)

---

## 🚀 Instalación y Ejecución

### 1. Clonar el repositorio

### 2. Crear entorno virtual (opcional)
```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instalar dependencias
```bash
pip install flask
```

### 4. Ejecutar el servidor
```bash
python app.py
```

### 5. Acceder desde el navegador
```
http://127.0.0.1:5000
```

---

## 🧰 Tecnologías Utilizadas

- **Python 3**
- **Flask** (servidor web)
- **SQLite3** (base de datos local)
- **Threading + Queue** (procesamiento concurrente)
- **HTML + CSS + JavaScript** (interfaz de usuario)

---
