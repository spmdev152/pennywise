from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View


class AccountView(View):
    """
    Account view.

    Methods
    -------
    get(request: WSGIRequest) -> HttpResponse
        Renders the account page.
    """

    @method_decorator(login_required)
    def get(self, request: WSGIRequest) -> HttpResponse:
        """
        Renders the account page.

        Parameters
        ----------
        request : WSGIRequest
            The request object.

        Returns
        -------
        HttpResponse
            The rendered account page.
        """

        return render(request, "pages/user/account.html")
