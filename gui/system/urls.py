#+
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

from django.conf.urls import patterns, url
from freenasUI.system.forms import (
    FirmwareWizard,
    FirmwareTemporaryLocationForm,
    FirmwareUploadForm,
    InitialWizard,
    InitialWizardConfirmForm,
    InitialWizardDSForm,
    InitialWizardShareFormSet,
    InitialWizardVolumeForm,
    InitialWizardVolumeImportForm
)

urlpatterns = patterns('freenasUI.system.views',
    url(r'^$', 'home', name="system_home"),
    url(r'^wizard/$', InitialWizard.as_view(
        [
            ('import', InitialWizardVolumeImportForm),
            ('volume', InitialWizardVolumeForm),
            ('ds', InitialWizardDSForm),
            ('shares', InitialWizardShareFormSet),
            ('confirm', InitialWizardConfirmForm),
        ],
        condition_dict={
            'import': InitialWizardVolumeImportForm.show_condition,
            'volume': InitialWizardVolumeForm.show_condition,
        },
    ), name='system_initialwizard'),
    url(r'^wizard/progress/$', 'initialwizard_progress', name="system_initialwizard_progress"),
    url(r'^reboot/$', 'reboot', name="system_reboot"),
    url(r'^reboot/dialog/$', 'reboot_dialog', name="system_reboot_dialog"),
    url(r'^reboot/run/$', 'reboot_run', name="system_reboot_run"),
    url(r'^shutdown/$', 'shutdown', name="system_shutdown"),
    url(r'^shutdown/dialog/$', 'shutdown_dialog', name="system_shutdown_dialog"),
    url(r'^shutdown/run/$', 'shutdown_run', name="system_shutdown_run"),
    url(r'^reporting/$', 'reporting', name="system_reporting"),
    url(r'^info/$', 'system_info', name="system_info"),
    url(r'^firmwizard/$', FirmwareWizard.as_view(
        [FirmwareTemporaryLocationForm, FirmwareUploadForm]
    ), name='system_firmwizard'),
    url(r'^firmwizard/progress/$', "firmware_progress", name="system_firmware_progress"),
    url(r'^config/restore/$', 'config_restore', name='system_configrestore'),
    url(r'^config/save/$', 'config_save', name='system_configsave'),
    url(r'^config/upload/$', 'config_upload', name='system_configupload'),
    url(r'^debug/$', 'debug', name='system_debug'),
    url(r'^backup/$', 'backup', name='system_backup'),
    url(r'^backup/progress$', 'backup_progress', name='system_backup_progress'),
    url(r'^backup/abort$', 'backup_abort', name='system_backup_abort'),
    url(r'^varlogmessages/(?P<lines>\d+)?/?$', 'varlogmessages', name="system_messages"),
    url(r'^top/', 'top', name="system_top"),
    url(r'^test-mail/$', 'testmail', name="system_testmail"),
    url(r'^lsdir/(?P<path>.*)$', 'directory_browser', name="system_dirbrowser"),
    url(r'^lsfiles/(?P<path>.*)$', 'file_browser', name="system_filebrowser"),
    url(r'^perftest/$', 'perftest', name='system_perftest'),
    url(r'^perftest/download/$', 'perftest_download', name='system_perftest_download'),
    url(r'^perftest/progress/$', 'perftest_progress', name='system_perftest_progress'),
    url(r'^restart-httpd/$', 'restart_httpd', name="system_restart_httpd"),
    url(r'^reload-httpd/$', 'reload_httpd', name="system_reload_httpd"),
    url(r'^terminal/$', 'terminal', name="system_terminal"),
    url(r'^terminal/paste/$', 'terminal_paste', name="system_terminal_paste"),
)
