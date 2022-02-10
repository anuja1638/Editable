from django.shortcuts import render

# Create your views here.
def homePageView(request):
    return render(request, 'AIEditingApp/index.html', context={})

def manualEditView(request):
    return render(request, 'ManualEditing/manualEditPage.html', context={})