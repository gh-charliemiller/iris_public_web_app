#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 05:52:41 2023

@author: charliemiller
"""
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output, State

# Iris bar figure
def drawFigure():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(id='graph1',
                    figure=px.scatter(
                        df, x="sepal_width", y="sepal_length", color="species",
                    marginal_x='histogram',marginal_y='histogram').update_layout(
                        template='plotly_white',
                        plot_bgcolor= 'rgba(218, 223, 225, 1)',
                        paper_bgcolor= 'rgba(232, 236, 241, 1)',
                    ),
                    config={
                        'displayModeBar': False
                    }
                ) 
            ])
        ),  
    ])

# Text field
def drawText():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.P("Text"),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])


# Text field
def selectX(params):
    return html.Div([
        dbc.Card( [
            dbc.CardHeader("Select X Variable"),
            dbc.CardBody([
                html.Div([
                    dcc.Dropdown(params, params[0],
                                 id='xvar',
                                  style={'color': 'blue',
                          'fontSize': '12px'}
                            ),
                
        
                ], style={'textAlign': 'center'}) 
            ])  ]
        ),
    ])

def selectY(params):
    return html.Div([
        dbc.Card( [
            dbc.CardHeader("Select Y Variable"),
            dbc.CardBody([
                html.Div([
                    dcc.Dropdown(params, params[2],
                                 id='yvar',
                                  style={'color': 'blue',
                          'fontSize': '12px'}
                            ),
                
        
                ], style={'textAlign': 'center'}) 
            ])  ]
        ),
    ])

# Data
df = px.data.iris()

params=df.columns[:4]

# Build App
app = Dash(__name__,external_stylesheets=[dbc.themes.SLATE])
server=app.server

app.layout = html.Div([
    html.H3(children='Explore the Iris Data Set'),
    dbc.Card(
        dbc.CardBody([
 
            dbc.Row([
                dbc.Col([
                    selectX(params)
                ], width=5),
                dbc.Col([
                    selectY(params)
                ], width=5),
            ], align='center'), 
#            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawFigure() 
                ], width=10),
            ], align='center'),      
        ]), color = 'dark'
    )
])

@app.callback(
    Output(component_id='graph1', component_property='figure'),
    Input(component_id='yvar', component_property='value'),
    Input(component_id='xvar', component_property='value')   
    )
def update_graph1(xvar,yvar):
    fig=px.scatter(
            df, x=xvar, y=yvar, color="species",
            marginal_x='histogram',marginal_y='histogram').update_layout(
                template='plotly_white',
                plot_bgcolor= 'rgba(218, 223, 225, 1)',
                paper_bgcolor= 'rgba(232, 236, 241, 1)',
                    )
    return fig        

# Run app and display result inline in the notebook
if __name__ == '__main__':
    app.run_server(debug=True)