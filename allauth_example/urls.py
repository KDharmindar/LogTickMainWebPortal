"""allauth_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Main import views
from dashing.utils import router
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token,\
    refresh_jwt_token



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.profile, name="profile"),
    path('new_project/', views.new_project, name="new_project"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('manage/', views.manage, name="manage"),
    path('screens/', views.screens, name="screens"),
    path('new_task/', views.new_task, name="new_task"),
    path('reports/overview/', views.report_overview, name="report_overview"),
    path('reports/timesheetdetail/', views.report_overview, name="timesheetdetail"),
    path('reports/project/week/timelog', views.report_overview, name="reports_project_week_timelog"),
    path('reports/project/lifetime/timelog/', views.report_overview, name="reports_project_lifetime_timelog"),
    path('reports/week/timesheet/', views.report_overview, name="reports_week_timesheet"),
    path('reports/timelog/', views.report_overview, name="reports_timelog"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    #path('dashboard/',include(router.urls)),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-auth/', include('rest_framework.urls')),
    path('process_data/', views.get_process_data, name='get_process_data')
]
