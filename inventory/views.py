from django.shortcuts import render

# Create your views here.
ITEMS = [
    {"id": 1, "name": "ノートPC", "price": 120000, "stock": 5},
    {"id": 2, "name": "無線マウス", "price": 3500, "stock": 0},
    {"id": 3, "name": "27インチモニター", "price": 45000, "stock": 2},
]


def item_list(request):
    context = {"items": ITEMS, "message": "本日の在庫状況です"}
    return render(request, "inventory/item_list.html", context)
