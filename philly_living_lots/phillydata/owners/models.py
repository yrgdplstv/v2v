from django.db import models
from django.utils.translation import ugettext_lazy as _

import reversion


class Owner(models.Model):

    name = models.CharField(_('name'),
        max_length=256,
        unique=True,
    )

    OWNER_TYPE_CHOICES = (
        ('private', 'private'),
        ('public', 'public'),
    )
    owner_type = models.CharField(_('owner type'),
        choices=OWNER_TYPE_CHOICES,
        default='public',
        max_length=20,
    )

    aliases = models.ManyToManyField('Alias',
        help_text=_('Other names for this owner'),
        verbose_name=_('aliases'),
        blank=True,
        null=True,
    )
    agency_codes = models.ManyToManyField('AgencyCode',
        help_text=_('Agency codes used to refer to this owner'),
        verbose_name=_('agency codes'),
        blank=True,
        null=True,
    )
    account_owners = models.ManyToManyField('opa.AccountOwner',
        help_text=_('OPA account owners this owner contains'),
        verbose_name=_('account owners'),
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.owner_type)


class AgencyCode(models.Model):
    """
    A code used in city data that refers to an agency as a property owner.

    """
    code = models.CharField(_('code'),
        max_length=256,
        unique=True,
    )

    def __unicode__(self):
        return self.code


class Alias(models.Model):
    name = models.CharField(_('name'),
        max_length=256,
        unique=True,
    )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('alias')
        verbose_name_plural = _('aliases')

reversion.register(Owner)
