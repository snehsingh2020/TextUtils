from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')

    if removepunc == 'on':
        punctuations = '''`-=~!@#$%^&*()_+[]\;',./:"<>?'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'remove punctuation', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to upper case', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if (djtext[index] == " " and djtext[index + 1] == " "):
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Spaces', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (removepunc != 'on' and extraspaceremover != 'on' and fullcaps != 'on' and newlineremover != 'on'):
        return HttpResponse("Please Select the Operation")

    return render(request, 'analyze.html', params)
