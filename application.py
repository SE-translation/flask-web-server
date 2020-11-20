from web_frontend import application

app = application
application = application


if __name__ == "__main__":

    application.run(debug=True,port=1200)