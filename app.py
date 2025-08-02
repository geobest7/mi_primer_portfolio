from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta de portada con selector de idioma
@app.route('/')
def welcome():
    lang = request.args.get('lang', 'en')
    return render_template('index.html', lang=lang)

# Ruta principal del portfolio (después de elegir idioma)
@app.route('/home')
def home():
    lang = request.args.get('lang', 'en')
    return render_template('home.html', lang=lang)

# Ruta /about
@app.route('/about')
def about():
    lang = request.args.get('lang', 'en')
    return render_template('about.html', lang=lang)

# Ruta /studies
@app.route('/studies')
def studies():
    lang = request.args.get('lang', 'en')
    return render_template('studies.html', lang=lang)

# Ruta /experience
@app.route('/experience')
def experience():
    lang = request.args.get('lang', 'en')
    return render_template('experience.html', lang=lang)

# Ruta /certifications
@app.route('/certifications')
def certifications():
    lang = request.args.get('lang', 'en')
    return render_template('certifications.html', lang=lang)

# Ruta /projects
@app.route('/projects')
def projects():
    lang = request.args.get('lang', 'en')
    return render_template('projects.html', lang=lang)

if __name__ == '__main__':
    app.run(debug=True)
