from django.shortcuts import render

def catalog(request):
    context= {
        'title':'Home - Catalog',
        'goods': [
        {'image': 'deps/images/goods/set of tea table and three chairs.jpg',
         'name': 'Tea table and three chairs',
         'description': 'A set of three chairs and a designer table for the living room.',
         'price': 150.00},

         {'image': 'deps/images/goods/set of tea table and two chairs.jpg',
         'name': 'Tea table and two chairs',
         'description': 'A set of a table and two chairs in a minimalist style.',
         'price': 93.00},

         {'image': 'deps/images/goods/double bed.jpg',
         'name': 'Double bed',
         'description': 'The bed is double with a headrest and is generally very orthopedic.',
         'price': 670.00},

         {'image': 'deps/images/goods/kitchen table.jpg',
         'name': 'Kitchen table with sink',
         'description': 'Kitchen dining table with built-in sink and chairs.',
         'price': 365.00},

         {'image': 'deps/images/goods/kitchen table 2.jpg',
         'name': 'Kitchen table with built-in',
         'description': 'Kitchen table with built-in stove and sink. Lots of shelves and generally beautiful.',
         'price': 430.00},

         {'image': 'deps/images/goods/corner sofa.jpg',
         'name': 'Corner sofa for the living room',
         'description': 'Corner sofa, unfolds into a double bed, for the living room and reception of guests is the very thing!',
         'price': 610.00},

         {'image': 'deps/images/goods/bedside table.jpg',
         'name': 'Bedside table',
         'description': 'Bedside table with two drawers (flower is not included).',
         'price': 55.00},

         {'image': 'deps/images/goods/sofa.jpg',
         'name': 'The sofa is ordinary',
         'description': 'A sofa, aka an ordinary sofa, nothing remarkable to describe.',
         'price': 190.00},

         {'image': 'deps/images/goods/office chair.jpg',
         'name': 'Office chair',
         'description': 'Product description, about how cool it is, but it is a chair, what can I say...',
         'price': 30.00},

         {'image': 'deps/images/goods/plants.jpg',
         'name': 'Plant',
         'description': 'A plant for decorating your interior will give freshness and serenity to the surroundings.',
         'price': 10.00},

         {'image': 'deps/images/goods/flower.jpg',
         'name': 'Stylized flower',
         'description': 'A designer flower (possibly artificial) for interior decoration.',
         'price': 15.00},

         {'image': 'deps/images/goods/strange table.jpg',
         'name': 'Bedside table',
         'description': 'A table, rather strange in appearance, but suitable for placing next to the bed.',
         'price': 25.00},
        ],
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    return render(request, 'goods/product.html')