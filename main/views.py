from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306244993',
        'name': 'Erdafa Andikri',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
