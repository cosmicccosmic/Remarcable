from django.shortcuts import render
from django.db.models import Count, Q
from django.http import JsonResponse
from .models import Category, Tag, Product


def api_search_products(request):
    """
    API endpoint for searching products and returning JSON results.
    
    This function processes search parameters to retrieve matching products using 
    the query_products helper function, and returns the the product details results
    via a JSON response.
    
    Parameters:
        request (HttpRequest object): contains the search parameters
    
    Returns:
        JsonResponse: Contains a 'products' key with an array of product objects
                     Each product object includes name, description, category, and tags.
    """
    # Get search parameters from request
    selected_category = request.GET.get("category")  
    description = request.GET.get("description_search")
    selected_tags = request.GET.getlist("tags")
    
    # Get filtered products
    products = query_products(selected_category, description, selected_tags)
    
    # Convert products to JSON format
    products_data = []
    for product in products:
        products_data.append({
            'name': product.name,
            'description': product.description,
            'category': product.category.name,
            'tags': [tag.name for tag in product.tags.all()]
        })
    
    return JsonResponse({"products": products_data})

def search_products(request):
    """
    View function to handle product search requests and render the search results.
    
    This function utilizes search parameters and queries the database with them for matching 
    products. It then renders them in search_table.html along with all categories and tags 
    for filtering.
    
    Parameters:
        request (HttpRequest object): contains the search parameters
    
    Returns:
        HttpResponse with rendered template containing search results and filter options
    """
    context = {}
    if request.method == "GET":
        # Get the category, description, tag parameters from the request
        selected_category = request.GET.get("category")  
        description = request.GET.get("description_search")
        selected_tags = request.GET.getlist("tags")

        # Handle the search logic
        products = query_products(selected_category, description, selected_tags)

        categories = Category.objects.all()
        tags = Tag.objects.all()

        # Build the context
        context = {
            "products": products,
            "categories": categories,
            "tags": tags,
            "selected_category": selected_category,
            "selected_tags": selected_tags,
            "description": description,
        }

    return render(request, "product_search/search_table.html", context)

def query_products(category, description, tags):
    """
    Query the product database with the given parameters.
    
    This function filters the Product queryset based on the provided category,
    description text, and tag(s). Products are returned only if they match all
    specified criteria.
    
    Parameters:
        category (str): Name of category to filter by, or None for all categories
        description (str): Text to search for in product descriptions, or None to skip
        tags (list): List of tag names to filter by, or empty list for no tag filtering
    
    Returns:
        QuerySet: Filtered Product objects matching all criteria
    """
    # Get the base Product QuerySet
    productQuerySet = Product.objects.all()
    
    # Handle if there is a description to search for
    if description:
        productQuerySet = productQuerySet.filter(description__icontains=description)
    
    # Handle if there is a category to filter by
    if category:
        productQuerySet = productQuerySet.filter(category__name=category)

    # Handle if there are tags to filter by
    if tags:
        productQuerySet = productQuerySet.annotate( # get the number
            num_tags=Count('tags', filter=Q(tags__name__in=tags), distinct=True)
        ).filter(num_tags=len(tags))

    return productQuerySet
