from flask import Flask,Blueprint,render_template,redirect,url_for,request,flash 
from database import*

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():

	return render_template('admin_home.html')

@admin.route('/admin_viewseller')	
def admin_viewseller():

	data={}
	q="select * from sellers"
	res=select(q)
	data['sell']=res

	return render_template('admin_viewseller.html',data=data)

@admin.route('/admin_viewcustomer')	
def admin_viewcustomer():
	data={}
	q="select * from customers"
	res=select(q)
	data['cust']=res

	return render_template('admin_viewcustomer.html',data=data)

@admin.route('/admin_viewagent')
def admin_viewagent():
	data={}
	q="select * from agent"
	res=select(q)
	data['agen']=res

	return render_template('admin_viewagent.html',data=data)


@admin.route('/admin_manageproductcategories',methods=['post','get'])	
def admin_manageproductcategories():

	data={}
	q="select * from product_category"
	res=select(q)
	data['cat']=res

	if "product" in request.form:
		c=request.form['cat']
		q="insert into product_category values(null,'%s')"%(c)
		insert(q)
		flash('successfully')
		return redirect(url_for('admin.admin_manageproductcategories'))

	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']

	else:
		action=None

	if action=='delete':
		q="delete from product_category where cat_id='%s'"%(cid)
		delete(q)
		flash('successfully')
		return redirect(url_for('admin.admin_manageproductcategories'))

	if action=='update':
		q="select * from product_category where cat_id='%s'"%(cid)
		res=select(q)
		data['pro']=res

	if "update" in request.form:
		c=request.form['cat']
		q="update product_category set cat_name='%s' where cat_id='%s'"%(c,cid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_manageproductcategories'))
		
	return render_template('admin_manageproductcategories.html',data=data)
	
@admin.route('/admin_mangecommission',methods=['post','get'])
def admin_mangecommission():
	data={}
	q="select * from product_category"
	res=select(q)
	data['pro']=res

	q="select * from  commission inner join product_category using(cat_id)"
	res=select(q)
	data['comm']=res

	if "comm" in request.form:
		c=request.form['cat']
		p=request.form['per']
		q="insert into commission values(null,'%s','%s')"%(c,p)
		insert(q)
		flash('successfully')
		return redirect(url_for('admin.admin_mangecommission'))

	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']

	else:
		action=None

	if action=='delete':
		q="delete  from commission where commission_id='%s'"%(cid)
		delete(q)
		flash('successfully')
		return redirect(url_for('admin.admin_mangecommission'))

	if action=='update':
		q="select * from commission inner join product_category using(cat_id) where commission_id='%s'"%(cid)
		res=select(q)
		data['comp']=res

	if "update" in request.form:
		c=request.form['cat']
		p=request.form['per']
		q="update commission set cat_id='%s',percentage='%s' where commission_id='%s'"%(c,p,cid)
		update(q)
		flash('successfully')
		
		return redirect(url_for('admin.admin_mangecommission'))

	return render_template('admin_mangecommission.html',data=data)	

@admin.route('/admin_viewpayments')	
def admin_viewpayments():
	data={}
	q="SELECT * FROM payment INNER JOIN `order` USING (order_id) INNER JOIN customers USING (customer_id)"
	res=select(q)
	data['pay']=res


	return render_template('admin_viewpayments.html',data=data)

@admin.route('/admin_viewcomplaint')	
def admin_viewcomplaint():
	data={}
	q="select * from complaints inner join customers using (customer_id)"
	res=select(q)
	data['comp']=res
	
	return render_template('admin_viewcomplaint.html',data=data)

@admin.route('/admin_vieworders')	
def admin_vieworders():
	data={}
	q="SELECT * FROM `orderdetails` INNER JOIN `order` USING (order_id) INNER JOIN customers USING (customer_id)INNER JOIN products USING (product_id)"
	res=select(q)
	data['order']=res
	
	return render_template('admin_vieworders.html',data=data)	
@admin.route('/admin_sendreply',methods=['post','get'])
def admin_sendreply():
	if "reply" in request.form:
		cid=request.args['cid']
		r=request.form['rep']
		q="update complaints set reply='%s' where complaint_id='%s'"%(r,cid)
		update(q)
		flash('successfully')
		return redirect(url_for('admin.admin_viewcomplaint'))
		
	return render_template('admin_sendreply.html')




