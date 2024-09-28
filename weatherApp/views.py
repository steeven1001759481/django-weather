from django.shortcuts import render

# Create your views here.
def indexView(request):
    if request.method == "POST":
        city = request.POST['city']
    else:
        city = ''    
    return render(request, 'index.html', {'city': city})