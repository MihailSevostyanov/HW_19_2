from django.shortcuts import render


def home(request):
    return render(request, template_name="home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name}, {phone}, {message}")
    return render(request, template_name="contacts.html")
