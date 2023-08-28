from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from datetime import date

# Create your views here.

def index(request):
    return render(request,'index.html')

def all_logins(request):
    return render(request,'all_logins.html')

def donor_login(request):
    if request.method=='POST':
        u=request.POST['emailid']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            error="no"
        else:
            error="yes"
    return render(request,'donor_login.html',locals())

def donor_home(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    return render(request,'donor_home.html')

def Logout(request):
    logout(request)
    return redirect('index')

def donate_now(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user=request.user
    donor=Donor.objects.get(user=user)
    if request.method=="POST":
        donationname= request.POST['donationname']
        donationpic=request.FILES['donationpic']
        collectionloc=request.POST['collectionloc']
        description=request.POST['description']
        try:
            Donation.objects.create(donor=donor,donationname=donationname,donationpic=donationpic,collectionloc=collectionloc,description=description,stat="pending")
            error = "no"
        except:
            error = "yes"
    return render(request,'donate_now.html',locals())

def admin_login(request):
    if request.method=='POST':
        u=request.POST['username']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    return render(request,'admin_login.html',locals())

def donor_reg(request):
    error=""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        contact = request.POST['contact']
        pwd = request.POST['pwd']
        userpic = request.FILES['userpic']
        address = request.POST['address']

        try:
            user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            Donor.objects.create(user=user,contact=contact,userpic=userpic,address=address)
            error="no"
        except:
            error="yes"

    return render(request,'donor_reg.html',locals())

def donation_history(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user=request.user
    donor=Donor.objects.get(user=user)
    donation=Donation.objects.filter(donor=donor)
    return render(request,'donation_history.html',locals())

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')

def pending_donation(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation=Donation.objects.filter(stat="pending")
    return render(request,'pending_donation.html',locals())


def view_donationdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation=Donation.objects.get(id=pid)
    if request.method == "POST":
        stat=request.POST['status']
        adminremark=request.POST['adminremark']
        try:
            donation.adminremark=adminremark
            donation.stat=stat
            donation.updationdate=date.today()
            donation.save()
            error="no"
        except:
            error="yes"

    return render(request,'view_donationdetail.html',locals())

def accepted_donation(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation=Donation.objects.filter(stat = 'Accept')
    return render(request,'accepted_donation.html',locals())

def add_area(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if request.method == "POST":
        areaname=request.POST['areaname']
        description=request.POST['description']
        try:
            DonationArea.objects.create(areaname=areaname,description=description)
            error="no"
        except:
            error="yes"

    return render(request,'add_area.html',locals())


def manage_area(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    area=DonationArea.objects.all()
    return render(request,'manage_area.html',locals())

def donor_detail(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donor = Donor.objects.all()
    return render(request,'donor_detail.html',locals())

def view_donordetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donor = Donor.objects.get(id=pid)
    return render(request,'view_donordetail.html',locals())
    
def delete_donor(request,pid):
    User.objects.get(id=pid).delete()
    return redirect('donor_detail')

def volunteer_reg(request):
    error=""
    if request.method == "POST":
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        em=request.POST['email']
        contact=request.POST['contact']
        pwd=request.POST['pwd']
        userpic=request.FILES['userpic']
        picid=request.FILES['picid']
        address=request.POST['address']
        aboutme=request.POST['aboutme']
        try:
            user=User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            Volunteer.objects.create(user=user,contact=contact,address=address,userpic=userpic,picid=picid,aboutme=aboutme,stat="pending")
            error="no"
        except:
            error="yes"
    return render(request,'volunteer_reg.html',locals())

def volunteer_home(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    return render(request,'volunteer_home.html')

def volunteer_login(request):
    if request.method == "POST":
        u=request.POST['emailid']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        if user:
            try:
                user1= Volunteer.objects.get(user=user)
                if user1.stat != "pending":
                    login(request,user)
                    error="no"
                else:
                    error="not"
            except:
                error="yes"
    return render(request,'volunteer_login.html',locals())

def new_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.filter(stat="pending")
    return render(request,'new_volunteer.html',locals())

def view_volunteerdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer=Volunteer.objects.get(id=pid)
    if request.method == "POST":
        stat=request.POST['status']
        adminremark=request.POST['adminremark']
        try:
            volunteer.adminremark=adminremark
            volunteer.stat=stat
            volunteer.updationdate=date.today()
            volunteer.save()
            error="no"
        except:
            error="yes"

    return render(request,'view_volunteerdetail.html',locals())


def accepted_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer = Volunteer.objects.filter(stat="Accept")
    return render(request,'accepted_volunteer.html',locals())

def rejected_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer=Volunteer.objects.filter(stat="Reject")
    return render(request,'rejected_volunteer.html',locals())

def all_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    volunteer=Volunteer.objects.all()
    return render(request,'all_volunteer.html',locals())

def delete_volunteer(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    Volunteer.objects.get(id=pid).delete()
    return redirect('all_volunteer')



def accepted_donationdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation=Donation.objects.get(id=pid)
    donationarea=DonationArea.objects.all()
    volunteer=Volunteer.objects.all()
    if request.method == "POST":
        donationareaid=request.POST['donationareaid']
        volunteerid=request.POST['volunteerid']
        da=DonationArea.objects.get(id=donationareaid)
        v=Volunteer.objects.get(id=volunteerid)
        try:
            donation.donationarea=da
            donation.volunteer=v
            donation.stat="Volunteer Allocated"
            donation.updationdate=date.today()
            donation.save()
            error="no"
        except:
            error="yes"

    return render(request,'accepted_donationdetail.html',locals())

def collection_reg(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user=request.user
    volunteer=Volunteer.objects.get(user=user)
    donation=Donation.objects.filter(volunteer=volunteer,stat="Volunteer Allocated")
    return render(request,'collection_reg.html',locals())

def donationcollection_detail(request,pid):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    donation=Donation.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        statu=request.POST['statu']
        volunteerremark=request.POST['volunteerremark']
        try:
            donation.stat=statu
            donation.volunteerremark=volunteerremark
            donation.updationdate=date.today()
            donation.save()
            error="no"
        except:
            error="yes"

    return render(request,'donationcollection_detail.html',locals())

def donationrec_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user=request.user
    volunteer=Volunteer.objects.get(user=user)
    donation=Donation.objects.filter(volunteer=volunteer,stat="Donation Received")
    return render(request,'donationrec_volunteer.html',locals())

def donationrec_detail(request,pid):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    donation=Donation.objects.get(id=pid)
    error=""
    if request.method == "POST":
        statu=request.POST['statu']
        deliverypic=request.FILES['DeliveryPic']

        try:
            donation.stat=statu
            donation.deliverypic=deliverypic
            donation.updatedate=date.today()
            donation.save()
            error="no"
        except:
            error="yes"
    return render(request,'donationrec_detail.html',locals())

def donationnotrec_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user=request.user
    volunteer=Volunteer.objects.get(user=user)
    donation=Donation.objects.filter(volunteer=volunteer,stat="Donation NotReceived")
    return render(request,'donationnotrec_volunteer.html',locals())

def donation_delivered(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user=request.user
    volunteer=Volunteer.objects.get(user=user)
    donation=Donation.objects.filter(volunteer=volunteer,stat="Donation Delivered Successfully")
    return render(request,'donation_delivered.html',locals())

def all_donation(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation=Donation.objects.filter(stat="Donation Delivered Successfully")
    return render(request,'all_donation.html',locals())

def donationrec_detailadmin(request,pid):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    donation=Donation.objects.get(id=pid)
    error=""
    if request.method == "POST":
        statu=request.POST['statu']
        deliverypic=request.FILES['DeliveryPic']

        try:
            donation.stat=statu
            donation.deliverypic=deliverypic
            donation.updatedate=date.today()
            donation.save()
            error="no"
        except:
            error="yes"
    return render(request,'donationrec_detailadmin.html',locals())

def profile_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user=request.user
    volunteer=Volunteer.objects.get(user=user)
    error=""
    if request.method == "POST":
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        contact=request.POST['contact']
        address=request.POST['address']
        aboutme=request.POST['aboutme']
        volunteer.user.first_name=fn
        volunteer.user.last_name=ln
        volunteer.contact=contact
        volunteer.address=address
        volunteer.aboutme=aboutme
        try:
            volunteer.save()
            volunteer.user.save()
            error="no"
        except:
            error="yes"

        try:
            userpic=request.FILES['userpic']
            volunteer.userpic=userpic
            volunteer.save()
            error="no"
        except:
            pass

        try:
            picid=request.FILES['picid']
            volunteer.picid=picid
            volunteer.save()
            error="no"
        except:
            pass
    
        
    return render(request,'profile_volunteer.html',locals())

def changepwd_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    user=request.user
    error=""
    if request.method == "POST":
        o=request.POST['currentpassword']
        n=request.POST['newpassword']
        try:
            if user.check_password(o):
                user.set_password(n)
                user.save()
                error="no"
            else:
                error="not"
        except:
            error="yes"


    return render(request,'changepwd_volunteer.html',locals())

def donation_update(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donation=Donation.objects.all()
    return render(request,'donation_update.html',locals())


def donor_historyupdate(request,pid):
    if not request.user.is_authenticated:
        return redirect('volunteer_login')
    donation=Donation.objects.get(id=pid)
    return render(request,'donor_historyupdate.html',locals())

def changepwd_donor(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user=request.user
    error=""
    if request.method == "POST":
        o = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            if user.check_password(o):
                user.set_password(n)
                user.save()
                error="no"
            else:
                error="not"
        except:
            error="yes" 
    return render(request,'changepwd_donor.html',locals())

def profile_donor(request):
    if not request.user.is_authenticated:
        return redirect('profile_donor')
    user=request.user
    donor=Donor.objects.get(user=user)
    error=""
    if request.method == "POST":
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        contact=request.POST['contact']
        address=request.POST['address']
        donor.user.first_name=fn
        donor.user.last_name=ln
        donor.contact=contact
        donor.address=address
        try:
            donor.save()
            donor.user.save()
            error="no"
        except:
            error="yes"
    return render(request,'profile_donor.html',locals())








    


    



    