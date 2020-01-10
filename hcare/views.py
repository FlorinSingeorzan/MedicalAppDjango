from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Doctor, Message
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, MessageForm
from django.views import generic


class HomeView(generic.ListView):
    template_name = "healthcare/login.html"

    def get_queryset(self):
        return Doctor.objects.all()


class DetailView(generic.DetailView):
    model = Doctor
    template_name = "healthcare/user.html"


class UserFormView(View):
    form_class = UserForm
    template_name = 'healthcare/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            print(email)
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
        return render(request, self.template_name, {'form': form})


def home(request):
    home = True
    doctors = Doctor.objects.all()
    context = {'object_list': doctors, 'hom': home}
    return render(request, 'healthcare/user.html', context)


def index(request):
    return render(request, 'healthcare/index.html')


def register(request):
    return render(request, 'healthcare/register.html')


def detail(request, doctor_id):
    home = True
    try:
        doc = Doctor.objects.get(pk=doctor_id)
    except:
        raise Http404('Inexistent')
    return render(request, 'healthcare/detail.html', {'doc': doc, 'hom': home})


def login_user(request):
    hom = True
    if request.method == "POST":
        doctors = Doctor.objects.all()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.is_staff:
                    messages = Message.objects.filter(receiver=username)
                    return render(request, 'healthcare/doctor.html', {'messages': messages, 'hdoc': hom})
                else:
                    return render(request, 'healthcare/user.html', {'object_list': doctors, 'hom': hom})
            else:
                return render(request, 'healthcare/user.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'healthcare/login.html', {'error_message': 'Invalid login'})
    return render(request, 'healthcare/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'healthcare/login.html')


def send(request):
    hom = True
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.sender = request.user.username
            post.save()
            return render(request, 'healthcare/message.html', {'hom': hom})
        print("---sdasd-s--")
        return render(request, 'healthcare/detail.html', {'hom': hom})


def view_messages(request):
    hom = True
    username = request.user.username
    messages = Message.objects.filter(receiver=username)
    return render(request, 'healthcare/doctor.html', {'messages': messages, 'hdoc': hom})


def respond(request):
    hdoc = True
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.sender = request.user.username
            post.save()
            return render(request, 'healthcare/message.html', {'hdoc': hdoc})
        return render(request, 'healthcare/detail.html', {'hom': hdoc})


def feed(request):
    hom= True
    messages = Message.objects.filter(receiver=request.user.username)
    return render(request, 'healthcare/feed.html', {'hom': hom, 'messages': messages})
