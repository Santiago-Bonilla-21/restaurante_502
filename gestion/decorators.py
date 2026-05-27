from django.shortcuts import redirect

def rol_permitido(roles=[]):

    def decorator(view_func):

        def wrapper(request, *args, **kwargs):

            rol = request.user.perfil.rol.nombre

            if rol in roles:
                return view_func(request, *args, **kwargs)

            return redirect('inicio')

        return wrapper

    return decorator