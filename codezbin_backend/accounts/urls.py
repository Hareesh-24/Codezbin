from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
     path('personal/edit/', views.edit_personal_view, name='edit_personal'),

    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('personal/', views.personal_details_view, name='personal_details'),

    # Static pages
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms_conditions, name='terms_conditions'),
    path('certificates/', views.certificates, name='certificates'),
    path('help/', views.help_center, name='help_center'),
    path('settings/', views.settings, name='settings'),

    # Dashboard grid pages
    path('courses/', views.course_dashboard, name='courses'),
    path('career/', views.career_guide, name='career'),
    path('mentorship/', views.mentorship, name='mentorship'),
    path('videos/', views.video_tutorials, name='videos'),
    path('books/', views.books, name='books'),
    path('editor/', views.text_editor, name='editor'),
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
    path('python-course/', views.python_course, name='python_course'),
    path('editor/', views.text_editor, name='text_editor'),
    path('run-code/', views.run_code, name='run_code'),

]
