from django.shortcuts import redirect

def redirect_COC(request):
    return redirect('commercial_offers_list_url', permanent=True)
