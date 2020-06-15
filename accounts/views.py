from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Entry
# from .form import PostEntry


class Home(ListView):
    model = Entry
    Template_name = 'accounts/miniblog.html'
    context_object_name = 'posts'
    ordering = ['-post_date']
    paginate_by = 3

    # post = Entry.objects.all()
    # context = {
    #     'posts': post
    # }
    # ordering = ['-post_date']
    # paginate_by = 3
    #
    # return render(request, 'miniblog.html', context)


class Detail(DetailView):
    model = Entry
    Template_name = 'entry_detail.html'


class CreatePost(CreateView):
    model = Entry
    Template_name = 'accounts/post.html'
    fields = ['post_title', 'post_body']
    ordering = ['-post_date']
    paginate_by = 3

    # def form_valid(self, form):
    #     form.instance.post_author = self.request.User
    #     return super().form_valid(form)


def ldetail(request):
    details = Entry.objects.all()
    context = {
        'detail': details
    }
    return render(request, 'detail.html', context)


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 != password2:
            messages.info(request, 'password not matching')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'username taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'email taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,
                                            last_name=last_name)
            user.save()
            messages.info(request, 'user created successfully')
        return redirect('login')
    else:
        return render(request, 'register.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('ldetail')
        else:
            messages.info(request, 'Please register to log in or you cross check your log in details')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


# def post(request):
#     mypost = PostEntry(request.POST)
#
#     if mypost.is_valid():
#         post = Entry(post_title=mypost.cleaned_data['post_title'],
#                      post_body=mypost.cleaned_data['post_body'],
#                      post_author=mypost.cleaned_data['post_author'])
#         post.save()
#         return redirect('/')
#     else:
#         return render(request, 'post.html')

