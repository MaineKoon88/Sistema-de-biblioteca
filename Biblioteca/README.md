# Sistema de Gestión de Biblioteca

Trabajo Práctico Integrador - Análisis de Sistemas

## Estructura del Proyecto

Biblioteca/
├── presentacion/
│   └── app.py
├── objetos/
│   ├── libro.py
│   ├── socio.py
│   └── prestamo.py
├── datos/
│   ├── db_config.py
│   ├── libroData.py
│   ├── socioData.py
│   └── prestamoData.py
├── database/
│   └── biblioteca.sql
└── README.md

## Ejecución

1. Importar `database/biblioteca.sql` en phpMyAdmin.
2. Desde la terminal en la raíz `Biblioteca`:
   ```bash
   python presentacion/app.py
   ```
