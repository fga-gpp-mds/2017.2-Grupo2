# django
from django import forms
from django.utils.translation import ugettext_lazy as _

# local django
from chat import constants
from chat.models import Message
from user.models import User


class MessageValidator():
    """
    Validating Custom Exam fields.
    """

    def validator_text(self, text):
        """
        Validating text.
        """

        if text is not None and len(text) > constants.MAX_LENGTH_TEXT_MESSAGE:
            raise forms.ValidationError({'text': [_(constants.TEXT_SIZE)]})

    def validator_user_to(self, user_to):
        """
        Validating user.
        """
        email_from_database = User.objects.filter(email=user_to)

        if not email_from_database.exists():
            raise forms.ValidationError({'user_to': [_(constants.USER_EXISTS)]})

    def validator_subject(self, subject):
        """
        Validating subject.
        """

        if subject is not None and len(subject) > constants.MAX_LENGTH_TEXT_SUBJECT:
            raise forms.ValidationError({'subject': [_(constants.SUBJECT_SIZE)]})