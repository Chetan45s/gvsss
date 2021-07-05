from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",RedirectView.as_view(url="index")),
    path("index/", views.index, name="index"),
    path("about/", views.intro, name="about"),
    path("faq/", views.faqq, name="faq"),
    path("gallery/", views.galleryphotos, name="gallery"),
    path("staff/", views.members, name="staff"),
    path("pastevents/", views.pastevents, name="pastevents"),
    path("upcomingevents/", views.upevents, name="upcomingevents"),
    path("guidelines/", views.guidelines, name="guidelines"),
    path("announcements/", views.announcements, name="announcements"),
    path("contact/", views.contacts, name="Contact"),

    path("login/", views.login_page, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", LogoutView.as_view(), name='logout'),

    path("student/", views.student, name="student"),
    path("studentdetails/", views.studentdetails, name="studentdetails"),
    path("editdetails_student/", views.student_editform, name="student_editform"),

    path("teacher/", views.teacher, name="teacher"),
    path("teacherdetails/", views.teacherdetails, name="teacherdetails"),
    path("editdetails/", views.teacher_editform, name="editform"),

    path("allteachers/", views.allteachers, name="allteachers"),
    path("teacherprofile/", views.teacherprofile, name="teacherprofile"),
    path("student/subjects/", views.subjects, name="subjects"),
    path("teacher/liveclass/", views.liveclass, name="liveclass"),

]