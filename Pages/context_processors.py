from .models import PageInfo

def global_context(request):
    page_info_list = PageInfo.objects.all()

    if not page_info_list:
        return {}

    return {
        "page_title": page_info_list[0].title,
        "subtitle": page_info_list[0].subtitle,
        "phone": page_info_list[0].phone,
        "email": page_info_list[0].email,
        "instagram": page_info_list[0].instagram,
        "facebook": page_info_list[0].facebook,
        "company": page_info_list[0].company,
        "address": page_info_list[0].address
    }