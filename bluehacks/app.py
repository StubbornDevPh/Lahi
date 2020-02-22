from flask import Flask, render_template ,url_for ,request

app = Flask(__name__)
app.TEMPLATES_AUTO_RELOAD=True

@app.route('/')
def index():
    return render_template('index.html')
#index then feed
#about
#places`
#option search place
@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/places')
def places():
    return render_template('places.html')

@app.route('/POP')
def popup():
    if 
if __name__ == "__main__":
    app.run(debug=True, port=6969)
    
    