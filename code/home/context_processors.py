# context_processors.py
from .models import Cart

def custom_context(request):
    if request.user.is_authenticated:
        # Fetch the count of products in the cart for the logged-in user
        product_count = Cart.objects.filter(username=request.user).count()
    else:
        product_count = 0  # Set a default value if the user is not authenticated
    
    # Return the product count in a dictionary
    return {'product_count': product_count}

