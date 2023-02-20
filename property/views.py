from django.shortcuts import render


def homepage(request):
    page = 'homepage'

    template_name = 'property/index.html'
    context = {'page': page}
    return render(request, template_name, context)


def properties(request):
    page = 'properties'
    
    template_name = 'property/properties.html'
    context = {'page': page}
    return render(request, template_name, context)


def aboutUs(request):
    page = 'aboutUs'
    
    template_name = 'property/about.html'
    context = {'page': page}
    return render(request, template_name, context)


def contactUs(request):
    page = 'contactUs'
    
    template_name = 'property/contact.html'
    context = {'page': page}
    return render(request, template_name, context)