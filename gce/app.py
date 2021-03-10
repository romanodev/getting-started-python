import dash
import dash_html_components as html

app = dash.Dash()

server = app.server


app.layout = html.Div([
            html.H1(children="Hello world!",className="hello",
    style={'color':'#00361c','text-align':'center'
          })
      ])

if __name__=='__main__':
    app.run_server(host='127.0.0.1',port=8080,debug=True)
