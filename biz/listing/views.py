from django.shortcuts import render
from listing.models import Biz,Category

from listing.forms import BizForm,CatForm
# Create your views here.
def home(req):
    data = {
        "biz":Biz.objects.all(),
        "category":Category.objects.all()
    }
    return render(req,"home.html",data)


def insert(req):
    data = {
        "form":BizForm,
        "catform":CatForm
        }
    return render(req,"insert.html",data)