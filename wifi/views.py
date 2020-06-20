from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView

from .models import Local, Password


def index(request):
    locations = Local.objects.order_by('name').all()
    return render(request, "index.html", {"locations": locations})


class CreateLocal(LoginRequiredMixin, CreateView):
    model = Local
    fields = ('name', 'location')
    template_name = "create_local.html"
    success_url = "/"


class CreatePassword(LoginRequiredMixin, CreateView):
    model = Password
    fields = ('value', 'location')
    template_name = "create_password.html"
    success_url = "/"

    # def form_valid(self, form):
        # import code
        # code.interact(local=dict(globals(), **locals()))
        # try:
        #     user = User.objects.get(email=form.email)
        # except User.DoesNotExist:
        #     user = User.objects.create_user(form.email, form.email, ''.join(
        #         [random.choice(string.digits + string.letters) for i in range(0, 10)]))
        #     user.save()
        # form.instance.user = user
        # return super(ProjectCreateDetails, self).form_valid(form)

def about(request):
    return render(request, "about.html")
