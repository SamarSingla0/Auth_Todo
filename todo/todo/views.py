from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from todo.models import TodoItem
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        # print(fnm, email, pwd)
        my_user = User.objects.create_user(fnm, email, pwd)
        my_user.save()
        return redirect('/login')
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        # print(fnm, pwd)
        
        user = authenticate(request, username=fnm, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('/todoapp')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')



def todo_app(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    if request.method == 'POST':
        title = request.POST.get('title')
        todo_item = TodoItem(title=title, user=request.user)
        todo_item.save()

    todo_items = TodoItem.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res': todo_items})




def signout(request):
    logout(request)
    return redirect('/login')


def edit_todo(request, srno):
    if not request.user.is_authenticated:
        return redirect('/login')

    todo_item = TodoItem.objects.get(srno=srno, user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        todo_item.title = title
        todo_item.save()
        return redirect('/todoapp')

    todo_items = TodoItem.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res': todo_items, 'obj': todo_item})



def delete_todo(request, srno):
    if not request.user.is_authenticated:
        return redirect('/login')

    try:
        todo_item = TodoItem.objects.get(srno=srno, user=request.user)
        todo_item.delete()
    except TodoItem.DoesNotExist:
        pass

    return redirect('/todoapp')
