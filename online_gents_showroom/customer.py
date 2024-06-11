from flask import Flask,Blueprint,render_template,request,session,redirect,url_for,flash
from database import*

customer=Blueprint('customer',__name__)

@customer.route('/customer_home')
def customer_home():

	return render_template('customer_home.html')

@customer.route('/customer_viewproduct')	
def customer_viewproduct():

	data={}
	q="SELECT * FROM products INNER JOIN product_category USING (cat_id) INNER JOIN sellers USING (seller_id)"
	res=select(q)
	data['pr']=res

	return render_template('customer_viewproduct.html',data=data)

@customer.route('/customer_addtocart',methods=['post','get'])
def customer_addtocart():
	data={}
	a=request.args['amt']
	data['amount']=a

	p=request.args['pro']
	data['product']=p

	q="SELECT * FROM `orderdetails` INNER JOIN `order` USING (order_id) INNER JOIN customers USING (customer_id)INNER JOIN products USING (product_id)"
	res=select(q)
	data['ord']=res

	

	if "add" in request.form:
		cid=session['customer_id']
		pid=request.args['pid']
		qu=request.form['qua']
		a=request.args['amt']
		t=request.form['total']

		q="select * from `order` where customer_id='%s' and  status='pending'" %(cid)
		res=select(q)
		if res:
			oid=res[0]['order_id']
		else:
	
			q="insert into `order` values(null,'%s',curdate(),'0','pending')"%(cid)
			oid=insert(q)
			flash('successfully')
			print(q)

		q="select * from orderdetails where product_id='%s' and order_id='%s' " %(pid,oid)
		res1=select(q)
		if res1:
			q="update orderdetails set quantity=quantity+'%s'  , amount=amount+'%s' where od_id='%s'" %(qu,t,res1[0]['od_id'])
			update(q)
			flash('successfully')
		else:
			q="insert into `orderdetails` values(null,'%s','%s','%s','%s')"%(oid,pid,qu,t)
			insert(q)
			flash('successfully')
			print(q)
		q="update `order` set total_amount =total_amount+'%s' where order_id='%s'" %(t,oid)
		update(q)
		flash('successfully')
		return redirect(url_for('customer.customer_viewproduct'))

		
	return render_template('customer_addtocart.html',data=data)

@customer.route('/customer_sendcomplaint',methods=['post','get'])	
def customer_sendcomplaint():
	data={}
	q=" SELECT * FROM complaints INNER JOIN customers USING (customer_id)"
	res=select(q)
	data['com']=res

	if "complaint" in request.form:
		cid=session['customer_id']
		c=request.form['comp']

		q="insert into complaints values(null,'%s','%s','pending',curdate())"%(cid,c)
		insert(q)
		flash('successfully')

		return redirect(url_for('customer.customer_sendcomplaint'))

	
	return render_template('customer_sendcomplaint.html',data=data)

@customer.route('/customer_makepayment',methods=['post','get'])	
def customer_makepayment():
	data={}
	a=request.args['amt']
	data['amount']=a

	if "payment" in request.form:
		oid=request.args['oid']
		a=request.args['amt']
		q="insert into payment values(null,'%s','%s',curdate())"%(oid,a)
		insert(q)
		flash('successfully')
		q="update `order` set status='payed' where order_id='%s'"%(oid)
		update(q)
		flash('successfully')
		return redirect(url_for('customer.customer_viewproduct'))
		
	return render_template('customer_makepayment.html',data=data)

@customer.route('/customer_trackorder')	
def customer_trackorder():
	data={}
	q="select * from orderdetails inner join `order` using (order_id) inner join products  using(product_id) inner join customers using (customer_id)"
	res=select(q)
	data['ord']=res

	return render_template('customer_trackorder.html',data=data)
	

	

	
	