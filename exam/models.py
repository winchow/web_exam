from django.db import models
import requests
import json
from django.shortcuts import render_to_response
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.core.validators import RegexValidator

# Create your models here.
class Lac(models.Model):
	name=models.CharField(max_length=100)
	job_position=models.CharField(max_length=100)
	department=models.CharField(max_length=100)
	campus=models.CharField(max_length=100)
	type=models.CharField(max_length=100)
	ict_id=models.CharField(max_length=100,null=True,blank=True)
	def __str__(self):
		return "name : {}, job_position : {}, department : {}, campus : {}, type : {}, ict_id : {}".format(self.name,self.job_position,self.department,self.campus,self.type,self.ict_id)
	class Meta:
		ordering = ['id']

class Subject(models.Model):
	SectionT = (
		('0','เคมี'),
		('1','สิ่งทอ'),
		('2','ฟิสิกส์'),
		('3','เทคโนโลยีชนบท'),
		('4','เทคโนโลยีชีวภาพ'),
		('5','เทคโนโลยีการเกษตร'),
		('6','คณิตศาสตร์และสถิติ'),
		('7','วิทยาการคอมพิวเตอร์'),
		('8','วิทยาศาสตร์สิ่งแวดล้อม'),
		('9','วิทยาศาสตร์และเทคโนโลยีอาหาร')
		)
	ExamT = (
		('0','Choice'),
		('1','Short answer'),
		('2','Short answer and Choice'),
		('3','Interview and Practice')
		)
	InstrucT = (
		('0','One Instructor'),
		('1','Multiple Instructor')
		)
	DegreeT = (
		('0','Bachelor'),
		('1','Master'),
		('2','Doctor')
		)
	examiner=models.CharField(max_length = 100,null = False,default = 'foo')
	Section=models.CharField(choices=SectionT,max_length = 1,default = '0')
	Sid=models.CharField(max_length=5,default = 'foo')
	student=models.IntegerField(default='0')
	ratio=models.FloatField(default='0.0000')
	T_type=models.CharField(choices=ExamT,max_length = 1,default = 'Choice')
	S_type=models.CharField(choices=InstrucT,max_length = 1,default = '0')
	Degree=models.CharField(choices=DegreeT,max_length = 1,default = '0')
	yeasr=models.CharField(max_length = 6,null = False,default = '1/25xx')
	amount=models.IntegerField(null = False,default = 1)
	ps=models.CharField(max_length = 100,default = '')
	
	def __str__(self):
		return "examiner : {},Section : {}, Sid : {}, student : {},ratio : {},T_type : {},S_type : {},Degree : {},yeasr : {},amount : {},ps : {}".format(self.examiner,self.Section,self.Sid,self.student,self.ratio,self.T_type,self.S_type,self.Degree,self.yeasr,self.amount,self.ps)
	class Meta:
		ordering = ['examiner']


	
# def logged_in_handle(sender, user, request, **kwargs):
#     ROLE = {
#         'STUDENT': '1',

#     }
#     #
#     # Check if TU login
#     prov = user.social_auth.filter(provider='tu')
#     if prov.exists():
#         data    = prov[0].extra_data
#         headers = {
#             "Authorization": "Bearer {}".format(data['access_token'])
#         }
#         api  = requests.get('https://api.tu.ac.th/api/me/', headers=headers).json()
#         if api['company'] == 'คณะวิทยาศาสตร์และเทคโนโลยี':
#             if api['role'] == ROLE['STUDENT']:
#                 print("API : ", api)
#                 print("api['username'] :", api['username'])
#                 print("api['role'] :", api['role'])
#                 index   = User.objects.all().filter(username = api['username'])[0]
#                 check1 = api['role']

#                 # return render(request, 'form2.html', {'check1':check1})

# user_logged_in.connect(logged_in_handle)
