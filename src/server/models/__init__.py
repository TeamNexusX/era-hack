from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy import inspect

db = SQLAlchemy()
class Management(db.Model):
    __tablename__ = 'managements'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def object_as_dict(obj):
        return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

    def __repr__(self):
        return '<Management %m>' % self.username
class Candidate(db.Model):
    __tablename__ = 'candidates'

    id = db.Column(db.Integer(), primary_key=True)
    #TODO Уникальная почта
    email = db.Column(db.String(), nullable=False)
    firstname = db.Column(db.String(), nullable=False)
    middlename = db.Column(db.String(), nullable=False)
    lastname = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    education = db.Column(db.String(), nullable=True)
    speciality = db.Column(db.String(), nullable=True)
    experience = db.Column(db.String(), nullable=True)
    hobby = db.Column(db.String(), nullable=False)
    hobby_speciality_overlap = db.Column(db.Integer(), nullable=True, default=0)
    average_score = db.Column(db.Float(), nullable=False, default=0.0)
    img = db.Column(db.String(), nullable=False)

    frontend = relationship('Frontend', backref='candidate', uselist=False)
    backend = relationship('Backend', backref='candidate', uselist=False)
    java = relationship('Java', backref='candidate', uselist=False)
    go = relationship('Go', backref='candidate', uselist=False)
    android = relationship('Android', backref='candidate', uselist=False)
    qa = relationship('QA', backref='candidate', uselist=False)

    def object_as_dict(obj):
        return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

    def __init__(self, email, firstname, middlename, lastname, age, speciality, experience, education, hobby, average_scrore, img):
        self.email = email
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.age = age
        self.speciality = speciality
        self.experience = experience
        self.education = education
        self.average_score = average_scrore
        self.hobby = hobby
        self.img = img
class Frontend(db.Model):
    __tablename__ = 'frontend'

    id = db.Column(db.Integer(), primary_key=True)
    candidate_id = db.Column(db.Integer(), ForeignKey('candidates.id'))
    
    html = db.Column(db.Integer(), nullable=False, default=0)
    css = db.Column(db.Integer(), nullable=False, default=0)
    java_scrpit = db.Column(db.Integer(), nullable=False, default=0)
    usage_on_git = db.Column(db.Integer(), nullable=False, default=0)
    packet_managers = db.Column(db.Integer(), nullable=False, default=0)
    build_tools = db.Column(db.Integer(), nullable=False, default=0)
    css_frameworks = db.Column(db.Integer(), nullable=False, default=0)

    def object_as_dict(obj):
        return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

    def __init__(self,candidate_id, html, css, java_script, usage_on_git, packet_managers, build_tools, css_frameworks):
        self.candidate_id = candidate_id
        self.html = html
        self.css = css
        self.java_script = java_script
        self.usage_on_git = usage_on_git
        self.packet_managers = packet_managers
        self.build_tools = build_tools
        self.css_frameworks = css_frameworks

    def __repr__(self):
        return '<Owner %o>' % self.candidate_id
class Backend(db.Model):
    __tablename__ = 'backend'

    id = db.Column(db.Integer(), primary_key=True)
    candidate_id = db.Column(db.Integer(), ForeignKey('candidates.id'))

    go = db.Column(db.Integer(), nullable=False, default=0)
    pytnon = db.Column(db.Integer(), nullable=False, default=0)
    usage_on_git = db.Column(db.Integer(),nullable=False,default=0)
    relations_databases = db.Column(db.Integer(), nullable=False, default=0)
    nosql_databases = db.Column(db.Integer(), nullable=False, default=0)
    web_security_knowledge = db.Column(db.Integer(), nullable=False, default=0)

    def object_as_dict(obj):
        return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

    def __init__(self,candidate_id ,go, python, usage_on_git, relations_databases, nosql_databases, web_security_knowledge):
        self.candidate_id = candidate_id
        self.go = go
        self.pytnon = python
        self.usage_on_git = usage_on_git
        self.relations_databases = relations_databases
        self.nosql_databases = nosql_databases
        self.web_security_knowledge = web_security_knowledge

    def __repr__(self):
        return '<Owner %o>' % self.candidate_id
class Java(db.Model):
    __tablename__ = 'java'

    id = db.Column(db.Integer(), primary_key=True)
    candidate_id = db.Column(db.Integer(), ForeignKey('candidates.id'))

    generics = db.Column(db.Integer(),nullable=False,default=0)
    build_tools = db.Column(db.Integer(),nullable=False,default=0)
    web_frameworks = db.Column(db.Integer(),nullable=False,default=0)
    orm = db.Column(db.Integer(),nullable=False,default=0)
    java_jdbc = db.Column(db.Integer(),nullable=False,default=0)
    
    def __init__(self,candidate_id, generics, build_tools, web_frameworks, orm, java_jdbc):
        self.candidate_id = candidate_id
        self.generics = generics
        self.build_tools = build_tools 
        self.web_frameworks = web_frameworks
        self.orm = orm
        self.java_jdbc = java_jdbc

    def object_as_dict(obj):
        return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

    def __repr__(self):
        return '<Owner %o>' % self.candidate_id
class Go(db.Model):
    __tablename__ = 'go'

    id = db.Column(db.Integer(), primary_key=True)
    candidate_id = db.Column(db.Integer(), ForeignKey('candidates.id'))

    build_cli_application = db.Column(db.Integer(),nullable=False,default=0)
    orm = db.Column(db.Integer(),nullable=False,default=0)
    web_frameworks = db.Column(db.Integer(),nullable=False,default=0)
    logging = db.Column(db.Integer(),nullable=False,default=0)
    go_realtime_communication = db.Column(db.Integer(),nullable=False,default=0)
    api_clients = db.Column(db.Integer(),nullable=False,default=0)
    microservices = db.Column(db.Integer(),nullable=False,default=0)

    def __init__(self,candidate_id ,build_cli_application, orm, web_frameworks, logging, go_realtime_communication, api_clients,microservices):
        self.candidate_id = candidate_id
        self.build_cli_application = build_cli_application
        self.orm = orm
        self.web_frameworks = web_frameworks
        self.logging = logging
        self.go_realtime_communication = go_realtime_communication
        self.api_clients = api_clients
        self.microservices = microservices

    def object_as_dict(obj):
        return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

    def __repr__(self):
        return '<Owner %o>' % self.candidate_id
class Android(db.Model):
    __tablename__ = 'android'

    id = db.Column(db.Integer(), primary_key=True)
    candidate_id = db.Column(db.Integer(), ForeignKey('candidates.id'))

    kotlin = db.Column(db.Integer(),nullable=False,default=0) 
    usage_of_git = db.Column(db.Integer(),nullable=False,default=0) 
    components_and_their_usage = db.Column(db.Integer(),nullable=False,default=0)
    application_building = db.Column(db.Integer(),nullable=False,default=0)
    testing = db.Column(db.Integer(),nullable=False,default=0)
    security = db.Column(db.Integer(),nullable=False,default=0)

    def __init__(self,candidate_id ,kotlin,usage_of_git,components_and_their_usage,app_build,test,security):
        self.candidate_id = candidate_id
        self.kotlin = kotlin
        self.usage_of_git = usage_of_git
        self.components_and_their_usage = components_and_their_usage
        self.application_building = app_build
        self.testing = test 
        self.security = security

    def object_as_dict(obj):
        return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

    def __repr__(self):
        return '<Owner %o>' % self.candidate_id
    
class QA(db.Model):
    __tablename__ = 'qa'

    id = db.Column(db.Integer(), primary_key=True)
    candidate_id = db.Column(db.Integer(), ForeignKey('candidates.id'))

    qa_engineer = db.Column(db.Integer(),nullable=False,default=0)
    project_management = db.Column(db.Integer(),nullable=False,default=0)
    sd_lc = db.Column(db.Integer(),nullable=False,default=0) 
    qa_manual_testing = db.Column(db.Integer(),nullable=False,default=0)
    automated_testing = db.Column(db.Integer(),nullable=False,default=0)
    non_functional_testing = db.Column(db.Integer(),nullable=False,default=0)
    ci_cd = db.Column(db.Integer(),nullable=False,default=0)

    def __init__(self,candidate_id,qa_eng,prj_man,sd_lc,qa_man_test,auto_test,non_func_test,ci_cd):
        self.candidate_id = candidate_id
        self.qa_engineer = qa_eng
        self.project_management = prj_man
        self.sd_lc = sd_lc
        self.qa_manual_testing = qa_man_test
        self.automated_testing = auto_test
        self.non_functional_testing = non_func_test
        self.ci_cd = ci_cd

    def object_as_dict(obj):
        return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

    def __repr__(self):
        return '<Owner %o>' % self.candidate_id