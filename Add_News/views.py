from django.shortcuts import render
import requests
apiKey='517cea3ba8ea4b18bebd176b5bb111e6'
  
# Create your views here. 
def index(request):
    Source=request.GET.get('q')
    Category=request.GET.get('category')
    Language=request.GET.get('language')
    if Source:
        url = f'https://newsapi.org/v2/top-headlines?q={Source}&apiKey={apiKey}'
        response=requests.get(url)
        Data=response.json()
        articles=Data['articles']
    elif Category:
        url = f'https://newsapi.org/v2/top-headlines?category={Category}&apiKey={apiKey}'
        response=requests.get(url)
        Data=response.json()
        articles=Data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?language={Language}&apiKey={apiKey}'
        response=requests.get(url)
        Data=response.json()
        articles=Data['articles']

    context={
        'articles':articles
    }       
    return render(request, 'index.html', context)

def refresh(request):
    url=f'https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey={apiKey}'
    response=requests.get(url)
    Data=response.json()
    articles=Data['articles']
    context={"articles":articles}
    return render(request, 'index.html', context)
