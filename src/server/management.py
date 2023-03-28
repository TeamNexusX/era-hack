from flask import (
    request,
    jsonify,
    session,
    abort
)

from server.utils.management import (
    check_password_hash,
    generate_password_hash,
    check_management_in_db
)

from server import app
from server.models import db,Management,Candidate

@app.route('/register',methods=['POST'])

def register(data=None):
    try:
        if request.method == 'POST':
            username=request.json['email']
            password=request.json['password']
            management=check_management_in_db(username)
            if management != None:
                return abort(400)
            management=Management(username=username,password=generate_password_hash(password))
            db.session.add(management)
            db.session.commit()
            return jsonify(message='Регистрация руководителя {} успешна.'.format(username))
    except:
        return abort(500)
    
@app.route('/login',methods=['POST'])
def login(data=None):
    try:    
        if request.method == 'POST':
            username=request.json['email']
            password=request.json['password']
            management=check_management_in_db(username)
            if management == None or not check_password_hash(management.password,password):
                return abort(401)
            else:
                session['username']=username
                jsonManagement=Management.object_as_dict(management)
                return jsonify(jsonManagement)
    except:
        return abort(500)

@app.route('/logout',methods=['GET'])
def logout(data=None):
    try:
        if request.method == 'GET' and 'username' in session:
            message='Пользователь {} успешно вышел из системы'.format(session['username'])
            session.pop('username')
            return jsonify(message=message)    
        else:
            return abort(401)
    except:
        return abort(500)
    

@app.route('/candidates',methods=['GET'])
def candidates():
    try:
        filter_args = request.args.to_dict()
        jsonCandidates=[]

        #TODO Расчитываю, что пагинация в дефолте будет page-1 limits-10
        candidates = Candidate.query.order_by(Candidate.id).limit(int(filter_args['limit'])).offset((int(filter_args['page']) - 1) * int(filter_args['limit']))
        
        #     tmp=[]
        #     boof_to_result=[]
        #     candidates=Candidate.query.all()
        #     for candidate in candidates:
        #         tmp.append(Candidate.object_as_dict(candidate))
            
        #         for one in tmp:
        #             if request.args.get('education') != None and one['education'] == request.args.get('education'):
        #                 boof_to_result.append(one)
        #             if request.args.get('speciality') != None and one['speciality'] == request.args.get('speciality'):
        #                 boof_to_result.append(one)

                #TODO -  допилить сортировку
            # tmp=[]
            # candidates=Candidate.query.all()
            # for candidate in candidates:
            #     tmp.append(Candidate.object_as_dict(candidate))
            
            # for t in tmp:
            #     if filter_args['education'] != None:
            #         if t['education'] == filter_args['education']:
            #             jsonCandidates.append(t)
            #         else:
            #             continue
            #     if filter_args['speciality'] != None:
            #         if t['speciality'] == filter_args['speciality']:
            #             jsonCandidates.append(t)
            #         else: 
            #             continue
        #         if age_lte != None and age_gte != None:
        #             if int(age_gte) < int(t['age']) < int(age_lte) and t not in jsonCandidates:
        #                 jsonCandidates.append(t)
        #             else:
        #                 continue
        #         if age_lte != None:
        #             if int(t['age']) < int(age_lte) and t not in jsonCandidates:
        #                 jsonCandidates.append(t)
        #             else:
        #                 continue
        #         if age_gte != None:
        #             if int(t['age']) > int(age_gte) and t not in jsonCandidates:
        #                 jsonCandidates.append(t)
        #             else:
        #                 continue
        #         if experience_lte != None and experience_gte != None:
        #             if int(experience_gte) < int(t['experience']) < int(experience_lte) and t not in jsonCandidates:
        #                 jsonCandidates.append(t)
        #             else:
        #                 continue
        #         if experience_lte != None:
        #             if int(t['experience']) < int(experience_lte) and t not in jsonCandidates:
        #                 jsonCandidates.append(t)
        #             else:
        #                 continue
        #         if experience_gte != None:
        #             if int(t['experience']) > int(experience_gte) and t not in jsonCandidates:
        #                 jsonCandidates.append(t)
        #             else:
        #                 continue
            #TODO исключение повторяющихся объектов json       
            #jsonCandidates=[dict(s) for s in set(frozenset(d.items()) for d in boof_to_result)]
        for candidate in candidates:
            jsonCandidates.append(Candidate.object_as_dict(candidate))

        return jsonify(jsonCandidates)  
    except ValueError as e:
        print(e)
        return abort(500)