def enroll_student():
    if not request.env.request_method == 'POST': 
        raise HTTP(403)
    
    course_id=request.vars.course_id
    student_name=request.vars.student_name
    enroll_date=request.vars.enroll_date
    
    if course_id==None:
        course_id=''
    if student_name==None:
        student_name=''
    if enroll_date==None:
        enroll_date=''
        
    if course_id =='':
        res_data={'status': '400', 'ret_str': 'course_id is required'}
    elif student_name =='':
        res_data={'status': '400', 'ret_str': 'student is required'}
    elif enroll_date =='':
        res_data={'status': '400', 'ret_str': 'enroll_date is required'}
    else: 
        course_sql = """
            select * from courses where course_id='{course_id}' limit 0,1
        """.format(course_id=course_id)
        course_records = db.executesql(course_sql, as_dict=True)
        if len(course_records) == 0:
            res_data={'status': '200', 'ret_str': 'Course not exists'}
        else:
            enroll_sql = """
                select * from enrollments where course_id='{course_id}' and student_name='{student_name}' limit 0,1
            """.format(course_id=course_id,student_name=student_name)
            enroll_records = db.executesql(enroll_sql, as_dict=True)
            if len(enroll_records) > 0:
                res_data={'status': '200', 'ret_str': 'Course already Enrolled!'}
            else:
                max_entry_sql = 'SELECT ifnull(max(enroll_id),1000) as enroll_id FROM enrollments'
                max_entry_rec=db.executesql(max_entry_sql,as_dict=True)
                enroll_id=int(max_entry_rec[0]['enroll_id'])+1
                
                course_reg_sql="""
                    insert into enrollments (enroll_id,student_name,course_id,enroll_date,status)
                    values ('{enroll_id}','{student_name}','{course_id}','{enroll_date}','{status}')
                """.format(enroll_id=enroll_id,student_name=student_name,course_id=course_id,enroll_date=enroll_date,status='1')
                
                db.executesql(course_reg_sql)
                res_data={
                    'status': '200',
                    'ret_str':'Course Successfully Enrolled'
                    }  
    
    data=response.json(res_data)
    return data