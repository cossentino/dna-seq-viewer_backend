from registration.backends import JWTAuthentication


def current_user(request):
    j = JWTAuthentication()
    return j.authenticate(request)[0]
