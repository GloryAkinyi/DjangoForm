from django.shortcuts import render
from .models import Member
from .forms import MemberForm


# Create your views here.
def home(request):
    all_members = Member.objects.all

    return render(request, 'home.html', {'all': all_members})


def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'join.html', {})

    else:
        return render(request, 'join.html', {})
