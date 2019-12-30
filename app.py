from flask import Flask, render_template, url_for, request, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)



app.config['SECRET_KEY'] = 'fddddddddddd'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '11111'
app.config['MYSQL_DB'] = 'appsdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'





post=[
    {'id':1,
    'title': 'Hello Flask',
    'body':'ndustry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheet'
    
    },
     {'id':2,
    'title': 'Hello Flask 2',
    'body':'ndustry. Lorem Ipsum has been the industry type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s wi'
    
    },
     {'id':3,
    'title': 'Hello Flask',
    'body':'ndustry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheet'
    
    },
     {'id':4,
    'title': 'Hello Flask 2',
    'body':'ndustry. Lorem Ipsum has been the industry type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s wi'
    
    }
]

@app.route('/')
def index():
    return render_template('index.html',post=post)

@app.route('/dashboard')
def about():
    return render_template('about.html')

@app.route('/write', methods=['POST','GET'])
def write():
    if request.method == "POST":
        title = request.form['title']
        body = request.form['body']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO post(title, body)" "VALUES(%s,%s)",(title, body))
        mysql.connection.commit()
        cur.close()
        flash('Your blog has been successfully inserted', 'success')
        return redirect('/')

    return render_template('write.html')    

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return 'Logout Successfull'



if __name__=="__main__":
    app.run(debug=True)