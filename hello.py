from flask import Flask
import sqlite3
from tasks import tasks
app = Flask(__name__)

@app.route('/hello')
def hello_world():
   sql_con = sqlite3.connect("tasks.db").cursor()
   sql_con.execute("CREATE TABLE IF NOT EXISTS to_do("
                   "tasks VARCHAR, completed BOOL)"
                   )
   sql_con.close()
   return "Hello!\nLet's see your tasks."

@app.route('/show_all')
def show_all():
   sql_con = sqlite3.connect("tasks.db")
   data = sql_con.execute("SELECT * FROM to_do")
   # data = sql_con.fetchall()
   sql_con.close()
   return data

@app.route('/add')
def add_task():
   sql_con = sqlite3.connect("tasks.db")
   t = input("Add your task: ")
   params = (t, False)
   # obj = tasks(t)
   sql_con.execute("INSERT INTO to_do VALUES (?, ?)", params)
   sql_con.commit()
   sql_con.close()

@app.route('/task/completed')
def task_completed():
   sql_con = sqlite3.connect("tasks.db")
   t = "make table"
   params = (t,)
   sql_con.execute("UPDATE to_do SET completed = TRUE where tasks = ?;", params)
   sql_con.commit()
   sql_con.close()


# hello_world()
# add_task()
# task_completed()
# show_all()
if __name__ == '__main__':
   app.run(debug = True)