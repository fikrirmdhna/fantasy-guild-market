from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Fikri Dhiya Ramadhana',
        'class': 'PBP C',
        'amount': 0,
        'items' : "long sword",
        'price' : 200,
        'power' : 100,
        'description' : "long double-edged sword",
    }
    return render(request, "main.html", context)
