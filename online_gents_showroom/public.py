from flask import Flask,Blueprint,render_template,request,url_for,redirect,session,flash 
from database import*


public=Blueprint('public',__name__)



@public.route('/')
def home():

	return render_template('public_home.html')

@public.route('/agent_registration',methods=['post','get'])
def agent_registration():
	if "agent" in request.form:
		a=request.form['aname']
		s=request.form['street']
		c=request.form['city']
		d=request.form['dis']
		p=request.form['pin']
		ph=request.form['Phone']
		e=request.form['email']
		u=request.form['uname']
		pa=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(u,pa)
		res=select(q)
		if res:
			flash('already exist')
		else:
			
			q="insert into login values(null,'%s','%s','agent')"%(u,pa)
			id=insert(q)
			q="insert into agent values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(id,a,s,c,d,p,ph,e)
			insert(q)
			flash('successfully')
			return redirect(url_for('public.agent_registration'))

	return render_template('agent_registration.html')

@public.route('/seller_registration',methods=['post','get'])	
def seller_registration():
	if "seller" in request.form:
		a=request.form['aname']
		p=request.form['place']
		ph=request.form['Phone']
		e=request.form['email']
		u=request.form['uname']
		pa=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(u,pa)
		res=select(q)
		if res:
			flash('already exist')
		else:
			q="insert into login values(null,'%s','%s','seller')"%(u,pa)
			id=insert(q)
			q="insert into sellers values(null,'%s','%s','%s','%s','%s')"%(id,a,p,ph,e)
			insert(q)
			flash('successfully')
			return redirect(url_for('public.seller_registration'))

	return render_template('seller_registration.html')

@public.route('/customer_registration',methods=['post','get'])	
def customer_registration():
	if "customer" in request.form:
		f=request.form['fname']
		l=request.form['lname']
		d=request.form['dob']
		a=request.form['add']
		s=request.form['street']
		c=request.form['city']
		di=request.form['dis']
		p=request.form['pin']
		ph=request.form['Phone']
		e=request.form['email']
		u=request.form['uname']
		pa=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(u,pa)
		res=select(q)
		if res:
			flash('already exist')
		else:
			q="insert into login  values(null,'%s','%s','customer')"%(u,pa)
			id=insert(q)
			q="insert into customers values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id,f,l,d,a,s,c,di,p,ph,e)
			insert(q)
			flash('successfully')
			return redirect(url_for('public.customer_registration'))

	return render_template('customer_registration.html')

@public.route('/login',methods=['post','get'])	
def login():
	if "login" in request.form:
		u=request.form['uname']
		pa=request.form['pwd']
		q="select * from login where username='%s'and password='%s' "%(u,pa)
		res=select(q)
		if res:
			session['login_id']=res[0]['login_id']
			lid=session['login_id']
			print(lid)
			if res[0]['type']=="admin":
				return redirect(url_for('admin.admin_home'))
			if res[0]['type']=="agent":
				q="select * from agent where login_id='%s'"%(lid)
				print(q)
				res=select(q)
				if res:
					session['agent_id']=res[0]['agent_id']
					aid=session['login_id']
					print(aid)

				return redirect(url_for('agent.agent_home'))

			if res[0]['type']=="seller":
				q="select * from sellers where login_id='%s'"%(lid)
				print(q)
				res=select(q)
				if res:
					session['seller_id']=res[0]['seller_id']
					sid=session['seller_id']
					print(sid)
				return redirect(url_for('seller.seller_home'))
			if res[0]['type']=="customer":
				q="select * from customers where login_id='%s'"%(lid)
				res=select(q)
				if res:
					session['customer_id']=res[0]['customer_id']
					cid=session['customer_id']
					
				return redirect(url_for('customer.customer_home'))
	return render_template('login.html')