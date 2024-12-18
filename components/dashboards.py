from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash_bootstrap_templates import template_from_url, ThemeChangerAIO
from globals import *
from app import app

peças_dobradas = len(df_ordens[df_ordens['DOBRAS'] > 0])
pecas_rebitadas = len(df_ordens[df_ordens['REBITES'] > 0])
# Layout do Dashboard
layout = dbc.Col([
    # Cards com as métricas
    dbc.Row([
        dbc.Col([
            # Exibindo o total de ordens de compra
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Total de peças"),
                    html.H5(f"{df_ordens['QUANTIDADE'].sum():,.0f} und", id="total-valores"),
                ], style={"padding-left": "20px", "padding-top": "10px"}),
                dbc.Card(
                    html.Div(className="fa fa-shopping-cart", style={"color": "white", "textAlign": "center", "fontSize": 30, "margin": "auto"}), 
                    color="warning",
                    style={"maxWidth": 75, "height": 100, "margin-left": "-10px"},
                )
            ])
        ], width=3),

        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Tempo total"),
                    html.H5(f"{df_ordens[['HORAS REBITE', 'HORAS DOBRADEIRA', 'HORAS LASER']].sum().sum():,.0f} horas", id="tempo-total"),
                ], style={"padding-left": "20px", "padding-top": "10px"}),
                dbc.Card(
                    html.Div(className="fa fa-clock", style={"color": "white", "textAlign": "center", "fontSize": 30, "margin": "auto"}), 
                    color="warning",
                    style={"maxWidth": 75, "height": 100, "margin-left": "-10px"},
                )
            ])
        ], width=3),
        
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Valor total"),
                    html.H5(f"R$ {df_ordens[['VALOR REBITE','VALOR DOBRA', 'VALOR LASER', 'VALOR MATERIAL', 'VALOR ROSCA', 'VALOR SOLDA']].sum().sum():,.0f}", id="valor-total"),
                ], style={"padding-left": "20px", "padding-top": "10px"}),
                dbc.Card(
                    html.Div(className="fa-solid fa-dollar-sign", style={"color": "white", "textAlign": "center", "fontSize": 30, "margin": "auto"}), 
                    color="warning",
                    style={"maxWidth": 75, "height": 100, "margin-left": "-10px"},
                )
            ])
        ], width=3),
        
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Ticket médio"),
                    html.H5(f"R$ {df_ordens['DOBRAS'].sum():,.0f}", id="ticket-medio"),
                ], style={"padding-left": "20px", "padding-top": "10px"}),
                dbc.Card(
                    html.Div(className="fa-solid fa-dollar-sign", style={"color": "white", "textAlign": "center", "fontSize": 30, "margin": "auto"}), 
                    color="warning",
                    style={"maxWidth": 75, "height": 100, "margin-left": "-10px"},
                )
            ])
        ], width=3),
        
    ], style={"margin": "10px"}),

    # Gráficos
    dbc.Row([
        dbc.Col(dbc.Card(dcc.Graph(id="grafico-tempo-corte"), style={"padding": "10px"}), width=7),
        dbc.Col(dbc.Card(dcc.Graph(id="grafico-valores"), style={"padding": "10px"}), width=5),
    ], style={"margin": "10px"}),

    dbc.Row([
        dbc.Col(dbc.Card(dcc.Graph(id="grafico-material"), style={"padding": "10px"}), width=5),
        dbc.Col(dbc.Card(dcc.Graph(id="grafico-detalhado"), style={"padding": "10px"}), width=7),
    ], style={"margin": "10px"}),
    
    dbc.Row([
        dbc.Col([
            # Exibindo o total de ordens de compra
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Dobras Totais"),
                    html.H5(f"{df_ordens['DOBRAS'].sum():,.0f}", id="total-dobras"),
                ], style={"padding-left": "20px", "padding-top": "10px"}),
                dbc.Card(
                    html.Div(className="fa fa-shopping-cart", style={"color": "white", "textAlign": "center", "fontSize": 30, "margin": "auto"}), 
                    color="primary",
                    style={"maxWidth": 75, "height": 100, "margin-left": "-10px"},
                )
            ])
        ], width=3),

        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Peças Dobradas"),  # Título do card
                    html.H5(f"{peças_dobradas:,} peças", id="pecas-dobradas"),  # Exibindo a quantidade de peças
                ], style={"padding-left": "20px", "padding-top": "10px"}),

                dbc.Card(
                    html.Div(className="fa fa-check", style={"color": "white", "textAlign": "center", "fontSize": 30, "margin": "auto"}), 
                    color="primary",  # Usando cor verde para indicar sucesso
                    style={"maxWidth": 75, "height": 100, "margin-left": "-10px"},
                )
            ])
        ], width=3),
        
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Rebites Totais"),
                    html.H5(f"{df_ordens['REBITES'].sum():,.0f}", id="total-rebites"),
                ], style={"padding-left": "20px", "padding-top": "10px"}),
                dbc.Card(
                    html.Div(className="fa fa-shopping-cart", style={"color": "white", "textAlign": "center", "fontSize": 30, "margin": "auto"}), 
                    color="success",
                    style={"maxWidth": 75, "height": 100, "margin-left": "-10px"},
                )
            ])
        ], width=3),
        
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Peças Rebitadas"),
                    html.H5(f"{pecas_rebitadas:,} peças", id="pecas-rebitadas"),  # Exibindo a quantidade de peças
                ], style={"padding-left": "20px", "padding-top": "10px"}),
                dbc.Card(
                    html.Div(className="fa fa-check", style={"color": "white", "textAlign": "center", "fontSize": 30, "margin": "auto"}), 
                    color="success",
                    style={"maxWidth": 75, "height": 100, "margin-left": "-10px"},
                )
            ])
        ], width=3),
        
    ], style={"margin": "10px"}),

    dbc.Row([
        dbc.Col(dbc.Card(dcc.Graph(id="grafico-chapas-material"), style={"padding": "10px"}), width=7),
        dbc.Col(dbc.Card(dcc.Graph(id="grafico-material-valor"), style={"padding": "10px"}), width=5),
    ], style={"margin": "10px"}),

    

   
])

# Callbacks para os gráficos
@app.callback(
    Output("grafico-tempo-corte", "figure"),
    Output("grafico-valores", "figure"),
    Output("grafico-material", "figure"),
    Output("grafico-detalhado", "figure"),
    Output("grafico-chapas-material", "figure"),
    Output("grafico-material-valor", "figure"),
    [Input("store-ordens", "data"),
    Input(ThemeChangerAIO.ids.radio("theme"), "value")]
    
)


def atualizar_graficos(data, theme):
    df = pd.DataFrame(data)
    cores_barras = ['#f8790a', '#ffad33', '#ff8c1a', '#ffcc66', '#ffdb85']
    # Função para configurar o layout dos gráficos (fundo transparente)
    def custom_layout(fig):
        fig.update_layout(
            template=template_from_url(theme),
            plot_bgcolor='rgba(0,0,0,0)',  # Fundo do gráfico transparente
            paper_bgcolor='rgba(0,0,0,0)'  # Fundo do papel transparente
        )
        return fig

    df_filtered = df[df['TEMPO DE CORTE'] > 0]

    # Ordenando o DataFrame em ordem crescente pelo 'TEMPO DE CORTE'
    df_sorted = df_filtered.sort_values('TEMPO DE CORTE', ascending=True)
    # Gráfico de Tempo de Corte por Peça
    fig1 = px.bar(df_sorted, x="TEMPO DE CORTE", y="CÓD. PEÇA", orientation='h',
                  title="Tempo de Corte por Peça",
                  labels={"CÓD. PEÇA": "Código da Peça", "TEMPO DE CORTE": "Tempo de Corte (horas)"}, color_discrete_sequence=cores_barras)
    
    fig1 = custom_layout(fig1)
    fig1.update_layout(
    bargap=0.3,
    height=800,
    width = 650,
    margin={"l": 30, "r": 0, "t": 30, "b": 90}
    )

    # Adicionando o valor na frente da barra
    fig1.update_traces(
        text=df_sorted['TEMPO DE CORTE'],  # Exibe o valor de TEMPO DE CORTE na barra
        textposition='outside'  )
    
    fig1.update_layout(
    yaxis=dict(
        tickmode='array',  # Usando modo array para controlar o espaçamento
        tickvals=df['CÓD. PEÇA'],  # Definindo os valores do eixo Y
        ticktext=df['CÓD. PEÇA'],  # Exibindo os valores dos itens no eixo Y
        tickangle=0,  # Ajustando o ângulo dos rótulos, se necessário
        ticklen=10,  # Controlando o tamanho dos ticks (espessura do traço)
        ticks='outside',  # Colocando os ticks para fora do gráfico
    )
)
    
    
    
    
    
    
    
    df_chapa_valor = df[df['VALOR MATERIAL'] > 0]

    # Gráfico de Valores de Materiais (Gráfico de Rosca)
    fig2 = px.pie(df_chapa_valor, names="MATERIAL", values="VALOR MATERIAL",
                title="Valor material", color_discrete_sequence=cores_barras,
                hole=0.5)  # Criando o buraco no meio para transformá-lo em uma rosca

    # Customizando o layout
    fig2 = custom_layout(fig2)

    # Ajustando o layout para centralizar o gráfico e a legenda
    fig2.update_layout(
        legend_title="Material",
        legend_orientation="h",  # Faz a legenda ficar horizontal
        legend_y=-0.1,  # Coloca a legenda um pouco abaixo do gráfico
        legend_x=-0.5,  # Centraliza a legenda
        margin={"l": 30, "r": 30, "t": 50, "b": 100},  # Ajuste de margens para dar mais espaço ao redor
         # Altura do gráfico (aumentando o tamanho geral)
        autosize=True,  # Ajusta automaticamente o tamanho
        title_y=0.95  # Ajusta a posição do título para mais acima
    )

    # Gráfico de Distribuição de Materiais
    fig3 = px.pie(df, names="MATERIAL", values="VALOR MATERIAL",
                  title="Distribuição de Materiais", hole=0.3)
    fig3 = custom_layout(fig3)

    # Gráfico detalhado de valores e horas
    
    # Agrupando e filtrando os dados
    df_horas = df.groupby('MATERIAL')['HORAS LASER'].sum().reset_index()
    df_horas = df_horas[df_horas['HORAS LASER'] > 0]  # Filtrando apenas os valores maiores que 0
    df_horas_sorted = df_horas.sort_values('HORAS LASER', ascending=True)  # Ordenando por 'HORAS LASER'

    # Criando o gráfico de barras
    fig4 = px.bar(df_horas_sorted, x="HORAS LASER", y="MATERIAL", orientation='h', color_discrete_sequence=cores_barras,
                title="Horas laser por material")

    # Aplicando layout customizado
    fig4 = custom_layout(fig4)

    # Ajustando as margens e o espaçamento entre as barras
    fig4.update_layout(
        bargap=0.3,
        margin={"l": 30, "r": 0, "t": 60, "b": 90}
    )

    # Adicionando os valores das barras
    fig4.update_traces(
        text=df_horas_sorted['HORAS LASER'],  # Utilizando df_horas_sorted ao invés de df_chapas_sorted
        textposition='outside'  # Colocando os valores fora das barras
    )



    df_chapas = df.groupby('MATERIAL')['QTD CHAPAS'].sum().reset_index()

    # Filtrando para pegar apenas valores maiores que 0
    df_chapas = df_chapas[df_chapas['QTD CHAPAS'] > 0]

    # Ordenando em ordem crescente
    df_chapas_sorted = df_chapas.sort_values('QTD CHAPAS', ascending=True)

    # Criando o gráfico de barras com a ordem crescente
    fig5 = px.bar(df_chapas_sorted, y='MATERIAL', x='QTD CHAPAS', orientation='h', color_discrete_sequence=cores_barras,
                title='Quantidade de chapas')

    # Personalizando o layout do gráfico
    fig5 = custom_layout(fig5)
    fig5.update_layout(
        bargap=0.3,
        margin={"l": 30, "r": 0, "t": 60, "b": 90}
    )

    # Adicionando o valor na frente da barra
    fig5.update_traces(
        text=df_chapas_sorted['QTD CHAPAS'],  
        textposition='outside'
    )
    
    
 

# Agrupando os dados e somando os valores das colunas
    df_totals = df[['VALOR LASER', 'VALOR DOBRA', 'VALOR MATERIAL', 'VALOR SOLDA']].sum().reset_index()
    df_totals.columns = ['Categoria', 'Valor Total']

    # Plotando o gráfico de rosca
    fig6 = px.pie(df_totals, 
                names='Categoria', 
                values='Valor Total',
                title='Valor Total por Categoria',
                labels={'Categoria': 'Categoria', 'Valor Total': 'Valor (R$)'},
                hole=0.4,  # Criando o buraco no meio para ser uma rosca
                color='Categoria',  # Colorir as fatias por categoria
                color_discrete_sequence=cores_barras)  # Definindo cores para cada categoria

    # Customizando o layout
    fig6 = custom_layout(fig6)





    # Gráfico de Horas por Atividade
    df_atividades = df[['HORAS LASER', 'HORAS REBITE', 'HORAS DOBRADEIRA']].sum().reset_index()
    df_atividades.columns = ['Atividade', 'Horas']
    fig7 = px.bar(df_atividades, x='Atividade', y='Horas', color_discrete_sequence=cores_barras,
                  title="Horas por atividade", labels={"Atividade": "Atividade", "Horas": "Horas"})
    fig7 = custom_layout(fig7)
    fig7.update_layout(
    bargap=0.5,
    )

    return fig5, fig2, fig7,  fig4, fig1, fig6
