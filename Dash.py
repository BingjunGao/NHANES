import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import joblib

# 加载模型
model = joblib.load('E:\\Rprojects\\MRCH\\model.pkl')

app = dash.Dash(__name__)

# 定义布局，包含八个输入框，用于输入每个变量的值
app.layout = html.Div([
    html.H1("Machine Learning Prediction Model"),
    
    html.Label('AP (碱性磷酸酶)'),
    dcc.Input(id='input-ap', type='number', placeholder='AP value', step=0.01),

    html.Label('CRP (C反应蛋白)'),
    dcc.Input(id='input-crp', type='number', placeholder='CRP value', step=0.01),

    html.Label('CA (钙)'),
    dcc.Input(id='input-ca', type='number', placeholder='Calcium value', step=0.01),

    html.Label('GGT (γ-谷氨酰转移酶)'),
    dcc.Input(id='input-ggt', type='number', placeholder='GGT value', step=0.01),

    html.Label('TP (总蛋白)'),
    dcc.Input(id='input-tp', type='number', placeholder='TP value', step=0.01),

    html.Label('AB (白蛋白)'),
    dcc.Input(id='input-ab', type='number', placeholder='Albumin value', step=0.01),

    html.Label('GC (血糖)'),
    dcc.Input(id='input-gc', type='number', placeholder='Gamma Globulin value', step=0.01),

    html.Label('NAB (非白蛋白)'),
    dcc.Input(id='input-nab', type='number', placeholder='Neutral Albumin value', step=0.01),

    html.Button('Submit', id='submit-val', n_clicks=0),
    
    html.Div(id='output-prediction')
])

# 回调函数，使用输入的八个变量值进行预测
@app.callback(
    Output('output-prediction', 'children'),
    [Input('submit-val', 'n_clicks')],
    [State('input-ap', 'value'),
     State('input-crp', 'value'),
     State('input-ca', 'value'),
     State('input-ggt', 'value'),
     State('input-tp', 'value'),
     State('input-ab', 'value'),
     State('input-gc', 'value'),
     State('input-nab', 'value')]
)
def update_prediction(n_clicks, ap, crp, ca, ggt, tp, ab, gc, nab):
    # 检查所有值是否已输入
    if None not in [ap, crp, ca, ggt, tp, ab, gc, nab]:
        input_data = [[ap, crp, ca, ggt, tp, ab, gc, nab]]
        prediction = model.predict(input_data)
        return f'Prediction: {prediction[0]}'
    else:
        return 'Please enter all values before submitting.'

if __name__ == '__main__':
    app.run_server(debug=True)
