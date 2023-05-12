import sqlite3, random
from flask import Flask, render_template, request, url_for, flash, redirect, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

def get_db_connection():
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('select * from posts where id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('select * from posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required')
        elif not content:
            flash('Content is required!')
        else:
            addTable = random.randint(0,4)
            conn = get_db_connection() 
            conn.execute('insert into posts (title,content, test) values (?,?,?)', (title, content,addTable))
            if addTable == 1:
                conn.execute('insert into test1 (title,content) values (?,?)', (title, content))
            elif addTable == 2:
                conn.execute('insert into test2 (title,content) values (?,?)', (title, content))
            elif addTable == 3:
                conn.execute('insert into test3 (title,content) values (?,?)', (title, content))
            elif addTable == 4:
                conn.execute('insert into final (title,content) values (?,?)', (title, content))
            
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    
    return render_template('create.html')

@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        developer = request.form['developer']
        genre = request.form['genre']

        if not title:
            flash('Title is required!')
        
        elif not content:
            flash('Content is required!')
        
        else:
            conn = get_db_connection()
            conn.execute('update posts set title = ?, content = ?, developer= ?, genre = ?'
                            'where id = ?',
                            (title, content, developer, genre, id))    
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('delete from posts where id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

@app.route('/<int:id>/gamePage/', methods=('GET','POST'))
def gamePage(id):
    post = get_post(1)
    return render_template('gamePage.html', post=post)

@app.route('/test_1/')
def test_1():
    conn = get_db_connection()
    games = conn.execute('select * from test1').fetchall()
    conn.close()
    return render_template('test_1.html', games=games)

@app.route('/test_2/')
def test_2():
    conn = get_db_connection()
    games = conn.execute('select * from test2').fetchall()
    conn.close()
    return render_template('test_2.html', games=games)

@app.route('/test_3/')
def test_3():
    conn = get_db_connection()
    games = conn.execute('select * from test3').fetchall()
    conn.close()
    return render_template('test_3.html', games=games)
@app.route('/final/')
def final():
    conn = get_db_connection()
    games = conn.execute('select * from final').fetchall()
    conn.close()
    return render_template('final.html', games=games)
