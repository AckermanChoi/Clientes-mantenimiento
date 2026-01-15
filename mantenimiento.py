import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Configuración de rutas absolutas (Para evitar el error de directorio anterior)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Montar archivos estáticos (CSS, Imágenes)
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Configurar plantillas HTML
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/", response_class=HTMLResponse)
async def read_mantenimiento(request: Request):
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mantenimiento - Gestión de Clientes</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="/static/css/style.css">
    </head>
    <body class="bg-gradient-blue-green">
        
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark shadow">
            <div class="container">
                <a class="navbar-brand" href="#">
                    <img src="/static/img/logo_jc.svg" alt="Logo">
                </a>
            </div>
        </nav>

        <main class="d-flex align-items-center justify-content-center">
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-md-8 col-lg-6">
                        <div class="card shadow-lg border-0" style="border-radius: 15px; overflow: hidden;">
                            <div class="card-header py-3 text-center" style="background-color: var(--second-color); border-bottom: 3px solid var(--first-color);">
                                <h2 class="m-0 text-white">Aviso de Mantenimiento</h2>
                            </div>
                            <div class="card-body p-5 text-center">
                                <h3 style="color: var(--second-color);" class="mb-4">Gestión de Clientes</h3>
                                <p class="lead text-muted">
                                    Lo sentimos, el servicio principal se encuentra temporalmente deshabilitado por tareas de mantenimiento.
                                </p>
                                
                                <p class="mt-4 mb-0 small text-secondary">
                                    Disculpa las molestias. Volveremos a estar operativos en breve.
                                </p>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        </main>

        <footer class="bg-dark text-white text-center py-3 mt-auto">
            <small>&copy; 2026 Gestión de Clientes - Modo Mantenimiento</small>
        </footer>
    </body>
    </html>
    """