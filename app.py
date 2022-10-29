import dash     # (version 2.4.1)
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
from dash import dash_table as dt    # (version 5.0.0)
import plotly.express as px     # (version 5.8.0)
import pandas as pd     # (version 1.4.2)
from plotly.subplots import make_subplots
from datetime import date
import numpy_financial as npf   # (version 1.0.0)

app = dash.Dash(__name__)


colorsel='#0070B8'
estilo_input={ 'width': 170, 'display':'flex', 'flex-direction':'column','margin-left':'15px', 'margin-right':'15px',
 'color': '#061E44',  'fontSize': 18, 'padding':'5px'}

#DataFrame para la TABLA inicial
ANNO=[str(date.today().year+i) for i in list(range(0,21))]  #El año inicial se actualiza cada año
columna=['Concepto']+ANNO
data = [['Ingresos',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ['Costos Operativos',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ['EBITDA',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ['Depreciación (-)',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ['EBIT',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ['Intereses',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ['EBT',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ['Impuesto a las Ganancias',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ['Utilidad desp. Impuestos',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ['Depreciación (+)',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ['Inversión Inicial',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ['Préstamo',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ['Amortización Préstamo',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ['Flujo de Fondos',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        ]

df = pd.DataFrame(data,columns=columna)

app.layout = html.Div([  #Div-1 PRINCIPAL

  ##### ESTE ES EL TITULO DEL LAYOUT ###############################################################################################
  ##################################################################################################################################

  html.Div([   #Div-2 TITULO DEL LAYOUT

    html.H1('EVALUACIÓN DEL PROYECTO', style={"padding": "5px", 'textAlign': 'center', 'color': '#fff','font-family': 'Open Sans, sans-serif',
            'letter-spacing': '0.23rem', 'font-size': '2em', 'display': 'flex','justify-content': "center", 'margin-bottom': '2px'
             , 'margin-top': '2px' })
            ]),

  ################################################################################################################################# 
  ###### ACA LOS USUARIOS INTRODUCEN LOS DATOS ####################################################################################
 
    html.Div([ #Div-3  CONTENEDOR DATOS INGRESO Y GRAFICO dist horizontal 

    html.Div([ #Div-4 CONTENEDOR DE SUBTITULO, DATOS y RESULTADO

    html.P('INGRESO DE DATOS DEL PROYECTO', className='fix_label', style={"color": "#fff", 'fontSize': 18 ,
     "justify-content": "center", 'textAlign': 'center', 'margin':'0px' }),
    
    html.Div([  #Div-5 CONTINE LOS DATOS DE INGRESO

      html.Div([ #Div-5.1 
      
      html.Label('INVERSION INICIAL (US$):', style={ "color": "#fff",'margin-left':'15px', 'margin-right':'15px','fontSize': 12 }),
      dcc.Input(id='in_inv', type="number", value=22000, min=0,  style=estilo_input),
      
      html.Label('DEPRECIACION (Años):', style={ "color": "#fff",'margin-left':'15px', 'margin-right':'15px','fontSize': 12 }),
      dcc.Input(id='in_dep', type="number", value=5, min=0, max=20 , style=estilo_input),
      
       html.Label('RENTABILIDAD REQUERIDA (%):', style={ "color": "#fff",'margin-left':'15px', 'margin-right':'15px', 'fontSize': 12}),
      dcc.Input(id='input_k', type="number",value=12, min=0, max=100, style=estilo_input),

     ], style= {'display':'flex', 'flex-direction':'column',} ),
      
      html.Div([ #Div-5.2 
     
      html.Label('INGRESO ANUAL (US$):', style={ "color": "#fff",'margin-left':'15px', 'margin-right':'15px', 'fontSize': 12} ),
      dcc.Input(id='in_ing',type="number", value=8000, min=0, style=estilo_input),
      
      html.Label('COSTO OP. ANUAL (US$):', style={ "color": "#fff",'margin-left':'15px', 'margin-right':'15px', 'fontSize': 12}),
      dcc.Input(id='in_cost',type="number", value=2500,min=0, style=estilo_input),
      
      html.Label('IMPUESTO S/GANANCIAS (%):', style={ "color": "#fff",'margin-left':'15px', 'margin-right':'15px', 'fontSize': 12}),
      dcc.Input(id='in_imp', type="number", value=25,min=0, max=100, style=estilo_input),

      ], style= {'display':'flex', 'flex-direction':'column', }),
 
      html.Div([ #Div-5.3 

      html.Label('PRESTAMO (US$):', style={ "color": "#fff",'margin-left':'15px', 'margin-right':'25px', 'fontSize': 12} ),
      dcc.Input(id='in_Deuda', type="number",value=12000 , min=0, style=estilo_input ),
      
      html.Label('PLAZO (Años):', style={ "color": "#fff",'margin-left':'15px', 'margin-right':'15px', 'fontSize': 12}),
      dcc.Input(id='in_plazo', type="number",value=8,min=1, max=20, style=estilo_input),
      
      html.Label('TASA DE INTERES (%):', style={ "color": "#fff",'margin-left':'15px', 'margin-right':'15px', 'fontSize': 12}),
      dcc.Input(id='in_int', type="number",value=3,min=0, max=100, style=estilo_input),

     ], style= {'display':'flex', 'flex-direction':'column',}),
      
       ], style = {'border-radius': '0.55rem', 
    'display':'flex', 'flex-direction':'row', "padding":"20px 5px" , "margin":"10px"
     
  }), #Div-5  Contiene los datos de ingreso

#### ACA VA EL TEXTO DE SALIDA CON LOS RESULTADOS ##################
    
    dcc.Textarea(
        id='textarea-example',
        value={},
        style={'width': 590, 'height': 200, "font-family": "Open Sans, sans-serif",'fontSize': 18, 'resize': 'none',
         'background-color': "#fff","color": '#082255', 'fontWeight': 'bold', 'border-color': 'white', 'display':'flex', 
         'flex-direction':'row',
          'border-radius': '0.55rem',"box-shadow": "0 1px 2px rgba(0,0,0,0.24)", 'textAlign': 'justify', "padding": "15px 15px ",
          'margin-left': '25px',},
                  ), 

],  style = {'backgroundColor': '#082255','border-radius': '0.55rem', "box-shadow": "0 3px 3px rgba(0,0,0,0.24)", 'display':'flex',
 'flex-direction':'column', "padding":"20px 5px " , "margin":"10px"
     
  }), #Div-4

 
  #####ACA VA EL GRAFICO ##############################################################################################################################
  html.Div([  #HDiv-6

     # TITULO DE GRAFICO
    html.P("GRÁFICO: FLUJO DE FONDOS DEL INVERSIONISTA (US$)", className='fix_label', style={"color": "#fff",
      'fontSize': 18 , "justify-content": "center", 'textAlign': 'center', 'margin':'0px' }),


      # GRAFICO
      dcc.Graph(id='flujo_fondos', figure={}, style={ 'width': '760px','height': '440px','display':'flex', 'flex-direction':'row',
        })  

    ], style={'backgroundColor': '#082255','border-radius': '0.55rem', 
   "box-shadow": "0 3px 3px rgba(0,0,0,0.24)", 'display':'flex', 'flex-direction':'column',"padding": "20px 5px",  "margin":"10px", 
   "margin-right":"0px" }),
   
   ], style={'display':'flex', 'flex-direction':'row'}),  #Div-3 Aca termina el contenedor del Grafico


  ################### ACA VA LA TABLA CON EL FLUJO DE FONDOS  ########################################################### 
  html.Div([ #HDiv-8

####### Titulo del Cuadro ###########################################################################################
     html.P('CUADRO: FLUJO DE FONDOS DEL INVERSIONISTA PROYECTADO (US$)',
    style={'width': '100%', 'height': 12, "font-family": "Open Sans, sans-serif",'fontSize': 18, 'margin-bottom': '10px','textAlign': 'left',
       'margin-left': '20px',"color": "#fff", 'display':'flex',
  
   },
    ),
##################
 
    html.Div([     
       #HDiv-9 TABLA Y ADRIAN
    dt.DataTable(
        id = 'dt1', 
        columns =  [{"name": i, "id": i} for i in (df.columns)], data=[{}],        
        
        style_table={'order': '1',  'border-radius': '0.55rem',"box-shadow": "0 1px 2px rgba(0,0,0,0.24)",'display':'flex',
        'flex-direction':'row' },
       
        style_as_list_view=True,
        
        style_data={'color': 'Black','backgroundColor': '#fff', "font-family": "Open Sans, sans-serif",'fontSize': 11,  
        'overflow': 'hidden','textOverflow': 'ellipsis','width': '43px', 'maxWidth': '43px','flex-direction':'column'
        },   # Estilo de la tabla

        style_data_conditional=[{'if': {'row_index': c},'backgroundColor': colorsel,"color": "#fff",  'fontWeight': 'bold', 
        'flex-direction':'column'} for c in [ 2, 4, 6, 8,13] ],
        
        style_header={'backgroundColor': colorsel,'color': 'white','fontWeight': 'bold',"font-family": "Open Sans, sans-serif" ,'fontSize': 13, 
        'flex-direction':'column'},
        
        style_cell_conditional=[{ 'if': {'column_id': c}, 'textAlign': 'left','minWidth': '100px', 'width': '100px', 'maxWidth': '100px', 'flex-direction':'column' } 
        for c in ['Concepto']]
        
    ),

######## Marca Elaborado por ###########################################################################################
       html.Label('Elaborado por Adrián Risso',
        style={'width': '100%', 'height': 14, "font-family": "Open Sans, sans-serif",'fontSize': 11, 'margin-top': '20px', 'resize': 'none',
         'background-color': '#082255',"color": "#fff", 'display':'flex', 'flex-direction':'column', "border": "none" ,
          'textAlign': 'right','margin-bottom': '5px'},
    )
####################################################################################################################

    ],  style = {'backgroundColor': "#082255",'border-radius': '0.55rem',
       "margin-top": "10px",  'display':'flex', 
    'flex-direction':'column', "padding": "20px 5px", "margin": "5px" }),  #Div-9 TABLA Y ADRIAN
    
    ], style = {'backgroundColor': "#082255",'border-radius': '0.55rem',"box-shadow": "0 3px 3px rgba(0,0,0,0.24)",
    'display':'flex', 'flex-direction':'column',
       
    "padding": "20px ",
    "margin":"10px",
    'margin-right':'10',
    "margin-top": "10px",
     }
     ), #Div-8
   

    ], style={"font-family": "Open Sans, sans-serif" ,'backgroundColor': "#061E44", 'display':'flex', 'flex-direction':'column',
    "padding": "20px 5px", "margin": "0px" ,
         })  #Div-1  FIN DEL LAYOUT 
 
###### GRAFICO - CALLBACK
@app.callback(
  Output(component_id='flujo_fondos', component_property='figure'),
  [Input(component_id='in_inv', component_property='value')],
  [Input(component_id='in_dep', component_property='value')],
  [Input(component_id='in_ing', component_property='value')],
  [Input(component_id='in_cost', component_property='value')],
  [Input(component_id='in_imp', component_property='value')],
  [Input(component_id='in_Deuda', component_property='value')],
  [Input(component_id='in_plazo', component_property='value')],
  [Input(component_id='in_int', component_property='value')],
   [Input(component_id='input_k', component_property='value')], )

##### GRAFICO - FUNCION ###############################################################################################################
def update_value(in_inv, in_dep, in_ing, in_cost, in_imp,in_Deuda, in_plazo, in_int, input_k):
  
  ingresos=[float(0)]+[float(in_ing) for i in list(range(0,21))]
  costos=[float(0)]+[float(in_cost) for i in list(range(0,21))]
  inversion=[float(in_inv)]+[0.0 for i in list(range(0,21))]
  prestamo=[float(in_Deuda)]+[0.0 for i in list(range(0,21))]
  
  dep = []  #### flujo de las depreciaciones
  for i in list(range(0,21)):
    if 0<i <= float(in_dep):
        dep.append(float(float(in_inv)/float(in_dep)))
    else:
        dep.append(float(0))
  
  ####### financiamiento #########################
  amort = [] #flujo de las amortizacion de la depreciacion
  saldo = [] #flujo del Saldo de la deuda 
  intereses =[]  #flujo de intereses
  for i in list(range(0,21)):
    if 0<i <= float(in_plazo):
        amort.append(float(in_Deuda)/float(in_plazo))
    else:
        amort.append(0.0)
    saldo.append(float(in_Deuda)- sum(amort))
    intereses.append((float(in_int)/100)*saldo[i-1])
  intereses[0]=0.0
  
  ##### impuestos  ###############################
  impuestos=[max((float(in_imp)/100)*(ingresos[i]-costos[i]-dep[i]-intereses[i]),0) for i in list(range(0,21)) ]  #flujo de impuestos

  #####  Flujo de Fondos   #######################
  flow=[ingresos[i]-costos[i]-inversion[i]+prestamo[i]-impuestos[i] -amort[i] -intereses[i] for i in list(range(0,21))]
  
  #####  Flujo de fondos acumulado  ##############
  acc_flow=[]
  for i in  list(range(0,21)):
    if i==0:
      acc_flow.append(float(flow[0]))
    else:
      acc_flow.append(float(acc_flow[i-1])+float(flow[i]))

  
  
  npvt=[]
  for i in list(range(1,22)):
    npvt.append(round(npf.npv((float(input_k)/100),flow[0:i]),2))
    

  #creacion de la base y el dataframe para poder graficar
  base={'Año': ANNO, 'Flujo de Fondos': flow , 'VAN acumulado': npvt}
  df = pd.DataFrame(data=base)
  
  fig = make_subplots(specs=[[{"secondary_y": True}]] )
  fig1= px.bar( df, x='Año', y='Flujo de Fondos', text_auto='.2s')
  fig1.update_traces(marker_color=colorsel) 
  fig2= px.line( df, x='Año', y='VAN acumulado')
  fig2.update_traces(yaxis="y2", line_color='#FF5800',line=dict( width=4) )#'#7a00c0'
  fig.add_traces(fig1.data + fig2.data )
  fig.layout.xaxis.title="Año"
  fig.layout.yaxis.title="Flujo de Fondos (US$)"
  fig.layout.yaxis2.title="VAN Acumulado (US$)"
  fig.update_layout( legend_bgcolor='Black',
  paper_bgcolor='#082255', plot_bgcolor= 'white', margin=dict(l=5, r=5, t=30, b=5, pad=5),font=dict(family="Open Sans, sans-serif",
        size=12,      ), font_family="Open Sans, sans-serif",
    font_color="white")
  return fig

###### TABLA - CALLBACKS
@app.callback(Output('dt1','data'),
            [Input(component_id='in_inv', component_property='value')],
            [Input(component_id='in_dep', component_property='value')],
            [Input(component_id='in_ing', component_property='value')],
            [Input(component_id='in_cost', component_property='value')],
            [Input(component_id='in_imp', component_property='value')],
            [Input(component_id='in_Deuda', component_property='value')],
            [Input(component_id='in_plazo', component_property='value')],
            [Input(component_id='in_int', component_property='value')]
            
             )

#TABLA FUNCION
def update_table(in_inv, in_dep, in_ing, in_cost, in_imp,in_Deuda, in_plazo, in_int):
  data[10][1]=-float(in_inv)
  data[11][1]=float(in_Deuda)
  for i in list(range(2,22)): data[0][i]=float(in_ing)  
  for i in list(range(2,22)): data[1][i]=-float(in_cost)
  for i in list(range(2,22)): data[2][i]=float(in_ing)-float(in_cost)
  
  dep = []  #flujo de las depreciaciones
  for i in list(range(0,21)):
    if 0<i <= float(in_dep):
        dep.append(float(float(in_inv)/float(in_dep)))
    else:
        dep.append(float(0))
  for i in list(range(2,22)): data[3][i]=-float(dep[i-1])
  for i in list(range(2,22)): data[9][i]=float(dep[i-1])
  for i in list(range(2,22)): data[4][i]=data[2][i]+data[3][i]
  #financiamiento
  amort = [] #flujo de las amortizacion de la depreciacion
  saldo = [] #flujo del Saldo de la deuda 
  intereses =[]  #flujo de intereses
  for i in list(range(0,21)):
    if 0<i <= float(in_plazo):
        amort.append(float(in_Deuda)/float(in_plazo))
    else:
        amort.append(0.0)
    saldo.append(float(in_Deuda)- sum(amort))
    intereses.append((float(in_int)/100)*saldo[i-1])
  intereses[0]=0.0
  for i in list(range(2,22)): data[5][i]=-float(intereses[i-1])
  for i in list(range(2,22)): data[6][i]=data[4][i]+data[5][i]
  #impuestos
  impuestos=[max(((float(in_imp)/100.0)*(data[6][i+1])),0.0) for i in list(range(0,21)) ]  #flujo de impuestos
  for i in list(range(1,22)): data[7][i]=-float(impuestos[i-1])
  for i in list(range(1,22)): data[8][i]=data[6][i]+data[7][i]
  for i in list(range(1,22)): data[12][i]=-float(amort[i-1])
  for i in list(range(1,22)): data[13][i]=data[8][i]+data[9][i]+data[10][i]+ data[11][i]+ data[12][i]
  df=pd.DataFrame(data, columns=columna)
  for i in ANNO:
    df[i]=df[i].map("{:,.0f}".format)  #para redondear los datos al aparecer en la tabla
  return df.to_dict('records')  
  
 
#######TEXTO - CALLBACKS #######################
@app.callback(Output('textarea-example','value'),
            [Input(component_id='in_inv', component_property='value')],
            [Input(component_id='in_dep', component_property='value')],
            [Input(component_id='in_ing', component_property='value')],
            [Input(component_id='in_cost', component_property='value')],
            [Input(component_id='in_imp', component_property='value')],
            [Input(component_id='in_Deuda', component_property='value')],
            [Input(component_id='in_plazo', component_property='value')],
            [Input(component_id='in_int', component_property='value')],
            [Input(component_id='input_k', component_property='value')]
             )

####### TEXTO -FUNCION #######################
def update_texto(in_inv, in_dep, in_ing, in_cost, in_imp,in_Deuda, in_plazo, in_int, input_k):
  data[10][1]=-float(in_inv)
  data[11][1]=float(in_Deuda)
  for i in list(range(2,22)): data[0][i]=float(in_ing)  
  for i in list(range(2,22)): data[1][i]=-float(in_cost)
  for i in list(range(2,22)): data[2][i]=float(in_ing)-float(in_cost)
  
  dep = []  #flujo de las depreciaciones
  for i in list(range(0,21)):
    if 0<i <= float(in_dep):
        dep.append(float(float(in_inv)/float(in_dep)))
    else:
        dep.append(float(0))
  for i in list(range(2,22)): data[3][i]=-float(dep[i-1])
  for i in list(range(2,22)): data[9][i]=float(dep[i-1])
  for i in list(range(2,22)): data[4][i]=data[2][i]+data[3][i]
  #financiamiento
  amort = [] #flujo de las amortizacion de la depreciacion
  saldo = [] #flujo del Saldo de la deuda 
  intereses =[]  #flujo de intereses
  for i in list(range(0,21)):
    if 0<i <= float(in_plazo):
        amort.append(float(in_Deuda)/float(in_plazo))
    else:
        amort.append(0.0)
    saldo.append(float(in_Deuda)- sum(amort))
    intereses.append((float(in_int)/100)*saldo[i-1])
  intereses[0]=0.0
  for i in list(range(2,22)): data[5][i]=-float(intereses[i-1])
  for i in list(range(2,22)): data[6][i]=data[4][i]+data[5][i]
#impuestos
  impuestos=[max(((float(in_imp)/100.0)*(data[6][i+1])),0.0) for i in list(range(0,21)) ]  #flujo de impuestos
  for i in list(range(1,22)): data[7][i]=-float(impuestos[i-1])
  for i in list(range(1,22)): data[8][i]=data[6][i]+data[7][i]
  for i in list(range(1,22)): data[12][i]=-float(amort[i-1])
  for i in list(range(1,22)): data[13][i]=data[8][i]+data[9][i]+data[10][i]+ data[11][i]+ data[12][i]
  
  irr = round(npf.irr(data[13][1:22])*100 ,2)
  
  flujo=data[13][1:22] #Para aislar solo el flujo de fondos
  npv= round(npf.npv((float(input_k)/100),flujo[0:21]),2)
  
  npvt=[]
  for i in list(range(0,20)):
    npvt.append(round(npf.npv((float(input_k)/100),flujo[0:i]),2))



  fac=sum(data[13][1:22])
  text11= "Si se realiza una inversión de US$ {:,.0f}".format(in_inv).replace(",", "@").replace(".", ",").replace("@", ".")
  text12= " en el año {} bajo las condiciones indicadas, dentro de 20 años se obtendrá una acumulación de fondos de".format(ANNO[0])
  text13= " US$ {:,.2f} por encima del capital inicial invertido".format(float(fac)).replace(",", "@").replace(".", ",").replace("@", ".")

  if npv<0:
    text2=f'. Considerando que la tasa de rentabilidad requerida es de {input_k}%, el proyecto no es rentable y no es aconsejable invertir.'
  else:
    text2=f'. Considerando que la tasa de rentabilidad requerida es de {input_k}%, el proyecto es rentable y conviene realizar la inversión.'
  
  if in_inv>=in_Deuda:
    return (text11+text12+text13+". En este sentido, evaluando el proyecto se obtiene un Valor Actual Neto (VAN) igual a"+" US$ {:,.2f} ".format(npv).replace(",", "@").replace(".", ",").replace("@", ".") 
                    + "y una Tasa Interna de Retorno (TIR) de {:,.2f}%".format(irr).replace(",", "@").replace(".", ",").replace("@", ".") + text2)
  else:
    return "Por favor, corregir el monto del préstamo por uno inferior al monto invertido."      


if __name__ == '__main__':
  app.run_server(debug=False)