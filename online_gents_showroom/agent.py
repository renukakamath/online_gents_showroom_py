from flask import Flask,Blueprint,render_template,session,request,redirect,url_for 
from database import*

agent=Blueprint('agent',__name__)


@agent.route('/agent_home')
def agent_home():

	return render_template('agent_home.html')

@agent.route('/agent_viewassign')
def agent_viewassign():
	data={}
	q="select * from assign inner join `order` using (order_id) inner join agent using (agent_id)"
	res=select(q)
	data['agg']=res

	return render_template('agent_viewassign.html',data=data)
@agent.route('/agent_assignnextagent',methods=['post','get'])	
def agent_assignnextagent():
	data={}
	aid=session['login_id']
	q="select * from agent where not login_id='%s'"%(aid)
	res=select(q)
	data['agen']=res

	if "agents" in request.form:
		oid=request.args['oid']
		a=request.form['agg']
		q="insert into assign values(null,'%s','%s','assign')"%(oid,a)
		insert(q)
		
		return redirect(url_for('agent.agent_viewassign'))

	return render_template('agent_assignnextagent.html',data=data)
	
		