from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '''
    <html>
        <head>
            <style>
                h1,h3 {
                    color: #4F6F52;  /* Change to your desired color */
                    text-align:center;
                    font-size:30px;
                }
            </style>
        </head>
        <body>
            <h1> Python Webapp Deployment on Heroku Using Github Actions </h1>
            <h3 style="color:black"> Visit here for Documentation : <a href="https://github.com/Raghul-M/Python-Github_Actions-Heroku">https://github.com/Raghul-M/Python-Github_Actions-Heroku</a></h3>
        </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)