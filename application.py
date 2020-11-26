from web_frontend import application, app

app
application

if __name__ == "__main__":
    application.run("0.0.0.0", debug=True, port=5000)
