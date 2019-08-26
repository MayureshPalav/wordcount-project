from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')
def count(request):
    wordcounts={ }
    fultext=request.GET['FULLTEXT']
    wordcount=fultext.split()
    for words in wordcount:
        if words in wordcounts:
            wordcounts[words] += 1
        else:
            wordcounts[words] = 1
    sortedwords=sorted(wordcounts.items(),key=operator.itemgetter(1),reverse=True)





    return render(request,'count.html',{'fulltext':fultext,'count':len(wordcount),'sortedwords':sortedwords})
def about(request):
    return render(request,'about.html')    
