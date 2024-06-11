from flask import Flask,Blueprint,render_template,request,redirect,url_for,session,flash 
from database import*
import uuid

seller=Blueprint('seller',__name__)

@seller.route('/seller_home')
def seller_home():

	return render_template('seller_home.html')

@seller.route('/seller_manageproducts',methods=['post','get'])
def seller_manageproducts():

	data={}
	q="select * from product_category"
	res=select(q)
	data['pro']=res

	q="select * from products inner join product_category using (cat_id)"
	res=select(q)
	data['pr']=res



	if "product" in request.form:

		sid=session['seller_id']
		pc=request.form['pc']
		pn=request.form['pname']
		i=request.files['imgg']
		path="static/image/"+str(uuid.uuid4())+i.filename
		i.save(path)
		a=request.form['amo']
		aq=request.form['aq']
		de=request.form['des']
		si=request.form['size']
		q="insert into products values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(sid,pc,pn,path,a,aq,de,si)
		insert(q)
		flash('successfully')
		return redirect(url_for('seller.seller_manageproducts'))


	if "action" in request.args:
		action=request.args['action']
		pid=request.args['pid']

	else:
		action=None

	if action=='delete':
		q="delete from products where product_id='%s'"%(pid)
		delete(q)
		flash('successfully')
		return redirect(url_for('seller.seller_manageproducts'))

	if action=='update':
		q="select * from products inner join product_category using (cat_id)"
		res=select(q)
		data['produ']=res

	if "update" in request.form:
		
		pc=request.form['pc']
		pn=request.form['pname']
		i=request.files['imgg']
		path="static/image/"+str(uuid.uuid4())+i.filename
		i.save(path)
		a=request.form['amo']
		aq=request.form['aq']
		de=request.form['des']
		si=request.form['size']
		q="update products set cat_id='%s',product_name='%s',product_image='%s',amount='%s',available_quantity='%s',description='%s',size='%s' where product_id='%s'"%(pc,pn,path,a,aq,de,si,pid)
		update(q)
		flash('successfully')
		return redirect(url_for('seller.seller_manageproducts')) 

	return render_template('seller_manageproducts.html',data=data)

@seller.route('/seller_vieworders')	
def seller_vieworders():
	data={}
	q="SELECT * FROM `orderdetails` INNER JOIN `order` USING (order_id) INNER JOIN customers USING (customer_id)INNER JOIN products USING (product_id)"
	res=select(q)
	data['order']=res

	if "action" in request.args:
		action=request.args['action']
		oid=request.args['oid']
		
	else:
		action=None

	if action=='accept':
		q="update `order` set status='accept' where order_id='%s'"%(oid)
		update(q)
		flash('successfully')
		return redirect(url_for('seller.seller_vieworders'))

	if action=='reject':
		q="update `order` set status='reject ' where order_id='%s'"%(oid)
		update(q)
		flash('successfully')
		return redirect(url_for('seller.seller_vieworders'))
	
	return render_template('seller_vieworders.html',data=data)

@seller.route('/seller_viewpayment')
def seller_viewpayment():
	data={}
	q="SELECT * FROM payment INNER JOIN `order` USING (order_id) INNER JOIN customers USING (customer_id)"
	res=select(q)
	data['pay']=res

	return render_template('seller_viewpayment.html',data=data)

@seller.route('/seller_viewcommission')	
def seller_viewcommission():
	data={}
	q="select * from commission inner join product_category using (cat_id)"
	res=select(q)
	data['comm']=res

	return render_template('seller_viewcommission.html',data=data)

@seller.route('/seller_assignagent',methods=['post','get'])
def seller_assignagent():
	data={}
	q="select * from agent"
	res=select(q)
	data['ag']=res

	if "agents" in request.form:
		oid=request.args['oid']
		a=request.form['agg']
		q="insert into assign values(null,'%s','%s','assign')"%(oid,a)
		insert(q)
		flash('successfully')
		q="update `order` set status='assign to agent' where order_id='%s'"%(oid)
		update(q)
		return redirect(url_for('seller.seller_assignagent'))

		
	return render_template('seller_assignagent.html',data=data)
			
