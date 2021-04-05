from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Sum
from datetime import date
# from verify_email.email_handler import send_verification_email
from django.utils.crypto import get_random_string
from .form import *
from django.core.files.storage import FileSystemStorage

# Create your views here.


def IndexPage(request):
    return render(request, "garbage/index home.html")


def Signup(request):
    return render(request, "garbage/auth/signup.html")


def RegisterData(request):
    # if request.method == "POST":
    role = request.POST['role']
    name = request.POST['name']
    email = request.POST['email']
    passwd = request.POST['pass']
    check = Admin.objects.filter(Email=email)
    if check:
        msg = "*User already Exist"
        return render(request, "garbage/auth/signup.html", {'msg': msg})
    elif role == 'Admin':
        
        subject = "Thanks for Registration"
        msg1 = f"Hello {name}\n Welcome to GoGreen,"
        from_email = settings.EMAIL_HOST_USER
        reception_list = []
        reception_list.append(email)
        send_mail(subject, msg1, from_email, reception_list)
        
        admin = Admin.objects.create(
            Name=name, Email=email, Password=passwd, Role=role)
        admin.save()
        # return render(request,"garbage/admin/admin_index.html")
        msg = "*Registration Successful!/n You can now Login"
        return render(request, "garbage/auth/login.html", {'msg': msg})
        # return redirect('log-in')

    elif role == 'User':

        name = request.POST['name']
        email = request.POST['email']
        passwd = request.POST['pass']
        otp = get_random_string(6, allowed_chars='0123456789')
        admin = Admin.objects.create(
            Name=name, Email=email, Password=passwd, Role=role)
        user = User.objects.create(
            User=admin, Name=name, Email=email, Password=passwd, Role=role, OTP=otp)
        subject = "Thanks for Registration"
        msg1 = f"Hello {name}\n Welcome to GoGreen, Your OTP is: {otp}"
        from_email = settings.EMAIL_HOST_USER
        reception_list = []
        reception_list.append(email)
        send_mail(subject, msg1, from_email, reception_list)

        msg = "*Registration Successful!" + '/n' + "You can now Login"
        return redirect('otp-page')
        # return render(request,"garbage/auth/login.html", {'msg':msg})

    elif role == 'Garbage Collector':

        name = request.POST['name']
        email = request.POST['email']
        passwd = request.POST['pass']
        admin = Admin.objects.create(
            Name=name, Email=email, Password=passwd, Role=role)
        user = GarbageCollector.objects.create(
            GC=admin, Name=name, Email=email, Password=passwd, Role=role)
        subject = "Thanks for Registration"
        msg1 = f"Hello {name}\n Welcome to GoGreen,"
        from_email = settings.EMAIL_HOST_USER
        reception_list = []
        reception_list.append(email)
        send_mail(subject, msg1, from_email, reception_list)
        msg = "*Registration Successful!/n You can now Login"
        return render(request, "garbage/auth/login.html", {'msg': msg})
        # return redirect('log-in')
    else:
        msg = "*User doesn't Exist"
        return render(request, "garbage/auth/signup.html", {'msg': msg})

    # return render(request,"garbage/auth/signup.html")


def OTPPage(request):
    return render(request, "garbage/auth/OTP.html")


def OTPVerify(request):
    if request.method == "POST":
        otp1 = request.POST['otp']
        user = User.objects.all().filter(OTP=otp1)

        if len(user) > 0:
            return redirect('log-in')
        else:
            msg = "Wrong OTP, Try again"

            return render(request, "garbage/auth/OTP.html", {"msg": msg})
    pass


def Login(request):
    return render(request, "garbage/auth/login.html")


def LoginData(request):
    if request.POST['role'] == "Admin":
        email = request.POST['email']
        password = request.POST['password']
        admin = Admin.objects.filter(Email=email)
        if len(admin) > 0:
            if admin[0].Email == email and admin[0].Password == password:
                admin = Admin.objects.get(Email=email)
                request.session['name'] = admin.Name
                request.session['email'] = admin.Email
                request.session['role'] = admin.Role
                request.session['id'] = admin.id
                print(f"Session role:::::{request.session['role']}")
                return redirect('admin-index')
            else:
                msg = "Check your details"
                return render(request, "garbage/auth/login.html", {'msg': msg})
        else:
            msg1 = "user doesn't exist"
            return render(request, "garbage/auth/login.html", {'msg': msg1})
    elif request.POST['role'] == "User":
        email = request.POST['email']
        password = request.POST['password']
        u = User.objects.filter(Email=email)
        if len(u) > 0:
            if u[0].Email == email and u[0].Password == password:
                user = User.objects.get(Email=email)

                request.session['name'] = user.Name
                request.session['email'] = user.Email
                request.session['role'] = user.Role
                request.session['id'] = user.User_id
                print(f"Session role:::::{request.session['role']}")
                return redirect('user-index')
            else:
                msg = "Check your details"
                return render(request, "garbage/auth/login.html", {'msg': msg})
        else:
            msg1 = "user doesn't exist"
            return render(request, "garbage/auth/login.html", {'msg': msg1})
    elif request.POST['role'] == "Garbage Collector":
        email = request.POST['email']
        password = request.POST['password']
        admin = Admin.objects.filter(Email=email)
        if len(admin) > 0:
            if admin[0].Email == email and admin[0].Password == password:
                gc = GarbageCollector.objects.get(GC=admin[0].id)

                request.session['name'] = gc.Name
                request.session['email'] = gc.Email
                request.session['role'] = gc.Role
                request.session['id'] = admin[0].id
                print(f"Session role:::::{request.session['role']}")
                url = f"/gc_orders/{request.session['id']}"
                return redirect(url)
            else:
                msg = "Check your details"
                return render(request, "garbage/auth/login.html", {'msg': msg})
        else:
            msg1 = "user doesn't exist"
            return render(request, "garbage/auth/login.html", {'msg': msg1})


def LogOut(request):
    del request.session['name']
    del request.session['email']
    del request.session['role']
    del request.session['id']

    return redirect('log-in')


def AdminIndex(request):
    return render(request, "garbage/admin/admin_index.html")


def AdminProfile(request):
    return render(request, "garbage/admin/admin_profile.html")


def AdminProfileEdit(request):
    return render(request, "garbage/admin/admin_profile_edit.html")


def AdminInBox(request):
    msg = Message.objects.all()
    return render(request, "garbage/admin/admin_inbox.html", {"msg": msg})


def AdminPayments(request):
    all_payments = GarbageItem.objects.all()
    return render(request, "garbage/admin/admin_payments.html", {"all_pay": all_payments})


def AdminPosts(request):
    return render(request, "garbage/admin/admin_posts.html")


def AdminProducts(request):
    products = Product.objects.all()
    return render(request, "garbage/admin/admin_products.html", {"Pro": products})


# MODEL FORMMM

def AdminProduct(request):


    if request.method == "POST":
        get_a = Admin.objects.get(id=request.session['id'])
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.admin_fk=get_a
            obj.save()
            return redirect('admin-index')
    else:
        form = ProductForm()
    return render(request, "garbage/admin/admin_product.html",{'form':form})

    

    



def UploadProduct(request):
    pass


def AdminOrder(request):
    return render(request, "garbage/admin/admin_order.html")


def AdminOrders(request):
    return render(request, "garbage/admin/admin_orders.html")


def XX(request):
    return render(request, "garbage/admin/experiment.html")


def UserIndex(request):
    return render(request, "garbage/index_user.html")


def Services(request):
    return render(request, "garbage/services.html")


def Shop(request):
    pro = Product.objects.all()
    return render(request, "garbage/shop/shop-right.html",{"products":pro})


def Blog(request):
    return render(request, "garbage/blog/blog-full.html")

# Contact


def Contact(request):
    return render(request, "garbage/other/contact.html")


def SendMessage(request, pk):
    if request.method == "POST":

        user1=User.objects.get(User_id=pk)
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        sub=request.POST['subject']
        msg=request.POST['message']
        today=date.today()
        message=Message.objects.create(
            user=user1, full_name=name, Phone=phone, Email=email, Subject=sub, Message=msg, Date=today)
        message.save()

        return redirect('contact')
# GC


def ViewRequests(request):
    return render(request, "garbage/garbage collector/View Requests.html")


def GCProfile(request, pk):
    if request.session['role'] == "Garbage Collector":

        admin=Admin.objects.get(id=pk)
        gc=GarbageCollector.objects.get(GC=admin)

        return render(request, "garbage/garbage collector/gc_profile.html", {"GC": gc})
    elif request.session['role'] == "Admin":

        admin=Admin.objects.get(id=pk)
        return render(request, "garbage/admin/admin_profile.html", {"Admin": admin})


def GCProfileEdit(request, pk):
    if request.session['role'] == "Garbage Collector":

        # admin=Admin.objects.get(id=pk)
        gc=GarbageCollector.objects.get(GC_id=pk)

        return render(request, "garbage/garbage collector/gc_profile2.html", {"GC": gc})
    elif request.session['role'] == "Admin":

        admin=Admin.objects.get(id=pk)
        return render(request, "garbage/admin/admin_profile2.html", {"Admin": admin})


def GCProfileSave(request, pk):
    if request.method == "POST":
        if request.session['role'] == "Garbage Collector":

            gc=GarbageCollector.objects.get(id=pk)

            gc.Name=request.POST['name'] if request.POST['name'] else gc.Name
            gc.Location=request.POST['location'] if request.POST['location'] else gc.Location
            gc.Email=request.POST['email'] if request.POST['email'] else gc.Email
            gc.Phone=request.POST['phone'] if request.POST['phone'] else gc.Phone
            gc.Address=request.POST['address'] if request.POST['address'] else gc.Address
            gc.save()
            return render(request, "garbage/garbage collector/gc_profile.html", {"GC": gc})

        elif request.session['role'] == "Admin":

            admin=Admin.objects.get(id=pk)

            admin.Name=request.POST['name'] if request.POST['name'] else admin.Name
            admin.Location=request.POST['location'] if request.POST['location'] else admin.Location
            admin.Email=request.POST['email'] if request.POST['email'] else admin.Email
            admin.Phone=request.POST['phone'] if request.POST['phone'] else admin.Phone
           # gc.Address = request.POST['address'] if request.POST['address'] else gc.Address
            admin.save()
            return render(request, "garbage/admin/admin_profile.html", {"Admin": admin})


def GCInBox(request):
    return render(request, "garbage/garbage collector/gc_inbox.html")


def GCPost(request):
    return render(request, "garbage/garbage collector/gc_post.html")


def GCPosts(request):
    return render(request, "garbage/garbage collector/gc_posts.html")


def GCProducts(request, pk):
    gc=GarbageCollector.objects.get(GC_id=pk)
    req=Request.objects.all().filter(GC_id=gc)

    return render(request, "garbage/garbage collector/gc_products.html", {"Req": req})


def GCProduct(request, pk):
    # gc = GarbageCollector.objects.get(GC_id=pk)
    req=Request.objects.all().get(id=pk)

    return render(request, "garbage/garbage collector/gc_product.html", {"Req": req})


# SaveProduct
def SaveProduct(request, pk):
    req=Request.objects.get(id=pk)
    title=request.POST['pro_title']
    quantity=request.POST['pro_quantity']
    ptype=request.POST['pro_type']
    price=request.POST['pro_price']
    description=request.POST['pro_desc']
    status=request.POST['Status']
    req.Status=status
    today=date.today()

    item=GarbageItem.objects.create(req_fk=req,
        Item_Name=title, Item_Description=description, Item_Type=ptype, Item_Quantity=quantity, Item_Price=price, pay_status=status, Date=today)
    item.save()
    # url = f"/gc_products/{request.session['id']}"
    # return redirect(url)
    return render(request, "garbage/GC_Payment.html", {"Price": price})

def GCPayment(request):
    return render(request, "garbage/GC_Payment.html")



def ShowProducts(request):
    products=Product.objects.all()
    return render(request, "garbage/admin/admin_products.html")


def GCOrder(request):
    return render(request, "garbage/garbage collector/gc_order.html")


def GCOrders(request, pk):
    gc=GarbageCollector.objects.get(GC_id=request.session['id'])
    req=Request.objects.all().filter(GC_id=gc)
    print(f"objecttt====++++ {req}")
    return render(request, "garbage/garbage collector/gc_orders.html", {"Req": req})


def UpdateReqStatus(request, pk):
    req=Request.objects.get(id=pk)
    status=request.POST['Status']
    req.Status=status
    req.save()
    url=f"/gc_orders/{request.session['id']}"
    return redirect(url)

# Consumer Details
def ConsumerDetails(request, pk):
    req=Request.objects.get(id=pk)


    return render(request, "garbage/Consumer Details.html", {"consumer": req})



def SelectGC(request):
    return render(request, "garbage/Search GC.html")


def SearchGC(request):

    location=request.POST['Area']
    # print(location)
    gc=GarbageCollector.objects.all().filter(Location=location)
    return render(request, "garbage/Search GC.html", {"GC": gc})


def Schedule(request, pk):
    gc=GarbageCollector.objects.get(id=pk)
    user=User.objects.get(User_id=request.session['id'])
    print(f"id:{user.id}\tphone:{user.Phone}")
    return render(request, "garbage/schedule pickup.html", {"GC": gc, "User": user})


def RequestPickup(request, pk):
    if request.method == "POST":
        garbage_type=request.POST['garbage_type']
        specify_garbage=request.POST['specify_garbage']
        garbage_quantity=request.POST['garbage_quantity']
        phone=request.POST['phone']
        address=request.POST['address']
        today=date.today()

        gc=GarbageCollector.objects.get(id=pk)
        user=User.objects.get(User_id=request.session['id'])

        req=Request.objects.create(User_id=user, GC_id=gc, Garbage_Type=garbage_type,
                                     Garbage_Description=specify_garbage, Phone=phone, Quantity=garbage_quantity, Address=address, Date=today)
        req.save()


        return redirect("user-index")


def UserRequests(request, pk):
    user=User.objects.get(User_id=pk)
    user_req=Request.objects.all().filter(User_id=user)
    return render(request, "garbage/user/View_GC_Requests.html", {"Req": user_req})

# Admin View Requests

def AdminViewRequests(request):
    all_req=Request.objects.all()

    return render(request, "garbage/admin/admin_view_requests.html", {"allreq": all_req})

def AdminViewPaymentDetails(request, pk):
    details=GarbageItem.objects.get(id=pk)

    return render(request, "garbage/Payment Detail.html", {"Detail": details})





# Show All CartItems
def CartItems(request):
    cartall=Cart.objects.all()
    total=Cart.objects.aggregate(Total=Sum('Price'))
    return render(request, "garbage/admin/Cart.html", {"Sum": total, "CartAll": cartall})


def CartPage(request, pk):
    ad=Admin.objects.get(id=request.session['id'])
    pro=Product.objects.get(id=pk)
    cart=Cart.objects.create(product=pro, Price=pro.Price, temp=ad)
    return redirect('cartitems')


def DelCartItem(request, pk):
    del_item=Cart.objects.get(id=pk)
    del_item.delete()
    return redirect('cartitems')
