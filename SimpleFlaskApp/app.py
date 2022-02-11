from re import T
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)       # referencing this file

# Init DB
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # return a string everytime we create a new element
    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST','GET'])             # set up route
def index():
    if request.method == 'POST':                    # Add task to list
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "CAN'T ADD TASK TO DB"
    else: 
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks=tasks)

@app.route('/delete/<int:id>')  
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "Error deleting task"


@app.route('/update/<int:id>', methods=['GET','POST'])  
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':                    # Add task to list
        task.content = request.form['content']
        
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "CAN'T UPDATE TASK TO DB"
    else:
        return render_template('update.html', task=task)
   
if __name__=="__main__":
    app.run(debug=True)