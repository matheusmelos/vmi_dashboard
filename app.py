import dash
import dash_bootstrap_components as dbc

# Adicionando o CDN mais recente do Font Awesome
estilos = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css",  # Font Awesome atualizado
    "https://fonts.googleapis.com/icon?family=Material+Icons",  # Material Icons
    dbc.themes.DARKLY,  # Tema do Bootstrap
]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"

app = dash.Dash(__name__, external_stylesheets=estilos + [dbc_css])

# Configurações adicionais do Dash
app.config['suppress_callback_exceptions'] = True
app.scripts.config.serve_locally = True

server = app.server
