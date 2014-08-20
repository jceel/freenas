# +
# Copyright 2010 iXsystems, Inc.
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
#####################################################################
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from freenasUI import choices
from freenasUI.freeadmin.models import Model
from freenasUI.middleware.notifier import notifier


class Alert(Model):
    message_id = models.CharField(
        unique=True,
        max_length=100,
        )
    dismiss = models.BooleanField(
        default=True,
        )


class Settings(Model):
    stg_guiprotocol = models.CharField(
            max_length=120,
            choices=choices.PROTOCOL_CHOICES,
            default="http",
            verbose_name=_("Protocol")
            )
    stg_guiaddress = models.CharField(
            max_length=120,
            blank=True,
            default='0.0.0.0',
            verbose_name=_("WebGUI IPv4 Address")
            )
    stg_guiv6address = models.CharField(
            max_length=120,
            blank=True,
            default='::',
            verbose_name=_("WebGUI IPv6 Address")
            )
    stg_guiport = models.IntegerField(
        verbose_name=_("WebGUI HTTP Port"),
        validators=[MinValueValidator(1), MaxValueValidator(65535)],
        default=80,
    )
    stg_guihttpsport = models.IntegerField(
        verbose_name=_("WebGUI HTTPS Port"),
        validators=[MinValueValidator(1), MaxValueValidator(65535)],
        default=443,
    )
    stg_guihttpsredirect = models.BooleanField(
        verbose_name=_('WebGUI HTTP -> HTTPS Redirect'),
        default=True,
        help_text=_(
            'Redirect HTTP (port 80) to HTTPS when only the HTTPS protocol is '
            'enabled'
        ),
    )
    stg_language = models.CharField(
            max_length=120,
            choices=settings.LANGUAGES,
            default="en",
            verbose_name=_("Language")
            )
    stg_kbdmap = models.CharField(
            max_length=120,
            choices=choices.KBDMAP_CHOICES(),
            verbose_name=_("Console Keyboard Map"),
            blank=True,
            )
    stg_timezone = models.CharField(
            max_length=120,
            choices=choices.TimeZoneChoices(),
            default="America/Los_Angeles",
            verbose_name=_("Timezone")
            )
    stg_syslogserver = models.CharField(
            default='',
            blank=True,
            max_length=120,
            verbose_name=_("Syslog server")
            )

    class Meta:
        verbose_name = _("Settings")


class NTPServer(Model):
    ntp_address = models.CharField(
            verbose_name=_("Address"),
            max_length=120,
            )
    ntp_burst = models.BooleanField(
            verbose_name=_("Burst"),
            default=False,
            help_text=_("When the server is reachable, send a burst of eight "
                "packets instead of the usual one. This is designed to improve"
                " timekeeping quality with the server command and s addresses."
                ),
            )
    ntp_iburst = models.BooleanField(
            verbose_name=_("IBurst"),
            default=True,
            help_text=_("When the server is unreachable, send a burst of eight"
                " packets instead of the usual one. This is designed to speed "
                "the initial synchronization acquisition with the server "
                "command and s addresses."),
            )
    ntp_prefer = models.BooleanField(
            verbose_name=_("Prefer"),
            default=False,
            help_text=_("Marks the server as preferred. All other things being"
                " equal, this host will be chosen for synchronization among a "
                "set of correctly operating hosts."),
            )
    ntp_minpoll = models.IntegerField(
            verbose_name=_("Min. Poll"),
            default=6,
            validators=[MinValueValidator(4)],
            help_text=_("The minimum poll interval for NTP messages, as a "
                "power of 2 in seconds. Defaults to 6 (64 s), but can be "
                "decreased to a lower limit of 4 (16 s)"),
            )
    ntp_maxpoll = models.IntegerField(
            verbose_name=_("Max. Poll"),
            default=10,
            validators=[MaxValueValidator(17)],
            help_text=_("The maximum poll interval for NTP messages, as a "
                "power of 2 in seconds. Defaults to 10 (1,024 s), but can be "
                "increased to an upper limit of 17 (36.4 h)"),
            )

    def __unicode__(self):
        return self.ntp_address

    def delete(self):
        super(NTPServer, self).delete()
        notifier().start("ix-ntpd")
        notifier().restart("ntpd")

    class Meta:
        verbose_name = _("NTP Server")
        verbose_name_plural = _("NTP Servers")
        ordering = ["ntp_address"]

    class FreeAdmin:
        icon_model = u"NTPServerIcon"
        icon_object = u"NTPServerIcon"
        icon_view = u"ViewNTPServerIcon"
        icon_add = u"AddNTPServerIcon"


class Advanced(Model):
    adv_consolemenu = models.BooleanField(
        verbose_name=_("Enable Console Menu"),
        default=False,
    )
    adv_serialconsole = models.BooleanField(
        verbose_name=_("Use Serial Console"),
        default=False,
    )
    adv_serialport = models.CharField(
        max_length=120,
        default="0x2f8",
        help_text=_(
            "Set this to match your serial port address (0x3f8, 0x2f8, etc.)"
        ),
        verbose_name=_("Serial Port Address"),
        choices=choices.SERIAL_CHOICES(),
    )
    adv_serialspeed = models.CharField(
            max_length=120,
            choices=choices.SERIAL_SPEED,
            default="9600",
            help_text=_("Set this to match your serial port speed"),
            verbose_name=_("Serial Port Speed")
            )
    adv_consolescreensaver = models.BooleanField(
        verbose_name=_("Enable screen saver"),
        default=False,
    )
    adv_powerdaemon = models.BooleanField(
        verbose_name=_("Enable powerd (Power Saving Daemon)"),
        default=False,
    )
    adv_swapondrive = models.IntegerField(
            validators=[MinValueValidator(0)],
            verbose_name=_("Swap size on each drive in GiB, affects new disks "
                "only. Setting this to 0 disables swap creation completely "
                "(STRONGLY DISCOURAGED)."),
            default=2)
    adv_consolemsg = models.BooleanField(
            verbose_name=_("Show console messages in the footer"),
            default=True)
    adv_traceback = models.BooleanField(
            verbose_name=_("Show tracebacks in case of fatal errors"),
            default=True)
    adv_advancedmode = models.BooleanField(
            verbose_name=_("Show advanced fields by default"),
            default=False)
    adv_autotune = models.BooleanField(
            verbose_name=_("Enable autotune"),
            default=False)
    adv_debugkernel = models.BooleanField(
            verbose_name=_("Enable debug kernel"),
            default=False)
    adv_uploadcrash = models.BooleanField(
        verbose_name=_("Enable automatic upload of kernel crash dumps"),
        default=True,
    )
    adv_anonstats = models.BooleanField(
            verbose_name=_("Enable report anonymous statistics"),
            default=True,
            editable=False)
    adv_anonstats_token = models.TextField(
            blank=True,
            editable=False)
    # TODO: need geom_eli in kernel
    #adv_encswap = models.BooleanField(
    #        verbose_name = _("Encrypt swap space"),
    #        default=False)
    adv_motd = models.TextField(
        max_length=1024,
        verbose_name=_("MOTD banner"),
        default='Welcome',
    )

    class Meta:
        verbose_name = _("Advanced")

    class FreeAdmin:
        deletable = False


class Email(Model):
    em_fromemail = models.CharField(
            max_length=120,
            verbose_name=_("From email"),
            help_text=_("An email address that the system will use for the "
                "sending address for mail it sends, eg: freenas@example.com"),
            default='',
            )
    em_outgoingserver = models.CharField(
            max_length=120,
            verbose_name=_("Outgoing mail server"),
            help_text=_("A hostname or ip that will accept our mail, for "
                "instance mail.example.org, or 192.168.1.1"),
            blank=True
            )
    em_port = models.IntegerField(
            default=25,
            validators=[MinValueValidator(1), MaxValueValidator(65535)],
            help_text=_("An integer from 1 - 65535, generally will be 25, "
                "465, or 587"),
            verbose_name=_("Port to connect to")
            )
    em_security = models.CharField(
            max_length=120,
            choices=choices.SMTPAUTH_CHOICES,
            default="plain",
            help_text=_("encryption of the connection"),
            verbose_name=_("TLS/SSL")
            )
    em_smtp = models.BooleanField(
            verbose_name=_("Use SMTP Authentication"),
            default=False
            )
    em_user = models.CharField(
            blank=True,
            null=True,
            max_length=120,
            verbose_name=_("Username"),
            help_text=_("A username to authenticate to the remote server"),
            )
    em_pass = models.CharField(
            blank=True,
            null=True,
            max_length=120,
            verbose_name=_("Password"),
            help_text=_("A password to authenticate to the remote server"),
            )

    class Meta:
        verbose_name = _("Email")

    class FreeAdmin:
        deletable = False


class SSL(Model):
    ssl_org = models.CharField(
            blank=True,
            null=True,
            max_length=120,
            verbose_name=_("Organization"),
            help_text=_("Organization Name (eg, company)"),
            )
    ssl_unit = models.CharField(
            blank=True,
            null=True,
            max_length=120,
            verbose_name=_("Organizational Unit"),
            help_text=_("Organizational Unit Name (eg, section)"),
            )
    ssl_email = models.CharField(
            blank=True,
            null=True,
            max_length=120,
            verbose_name=_("Email Address"),
            help_text=_("Email Address"),
            )
    ssl_city = models.CharField(
            blank=True,
            null=True,
            max_length=120,
            verbose_name=_("Locality"),
            help_text=_("Locality Name (eg, city)"),
            )
    ssl_state = models.CharField(
            blank=True,
            null=True,
            max_length=120,
            verbose_name=_("State"),
            help_text=_("State or Province Name (full name)"),
            )
    ssl_country = models.CharField(
            blank=True,
            null=True,
            max_length=120,
            verbose_name=_("Country"),
            help_text=_("Country Name (2 letter code)"),
            )
    ssl_common = models.CharField(
            blank=True,
            null=True,
            max_length=120,
            verbose_name=_("Common Name"),
            help_text=_("Common Name (eg, YOUR name)"),
            )
    ssl_passphrase = models.CharField(
            blank=True,
            null=True,
            max_length=120,
            verbose_name=_("Passphrase"),
            help_text=_("Private key passphrase"),
            )
    ssl_certfile = models.TextField(
            blank=True,
            null=True,
            verbose_name=_("SSL Certificate"),
            help_text=_("Cut and paste the contents of your private and "
                "public certificate files here."),
            )

    class Meta:
        verbose_name = _("SSL")

    class FreeAdmin:
        deletable = False


class Tunable(Model):
    tun_var = models.CharField(
            max_length=50,
            unique=True,
            verbose_name=_("Variable"),
            )
    tun_value = models.CharField(
            max_length=50,
            verbose_name=_("Value"),
            )
    tun_type = models.CharField(
        verbose_name=_('Type'),
        max_length=20,
        choices=choices.TUNABLE_TYPES,
        default='loader',
    )
    tun_comment = models.CharField(
            max_length=100,
            verbose_name=_("Comment"),
            blank=True,
            )
    tun_enabled = models.BooleanField(
            default=True,
            verbose_name=_("Enabled"),
            )

    def __unicode__(self):
        return unicode(self.tun_var)

    def delete(self):
        super(Tunable, self).delete()
        if self.tun_type == 'loader':
            notifier().reload("loader")
        else:
            notifier().reload("sysctl")

    class Meta:
        verbose_name = _("Tunable")
        verbose_name_plural = _("Tunables")
        ordering = ["tun_var"]

    class FreeAdmin:
        icon_model = u"TunableIcon"
        icon_object = u"TunableIcon"
        icon_add = u"AddTunableIcon"
        icon_view = u"ViewTunableIcon"


class Registration(Model):
    reg_firstname = models.CharField(
            max_length=120,
            verbose_name=_("First Name")
            )
    reg_lastname = models.CharField(
            max_length=120,
            verbose_name=_("Last Name")
            )
    reg_company = models.CharField(
            max_length=120,
            verbose_name=_("Company"),
            blank=True,
            null=True
            )
    reg_address = models.CharField(
            max_length=120,
            verbose_name=_("Address"),
            blank=True,
            null=True
            )
    reg_city = models.CharField(
            max_length=120,
            verbose_name=_("City"),
            blank=True,
            null=True
            )
    reg_state = models.CharField(
            max_length=120,
            verbose_name=_("State"),
            blank=True,
            null=True
            )
    reg_zip = models.CharField(
            max_length=120,
            verbose_name=_("Zip"),
            blank=True,
            null=True
            )
    reg_email = models.CharField(
            max_length=120,
            verbose_name=_("Email")
            )
    reg_homephone = models.CharField(
            max_length=120,
            verbose_name=_("Home Phone"),
            blank=True,
            null=True
            )
    reg_cellphone = models.CharField(
            max_length=120,
            verbose_name=_("Cell Phone"),
            blank=True,
            null=True
            )
    reg_workphone = models.CharField(
            max_length=120,
            verbose_name=_("Work Phone"),
            blank=True,
            null=True
            )

    class Meta:
        verbose_name = _("Registration")

    class FreeAdmin:
        deletable = False


class SystemDataset(Model):
    sys_pool = models.CharField(
        max_length=1024,
        blank=True,
        verbose_name=_("Pool"),
        choices=()
    )
    sys_syslog_usedataset = models.BooleanField(
        default=False,
        verbose_name=_("Syslog")
    )
    sys_rrd_usedataset = models.BooleanField(
        default=False,
        verbose_name=_("Reporting Database"),
        help_text=_(
            'Save the Round-Robin Database (RRD) used by system statistics '
            'collection daemon into the system dataset'
        )
    )

    class Meta:
        verbose_name = _("System Dataset")

    class FreeAdmin:
        deletable = False
        icon_model = u"SystemDatasetIcon"
        icon_object = u"SystemDatasetIcon"
        icon_view = u"SystemDatasetIcon"
        icon_add = u"SystemDatasetIcon"

    @property
    def usedataset(self):
        return self.sys_syslog_usedataset


class Backup(Model):
    bak_finished = models.BooleanField(
        default=False,
        verbose_name=_("Finished")
    )

    bak_failed = models.BooleanField(
        default=False,
        verbose_name=_("Failed")
    )

    bak_acknowledged = models.BooleanField(
        default=False,
        verbose_name=_("Acknowledged")
    )

    bak_worker_pid = models.IntegerField(
        verbose_name=_("Backup worker PID"),
        null=True
    )

    bak_started_at = models.DateTimeField(
        verbose_name=_("Started at")
    )

    bak_finished_at = models.DateTimeField(
        verbose_name=_("Finished at"),
        null=True
    )

    bak_destination = models.CharField(
        max_length=1024,
        blank=True,
        verbose_name=_("Destination")
    )

    bak_status = models.CharField(
        max_length=1024,
        blank=True,
        verbose_name=_("Status")
    )

    class FreeAdmin:
        deletable = False

    class Meta:
        verbose_name = _("System Backup")
