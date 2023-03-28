from flask import (
    render_template,
    request,
    jsonify,
    abort
)   

from sqlalchemy import func

import openai
openai.api_key = "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"

from zipfile import ZipFile
import os,re
from datetime import date,datetime 

from server import app
from server.models import db,Candidate,Frontend,Backend,Android,QA,Go,Java

from server.utils.candidate import (
    xml_parser,
    json_parser,
    yml_parser,
    sum_value_common
)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/files_upload',methods=['POST'])
def upload():
    try:
        if request.method == 'POST':
            if request.files == None:
                return abort(404)
            else:
                main_archive=request.files['files']
                path="../static/files/{}".format(date.today())+'_{}-{}-{}'.format(datetime.today().hour,datetime.today().minute,datetime.today().second)
                jsonCandidates=[]
                with ZipFile(main_archive,'r') as zips:
                    for name_zip in zips.namelist():
                        os.mkdir(path+'-'+name_zip.strip('.zip'))
                        with ZipFile(zips.extract(name_zip),'r') as current_zip:
                                current_zip.extractall(path+'-'+name_zip.strip('.zip'))
                                os.remove('./{}'.format(name_zip))
                    for dir_name in os.listdir(os.path.abspath('/static/files/')):
                        for file_name in os.listdir('/static/files/{}'.format(dir_name)):
                            if '.png' not in file_name and '.jpg' not in file_name and '.jpeg' not in file_name:
                                with open(f'/static/files/{dir_name}/{file_name}','r',encoding='cp1251') as form:
                                    if '.xml' in file_name:
                                        candidate_data=xml_parser(form,dir_name)
                                        jsonCandidates.append(candidate_data)
                                    elif '.yml' in file_name or '.yaml' in file_name:
                                        candidate_data=yml_parser(form,dir_name)
                                        jsonCandidates.append(candidate_data)
                                    elif '.json' in file_name:
                                        candidate_data=json_parser(form,dir_name)
                                        jsonCandidates.append(candidate_data)
                return jsonify(jsonCandidates)
    except ValueError as err:
        print(err)
        return abort(500)

@app.route('/compare_candidates',methods=['POST'])
def compare_candidates():
    try:
        ids=list(map(int,request.json['candidatesIds']))
        task=request.json['comparisonPurpose']        

        for candidate_id in ids:
            candidate=Candidate.query.filter_by(id=1).first()
            points_skills = sum_value_common(candidate.id)
            
            request_gpt_chat='''
                        I have 6 main skills: 'Frontend Developer', 'Backend Developer', 'Android Developer', 'QA Engineer', 'Go Developer', 'Java Developer'.
                        I also have a task that needs to be solved: {} Arrange the coefficients for skills from 0.5 to 3
                    '''.format(task)
        
            response_gpt_chat=openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": request_gpt_chat}]
            ).choices[0]['message']['content']
            
            key_words=['Frontend Developer','Backend Developer','Android Developer','QA Engineer','Go Developer','Java Developer']

            pattern = r'(?<!\d)(?<!\d\.)\d{1,2}(?:\.\d{1,2})?(?!\.?\d)'
            coefficients=list(map(float,(re.findall(pattern, response_gpt_chat, re.ASCII))))

            points_skills[key_words[0]]*=coefficients[0]
            points_skills[key_words[1]]*=coefficients[1]
            points_skills[key_words[2]]*=coefficients[2]
            points_skills[key_words[3]]*=coefficients[3]
            points_skills[key_words[4]]*=coefficients[4]
            points_skills[key_words[5]]*=coefficients[5]

            total_score=0
            for key in points_skills:
                total_score+=points_skills[key]
            
            total_score/=len(points_skills)

            ##################### Генерация кэфа по специальности и хобби ##########################
            request_gpt_chat='''
                    Evaluate how the specialty {} coincides with the hobby {} on a 3-point scale. In the answer, give only a number
                '''.format(candidate.speciality,candidate.hobby)

            response_gpt_chat=openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": request_gpt_chat}]
                ).choices[0]['message']['content']

            item=re.findall('(\d+)',response_gpt_chat)
            candidate.hobbySpecialityOverlap=float(item[0])
            total_score*=float(item[0])

            ######################### Генерация кэфа по вузу ####################################     
            military_university={
                    'ВАС':1.5,'КВВУ':2.5,'ВУРЭ':2,'ВУ МО':3,'ВМА':4,'ВКА им.А.Ф.Можайского':5,'ВВС':1
            }
            # TODO Если вуз военный, то выборка из списка выше.
            if military_university.get(candidate.education) != None:
                total_score*=military_university[candidate.education]
            else:
                #TODO балл вузу?
                request_gpt_chat='''
                        Evaluate the university {} in terms of the quality of education in technical specialties on a 3-point scale. In the answer, give only a number
                    '''.format(candidate.education)

                response_gpt_chat=openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": request_gpt_chat}]
                    ).choices[0]['message']['content']
                
                item=re.findall('(\d+)',response_gpt_chat)                
                total_score*=float(item[0])

            candidate.average_score=total_score/6
            db.session.commit()
        
        jsonCandidates=[]
        candidates=db.session.query(Candidate).filter(Candidate.id.in_(ids)).all()
        front_obj = {
            'subject':'Frontend Developer',
            'candidatesScores':{},
            'fullMark':10
        }
        back_obj = {
            'subject':'Backend Developer',
            'candidatesScores':{},
            'fullMark':10
        }
        android_obj = {
            'subject':'Android Developer',
            'candidatesScores':{},
            'fullMark':10
        }
        qa_obj = {
            'subject':'QA Engineer',
            'candidatesScores':{},
            'fullMark':10
        }
        go_obj = {
            'subject':'Go Developer',
            'candidatesScores':{},
            'fullMark':10
        }
        java_obj = {
            'subject':'Java Developer',
            'candidatesScores':{},
            'fullMark':10
        }

        for candidate in candidates:
            points=sum_value_common(candidate.id)
            
            print('очки для розы',points)
            
            name='{}'.format(candidate.lastname)
            #TODO поправить подсчет очков
            front_obj['candidatesScores'].update({
                name:points['Frontend Developer']
            })
            back_obj['candidatesScores'].update({
                name:points['Backend Developer']
            })
            android_obj['candidatesScores'].update({
                name:points['Android Developer']
            })
            qa_obj['candidatesScores'].update({
                name:points['QA Engineer']
            })
            go_obj['candidatesScores'].update({
                name:points['Go Developer']
            })
            java_obj['candidatesScores'].update({
                name:points['Java Developer']
            })

        jsonCandidates.append(front_obj)
        jsonCandidates.append(back_obj)
        jsonCandidates.append(android_obj)
        jsonCandidates.append(qa_obj)
        jsonCandidates.append(go_obj)
        jsonCandidates.append(java_obj)
        
        print('РЕЗУЛЬТАТ',jsonCandidates)

        overlap = {
            'Иванов': 1.2,
            'Корчак': 1.4,
            'Петров': 1.9,
        }
        
        return jsonify(radarDiagram=jsonCandidates, barsDiagram='', hobbyOverlap=overlap)
        #return jsonify(ok=1)
    except ValueError as e:
        print(e)
        return abort(500)
    

