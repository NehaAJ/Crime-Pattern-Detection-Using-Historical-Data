from django.urls import path
from .import views
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('registerip/',views.registerip,name="registerip"),
    path('registersp/',views.registersp,name="registersp"),
    path('registerdgp/',views.registerdgp,name="registerdgp"),
    path('afterlogin',views.afterlogin_view,name='afterlogin'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('home/',views.home,name='home'),
    path('logout',views.logout_request,name='logout'),
    path('profile/',views.prof,name='profile'),
    path('profileip/',views.prof1,name='profileip'),
    path('profilesp/',views.prof2,name='profilesp'),
    path('profiledgp/',views.prof3,name='profiledgp'),
    path('homeip/',views.homeip,name="homeip"),
    path('homesp/',views.homesp,name="homesp"),
    path('homedgp/',views.homedgp,name="homedgp"),
    path('fir/',views.Fir,name="fir"),
    path('firip/',views.Fir1,name="firip"),
    path('firsp/',views.Fir2,name="firsp"),
    path('firdgp/',views.Fir3,name="firdgp"),
    path('tourprogram/',views.TourProgram,name="tourprogram"),
    path('gallery/',views.Gallery,name="gallery"),
    path('weeklydiary/',views.WeeklyDiary,name="weeklydiary"),
    path('firform/',views.firform,name="firform"),
    path('pastrec/',views.PastRecords,name="pastrec"),
    path('medrec/',views.MedicalRecords_view,name="medrec"),
    path('asdut/',views.AssignDuties,name="asdut"),
    path('view_fir/', views.view_fir, name="view_fir"),
    path('user_list/', views.user_list, name="user_list"),
    path('weekly-calendar/', views.weekly_calendar, name='weekly_calendar'),
    path('add_diary/', views.add_diary, name='add_diary'),
    path('userMap/', views.userMap, name="userMap"),
    path('tour_planner/', views.tour_planner, name="tour_planner"),
    path('grievence/', views.grievence, name="grievence"),
    path('view_grievence/', views.view_grievence, name="view_grievence"),
    path('successration/',views.successration,name="successration"),
    path('visitor/', views.Visitors, name="visitor"),
    path('firview/', views.Firview, name="firview"),
    path('dutyview/', views.Dutyview, name="Dutyview"),
    path('crime-prediction/', views.Crime_prediction, name="crime-prediction"),
    path('crime-prediction2/', views.Crime_prediction2, name="crime-prediction2"),
    path('achievement_upload/', views.achievement_upload, name="achievement_upload"),
    path('web-scrapping/', views.iframe_view, name='web-scrapping'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
