from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields =["email","username","first_name", "last_name"]
        error_class = "error"

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields =["email","username","first_name", "last_name"]
        error_class = "error"



# from django import forms
# from django.utils.http import urlsafe_base64_encode
# from django.contrib.auth.tokens import default_token_generator
# from django.contrib.sites.shortcuts import get_current_site
# from django.contrib.auth import get_user_model
# from django.utils.encoding import force_bytes
# from django.core.mail import EmailMultiAlternatives
# from django.template import loader
# from django.utils.translation import ugettext_lazy as _
#
#
# User = get_user_model()
#
# class PasswordResetForm(forms.Form):
#     email = forms.EmailField(label=_("Email"), max_length=254)
#
#     def send_mail(self, subject_template_name, email_template_name,
#                   context, from_email, to_email, html_email_template_name=None):
#         """
#         Send a django.core.mail.EmailMultiAlternatives to `to_email`.
#         """
#         subject = loader.render_to_string(subject_template_name, context)
#         # Email subject *must not* contain newlines
#         subject = ''.join(subject.splitlines())
#         body = loader.render_to_string(email_template_name, context)
#
#         email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
#         if html_email_template_name is not None:
#             html_email = loader.render_to_string(html_email_template_name, context)
#             email_message.attach_alternative(html_email, 'text/html')
#
#         email_message.send()
#
#     def get_users(self, email):
#         """Given an email, return matching user(s) who should receive a reset.
#
#         This allows subclasses to more easily customize the default policies
#         that prevent inactive users and users with unusable passwords from
#         resetting their password.
#         """
#         active_users = User._default_manager.filter(**{
#             '%s__iexact' % User.get_email_field_name(): email,
#             'is_active': True,
#         })
#
#         if not active_users:
#             raise forms.ValidationError(_("The e-mail address is not assigned to any user account"),
#                                         code='invalid')
#         return (u for u in active_users if u.has_usable_password())
#
#     def save(self, domain_override=None,
#              subject_template_name='registration/password_reset_subject.txt',
#              email_template_name='registration/password_reset_email.html',
#              use_https=False, token_generator=default_token_generator,
#              from_email=None, request=None, html_email_template_name=None,
#              extra_email_context=None):
#         """
#         Generate a one-use only link for resetting password and send it to the
#         user.
#         """
#         email = self.cleaned_data["email"]
#         for user in self.get_users(email):
#             print('user')
#             print(user)
#             if not domain_override:
#                 current_site = get_current_site(request)
#                 site_name = current_site.name
#                 domain = current_site.domain
#             else:
#                 site_name = domain = domain_override
#             context = {
#                 'email': email,
#                 'domain': domain,
#                 'site_name': site_name,
#                 #'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
#                 'uid':urlsafe_base64_encode(force_bytes(user.pk)).encode().decode(),
#                 'user': user,
#                 'token': token_generator.make_token(user),
#                 'protocol': 'https' if use_https else 'http',
#             }
#             if extra_email_context is not None:
#                 context.update(extra_email_context)
#             self.send_mail(
#                 subject_template_name, email_template_name, context, from_email,
#                 email, html_email_template_name=html_email_template_name,
#             )