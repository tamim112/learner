
# ---- API (example) -----
def get_courses():
    if not request.env.request_method == 'GET': 
        raise HTTP(403)
    
    course_id = request.vars.course_id
    
    if course_id==None:
        course_id=''
    course_list=[]
    if course_id!='':
        course_sql = """
            select * from courses where course_id='{course_id}' limit 0,1
        """.format(course_id=course_id)
        course_records = db.executesql(course_sql, as_dict=True)
        if len(course_records) == 0:
            res_data={'status': '400', 'ret_str': 'Course not found'}
        else:            
            for rRow in range(len(course_records)):
                courses = course_records[rRow]
                course_info={
                    'course_id':str(courses['course_id']),
                    'title':str(courses['title']),
                    'description':str(courses['description']),
                    'instructor':str(courses['instructor']),
                    'duration':str(courses['duration']),
                    'price':'$'+str(courses['price'])
                    }  
                course_list.append(course_info)
            res_data={
                'status': '200',
                'course_info':course_list
                }  
    else:
        course_sql = """
            select * from courses where 1
        """.format(course_id=course_id)
        course_records = db.executesql(course_sql, as_dict=True)
        if len(course_records) == 0:
            res_data={'status': '400', 'ret_str': 'Course not found'}
        else:            
            for rRow in range(len(course_records)):
                courses = course_records[rRow]
                course_info={
                    'course_id':str(courses['course_id']),
                    'title':str(courses['title']),
                    'description':str(courses['description']),
                    'instructor':str(courses['instructor']),
                    'duration':str(courses['duration']),
                    'price':'$'+str(courses['price'])
                    }
                course_list.append(course_info)
            res_data={
                'status': '200',
                'course_info':course_list
                }  
    data=response.json(res_data)
    return data

def filter_courses():
    if not request.env.request_method == 'GET': 
        raise HTTP(403)
    
    title = request.vars.title
    instructor = request.vars.instructor
    price = request.vars.price
    duration = request.vars.duration
    
    if title==None:
        title=''
    if instructor==None:
        instructor=''
    if price==None:
        price=''
    if duration==None:
        duration=''
        
    conditions=''
    if instructor!='':
        conditions=' and instructor="'+instructor+'"'
    if title!='':
        conditions=conditions+' and title="'+title+'"'
    if price!='':
        conditions=conditions+' and price="'+price+'"'
    if duration!='':
        conditions=conditions+' and duration="'+duration+'"'
    
    course_sql = """
        select * from courses where 1 {conditions} 
    """.format(conditions=conditions)
    course_records = db.executesql(course_sql, as_dict=True)
    if len(course_records) == 0:
        res_data={'status': '200', 'ret_str': 'Course not found'}
    else:  
        course_list=[]          
        for rRow in range(len(course_records)):
            courses = course_records[rRow]
            course_info={
                'course_id':str(courses['course_id']),
                'title':str(courses['title']),
                'description':str(courses['description']),
                'instructor':str(courses['instructor']),
                'duration':str(courses['duration']),
                'price':'$'+str(courses['price'])
                }  
            course_list.append(course_info)
        res_data={
            'status': '200',
            'course_info':course_list
            }  
    data=response.json(res_data)
    return data
    
def create_course():
    if not request.env.request_method == 'POST': 
        raise HTTP(403)
    
    title=request.vars.title
    description=request.vars.description
    instructor=request.vars.instructor
    duration=request.vars.duration
    price=request.vars.price
    
    
    if title==None:
        title=''
    if description==None:
        description=''
    if instructor==None:
        instructor=''
    if duration==None:
        duration=''
    if price==None:
        price=''
        
    if title =='':
        res_data={'status': '400', 'ret_str': 'Title is required'}
    elif description =='':
        res_data={'status': '400', 'ret_str': 'Description is required'}
    elif instructor =='':
        res_data={'status': '400', 'ret_str': 'Instructor is required'}
    elif duration =='':
        res_data={'status': '400', 'ret_str': 'Duration is required'}
    elif price =='':
        res_data={'status': '400', 'ret_str': 'Price is required'}
    else: 
        course_sql = """
            select * from courses where title='{title}' limit 0,1
        """.format(title=title)
        course_records = db.executesql(course_sql, as_dict=True)
        if len(course_records) > 0:
            res_data={'status': '200', 'ret_str': 'Course already exists'}
        else:
            max_entry_sql = 'SELECT ifnull(max(course_id),1000) as course_id FROM courses'
            max_entry_rec=db.executesql(max_entry_sql,as_dict=True)
            course_id=int(max_entry_rec[0]['course_id'])+1
            
            course_reg_sql="""
                insert into courses (course_id,title,description,instructor,duration,price,status)
                values ('{course_id}','{title}','{description}','{instructor}','{duration}','{price}','{status}')
            """.format(course_id=course_id,title=title,description=description,instructor=instructor,duration=duration,price=price,status='1')
            
            db.executesql(course_reg_sql)
            res_data={
                'status': '200',
                'ret_str':'Course Successfully Created'
                }  
    
    data=response.json(res_data)
    return data