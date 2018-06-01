from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'test1/index.html')

def board(request):
    return render(request,'test1/message_board.html')