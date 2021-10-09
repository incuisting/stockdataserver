from stock import create_app

app = create_app()


@app.route('/status', methods=['GET'])
def status():
    return 'Running!'

# a simple page that says hello
@app.route('/hello')
def hello():
	return 'Hello, World!'

if __name__ == '__main__':
    app.run()