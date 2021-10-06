from flask import *  
   
app = Flask(__name__)  

@app.route('/')
def home():
    return 'Hello from the other side!'

@app.route('/admin')  
def admin():  
    return 'This is admin'  
  
@app.route('/staff')  
def staff():  
    return 'This is staff'  
  
@app.route('/student')  
def student():  
    return 'This is student'  
  
@app.route('/user/<name>')  
def user(name):  
    if name == 'admin':  
        return redirect(url_for('admin'))  
    if name == 'librarion':  
        return redirect(url_for('staff'))  
    if name == 'student':  
        return redirect(url_for('student'))  

@app.route('/login',methods = ['GET','POST'])  
def login(): 
    if (request.method == "POST"):
        userName=request.form['name']  
        password=request.form['pass']  
        if userName=="Shubham Katke" and password=="6969":  
            return ("Hello, %s" %(userName))
    return render_template("login.html", title="Login")
        
if __name__ =='__main__':  
    app.run(debug = True)

# from flask import Flask, jsonify, request
# from flask_restful import Resource, Api

# app = Flask(__name__)
# api = Api(app)

# class Hello(Resource):
# 	def get(self):
# 		return jsonify({'message': 'hello world'})
# 	def post(self):
# 		data = request.get_json()
# 		return jsonify({'data': data}), 201

# class Square(Resource):
# 	def get(self, num):
# 		return jsonify({'square': num**2})

# api.add_resource(Hello, '/')
# api.add_resource(Square, '/square/<int:num>')

if __name__ == '__main__':
	app.run(debug = True)
