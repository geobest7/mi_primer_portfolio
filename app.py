from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta de portada con selector de idioma
@app.route('/')
def welcome():
    return render_template('index.html')


# Ruta principal del portfolio (después de elegir idioma)
@app.route('/home')
def home():
    lang = request.args.get('lang', 'en')
    return render_template('home.html', lang=lang)


# Ruta /about
@app.route('/about')
def about():
    return render_template('about.html')


# Ruta /projects
@app.route('/projects')
def projects():
    return render_template('projects.html')


if __name__ == '__main__':
    app.run(debug=True)




