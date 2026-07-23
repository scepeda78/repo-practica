# Dev Blog — Repositorio de Práctica 🎮

Proyecto Django + PostgreSQL + Docker para aprender a contribuir código.
Úsalo junto con la guía **Dev Quest** para completar las misiones.

## 🚀 Inicio rápido

```bash
# 1. Clona el repositorio
git clone https://github.com/TU_USUARIO/repo-practica.git
cd repo-practica

# 2. Copia el archivo de configuración
cp .env.example .env

# 3. Levanta todo (primera vez tarda ~5 minutos)
docker compose up
```

Luego abre **http://localhost:8000** en el navegador.

**Panel de administración:** http://localhost:8000/admin
- Usuario: `admin`
- Contraseña: `admin123`

---

## 🌳 Estructura de ramas

| Rama | Descripción |
|------|-------------|
| `main` | Código estable. Solo se actualiza con Pull Requests aprobados. |
| `develop` | Rama de integración — los cambios se unen aquí antes de ir a main. |
| `feature/tu-nombre` | Tu rama personal de práctica. Créala tú misma. |

### Flujo de trabajo

```
main ←── develop ←── feature/tu-nombre
                  ←── feature/otra-persona
```

---

## 📁 Estructura del proyecto

```
repo-practica/
├── Dockerfile              # Cómo construir el contenedor de Django
├── docker-compose.yml      # Orquesta web + base de datos
├── requirements.txt        # Dependencias Python
├── .env.example            # Variables de entorno de ejemplo
├── manage.py               # Herramienta de comandos de Django
│
├── config/                 # Configuración del proyecto
│   ├── settings.py         # Configuración principal (BD, apps, etc.)
│   ├── urls.py             # URLs raíz del proyecto
│   └── wsgi.py             # Punto de entrada WSGI
│
└── blog/                   # La app del blog
    ├── models.py           # 📊 Estructura de la base de datos
    ├── views.py            # 🧠 Lógica de cada página
    ├── urls.py             # 🗺️ Mapa de URLs de la app
    ├── admin.py            # ⚙️ Panel de administración
    ├── fixtures/
    │   └── initial_data.json  # Datos de ejemplo
    └── templates/blog/
        ├── base.html       # 🏗️ Esqueleto HTML de todas las páginas
        ├── index.html      # 🏠 Página de inicio
        └── detail.html     # 📄 Página de detalle de un post
```

---

## 🛠️ Tecnologías

- **Python 3.12** + **Django 5.1** — el framework web
- **PostgreSQL 15** — la base de datos
- **Docker** + **Docker Compose** — contenedores

---

## 🎯 Ejercicios para practicar

### 🟢 Fácil (Misión 6)
- Cambiar el título en `templates/blog/index.html`
- Cambiar los colores CSS en `base.html`
- Crear posts desde el panel admin

### 🟡 Medio
- Agregar un campo `category` al modelo `Post`
- Crear una vista para filtrar posts por autor
- Agregar paginación a la lista

### 🔴 Desafío
- Sistema de comentarios
- Búsqueda de posts por texto
- Subida de imágenes a posts

---

## 🔧 Comandos útiles

```bash
# Encender la app
docker compose up

# Encender en background (sin bloquear la terminal)
docker compose up -d

# Ver logs
docker compose logs -f web

# Apagar todo
docker compose down

# Abrir una terminal dentro del contenedor Django
docker compose exec web bash

# Crear migraciones después de cambiar models.py
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

---

## 🌿 Crear tu rama de práctica

```bash
# Crear y cambiar a tu rama
git checkout -b feature/tu-nombre

# Ver en qué rama estás
git branch

# Subir tu rama a GitHub (primera vez)
git push -u origin feature/tu-nombre
```
