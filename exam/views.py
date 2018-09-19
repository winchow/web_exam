from django.contrib.auth.models import User
from django.template.loader import get_template
from django.db import DatabaseError, transaction
from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse
from exam.models import Lac,Subject
from django.views.generic.list import ListView
import json
import ast
import io
import xlwt
from .form import NameForm
import pandas as pd
import math
from django.contrib.auth.decorators import login_required
import requests
from django.contrib.auth.signals import user_logged_in

from django.shortcuts import redirect

@login_required
# def social_auth(sender, user, request, **kwargs):
def social_auth(request):
    user = request.user
    ROLE = {
        'STUDENT': '1',
        'STAFF' : '2',
        'INSTRUCTOR' : '3',
    }

    print(type(user),user)
    prov = user.social_auth.filter(provider='tu')

    if prov.exists():
        data    = prov[0].extra_data
        headers = {
            "Authorization": "Bearer {}".format(data['access_token'])
        }
        api  = requests.get('https://api.tu.ac.th/api/me/', headers=headers).json()
        try:
            if api['role'] == ROLE['STUDENT']:
                print("API : ", api)
                print("api['username'] :", api['username'])
                print("api['role'] :", api['role'])
                index   = User.objects.all().filter(username = api['username'])[0]
                ckRole  =  api['role']
            elif api['role'] == ROLE['STAFF']:
                ckRole = '2' 
            else:
                ckRole = '3' 
        except KeyError  as e:
                return redirect('/logout')
  

    return ckRole

def jo(request):
	data ='static/scidb_staff.json'
	with open(data, 'r', encoding="utf-8") as fp:
		data = json.load(fp)
		#print(data)
		print(type(data[1]))
		print(data[1])
		for d in data:
			print(d)
			with transaction.atomic():
				Lac.objects.update_or_create(**d)
		# for i in len(data):
			# o = Lac.objects.update_or_create(data)
		return HttpResponse("Success")

def LacListView(request):
    check = social_auth(request)
    thing_list = list(Lac.objects.all().values_list('name',flat=True))
    return render(request, 'form2.html', {'thing_list':thing_list,'check':check})

def saved(request):
    print(request.POST)
    section = request.POST.get("section", "")
    sub_id = request.POST.get("sub_id", "")
    academic_year = request.POST.get("academic_year", "")
    
    TotalStu1 = request.POST.get("TotalStu1", "")
    amount = 1
    myInput1 = request.POST.get("myInput1", "")
    myInput2 = request.POST.get("myInput2", "")
    if myInput2 != "":
        amount = 2
    myInput3 = request.POST.get("myInput3", "")
    if myInput3 != "":
        amount = 3
    myInput4 = request.POST.get("myInput4", "")
    if myInput4 != "":
        amount = 4
    myInput5 = request.POST.get("myInput5", "")
    if myInput5 != "":
        amount = 5
    myInput6 = request.POST.get("myInput6", "")
    if myInput6 != "":
        amount = 6
    myInput7 = request.POST.get("myInput7", "")
    if myInput7 != "":
        amount = 7
    myInput8 = request.POST.get("myInput8", "")
    if myInput8 != "":
        amount = 8
    myInput9 = request.POST.get("myInput9", "")
    if myInput9 != "":
        amount = 9
    myInput10 = request.POST.get("myInput10", "")
    if myInput10 != "":
        amount = 10
    myInput11 = request.POST.get("myInput11", "")
    if myInput11 != "":
        amount = 11
    myInput12 = request.POST.get("myInput12", "")
    if myInput12 != "":
        amount = 12
    myInput13 = request.POST.get("myInput13", "")
    if myInput13 != "":
        amount = 13
    myInput14 = request.POST.get("myInput14", "")
    if myInput14 != "":
        amount = 14
    myInput15 = request.POST.get("myInput15", "")
    if myInput15 != "":
        amount = 15                                    
    ################################################
    myInput1 = request.POST.get("myInput1", "")
    print("***********************************************************")
    print(myInput1)
    myInput2 = request.POST.get("myInput2", "")
    print("***********************************************************")
    print(myInput2)
    myInput3 = request.POST.get("myInput3", "")
    print(myInput3)
    myInput4 = request.POST.get("myInput4", "")
    print(myInput4)
    myInput5 = request.POST.get("myInput5", "")
    myInput6 = request.POST.get("myInput6", "")
    myInput7 = request.POST.get("myInput7", "")
    myInput8 = request.POST.get("myInput8", "")
    myInput9 = request.POST.get("myInput9", "")
    myInput10 = request.POST.get("myInput10", "")
    myInput11 = request.POST.get("myInput11", "")
    myInput12 = request.POST.get("myInput12", "")
    myInput13 = request.POST.get("myInput13", "")
    myInput14 = request.POST.get("myInput14", "")
    myInput15 = request.POST.get("myInput15", "")
    ################################################
    ratio1 = request.POST.get("ratio1", "")
    ratio2 = request.POST.get("ratio2", "")
    ratio3 = request.POST.get("ratio3", "")
    ratio4 = request.POST.get("ratio4", "")
    ratio5 = request.POST.get("ratio5", "")
    ratio6 = request.POST.get("ratio6", "")
    ratio7 = request.POST.get("ratio7", "")
    ratio8 = request.POST.get("ratio8", "")
    ratio9 = request.POST.get("ratio9", "")
    ratio10 = request.POST.get("ratio10", "")
    ratio11 = request.POST.get("ratio11", "")
    ratio12 = request.POST.get("ratio12", "")   
    ratio13 = request.POST.get("ratio13", "")
    ratio14 = request.POST.get("ratio14", "")
    ratio15 = request.POST.get("ratio15", "")
    ################################################
    sid = request.POST.get("sid", "")
    radio = request.POST.get("radio", "")

    test_type = request.POST.get("test_type", "")
    instructor_type = request.POST.get("instructor_type", "")
    Degree = request.POST.get("radio", "")
    student = request.POST.get("TotalStu1", "")
    if instructor_type == '0':
        s_type = 'เป็นวิชาสอนท่านเดียว'
    pss = 'su'
    print("************************************************************************************")
    print()
    print(ratio1)
   
    if test_type == '0' and Degree == '0': ##4bht/hour          
        pss='จำนวน น.ศ.'+str(student)+' คน อ.สอนร่วม '+str(amount)+' คน('+str(student)+'*3*4 =' +str(int(student)*3*4)+')'
    elif test_type == '0' and (Degree == '1' or Degree == '2'): ##6bht/hour                     
        pss='จำนวน น.ศ.'+str(student)+' คน อ.สอนร่วม '+str(amount)+' คน('+str(student)+'*3*6 =' +str(int(student)*3*6)+')'

    elif test_type == '1' and Degree == '0': ##1bht/hour                     
        pss='จำนวน น.ศ.'+str(student)+' คน อ.สอนร่วม '+str(amount)+' คน('+str(student)+'*3*1 =' +str(int(student)*3*1)+')'
    elif test_type == '1' and  (Degree == '1' or Degree == '2'): ##1.5bht/hour                 
        pss='จำนวน น.ศ.'+str(student)+' คน อ.สอนร่วม '+str(amount)+' คน('+str(student)+'*3*1.5 ='+str(int(student)*3*1.5)+')'

    elif test_type == '2' and Degree == '0': ##2bht/hour                       
        pss='จำนวน น.ศ.'+str(student)+' คน อ.สอนร่วม '+str(amount)+' คน('+str(student)+'*3*2 =' +str(int(student)*3*2)+')'

    elif test_type == '2' and  (Degree == '1' or Degree == '2'): ##3bht/hour           
        pss='จำนวน น.ศ.'+str(student)+' คน อ.สอนร่วม '+str(amount)+' คน('+str(student)+'*3*3 =' +str(int(student)*3*3)+')'

    elif test_type == '3' and Degree == '0': ##2bht/hour               
        pss='จำนวน น.ศ.'+str(student)+' คน อ.สอนร่วม '+str(amount)+' คน('+str(student)+'*3*2 =' +str(int(student)*3*2)+')'

    elif test_type == '3' and  (Degree == '1' or Degree == '2'): ##2bht/hour      
        pss='จำนวน น.ศ.'+str(student)+' คน อ.สอนร่วม '+str(amount)+' คน('+str(student)+'*3*2 =' +str(int(student)*3*2)+')'

    if amount >= 1:
        if instructor_type != '0':
            s_type = 'เป็นวิชาสอนหลายท่าน ท่านที่ 1 ใน '+ str(amount)+' ท่าน'
        instru1_object = Subject.objects.create(examiner=myInput1,Sid=sid,student=TotalStu1,ratio=float(ratio1),T_type=test_type,S_type=s_type,\
        Degree=radio,yeasr=academic_year,amount=amount,Section=section,ps=pss)
    if amount >= 2:
        if instructor_type != '0':
            s_type = 'เป็นวิชาสอนหลายท่าน ท่านที่ 2 ใน '+ str(amount)+' ท่าน'
        instru2_object = Subject.objects.create(examiner=myInput2,Sid=sid,student=TotalStu1,ratio=float(ratio2),T_type=test_type,S_type=s_type,\
        Degree=radio,yeasr=academic_year,amount=amount,Section=section,ps=pss)
    if amount >= 3:
        if instructor_type != '0':
            s_type = 'เป็นวิชาสอนหลายท่าน ท่านที่ 3 ใน '+ str(amount)+' ท่าน'
        instru3_object = Subject.objects.create(examiner=myInput3,Sid=sid,student=TotalStu1,ratio=float(ratio3),T_type=test_type,S_type=s_type,\
        Degree=radio,yeasr=academic_year,amount=amount,Section=section,ps=pss)
    if amount >= 4:
        if instructor_type != '0':
            s_type = 'เป็นวิชาสอนหลายท่าน ท่านที่ 4 ใน '+ str(amount)+' ท่าน'
        instru4_object = Subject.objects.create(examiner=myInput4,Sid=sid,student=TotalStu1,ratio=float(ratio4),T_type=test_type,S_type=s_type,\
        Degree=radio,yeasr=academic_year,amount=amount,Section=section,ps=pss)
    if amount >= 5:
        if instructor_type != '0':
            s_type = 'เป็นวิชาสอนหลายท่าน ท่านที่ 5 ใน '+ str(amount)+' ท่าน'
        instru5_object = Subject.objects.create(examiner=myInput5,Sid=sid,student=TotalStu1,ratio=float(ratio5),T_type=test_type,S_type=s_type,\
        Degree=radio,yeasr=academic_year,amount=amount,Section=section,ps=pss)
    if amount >= 6:
        if instructor_type != '0':
            s_type = 'เป็นวิชาสอนหลายท่าน ท่านที่ 6 ใน '+ str(amount)+' ท่าน'
        instru6_object = Subject.objects.create(examiner=myInput6,Sid=sid,student=TotalStu1,ratio=float(ratio6),T_type=test_type,S_type=s_type,\
        Degree=radio,yeasr=academic_year,amount=amount,Section=section,ps=pss)
    if amount >= 7:
        if instructor_type != '0':
            s_type = 'เป็นวิชาสอนหลายท่าน ท่านที่ 7 ใน '+ str(amount)+' ท่าน'
        instru7_object = Subject.objects.create(examiner=myInput7,Sid=sid,student=TotalStu1,ratio=float(ratio7),T_type=test_type,S_type=s_type,\
        Degree=radio,yeasr=academic_year,amount=amount,Section=section,ps=pss)
    if amount >= 8:
        if instructor_type != '0':
            s_type = 'เป็นวิชาสอนหลายท่าน ท่านที่ 8 ใน '+ str(amount)+' ท่าน'
        instru8_object = Subject.objects.create(examiner=myInput8,Sid=sid,student=TotalStu1,ratio=float(ratio8),T_type=test_type,S_type=s_type,\
        Degree=radio,yeasr=academic_year,amount=amount,Section=section,ps=pss)
    if amount >= 9:
        if instructor_type != '0':
            s_type = 'เป็นวิชาสอนหลายท่าน ท่านที่ 9 ใน '+ str(amount)+' ท่าน'
        instru9_object = Subject.objects.create(examiner=myInput9,Sid=sid,student=TotalStu1,ratio=float(ratio9),T_type=test_type,S_type=s_type,\
        Degree=radio,yeasr=academic_year,amount=amount,Section=section,ps=pss)
    if amount >= 10:
        if instructor_type != '0':
            s_type = 'เป็นวิชาสอนหลายท่าน ท่านที่ 10 ใน '+ str(amount)+' ท่าน'
        instru10_object = Subject.objects.create(examiner=myInput10,Sid=sid,student=TotalStu1,ratio=float(ratio10),T_type=test_type,S_type=s_type,\
        Degree=radio,yeasr=academic_year,amount=amount,Section=section,ps=pss)
    if amount >= 11:
        if instructor_type != '0':
            s_type = 'เป็นวิชาสอนหลายท่าน ท่านที่ 11 ใน '+ str(amount)+' ท่าน'
        instru11_object = Subject.objects.create(examiner=myInput11,Sid=sid,student=TotalStu1,ratio=float(ratio11),T_type=test_type,S_type=s_type,\
        Degree=radio,yeasr=academic_year,amount=amount,Section=section,ps=pss)
    if amount >= 12:
        if instructor_type != '0':
            s_type = 'เป็นวิชาสอนหลายท่าน ท่านที่ 12 ใน '+ str(amount)+' ท่าน'
        instru12_object = Subject.objects.create(examiner=myInput12,Sid=sid,student=TotalStu1,ratio=float(ratio12),T_type=test_type,S_type=s_type,\
        Degree=radio,yeasr=academic_year,amount=amount,Section=section,ps=pss)
    if amount >= 13:
        if instructor_type != '0':
            s_type = 'เป็นวิชาสอนหลายท่าน ท่านที่ 13 ใน '+ str(amount)+' ท่าน'
        instru13_object = Subject.objects.create(examiner=myInput13,Sid=sid,student=TotalStu1,ratio=float(ratio13),T_type=test_type,S_type=s_type,\
        Degree=radio,yeasr=academic_year,amount=amount,Section=section,ps=pss)
    if amount >= 14:
        if instructor_type != '0':
            s_type = 'เป็นวิชาสอนหลายท่าน ท่านที่ 14 ใน '+ str(amount)+' ท่าน'
        instru14_object = Subject.objects.create(examiner=myInput14,Sid=sid,student=TotalStu1,ratio=float(ratio14),T_type=test_type,S_type=s_type,\
        Degree=radio,yeasr=academic_year,amount=amount,Section=section,ps=pss)
    if amount == 15:
        if instructor_type != '0':
            s_type = 'เป็นวิชาสอนหลายท่าน ท่านที่ 15 ใน '+ str(amount)+' ท่าน'
        instru15_object = Subject.objects.create(examiner=myInput15,Sid=sid,student=TotalStu1,ratio=float(ratio15),T_type=test_type,S_type=s_type,\
        Degree=radio,yeasr=academic_year,amount=amount,Section=section,ps=pss)

    thing_list = Subject.objects.order_by().values_list('yeasr',flat=True).distinct()
    thing_list2 = Subject.objects.order_by().values_list('Section',flat=True).distinct()
    return render(request, 'dw.html', {'thing_list':thing_list,'thing_list2':thing_list2})

def download(request):

    return render(request,'dw.html')

def SubjectListView(request):
    thing_list = Subject.objects.order_by().values_list('yeasr',flat=True).distinct()
    thing_list2 = Subject.objects.order_by().values_list('Section',flat=True).distinct()
    return render(request, 'dw.html', {'thing_list':thing_list,'thing_list2':thing_list2})

def export(request):

    a = request.POST.get("academic_year")
    aa = request.POST.get("section")
    amount = 1
    myInput1 = request.POST.get("myInput1", "")
    myInput2 = request.POST.get("myInput2", "")
    print(myInput2)

    if myInput2 != "":
        amount = 2
    myInput3 = request.POST.get("myInput3", "")
    if myInput3 != "":
        amount = 3
    myInput4 = request.POST.get("myInput4", "")
    if myInput4 != "":
        amount = 4
    myInput5 = request.POST.get("myInput5", "")
    if myInput5 != "":
        amount = 5
    myInput6 = request.POST.get("myInput6", "")
    if myInput6 != "":
        amount = 6
    myInput7 = request.POST.get("myInput7", "")
    if myInput7 != "":
        amount = 7
    myInput8 = request.POST.get("myInput8", "")
    if myInput8 != "":
        amount = 8
    myInput9 = request.POST.get("myInput9", "")
    if myInput9 != "":
        amount = 9
    myInput10 = request.POST.get("myInput10", "")
    if myInput10 != "":
        amount = 10
    myInput11 = request.POST.get("myInput11", "")
    if myInput11 != "":
        amount = 11
    myInput12 = request.POST.get("myInput12", "")
    if myInput12 != "":
        amount = 12
    myInput13 = request.POST.get("myInput13", "")
    if myInput13 != "":
        amount = 13
    myInput14 = request.POST.get("myInput14", "")
    if myInput14 != "":
        amount = 14
    myInput15 = request.POST.get("myInput15", "")
    if myInput15 != "":
        amount = 15     
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        print('**************************45')
        a = request.POST.get("academic_year")
        aa = request.POST.get("section")
        subj = ''
        if aa == '0':
            subj = 'Chem'
        elif aa == '1':
            subj = 'Textiles'
        elif aa == '2':
            subj = 'Physic'
        elif aa == '3':
            subj = 'Rural_technology'
        elif aa == '4':
            subj = 'Biotechnology'
        elif aa == '5':
            subj = 'Agricultural_Technology'
        elif aa == '6':
            subj = 'Math'
        elif aa == '7':
            subj = 'Com-Sci'
        elif aa == '8':
            subj = 'Environmental_Science'
        elif aa == '9':
            subj = 'Food_Science'


        b = 'attachment; filename='+ a +"__"+ subj+".xls"
        print(a +"Test:"+ aa)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print('**************************51')
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        print('**************************51')

    #return render(request, 'name.html', {'form': form})
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = b

    #searchWord = request.POST.get('year','')
  
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('ค่าตรวจข้อสอบ',cell_overwrite_ok=True)
    

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['ชื่อผู้ตรวจข้อสอบ','อัตราส่วนในการตรวจ','จำนวนนักศึกษาที่เข้าสอบ','วิชา','ประเภทข้อสอบ','ประเภทการสอน','ระดับ','ปีการศึกษา','จำนวนเงิน บาท','สาขา','หมายเหตุ']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows

    font_style = xlwt.XFStyle()
    rows = Subject.objects.all().values_list('examiner','ratio','student','Sid','T_type','S_type','Degree','yeasr','amount','Section','ps')
    rows = rows.order_by('Sid')
    
    #num = 0
    #money = {()}
    #for row2 in rows:
    #    if row2[4] == '0' and row2[5] == '0' and row2[6] == '0':
    #        money = money + {(str(float(row2[1])*15 ),)
    #rows = rows + money
    ws.col(0).width = int(13*600)
    ws.col(1).width = int(13*400)
    ws.col(2).width = int(13*450)
    ws.col(4).width = int(13*350)
    ws.col(5).width = int(13*500)
    ws.col(7).width = int(13*200)
    ws.col(8).width = int(13*350)
    ws.col(9).width = int(13*350)
    
    for row in rows:
        if(row[7] == a ):
          if( row[9]==aa):
            row_num += 1
            for col_num in range(len(row)):
                if col_num == 4 :
                    if row[4] == '0':
                        ws.write(row_num, col_num, 'อัตนัย', font_style)
                    elif row[4] == '1':
                        ws.write(row_num, col_num, 'ปรนัย', font_style)
                    elif row[4] == '2' : 
                        ws.write(row_num, col_num, 'อัตนัย+ปรนัย',font_style)
                    else:
                        ws.write(row_num, col_num, 'สัมภาษณ์ + ปฏิบัติ', font_style)
                elif col_num == 6:
                    if row[6] == '0':
                       ws.write(row_num, col_num, 'ป.ตรี', font_style)
                    elif row[6] == '1':
                       ws.write(row_num, col_num, 'ป.โท', font_style) 
                    else:
                        ws.write(row_num, col_num, 'ป.เอก', font_style) 
                elif col_num == 7:
                    ws.write(row_num, col_num, row[col_num], font_style)
                elif col_num == 8:
                    
                    if row[4] == '0' and row[6] == '0': ##4bht/hour          
                            ws.write(row_num,col_num,int(((row[2]*3*4)*float(row[1]))/100),font_style)
                            print(float(row[1]))
                    elif row[4] == '0' and (row[6] == '1' or row[6] == '2'): ##6bht/hour                     
                            ws.write(row_num,col_num,int(((row[2]*3*6)*float(row[1]))/100),font_style)

                    elif row[4] == '1' and row[6] == '0': ##1bht/hour                     
                            ws.write(row_num,col_num,int(((row[2]*3*1)*float(row[1]))/100),font_style)

                    elif row[4] == '1' and  (row[6] == '1' or row[6] == '2'): ##1.5bht/hour                 
                            ws.write(row_num,col_num,int(((row[2]*3*1.5)*float(row[1]))/100),font_style)

                    elif row[4] == '2' and row[6] == '0': ##2bht/hour                       
                            ws.write(row_num,col_num,int(((row[2]*3*2)*float(row[1]))/100),font_style)

                    elif row[4] == '2' and  (row[6] == '1' or row[6] == '2'): ##3bht/hour           
                            ws.write(row_num,col_num,int(((row[2]*3*3)*float(row[1]))/100),font_style)

                    elif row[4] == '3' and row[6] == '0': ##2bht/hour               
                            ws.write(row_num,col_num,int(((row[2]*2)*float(row[1]))/100),font_style)

                    elif row[4] == '3' and  (row[6] == '1' or row[6] == '2'): ##2bht/hour      
                            ws.write(row_num,col_num,int(((row[2]*2)*float(row[1]))/100),font_style)
                elif col_num == 9:
                    
                    if row[9] == '0':
                        ws.write(row_num, col_num, 'เคมี', font_style)
                    elif row[9] == '1':
                        ws.write(row_num, col_num, 'สิ่งทอ', font_style)
                    elif row[9] == '2':
                        ws.write(row_num, col_num, 'ฟิสิกส์', font_style)
                    elif row[9] == '3':
                        ws.write(row_num, col_num, 'เทคโนโลยีชนบท', font_style)
                    elif row[9] == '4':
                        ws.write(row_num, col_num, 'เทคโนโลยีชีวภาพ', font_style)
                    elif row[9] == '5':
                        ws.write(row_num, col_num, 'เทคโนโลยีการเกษตร', font_style)
                    elif row[9] == '6':
                        ws.write(row_num, col_num, 'คณิตศาสตร์และสถิติ', font_style)
                    elif row[9] == '7':
                        ws.write(row_num, col_num, 'วิทยาการคอมพิวเตอร์', font_style)
                    elif row[9] == '8':
                        ws.write(row_num, col_num, 'วิทยาศาสตร์สิ่งแวดล้อม', font_style)
                    elif row[9] == '9':
                        ws.write(row_num, col_num, 'วิทยาศาสตร์และเทคโนโลยีอาหาร', font_style)


                # elif col_num == 10:
                    # if amount!=1:
                        # if row[4] == '0' and row[6] == '0': ##4bht/hour          
                        #         ws.write(row_num,col_num,'จำนวน น.ศ.'+str(row[2])+' คน อ.สอนร่วม '+str(Subject.amount)+' คน('+str(row[2])+'*3*4 =' +str(row[2]*3*4)+')',font_style)
                        # elif row[4] == '0' and (row[6] == '1' or row[6] == '2'): ##6bht/hour                     
                        #         ws.write(row_num,col_num,'จำนวน น.ศ.'+str(row[2])+' คน อ.สอนร่วม '+str(Subject.amount)+' คน('+str(row[2])+'*3*6 =' +str(row[2]*3*6)+')',font_style)

                        # elif row[4] == '1' and row[6] == '0': ##1bht/hour                     
                        #         ws.write(row_num,col_num,'จำนวน น.ศ.'+str(row[2])+' คน อ.สอนร่วม '+str(Subject.amount)+' คน('+str(row[2])+'*3*1 =' +str(row[2]*3*1)+')',font_style)

                        # elif row[4] == '1' and  (row[6] == '1' or row[6] == '2'): ##1.5bht/hour                 
                        #         ws.write(row_num,col_num,'จำนวน น.ศ.'+str(row[2])+' คน อ.สอนร่วม '+str(Subject.amount)+' คน('+str(row[2])+'*3*1.5 ='+str(row[2]*3*1.5)+')',font_style)

                        # elif row[4] == '2' and row[6] == '0': ##2bht/hour                       
                        #         ws.write(row_num,col_num,'จำนวน น.ศ.'+str(row[2])+' คน อ.สอนร่วม '+str(Subject.amount)+' คน('+str(row[2])+'*3*2 =' +str(row[2]*3*2)+')',font_style)

                        # elif row[4] == '2' and  (row[6] == '1' or row[6] == '2'): ##3bht/hour           
                        #         ws.write(row_num,col_num,'จำนวน น.ศ.'+str(row[2])+' คน อ.สอนร่วม '+str(Subject.amount)+' คน('+str(row[2])+'*3*3 =' +str(row[2]*3*3)+')',font_style)

                        # elif row[4] == '3' and row[6] == '0': ##2bht/hour               
                        #         ws.write(row_num,col_num,'จำนวน น.ศ.'+str(row[2])+' คน อ.สอนร่วม '+str(Subject.amount)+' คน('+str(row[2])+'*3*2 =' +str(row[2]*3*2)+')',font_style)

                        # elif row[4] == '3' and  (row[6] == '1' or row[6] == '2'): ##2bht/hour      
                        #         ws.write(row_num,col_num,'จำนวน น.ศ.'+str(row[2])+' คน อ.สอนร่วม '+str(Subject.amount)+' คน('+str(row[2])+'*3*2 =' +str(row[2]*3*2)+')',font_style)
                        # else :
                        #         ws.write(row_num, col_num, str(row[col_num]), font_style)
                    # else :
                    #     ws.write(row_num, col_num, str(row[col_num]), font_style)


                else :
                    ws.write(row_num, col_num, row[col_num], font_style)
        
    wb.save(response)

    return response
    template_name='dw.html'
