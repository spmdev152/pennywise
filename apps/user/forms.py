from django.forms import ModelForm

from authentication.models import AppUser


class UserDetailsForm(ModelForm):
    """
    User details form.
    """

    class Meta:
        """
        Form metadata.

        Attributes
        ----------
        model : AppUser
            The model associated with the form.
        fields : list[Literal["first_name"], Literal["username"]]
            The fields to include in the form.
        """

        model = AppUser
        fields = ["first_name", "username"]
