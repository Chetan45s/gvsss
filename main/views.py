from django.shortcuts import render,redirect
from datetime import datetime
from .forms import RegisterForm, LoginForm,StudentForm, TeacherForm, ClassLinkForm
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, get_user_model
from django.utils.http import is_safe_url
from django.contrib.auth.decorators import login_required

today = datetime.today()
# Create your views here.
def index(request):
    introduction = about.objects.all()
    faq1 = faq.objects.all()
    direct = director.objects.all()
    announce = announcement.objects.all()
    eve = event.objects.filter(eventdate__gte=today)
    photos = gallery.objects.all()
    guide = guideline.objects.all()
    slider = img_slider.objects.all()
    context = { 'introduction': introduction,'faq1': faq1,'announce': announce, 'eve': eve, 'photos': photos,   'guide': guide,'direct':direct,'slider': slider }
    return render(request, 'index.html', context)

def intro(request):
    introduction = about.objects.all()
    context = { 'introduction': introduction }
    return render(request, 'about.html', context)

def faqq(request):
    faq1 = faq.objects.all()
    context = { 'faq1': faq1 }
    return render(request, 'faq.html', context)

def galleryphotos(request):
    photos = gallery.objects.all()
    context = { 'photos': photos }
    return render(request, 'gallery.html', context)

def members(request):
    member = staff.objects.all()
    direct = director.objects.all()
    context = { 'member': member, 'direct' : direct }
    return render(request, 'staff.html', context)


def pastevents(request):
    today = datetime.today()
    even = event.objects.filter(eventdate__lt=today)
    context = { 'even': even }
    return render(request, 'pastevents.html', context)

def upevents(request):
    today = datetime.today()
    eve = event.objects.filter(eventdate__gte=today)
    context = { 'eve': eve }
    return render(request, 'upevents.html', context)

def guidelines(request):
    guide = guideline.objects.all()
    context = { 'guide': guide }
    return render(request, 'guidelines.html', context)

def announcements(request):
    announce = announcement.objects.all()
    context = { 'announce': announce }
    return render(request, 'announcements.html', context)

def contacts(request):
    thanks = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        feedback1 = feedback(name=name, email=email, subject=subject, message=message)
        feedback1.save()
        thanks = True
    return render(request, 'contact.html', {'thanks': thanks})





@login_required(login_url='/login/')
def student(request):
    return render(request, 'student/studentdash.html')

@login_required(login_url='/login/')
def studentdetails(request):
    if Student.objects.filter(user=request.user).exists():
        obj = Student.objects.get(user=request.user)
    else:
        obj = None
    context = {
        'obj':obj,
    }
    return render(request, 'student/student-details.html',context)
@login_required(login_url='/login/')
def student_editform(request):
    

    if request.method == "POST":
        studentform = StudentForm(request.POST,request.FILES or None)

        if studentform.is_valid():

            first_name = studentform.cleaned_data.get("first_name")
            last_name = studentform.cleaned_data.get("last_name")
            roll_no = studentform.cleaned_data.get("roll_no")
            gender = studentform.cleaned_data.get("gender")
            date_of_birth = studentform.cleaned_data.get("date_of_birth")
            phone = studentform.cleaned_data.get("phone")
            address = studentform.cleaned_data.get("address")
            father_name = studentform.cleaned_data.get("father_name")
            mother_name = studentform.cleaned_data.get("mother_name")
            class_name = studentform.cleaned_data.get("class_name")
            # profile_pic = studentform.cleaned_data.get("profile_pic")
            bio = studentform.cleaned_data.get("bio")

            qs = Student.objects.filter(user=request.user)

            if qs.exists():
                qs.update(first_name=first_name,
                        last_name=last_name,
                        roll_no=roll_no,
                        gender = gender,
                        date_of_birth = date_of_birth,
                        phone = phone,
                        address = address,
                        father_name = father_name,
                        mother_name = mother_name,
                        class_name = class_name,
                        # profile_pic = profile_pic,
                        bio = bio
                )

            else:
                Student.objects.create(user=request.user,
                        first_name=first_name,
                        last_name=last_name,
                        roll_no=roll_no,
                        gender = gender,
                        date_of_birth = date_of_birth,
                        phone = phone,
                        address = address,
                        father_name = father_name,
                        mother_name = mother_name,
                        class_name = class_name,
                        # profile_pic = profile_pic,
                        bio = bio
                )
            return redirect("studentdetails")
    else:
        studentform = StudentForm()
        if Student.objects.filter(user=request.user).exists():
            obj = Student.objects.get(user=request.user)
        else:
            obj = None
    context = {
        "studentform": studentform,
        "obj":obj,
    }
    return render(request, "student/editform.html",context)

@login_required(login_url='/login/')
def teacher(request):
    return render(request, 'teacher/teacherdash.html')
@login_required(login_url='/login/')
def teacherdetails(request):
    if Teacher.objects.filter(user=request.user).exists():
        obj = Teacher.objects.get(user=request.user)
    else:
        obj = None
    context = {
        "obj": obj,
    }
       
    return render(request, 'teacher/teacher-details.html',context)
@login_required(login_url='/login/')
def teacher_editform(request):
    if request.method == "POST":
        teacherform = TeacherForm(request.POST,request.FILES or None)

        if teacherform.is_valid():

            first_name = teacherform.cleaned_data.get("first_name")
            last_name = teacherform.cleaned_data.get("last_name")
            gender = teacherform.cleaned_data.get("gender")
            phone = teacherform.cleaned_data.get("phone")
            class_name = teacherform.cleaned_data.get("class_name")

            qs = Teacher.objects.filter(user=request.user)

            if qs.exists():
                qs.update(first_name=first_name,
                        last_name=last_name,
                        gender = gender,
                        phone = phone,
                        class_name = class_name,
                )

            else:
                Teacher.objects.create(user=request.user,
                        first_name=first_name,
                        last_name=last_name,
                        gender = gender,
                        phone = phone,
                        class_name = class_name,
                )
            return redirect("teacherdetails")
    else:
        teacherform = TeacherForm()
        if Teacher.objects.filter(user=request.user).exists():
            obj = Teacher.objects.get(user=request.user)
        else:
            obj = None
    context = {
        "teacherform": teacherform,
        "obj":obj,
    }

    return render(request, 'teacher/teachereditform.html',context)


##### Dont touch

User = get_user_model()
def signup(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        # username  = form.cleaned_data.get("username")
        email  = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")
        new_user  = User.objects.create_user(email, password)
        print(new_user)
        return redirect("/")

    return render(request, "signup.html", context)



def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        print(form)
        email  = form.cleaned_data.get("email")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)

            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print("Error")
    return render(request, "login.html", context)

@login_required(login_url='/login/')
def allteachers(request):

    obj = User.objects.all()

    context = {
        "obj":obj,
    }
    return render(request, 'student/all-teacher.html',context)
@login_required(login_url='/login/')
def teacherprofile(request):
    return render(request, 'student/teacherprofile.html')

@login_required(login_url='/login/')
def liveclass(request):

    if request.method == "POST":
        form = ClassLinkForm(request.POST)

        if form.is_valid():

            date_and_time = form.cleaned_data.get("date_and_time")
            topic = form.cleaned_data.get("topic")
            link = form.cleaned_data.get("link")
            class_name = form.cleaned_data.get("class_name")
            subject = form.cleaned_data.get("subject")

            ClassLink.objects.create(user=request.user,date_and_time=date_and_time,
                        topic=topic,
                        subject = subject,
                        link = link,
                        class_name = class_name,
                )
            return redirect("liveclass")
    else:
        form = ClassLinkForm()
    context = {
        "form": form,
    }


    return render(request, 'teacher/liveclass.html',context)
@login_required(login_url='login/')
def subjects(request):

    curr_stud = Student.objects.filter(user=request.user.id)[0]
    obj = ClassLink.objects.filter(class_name=curr_stud.class_name)


    context = {
        "obj":obj,
    }

    return render(request,'student/mysubjects.html',context)
