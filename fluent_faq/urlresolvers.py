from django.conf import settings
from django.core.urlresolvers import reverse

_HAS_FLUENT_PAGES = ('fluent_pages' in settings.INSTALLED_APPS)
if _HAS_FLUENT_PAGES:
    from fluent_pages.urlresolvers import mixed_reverse


def faq_reverse(viewname, args=None, kwargs=None, current_app='fluent_faq', current_page=None, language_code=None, multiple=False, ignore_multiple=False):
    """
    Reverse a URL to the blog, taking various configuration options into account.

    This is a compatibility function to allow django-fluent-faq to operate stand-alone.
    Either the app can be hooked in the URLconf directly, or it can be added as a pagetype of *django-fluent-pages*.
    """
    if _HAS_FLUENT_PAGES:
        return mixed_reverse(viewname, args=args, kwargs=kwargs, current_page=current_page, language_code=language_code, multiple=multiple, ignore_multiple=ignore_multiple)
    else:
        return reverse(viewname, args=args, kwargs=kwargs, current_app=current_app)


__all__ = (
    'faq_reverse',
)
