from registration.backends import JWTAuthentication


def current_user(request):
    """
        Input request should contain an Authorization header with content
        in the form of "Token <token>". Outputs Django User instance
        with corresponding token
    """
    return JWTAuthentication().authenticate(request)[0]
