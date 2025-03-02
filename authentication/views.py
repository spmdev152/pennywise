from django.contrib.auth import login
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render
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
            errors_html = ""
            status_code = 400

            for field in form.fields.keys():
                field_errors = form.errors.get(field)

                if field_errors:
                    errors_html += f'<p class="field-error" id="{field}-error">{field_errors[0]}</p>'

                    continue

                errors_html += f'<div id="{field}-error" style="display: none;"></div>'

            non_field_errors = form.non_field_errors()

            if form.non_field_errors():
                errors_html += f'<p class="form-error" id="credentials-error">{non_field_errors[0]}</p>'
                status_code = 403
            else:
                errors_html += (
                    f'<div id="credentials-error" style="display: none;"></div>'
                )

            return HttpResponse(errors_html, status=status_code)

        login(request, form.user)

        return HttpResponseClientRedirect("/user/account")
