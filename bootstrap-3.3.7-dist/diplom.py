import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
	#return 'Hello'
     return flask.render_template('index.html')
    
if __name__ == '__main__':
    app.run(
        # host="0.0.0.0",
        # port=int("80"),
         debug=True
    )
