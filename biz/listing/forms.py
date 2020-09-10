from django.forms import ModelForm
from listing.models import Biz,Category


class BizForm(ModelForm):
    class Meta:
        model = Biz
        fields = "__all__"

class CatForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"