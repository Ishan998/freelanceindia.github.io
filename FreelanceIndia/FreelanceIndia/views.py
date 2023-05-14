import sqlite3
import re
from django.contrib import messages
from django.http import request
from django.shortcuts import render,redirect
import aadhar

try:
    con=sqlite3.connect("hex01.db")
    mark=con.cursor()
    command='''create table if not jobs('taskname char(120)','tasktype char(30)','messagetodev (1000)')'''
    mark.execute(command)
except:
    print("unable to connect database")

class client:
    # def addproject(request,taskname,tasktype,message):
    #     tname=taskname
    #     ttype=tasktype
    #     msg=message
    #     query="""insert into jobs(taskname,tasktype,messagetodev) values (?,?,?)"""
    #     format=(tname,ttype,msg)
    #     con.execute(query,format)
    #     return render(request,"addproject.html")
    def auth(request):
        return render(request, "auth.html")
    def register(request):
        return render(request, "register.html")
    def registercheck(request):
        first_name=request.POST.get('fname')
        Last_name = request.POST.get('lname')
        Username = request.POST.get('uname')
        email = request.POST.get('email')
        passd = request.POST.get('password')
        passdr= request.POST.get('rpassword')
        state= request.POST.get('sname')
        city= request.POST.get('cname')
        pincode=request.POST.get('pcode')
        Adhar_number=request.POST.get('anumber')

        params={'fname':first_name,'lname':Last_name,'uname':Username,'email':email,'passd1':passd,'passd2':passdr,'state':state,'city':city,'pincode':pincode,'anumber':Adhar_number}
        if passd != passdr:
            message='password not matched'
            messages.error(request,message)

            return render(request,'register.html',params)
        else:
            regex = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
            p = re.compile(regex)
            if (pincode == ''):
                message="pincode is blank"
                messages.error(request, message)

                return render(request,'register.html',params)
            else:
                m = re.match(p, pincode)

                if m is None:
                    message="Invalid Pincode"
                    messages.error(request, message)

                    return render(request,'register.html',params)
                else:
                    ref=aadhar.validate(Adhar_number)
                    if ref=='Invalid Aadhar Number':
                        messages.error(request,ref)
                        return render(request, 'register.html', params)
                    else:
                        return redirect("/")





    def cldash(request):
        return render(request, "clientdash.html")

    def addproject(request):
        taskname=request.POST.get("taskname")
        tasktype = request.POST.get("categories")
        messsage = request.POST.get("message")
        print(taskname)
        print(tasktype)
        print(messsage)
        if taskname and tasktype and messsage is not None:
            print("data collected")
            return render(request,"clientdash.html")
        else:
            print("data not collected")
            return render(request,"addproject.html")
    def showjob(request):
        return render(request, "jobabout.html")

