from django.shortcuts import render, redirect

# Create your views here.


def tool(request):
	return render(request, 'tool/tool.html')