"""DonationToHelp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from donation.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('all_logins/',all_logins,name='all_logins'),
    path('donor_login/',donor_login,name='donor_login'),
    path('volunteer_login/',volunteer_login,name='volunteer_login'),
    path('admin_login/',admin_login,name='admin_login'),
    path('donor_reg/',donor_reg,name='donor_reg'),
    path('donor_home/',donor_home,name='donor_home'),
    path('logout/',Logout,name="logout"),
    path('donate_now/',donate_now,name="donate_now"),
    path('donation_history/',donation_history,name="donation_history"),
    path('admin_home',admin_home,name='admin_home'),
    path('pending_donation',pending_donation,name='pending_donation'),
    path('view_donationdetail/<int:pid>',view_donationdetail,name="view_donationdetail"),
    path('accepted_donation',accepted_donation,name='accepted_donation'),
    path('add_area',add_area,name="add_area"),
    path('manage_area',manage_area,name="manage_area"),
    path('donor_detail',donor_detail,name="donor_detail"),
    path('view_donordetail/<int:pid>',view_donordetail,name="view_donordetail"),
    path('delete_donor/<int:pid>',delete_donor,name="delete_donor"),
    path('volunteer_reg/',volunteer_reg,name="volunteer_reg"),
    path('volunteer_home/',volunteer_home,name='volunteer_home'),
    path('new_volunteer/',new_volunteer,name="new_volunteer"),
    path('view_volunteerdetail/<int:pid>',view_volunteerdetail,name="view_volunteerdetail"),
    path('accepted_volunteer',accepted_volunteer,name="accepted_volunteer"),
    path('rejected_volunteer',rejected_volunteer,name="rejected_volunteer"),
    path('all_volunteer',all_volunteer,name="all_volunteer"),
    path('delete_volunteer/<int:pid>',delete_volunteer,name="delete_volunteer"),
    path('accepted_donationdetail/<int:pid>',accepted_donationdetail,name="accepted_donationdetail"),
    path('collection_reg/',collection_reg,name="collection_reg"),
    path('donationcollection_detail/<int:pid>',donationcollection_detail,name="donationcollection_detail"),
    path('donationrec_volunteer',donationrec_volunteer,name="donationrec_volunteer"),
    path('donationrec_detail/<int:pid>',donationrec_detail,name="donationrec_detail"),
    path('donationnotrec_volunteer',donationnotrec_volunteer,name="donationnotrec_volunteer"),
    path('donation_delivered',donation_delivered,name="donation_delivered"),
    path('all_donation',all_donation,name="all_donation"),
    path('donationrec_detailadmin/<int:pid>',donationrec_detailadmin,name="donationrec_detailadmin"),
    path('profile_volunteer',profile_volunteer,name="profile_volunteer"),
    path('changepwd_volunteer',changepwd_volunteer,name="changepwd_volunteer"),
    path('donation_update',donation_update,name="donation_update"),
    path('donor_historyupdate/<int:pid>',donor_historyupdate,name="donor_historyupdate"),
    path('changepwd_donor',changepwd_donor,name="changepwd_donor"),
    path('profile_donor',profile_donor,name="profile_donor"),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)