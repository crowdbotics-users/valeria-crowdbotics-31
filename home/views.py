from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'12factor-vault', 'url': 'http://pypi.python.org/pypi/12factor-vault/0.1.16'},
    ]
    context = {
        'title': 'valeria-crowdbotics-31',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
