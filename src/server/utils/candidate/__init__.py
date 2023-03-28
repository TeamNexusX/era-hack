from server.models import Candidate,Frontend,Backend,Go,Java,QA,Android

from server import db

from yaml.loader import SafeLoader
from lxml import etree as LibXMLParser
from io import StringIO
import os,json,yaml,re,xmltodict

def sum_value_one(arr):
    var_sum=0
    for key in arr[0]:
        var_sum+=float(arr[0][key])
    return var_sum/6

def sum_value_common(candidate_id):
    res={}
    tmp=[]
    key_words=['Frontend Developer','Backend Developer','Android Developer','QA Engineer','Go Developer','Java Developer']

    frontend_query=Frontend.query.filter_by(candidate_id=candidate_id).first()
    tmp.append(Frontend.object_as_dict(frontend_query))
    res.update({
        'Frontend Developer':sum_value_one(tmp)
    })
    tmp.clear()

    backend_query=Backend.query.filter_by(candidate_id=candidate_id).first()
    tmp.append(Backend.object_as_dict(backend_query))
    res.update({
        'Backend Developer':sum_value_one(tmp)  
    })
    tmp.clear()

    android_query=Android.query.filter_by(candidate_id=candidate_id).first()
    tmp.append(Android.object_as_dict(android_query))
    res.update({
        'Android Developer':sum_value_one(tmp)
    })
    tmp.clear()

    qa_query=QA.query.filter_by(candidate_id=candidate_id).first()
    tmp.append(QA.object_as_dict(qa_query))
    res.update({
        'QA Engineer':sum_value_one(tmp)
    })
    tmp.clear()

    go_query=Go.query.filter_by(candidate_id=candidate_id).first()
    tmp.append(Go.object_as_dict(go_query))
    res.update({
        'Go Developer':sum_value_one(tmp)
    })
    tmp.clear()

    java_query=Java.query.filter_by(candidate_id=candidate_id).first()
    tmp.append(Java.object_as_dict(java_query))
    res.update({
        'Java Developer':sum_value_one(tmp)
    })
    tmp.clear()

    return res

def check_candidate_in_db(email):
    candidate=Candidate.query.filter_by(email=email).first()
    if candidate:return True
    else:return False

def xml_parser(form,dir_name):
    data_dict=xmltodict.parse(form.read())
    candidate_data=json.dumps(data_dict)
    print(candidate_data)

    # if check_candidate_in_db(candidate_data['email']):
    #     return False

    candidate=Candidate(
        email=candidate_data['email'],
        firstname=candidate_data['firstname'],
        middlename=candidate_data['middlename'],
        lastname=candidate_data['lastname'],
        age=candidate_data['age'],
        education=candidate_data['education'],
        experience=candidate_data['experience'],
        speciality=candidate_data['speciality'],
        average_scrore=candidate_data['average_score'],
        hobby=candidate_data['hobby'],
        img=f'/static/files/{dir_name}/'+candidate_data['img']
    )
    db.session.add(candidate)
    db.session.commit()

    frontend=Frontend(
        candidate_id=candidate.id,
        html=candidate_data['skills']['Frontend Developer']['children']['HTML'],
        java_script=candidate_data['skills']['Frontend Developer']['children']['Javascript'],
        css=candidate_data['skills']['Frontend Developer']['children']['CSS'],
        usage_on_git=candidate_data['skills']['Frontend Developer']['children']['Usage of Git'],
        packet_managers=candidate_data['skills']['Frontend Developer']['children']['Package Managers'],
        build_tools=candidate_data['skills']['Frontend Developer']['children']['Build Tools'],
        css_frameworks=candidate_data['skills']['Frontend Developer']['children']['CSS Frameworks']
    )
    db.session.add(frontend)

    backend=Backend(
        candidate_id=candidate.id,
        go=candidate_data['skills']['Backend Developer']['children']['Go'],
        python=candidate_data['skills']['Backend Developer']['children']['Python'],
        usage_on_git=candidate_data['skills']['Backend Developer']['children']['Usage of Git'],
        relations_databases=candidate_data['skills']['Backend Developer']['children']['Relational Databases'],
        nosql_databases=candidate_data['skills']['Backend Developer']['children']['NoSQL databases'],
        web_security_knowledge=candidate_data['skills']['Backend Developer']['children']['Web Security Knowledge']
    )
    db.session.add(backend)

    android=Android(
        candidate_id=candidate.id,
        kotlin=candidate_data['skills']['Android Developer']['children']['Kotlin'],
        usage_of_git=candidate_data['skills']['Android Developer']['children']['Usage of Git'],
        components_and_their_usage=candidate_data['skills']['Android Developer']['children']['Components and their usage'],
        app_build=candidate_data['skills']['Android Developer']['children']['Application'],
        test=candidate_data['skills']['Android Developer']['children']['Testing'],
        security=candidate_data['skills']['Android Developer']['children']['Security']
    )
    db.session.add(android)

    go=Go(
        candidate_id=candidate.id,
        build_cli_application=candidate_data['skills']['Go Developer']['children']['CLI Applications'],
        orm=candidate_data['skills']['Go Developer']['children']['ORMs'],
        web_frameworks=candidate_data['skills']['Go Developer']['children']['Web Frameworks'],
        logging=candidate_data['skills']['Go Developer']['children']['Logging'],
        go_realtime_communication=candidate_data['skills']['Go Developer']['children']['Go realtime communication'],
        api_clients=candidate_data['skills']['Go Developer']['children']['API Clients'],
        microservices=candidate_data['skills']['Go Developer']['children']['Microservices']
    )
    db.session.add(go)

    java=Java(
        candidate_id=candidate.id,
        generics=candidate_data['skills']['Java Developer']['children']['Generics'],
        build_tools=candidate_data['skills']['Java Developer']['children']['Tools'],
        web_frameworks=candidate_data['skills']['Java Developer']['children']['Web Frameworks'],
        orm=candidate_data['skills']['Java Developer']['children']['ORM'],
        java_jdbc=candidate_data['skills']['Java Developer']['children']['JDBC']
    )
    db.session.add(java)
    
    qa=QA(
        candidate_id=candidate.id,
        qa_eng=candidate_data['skills']['QA Engineer']['children']['QA'],
        prj_man=candidate_data['skills']['QA Engineer']['children']['Project'],
        sd_lc=candidate_data['skills']['QA Engineer']['children']['SDLC'],
        qa_man_test=candidate_data['skills']['QA Engineer']['children']['Manual Testing'],
        auto_test=candidate_data['skills']['QA Engineer']['children']['Automated Testing'],
        non_func_test=candidate_data['skills']['QA Engineer']['children']['Non Functional Testing'],
        ci_cd=candidate_data['skills']['QA Engineer']['children']['CI/CD'],
    )
    db.session.add(qa)

    db.session.commit()

    return candidate_data


def yml_parser(form,dir_name):
    candidate_data=yaml.load(form.read(),Loader=SafeLoader)
    print(candidate_data)
    
    # if check_candidate_in_db(candidate_data['email']):
    #     return False
    
    candidate=Candidate(
        email=candidate_data['email'],
        firstname=candidate_data['firstname'],
        middlename=candidate_data['middlename'],
        lastname=candidate_data['lastname'],
        age=candidate_data['age'],
        education=candidate_data['education'],
        experience=candidate_data['experience'],
        speciality=candidate_data['speciality'],
        average_scrore=candidate_data['average_score'],
        hobby=candidate_data['hobby'],
        img=f'/static/files/{dir_name}/'+candidate_data['img']
    )
    db.session.add(candidate)
    db.session.commit()

    frontend=Frontend(
        candidate_id=candidate.id,
        html=candidate_data['skills']['Frontend Developer']['children']['HTML'],
        java_script=candidate_data['skills']['Frontend Developer']['children']['Javascript'],
        css=candidate_data['skills']['Frontend Developer']['children']['CSS'],
        usage_on_git=candidate_data['skills']['Frontend Developer']['children']['Usage of Git'],
        packet_managers=candidate_data['skills']['Frontend Developer']['children']['Package Managers'],
        build_tools=candidate_data['skills']['Frontend Developer']['children']['Build Tools'],
        css_frameworks=candidate_data['skills']['Frontend Developer']['children']['CSS Frameworks']
    )
    db.session.add(frontend)

    backend=Backend(
        candidate_id=candidate.id,
        go=candidate_data['skills']['Backend Developer']['children']['Go'],
        python=candidate_data['skills']['Backend Developer']['children']['Python'],
        usage_on_git=candidate_data['skills']['Backend Developer']['children']['Usage of Git'],
        relations_databases=candidate_data['skills']['Backend Developer']['children']['Relational Databases'],
        nosql_databases=candidate_data['skills']['Backend Developer']['children']['NoSQL databases'],
        web_security_knowledge=candidate_data['skills']['Backend Developer']['children']['Web Security Knowledge']
    )
    db.session.add(backend)

    android=Android(
        candidate_id=candidate.id,
        kotlin=candidate_data['skills']['Android Developer']['children']['Kotlin'],
        usage_of_git=candidate_data['skills']['Android Developer']['children']['Usage of Git'],
        components_and_their_usage=candidate_data['skills']['Android Developer']['children']['Components and their usage'],
        app_build=candidate_data['skills']['Android Developer']['children']['Application'],
        test=candidate_data['skills']['Android Developer']['children']['Testing'],
        security=candidate_data['skills']['Android Developer']['children']['Security']
    )
    db.session.add(android)

    go=Go(
        candidate_id=candidate.id,
        build_cli_application=candidate_data['skills']['Go Developer']['children']['CLI Applications'],
        orm=candidate_data['skills']['Go Developer']['children']['ORMs'],
        web_frameworks=candidate_data['skills']['Go Developer']['children']['Web Frameworks'],
        logging=candidate_data['skills']['Go Developer']['children']['Logging'],
        go_realtime_communication=candidate_data['skills']['Go Developer']['children']['Go realtime communication'],
        api_clients=candidate_data['skills']['Go Developer']['children']['API Clients'],
        microservices=candidate_data['skills']['Go Developer']['children']['Microservices']
    )
    db.session.add(go)

    java=Java(
        candidate_id=candidate.id,
        generics=candidate_data['skills']['Java Developer']['children']['Generics'],
        build_tools=candidate_data['skills']['Java Developer']['children']['Tools'],
        web_frameworks=candidate_data['skills']['Java Developer']['children']['Web Frameworks'],
        orm=candidate_data['skills']['Java Developer']['children']['ORM'],
        java_jdbc=candidate_data['skills']['Java Developer']['children']['JDBC']
    )
    db.session.add(java)
    
    qa=QA(
        candidate_id=candidate.id,
        qa_eng=candidate_data['skills']['QA Engineer']['children']['QA'],
        prj_man=candidate_data['skills']['QA Engineer']['children']['Project'],
        sd_lc=candidate_data['skills']['QA Engineer']['children']['SDLC'],
        qa_man_test=candidate_data['skills']['QA Engineer']['children']['Manual Testing'],
        auto_test=candidate_data['skills']['QA Engineer']['children']['Automated Testing'],
        non_func_test=candidate_data['skills']['QA Engineer']['children']['Non Functional Testing'],
        ci_cd=candidate_data['skills']['QA Engineer']['children']['CI/CD'],
    )
    db.session.add(qa)

    db.session.commit()

    return candidate_data

def json_parser(form,dir_name):
    candidate_data=json.loads(form.read())
    #TODO проверка на оригинальность анкеты в бд
    # if check_candidate_in_db(candidate_data['email']):
    #     return 0
    print(candidate_data)
    candidate=Candidate(
        email=candidate_data['email'],
        firstname=candidate_data['firstname'],
        middlename=candidate_data['middlename'],
        lastname=candidate_data['lastname'],
        age=candidate_data['age'],
        education=candidate_data['education'],
        experience=candidate_data['experience'],
        speciality=candidate_data['speciality'],
        average_scrore=candidate_data['average_score'],
        hobby=candidate_data['hobby'],
        img=f'/static/files/{dir_name}/'+candidate_data['img']
    )
    db.session.add(candidate)
    db.session.commit()

    frontend=Frontend(
        candidate_id=candidate.id,
        html=candidate_data['skills']['Frontend Developer']['children']['HTML'],
        java_script=candidate_data['skills']['Frontend Developer']['children']['Javascript'],
        css=candidate_data['skills']['Frontend Developer']['children']['CSS'],
        usage_on_git=candidate_data['skills']['Frontend Developer']['children']['Usage of Git'],
        packet_managers=candidate_data['skills']['Frontend Developer']['children']['Package Managers'],
        build_tools=candidate_data['skills']['Frontend Developer']['children']['Build Tools'],
        css_frameworks=candidate_data['skills']['Frontend Developer']['children']['CSS Frameworks']
    )
    db.session.add(frontend)

    backend=Backend(
        candidate_id=candidate.id,
        go=candidate_data['skills']['Backend Developer']['children']['Go'],
        python=candidate_data['skills']['Backend Developer']['children']['Python'],
        usage_on_git=candidate_data['skills']['Backend Developer']['children']['Usage of Git'],
        relations_databases=candidate_data['skills']['Backend Developer']['children']['Relational Databases'],
        nosql_databases=candidate_data['skills']['Backend Developer']['children']['NoSQL databases'],
        web_security_knowledge=candidate_data['skills']['Backend Developer']['children']['Web Security Knowledge']
    )
    db.session.add(backend)

    android=Android(
        candidate_id=candidate.id,
        kotlin=candidate_data['skills']['Android Developer']['children']['Kotlin'],
        usage_of_git=candidate_data['skills']['Android Developer']['children']['Usage of Git'],
        components_and_their_usage=candidate_data['skills']['Android Developer']['children']['Components and their usage'],
        app_build=candidate_data['skills']['Android Developer']['children']['Application'],
        test=candidate_data['skills']['Android Developer']['children']['Testing'],
        security=candidate_data['skills']['Android Developer']['children']['Security']
    )
    db.session.add(android)

    go=Go(
        candidate_id=candidate.id,
        build_cli_application=candidate_data['skills']['Go Developer']['children']['CLI Applications'],
        orm=candidate_data['skills']['Go Developer']['children']['ORMs'],
        web_frameworks=candidate_data['skills']['Go Developer']['children']['Web Frameworks'],
        logging=candidate_data['skills']['Go Developer']['children']['Logging'],
        go_realtime_communication=candidate_data['skills']['Go Developer']['children']['Go realtime communication'],
        api_clients=candidate_data['skills']['Go Developer']['children']['API Clients'],
        microservices=candidate_data['skills']['Go Developer']['children']['Microservices']
    )
    db.session.add(go)

    java=Java(
        candidate_id=candidate.id,
        generics=candidate_data['skills']['Java Developer']['children']['Generics'],
        build_tools=candidate_data['skills']['Java Developer']['children']['Tools'],
        web_frameworks=candidate_data['skills']['Java Developer']['children']['Web Frameworks'],
        orm=candidate_data['skills']['Java Developer']['children']['ORM'],
        java_jdbc=candidate_data['skills']['Java Developer']['children']['JDBC']
    )
    db.session.add(java)
    
    qa=QA(
        candidate_id=candidate.id,
        qa_eng=candidate_data['skills']['QA Engineer']['children']['QA'],
        prj_man=candidate_data['skills']['QA Engineer']['children']['Project'],
        sd_lc=candidate_data['skills']['QA Engineer']['children']['SDLC'],
        qa_man_test=candidate_data['skills']['QA Engineer']['children']['Manual Testing'],
        auto_test=candidate_data['skills']['QA Engineer']['children']['Automated Testing'],
        non_func_test=candidate_data['skills']['QA Engineer']['children']['Non Functional Testing'],
        ci_cd=candidate_data['skills']['QA Engineer']['children']['CI/CD'],
    )
    db.session.add(qa)

    db.session.commit()    

    return candidate_data