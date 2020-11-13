#I have created this file.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    #params={'name':'Divya','place':'Telangana'}
    return render(request,'index.html')

    #return HttpResponse('''<h1><a href="https://emmadidivyasrujana.github.io/Divya_Portfolio/">Divya</a></h1>''')

def contactus(request):
    return HttpResponse("This is contact us Page ")

def about(request):
    return HttpResponse("This is about us page. To go <a href='/'>back")

def analyse(request):
    analysed_text=""
    text=request.GET.get('text','default')
    state1=request.GET.get('removepunc','off')
    state2=request.GET.get('capitalise','off')
    state3=request.GET.get('charcount','off')
    punctuations=['!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?"]
    if(state1=="on"):
        for i in text:
            if(i not in punctuations):
                analysed_text+=i
    elif(state2=="on"):
        analysed_text=text.upper()
    elif(state3=="on"):
        count_char=0
        for i in text:
            count_char+=1
        analysed_text=f"No of characters is {count_char}"
    else:
        analysed_text=text
    params={'analyse_text_content':analysed_text}
    return render(request,'analyse.html',params)