from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.contrib import messages


def Home(req):
    Data = Sweets.objects.all()
    return render(req, 'Home.html', context={'Data': Data})


def Register(req):
    if req.method == 'POST':
        name = req.POST['nm']
        email = req.POST['em']
        mobile = req.POST['mb']
        pwd = req.POST['pw1']
        pwd1 = req.POST['pw2']
        if pwd != pwd1:
            Error = 'Password Does Not Match !!'
            return render(req, 'Register.html', context={'Err': Error})
        if Users.objects.filter(mobile=mobile).exists():
            Error = 'Mobile Number Already Registered !!'
            return render(req, 'Register.html', context={'Err': Error})
        if Users.objects.filter(email=email).exists():
            Error = 'Mobile Number Already Registered !!'
            return render(req, 'Register.html', context={'Err': Error})
        else:
            ob = Users(full_name=name, email=email, mobile=mobile, Password=make_password(pwd1))
            ob.save()
            ob1 = User(username=email, password=make_password(pwd1))
            ob1.save()
            return redirect(Login)
    else:
        return render(req, 'Register.html')


def Login(req):
    if req.method == 'POST':
        email = req.POST['em']
        pwd = req.POST['pw']
        try:
            Record = Users.objects.get(email=email)
            if check_password(pwd, Record.Password):
                Data = authenticate(username=email, password=pwd)
                if Data is not None:
                    login(req, Data)
                    req.session['user-email'] = Record.full_name
                    req.session['user-phone'] = Record.mobile
                    return redirect(Home)
                else:
                    Error = 'User Not Found !!'
                    return render(req, 'Login.html', context={'Err': Error})
            else:
                Error = 'Password Does Not Match !!'
                return render(req, 'Login.html', context={'Err': Error})
        except:
            Error = 'Email Not Found !!'
            return render(req, 'Login.html', context={'Err': Error})
    else:
        return render(req, 'Login.html')


def Logout(req):
    logout(req)
    return redirect(Login)


def Contact_Us(req):
    if req.method == 'POST':
        name = req.POST['name']
        email = req.POST['email']
        message = req.POST['message']
        ob = Contact(name=name, email=email, message=message)
        ob.save()
        return redirect(Home)
    else:
        return HttpResponse('Go Back And Try Again !!')


def Menu(req):
    categories = [
        {"id": "Premium", "name": "Premium"},
        {"id": "Traditional", "name": "Traditional"},
        {"id": "Dry Fruit", "name": "Dry Fruit"},
        {"id": "Festival Special", "name": "Festival Special"}
    ]
    category = req.GET.get('category', '')
    search = req.GET.get('search', '')
    sweets = Sweets.objects.all()
    if category:
        sweets = sweets.filter(Category=category)
    if search:
        sweets = sweets.filter(Name__icontains=search)
    context = {
        'categories': categories,
        'sweets': sweets
    }
    return render(req, 'Menu.html', context)


def Admin_Login(req):
    if req.method == 'POST':
        email = req.POST['email']
        pwd = req.POST['pwd1']
        try:
            Record = AdminUsers.objects.get(email=email)
            if check_password(pwd, Record.Password):
                req.session['Admin-UserName'] = Record.email
                return redirect(DashBoard)
            else:
                Error = 'Password Does Not Match !!'
                return render(req, 'Admin-Login.html', context={'Err': Error})
        except:
            Error = 'Email Not Found !!'
            return render(req, 'Admin-Login.html', context={'Err': Error})
    else:
        return render(req, 'Admin-Login.html')


def DashBoard(req):
    users = req.session.get('Admin-UserName')
    Users_Data = Users.objects.all()
    Users_Data_Count = Users.objects.all().count()
    Sweets_Count = Sweets.objects.all().count()
    Messages = Sweets.objects.all().count()
    return render(req, 'DashBoard.html', context={'users': users, 'users_all': Users_Data,
                                                  'U_Count': Users_Data_Count, 'Sweets_C': Sweets_Count,
                                                  'Message': Messages})


def Sweet_Management(req):
    users = req.session.get('Admin-UserName')
    Data = Sweets.objects.all()
    return render(req, 'Sweet_Management.html', context={'users': users, 'Data': Data})


def Admin_Management(req):
    users = req.session.get('Admin-UserName')
    Data = AdminUsers.objects.all()
    return render(req, 'Admin_Management.html', context={'users': users, 'admin': Data})


def Contact_Management(req):
    users = req.session.get('Admin-UserName')
    Data = Contact.objects.all()
    return render(req, 'Contact.html', context={'users': users, 'message': Data})


def Add_Sweets(req):
    if req.method == 'POST':
        name = req.POST['name']
        price = req.POST['price']
        des = req.POST['category']
        stock = req.POST['stock']
        image = req.FILES['image']
        ob = Sweets(Name=name, price=price, Category=des,
                    Image=image, Stock=stock)
        ob.save()
        return redirect(Sweet_Management)
    else:
        return HttpResponse('Go Back And Try Again !!')


def Edit_Sweets(req, s_id):
    Data = Sweets.objects.get(id=s_id)
    if req.method == 'POST':
        name = req.POST['name']
        price = req.POST['price']
        des = req.POST['category']
        stock = req.POST['stock']
        image = req.FILES['image']
        Data.Name = name
        Data.price = price
        Data.Stock = stock
        Data.Image = image
        Data.Category = des
        Data.save()
        return redirect(Sweet_Management)
    else:
        return render(req, 'Sweet_Management.html', context={'Data': Data})


def Delete_Sweets(req, s_id):
    Data = Sweets.objects.get(id=s_id)
    Data.delete()
    return redirect(Sweet_Management)


def Edit_Users(req, u_id):
    Data = Users.objects.get(id=u_id)
    Data1 = User.objects.get(username=Data.email)
    if req.method == 'POST':
        name = req.POST['name']
        email = req.POST['email']
        phone = req.POST['phone']
        Data.full_name = name
        Data.email = email
        Data.mobile = phone
        Data1.username = email
        Data.save()
        Data1.save()
        return redirect(DashBoard)
    else:
        return render(req, 'DashBoard.html', context={'Data': Data})


def Delete_Users(req, u_id):
    Data = Users.objects.get(id=u_id)
    Data1 = User.objects.get(username=Data.email)
    Data.delete()
    Data1.delete()
    return redirect(DashBoard)


def Delete_Message(req, m_id):
    Data = Contact.objects.get(id=m_id)
    Data.delete()
    return redirect(Contact_Management)


def Admin_Register(req):
    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['pw1']
        ob = AdminUsers(username=username, email=email,
                        Password=make_password(password))
        ob.save()
        return redirect(Admin_Management)
    else:
        return render(req, 'Admin_Management.html')


def Delete_Admin(req, a_id):
    Data = AdminUsers.objects.get(id=a_id)
    Data.delete()
    return redirect(Admin_Management)


def Admin_Logout(req):
    logout(req)
    return redirect(Admin_Login)


def Submit_Order(req):
    if req.method == 'POST':
        sweet_id = req.POST['sweet_id']
        sweet_name = req.POST['sweet_name']
        quantity = int(req.POST['quantity'])
        address = req.POST['address']
        phone = req.session.get('user-phone')
        user = req.session.get('user-email')

        try:
            sweet = Sweets.objects.get(id=sweet_id)

            if sweet.Stock >= quantity:
                Order.objects.create(
                    user=user,
                    sweet=sweet_name,
                    quantity=quantity,
                    address=address,
                    phone=phone
                )
                sweet.Stock -= quantity
                sweet.save()
                messages.success(req, 'Order placed successfully!')
                return redirect(Home)
            else:
                messages.error(req, 'Not enough stock available.')
                return redirect(Home)
        except Sweets.DoesNotExist:
            return HttpResponse("Sweet not found")
    return redirect(Home)


def Order_List(req):
    Data = Order.objects.all()
    return render(req, 'Order-List.html', context={'Order': Data})


def Delete_Order(req, o_id):
    Data = Order.objects.get(id=o_id)
    Data.delete()
    return redirect(Order_List)
