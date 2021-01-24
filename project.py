from flask import Flask
from flask import request
from flask import render_template
from flask import current_app
from flask import send_from_directory
import sqlite3
import random
import string
import os

UPLOAD_FOLDER = './uploads'
app = Flask(__name__,static_folder='./static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/instructions')
def instructions():
    return render_template('instructions.html')

@app.route('/catalog')
def catalog():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM info;")
    conn.commit()
    output = c.fetchall()
    ids = list()
    titles = list()
    authors = list()
    for entry in output:
        ids.append(entry[0])
        titles.append(entry[1])
        authors.append(entry[2])
    print(output)
    return render_template('catalog.html', length = len(ids), ids = ids, titles = titles, authors = authors)

@app.route('/createstory', methods=['POST'])
def createstory():
    panel = 1
    toexit = False
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    if request.method == 'POST':
        try:
            title = request.form['title']
            author = request.form['author']
            query_info = "INSERT INTO info (title, author) VALUES (?, ?);"
            c.execute(query_info, (title, author,));
            conn.commit()
            c.execute("SELECT sqlite_sequence.seq FROM sqlite_sequence WHERE name = ?;",("info",))
            conn.commit()
            story_id = c.fetchall()[0][0]
            
            print(title)
            print(author)
            print(request.files)
            while not toexit:
                try:
                    panelstr = str(panel)
                    f = request.files["image-"+panelstr]
                    image = id_generator()+".png"
                    saveloc = "uploads/"+image
                    f.save(saveloc)
                    convo = request.form["convo"+panelstr]
                    speechone = request.form["speechone"+panelstr]
                    speechtwo = request.form["speechtwo"+panelstr]
                    speechthree = request.form["speechthree"+panelstr]
                    redirone = request.form["redirone"+panelstr]
                    redirtwo = request.form["redirtwo"+panelstr]
                    redirthree = request.form["redirthree"+panelstr]
                    insert_panel = "INSERT INTO panels (image, convo, speechone, speechtwo, speechthree, redirone, redirtwo, redirthree, story, current) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                    c.execute(insert_panel, (image, convo, speechone, speechtwo, speechthree, redirone, redirtwo, redirthree, story_id, panel,));
                    conn.commit()
                    panel = panel + 1
                except Exception as e:
                    print(e)
                    toexit = True
            conn.close()
            return render_template('finish.html')
        except Exception as e:
            print(e)
            return render_template('create.html')

@app.route('/<story>/<panel>', methods = ['GET'])
def serve_story(story, panel):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT image, convo, speechone, speechtwo, speechthree, redirone, redirtwo, redirthree FROM panels WHERE story = ? AND current = ?;",(story,panel,))
    conn.commit()
    attributes = c.fetchall()
    if len(attributes) == 0:
        c.execute("SELECT title, author FROM info WHERE id = ?;",(story,))
        conn.commit()
        newattr = c.fetchall()
        conn.close()
        if len(newattr) == 0:
            return render_template('thanks.html')
        else:
            return render_template('thanks.html', story = newattr[0][0], author = newattr[0][1])
    else:
        this_panel = attributes[0]
        print(this_panel)
        conn.close()
        return render_template('panel.html', image = this_panel[0], convo = this_panel[1], speechone = this_panel[2],
                               speechtwo = this_panel[3], speechthree = this_panel[4], redirone = this_panel[5], redirtwo = this_panel[6],
                               redirthree = this_panel[7], audio = "chill_vibes.mp3")
    
@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    print(filename)
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    print(uploads)
    return send_from_directory(directory=uploads, filename=filename)


def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
