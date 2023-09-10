from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Fikri Dhiya Ramadhana',
        'class': 'PBP C',
        'items' : ["sword", "potion", "shield", "armor"],
        'range': range(0,4),
        'price' : list([200 , 50, 100, 150]),
        'power' : list([100, 0, 150, 75]),
        'description' : list(["long double-edged sword", "restore health by 50%", "block enemy atk", "increase def stat"])
    }

    return render(request, "main.html", context,)
