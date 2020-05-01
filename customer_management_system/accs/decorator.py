from django.shortcuts import HttpResponse, render, redirect

def unauthorize_user(view_func):
    def wrapper_func(request,*args, **kwargs):
        # print(request.user.email)
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

def allow_user(allowed_user=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name   
            if  group in allowed_user:   
                return view_func(request, *args, **kwargs)
            else:
                return redirect('/product')
                
        return wrapper_func
    
    return decorator