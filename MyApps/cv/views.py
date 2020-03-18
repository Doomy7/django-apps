from django.shortcuts import render
from django.http import HttpResponseRedirect, FileResponse
from .models import cvModel
import io
from fpdf import FPDF
# Create your views here.
def index(request):
    return render(request, 'cv/index.html')

def addCV(request):
    fname = request.POST.get('fname')
    sname = request.POST.get('sname')
    phone = request.POST.get('phone')
    edu = request.POST.get('edu')
    languages = ""
    eng = request.POST.get('eng')
    if eng is not None : languages+=eng
    jap = request.POST.get('jap')
    if jap is not None: languages += jap
    gre = request.POST.get('gre')
    if gre is not None: languages += gre
    desc = request.POST.get('desc')
    new_item = cvModel(fname=fname, sname=sname, phone=phone, education=edu, languages=languages, details=desc)
    new_item.save()
    return HttpResponseRedirect('../../')

def newCV(request):
    return render(request, 'cv/newCV.html')

def viewCVs(request):
    cvs = cvModel.objects.all()
    cv_list = []
    for cv in cvs:
        cv_in_list = str(cv).split(' ')
        fname=cv_in_list[0]
        sname=cv_in_list[1]
        phone=cv_in_list[2]
        edu=cv_in_list[3]
        lang=cv_in_list[4]
        det = ' '.join(cv_in_list[5:])
        cv_list.append({'id': cv.id, 'fname':fname, 'sname':sname, 'phone':phone, 'edu':edu, 'lang':lang, 'det':det})
    return render(request, 'cv/viewCVs.html', {'cv_list': cv_list})

#get the city id and delete from saved locations
def deleteCV(request, cv_id):
    delCV = cvModel.objects.get(pk=cv_id)
    delCV.delete()
    return HttpResponseRedirect('../')

def printCV(request, cv_id):
    cv = cvModel.objects.get(pk=cv_id)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt="MY CV",ln=1)
    pdf.cell(200, 10, txt="name:{}".format(cv.fname), ln=2)
    pdf.cell(200, 10, txt="surname:{}".format(cv.sname),ln=3)
    pdf.cell(200, 10, txt="phone:{}".format(cv.phone),ln=4)
    pdf.cell(200, 10, txt="education:{}".format(cv.education),ln=5)
    pdf.cell(200, 10, txt="languages:{}".format(cv.languages),ln=6)
    pdf.cell(200, 10, txt="description:{}".format(cv.details),ln=7)
    pdf.output("myCV.pdf")
    return HttpResponseRedirect('../../')