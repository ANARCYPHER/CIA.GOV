from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def contact(request):
   # if request.method == "POST":
      # exampleInputEmail1 = request.['exampleInputEmail1']
    #else:    
    return render(request, 'contact.html', {})


