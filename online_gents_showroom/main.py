from flask import Flask
from public import public 
from admin import admin
from seller import seller
from customer import customer
from agent import agent

app=Flask(__name__)

app.secret_key='key'

app.register_blueprint(public)
app.register_blueprint(admin,url_prifix=('/admin'))
app.register_blueprint(seller,url_prifix=('/seller'))
app.register_blueprint(customer,url_prifix=('/customer'))
app.register_blueprint(agent,url_prifix=('/agent'))


app.run(debug=True,port=5343)