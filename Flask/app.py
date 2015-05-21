from flask import Flask, render_template, url_for, redirect,request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os
from flask import json

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE = 'flask.db'
DATABASE_PATH = os.path.join(basedir, DATABASE)
print DATABASE_PATH
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
SQLALCHEMY_ECHO = True

app = Flask(__name__)
app.config['SECRET_KEY'] = 'development'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_ECHO'] = SQLALCHEMY_ECHO
db = SQLAlchemy(app)

class Product(db.Model):

    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String, unique=False, nullable=False)
    model_name = db.Column(db.String, unique=False, nullable=False)
    model_number = db.Column(db.String, unique=False, nullable=True)
    size_options = db.Column(db.String, unique=False, nullable=True)
    color_options = db.Column(db.String, unique=False, nullable=True)
    filename = db.Column(db.String, unique=False, nullable=True)


    def __init__(self, brand_name, model_name, model_number, size_options, color_options, filename):
        self.brand_name = brand_name
        self.model_name = model_name
        self.model_number = model_number
        self.size_options = size_options
        self.color_options = color_options
        self.filename = filename

    def __repr__(self):
        return '<brand_name, model_name {0} {1}>'.format(self.brand_name, self.model_name)

Bootstrap(app)

@app.route('/',methods=('GET','POST'))
def index():
    products = Product.query.all()
    return render_template('index.html',products=products)
    
@app.route('/add',methods=('GET','POST'))
def add_product():
    db.create_all()
    color_options_one =[ ('Black', 'Black'),('Dark Brown','Dark Brown'),('Medium Brown', 'Medium Brown'),('Light Brown','Light Brown'),('Dark Blue', 'Dark Blue'),('Blue','Blue'),('Light Blue', 'Light Blue')]
    color_options_two = [('Dark Red','Dark Red'),('Medium Red', 'Medium Red'),('Light Red','Light Red'),
                     ('Pink', 'Pink'),('Gray','Gray'),('White', 'White'),('Neutral','Neutral'),
                     ('Purple', 'Purple'),('Green','Green'),('Green', 'Green'),('Yellow','Yellow'),
                     ('Orange', 'Orange'),('Pattern','Pattern'),('Silver', 'Silver'),('Gold','Gold')] 
    size_options_one = [('65', '65'), ('64', '64'), ('63', '63'), ('62', '62')]
    size_options_two = [('61', '61'), ('60', '60'), ('59', '59'), ('58', '58'), ('57', '57')]
    product1 = Product('test1','test1','test2',json.dumps(size_options_one),json.dumps(color_options_one),'test1')
    product2 = Product('test2','test2','test3',json.dumps(size_options_two),json.dumps(color_options_two),'test2')
    db.session.add(product1)
    db.session.add(product2)
    db.session.commit()
    return redirect('/')

@app.route('/data/<flag>',methods=('GET','POST'))
def get_data_from_product(flag):
    product_id = request.args.get('product_id', 0, type=int)
    print '*'*20
    print product_id
    print '*'*20
    if product_id == 0:
        return json.jsonify({"":'--'})
    product = Product.query.filter_by(product_id = product_id).first();
    colors = json.loads(product.color_options)
    sizes = json.loads(product.size_options)
    print sizes;
    if flag == 'color':
        return json.jsonify(dict(colors))
    else:
        return json.jsonify(dict(sizes))   
 
if __name__ == '__main__':
    app.run(debug=True)
