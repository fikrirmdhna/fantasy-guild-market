from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Fikri Dhiya Ramadhana',
        'class': 'PBP C',
        'amount': 0,
        'list_items' : [
            {
                'item'  : "long sword",
                'price' : 200,
                'power' : 100,
                'description': "long double-edged sword",
            },
            {
                'item'  : "healing potion",
                'price' : 50,
                'power' : 0,
                'description': "restore health by 50%",
            },
            {
                'item'  : "shield",
                'price' : 100,
                'power' : 50,
                'description': "block enemy atk",
            },
            {
                'item'  : "armor",
                'price' : 150,
                'power' : 75,
                'description': "increase def stat",
            }
        ]
    }

    return render(request, "main.html", context)