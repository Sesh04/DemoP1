from flask import Flask, render_template,request
from flask_mysqldb import MySQL
import MySQLdb.cursors
app = Flask(__name__)


app.config["MYSQL_HOST"] = "demoproductivity-server.mysql.database.azure.com"
app.config["MYSQL_USER"] = "buutwzbzzu@demoproductivity"
app.config["MYSQL_PASSWORD"] = "G7G18O52WJ1UF6TD$"
app.config["MYSQL_DB"] = "demoproductivity-database"


mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def user_login():
    if request.method == "POST":
       
        id=request.form["userid"]
        username = request.form["username"]
        password = request.form["password"]
           
           
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)


        cursor.execute('INSERT INTO accountsuser VALUES (% s, % s, % s)',(id, username, password),)
           
        mysql.connection.commit()
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

