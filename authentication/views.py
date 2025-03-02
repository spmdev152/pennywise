from django.contrib.auth import login
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import never_cache
from django_htmx.http import HttpResponseClientRedirect

from authentication.forms import SignInForm


class SignInView(View):
    """
    Sign in view.

    Methods
    -------
    get(request: WSGIRequest) -> HttpResponse
        Renders the sign in page.
    post(request: WSGIRequest) -> HttpResponse | HttpResponseClientRedirect
        Signs the user in.
    """

    @method_decorator(never_cache)
    def get(self, request: WSGIRequest) -> HttpResponse:
        """
        Renders the sign in page.

        Parameters
        ----------
        request : WSGIRequest
            The request object.

        Returns
        -------
        HttpResponse
            The rendered sign in page.
        """

        if request.user.is_authenticated:
            return redirect("/user/account")

        return render(request, "pages/authentication/sign-in.html")

    def post(self, request: WSGIRequest) -> HttpResponse | HttpResponseClientRedirect:
        """
        Signs the user in.

        Parameters
        ----------
        request : WSGIRequest
            The request object.

        Returns
        -------
        HttpResponse | HttpResponseClientRedirect
            A response with the form errors if any,
            otherwise a redirection to the account page.
        """

        form = SignInForm(request.POST)

        if not form.is_valid():
            html_response = ""

            for field in form.fields.keys():
                field_errors = form.errors.get(field)

                if field_errors:
                    html_response += render_to_string(
                        "components/error/field-error.html",
                        {"origin": field, "error": field_errors[0]},
                    )

                    continue

                html_response += render_to_string(
                    "components/error/error-recipient.html",
                    {"origin": field},
                )

            non_field_errors = form.non_field_errors()

            if form.non_field_errors():
                html_response += render_to_string(
                    "components/error/form-error.html",
                    {"origin": "credentials", "error": non_field_errors[0]},
                )
            else:
                html_response += render_to_string(
                    "components/error/error-recipient.html",
                    {"origin": "credentials"},
                )

            html_response = html_response.replace("\n", "")

            return HttpResponse(html_response)

        login(request, form.user)

        return HttpResponseClientRedirect("/user/account")
