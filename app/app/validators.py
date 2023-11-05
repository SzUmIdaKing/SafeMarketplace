from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class MaxLengthValidator:
    def __init__(self, max_length=128):
        self.max_length = max_length

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise ValidationError(
                _("Password must not exceed %(max_length)d characters."),
                code="password_too_long",
                params={"max_length": self.max_length},
            )


class NoTruncationValidator:
    def validate(self, password, user=None):
        if len(password) < len(password.lstrip()):
            raise ValidationError(
                _("Password truncation is not allowed."),
                code="password_truncation",
            )

    def get_help_text(self):
        return _("Consecutive multiple spaces may be replaced by a single space.")

class UnicodeCharacterValidator:
    def validate(self, password, user=None):
        if not any(ord(char) >= 32 and ord(char) <= 126 or ord(char) >= 128 for char in password):
            raise ValidationError(
                _("Password must include at least one printable Unicode character."),
                code="password_no_unicode",
            )

    def get_help_text(self):
        return _("Any printable Unicode character, including spaces and Emojis, is allowed in passwords.")
