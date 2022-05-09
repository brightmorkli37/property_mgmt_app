from django.shortcuts import render


def homepage(request):
    page = 'homepage'

    template_name = 'hotels/index.html'
    context = {'page': page}
    return render(request, template_name, context)


def properties(request):
    page = 'properties'
    
    template_name = 'hotels/properties.html'
    context = {'page': page}
    return render(request, template_name, context)


def aboutUs(request):
    page = 'aboutUs'
    
    template_name = 'hotels/about.html'
    context = {'page': page}
    return render(request, template_name, context)


def contactUs(request):
    page = 'contactUs'
    
    template_name = 'hotels/contact.html'
    context = {'page': page}
    return render(request, template_name, context)