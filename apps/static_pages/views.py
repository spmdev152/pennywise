from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class HomeView(View):
    """
    Home view.

    Methods
    -------
    get(request: WSGIRequest) -> HttpResponse
        Renders the home page.
    """

    def get(self, request: WSGIRequest) -> HttpResponse:
        """
        Renders the home page.

        Parameters
        ----------
        request : WSGIRequest
            The request object.

        Returns
        -------
        HttpResponse
            The rendered home page.
        """

        return render(request, "static_pages/home.html")
