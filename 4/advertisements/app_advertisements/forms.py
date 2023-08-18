from django import forms

# создаем класс формы, наследуя от джанговского класса
class AdvertisementForm(forms.Form):
    # указываем поля нашей формы, которые нужно заполнить (согласно базе данных)
    title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={"class": "form-control form-control-lg"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control form-control-lg"}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "form-control form-control-lg"}))
    auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control form-control-lg"}))
    # кроме user, date_added и date_update - они заполнятся автоматом