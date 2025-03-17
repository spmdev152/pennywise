from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View

from apps.user.forms import UserDetailsForm
from pennywise.utils import parse_query_string_from_body


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

    def patch(self, request: WSGIRequest) -> HttpResponse:
        """
        Updates the user details.

        Parameters
        ----------
        request : WSGIRequest
            The request object.

        Returns
        -------
        HttpResponse
            A response with the form errors if any,
            otherwise a response with a success toast.
        """

        form_data = parse_query_string_from_body(request.body)

        form = UserDetailsForm(form_data, instance=request.user)

        html_response = ""

        if not form.is_valid():

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

            html_response = html_response.replace("\n", "")

            return HttpResponse(html_response)

        for field in form.fields.keys():
            html_response += render_to_string(
                "components/error/error-recipient.html",
                {"origin": field},
            )

        form.save()

        toast_html = render_to_string(
            "components/toast.html",
            {
                "id": "user-details-toast",
                "type": "success",
                "message": "User details updated successfully",
            },
        )

        html_response += toast_html

        html_response = html_response.replace("\n", "")

        return HttpResponse(html_response)
