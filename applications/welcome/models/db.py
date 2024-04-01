# -- coding: utf-8 --

#########################################################################

from gluon.tools import *
mail = Mail()                                  # mailer
auth = Auth(globals(),db)                      # authentication/authorization
crud = Crud(globals(),db)                      # for CRUD helpers using auth
service = Service(globals())                   # for json, xml, jsonrpc, xmlrpc, amfrpc
plugins = PluginManager()

mail.settings.server = 'logging' or 'smtp.gmail.com:587'  # your SMTP server
mail.settings.sender = 'you@gmail.com'         # your email
mail.settings.login = 'username:password'      # your credentials or None

auth.settings.hmac_key = 'sha512:d6160708-08e3-4217-bd9e-e9a550109a8d'   # before define_tables()
#auth.define_tables()                           # creates all needed tables
auth.settings.mailer = mail                    # for user email verification
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.messages.verify_email = 'Click on the link http://'+request.env.http_host+URL('default','user',args=['verify_email'])+'/%(key)s to verify your email'
auth.settings.reset_password_requires_verification = True
auth.messages.reset_password = 'Click on the link http://'+request.env.http_host+URL('default','user',args=['reset_password'])+'/%(key)s to reset your password'

#########################################################################

crud.settings.auth = None                      # =auth to enforce authorization on crud

#########################################################################
# Common Variable
#mreporting_http_pass='abC321'
# ' " / \ < > ( ) [ ] { } ,

#======================date========================
import datetime
import os

datetime_fixed=str(date_fixed)[0:19]    # default datetime 2012-07-01 11:48:10
current_date=str(date_fixed)[0:10]   # default date 2012-07-01

first_currentDate = datetime.datetime.strptime(str(current_date)[0:7] + '-01', '%Y-%m-%d')

#================mytranscom_Database===================
#--------------------------- signature
signature=db.Table(db,'signature',
                Field('field1','string',length=100,default=''), 
                Field('field2','integer',default=0),
                Field('note','string',length=255,default=''),  
                Field('created_on','datetime',default=date_fixed),
                Field('created_by',default=session.emp_id),
                Field('updated_on','datetime',update=date_fixed),
                Field('updated_by',update=session.emp_id),
                )

#*******************Start Tables*******************

#=====================Users Table================
db.define_table('users',
                Field('user_id','string',length=20,default=session.cid),
                Field('user_name','string',length=20),
                Field('user_email','string',unique=True,length=50),
                Field('user_mobile','string',unique=True,length=50),
                Field('username','string',unique=True,length=50),
                Field('password','string',length=256),
                signature,
                migrate=False
                )

#=====================Courses ================
db.define_table('courses',
                Field('course_id','integer'),
                Field('title','string',length=200),
                Field('description','string',length=500),
                Field('instructor','string',length=100),
                Field('duration','integer'),   
                Field('price','float'),
                Field('status','integer',length=1),
                signature,
                migrate=False
                )


#=====================Enrollments ================
db.define_table('enrollments',
                Field('enroll_id','integer',length=20),
                Field('student_name','string',length=20),
                Field('course_id','string',length=100),
                Field('enroll_date','date'),
                Field('status','integer',length=1,default=1),
                signature,
                migrate=False
                )
#*******************End Tables*******************