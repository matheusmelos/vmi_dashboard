import os
import dash
import json
import plotly.express as px
from dash import html, dcc, dash_table
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from datetime import datetime, date
import base64
import io
from app import app
from components.price import Pricer
import pandas as pd
from dash_bootstrap_templates import ThemeChangerAIO

# ========= Diretório de Upload ========= #
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# ========= Layout ========= #
layout = dbc.Card([
    html.Img(src="/assets/logo_mec.svg"),
    html.Hr(),

    # Seção + NOVO ------------------------
    dbc.Row([
        dbc.Col([
            # Botão + Ordem de Compra para abrir o modal
            dbc.Button(color="warning", id="open-novo-receita", children=[" + Ordem de Compra"]),
        ], width=40),
    ]),

    # Modal para Upload de Arquivo
    html.Div([
        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle("Upload da Ordem de Compra")),
            dbc.ModalBody([
                dbc.Row([
                    dbc.Col([
                        html.H5("Faça o upload da planilha de Ordem de Compra"),
                        dcc.Upload(
                            id='upload-data',
                            children=html.Button('Escolher Arquivo'),
                            multiple=False,  # Permitir apenas um arquivo por vez
                            accept='.csv, .xls, .xlsx'  # Tipos de arquivos permitidos
                        ),
                    ], width=12),
                ]),

                # Exibir resultado após upload
                html.Div(id='output-data-upload', style={'margin-top': '20px'}),
            ]),
            dbc.ModalFooter([
                dbc.Button("Fechar", id="close-modal", color="secondary"),
            ])
        ],
        id="modal-novo-receita",
        size="lg",
        is_open=False,  # Modal começa fechado
        centered=True,
        backdrop=True)
    ]),

    # Seção NAV ------------------------
    html.Hr(),
    dbc.Nav(
        [
            dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
            dbc.NavLink("Extratos", href="/extratos", active="exact"),
        ], vertical=True, pills=True, id='nav_buttons', style={"margin-bottom": "50px"}),
    ThemeChangerAIO(aio_id="theme", radio_props={"value": dbc.themes.CYBORG})

], id='sidebar_completa')


# ========= Callback para Abrir o Modal ========= #
@app.callback(
    Output('modal-novo-receita', 'is_open'),
    [Input('open-novo-receita', 'n_clicks')],
    [State('modal-novo-receita', 'is_open')]
)
def toggle_modal(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open


# ========= Callback para Processar o Arquivo Carregado ========= #
@app.callback(
    Output('output-data-upload', 'children'),
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename')]
)
def upload_file(contents, filename):
    if contents is None:
        return html.Div("Nenhum arquivo carregado")

    # Decodificando o arquivo
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    
    # Caminho para salvar o arquivo
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    with open(file_path, 'wb') as f:
        f.write(decoded)

    try:
        # Processar o arquivo carregado (CSV ou Excel)
        if filename.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif filename.endswith('.xls') or filename.endswith('.xlsx'):
            process = Pricer(file_path)
            data = process.data
            
            
        else:
            return html.Div("Formato de arquivo não suportado")
        
        # Mensagem de sucesso
        return html.Div([
            html.H5(f'Arquivo "{filename}" salvo com sucesso.'),
            html.H6("Planilha salva e pronta para processamento."),
        ])

    except Exception as e:
        return html.Div(f'Erro ao processar o arquivo: {str(e)}')

