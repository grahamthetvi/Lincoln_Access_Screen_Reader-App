# A part of NonVisual Desktop Access (NVDA)
# Copyright (C) 2006-2025 NV Access Limited
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

"""
This module contains localizable version information such as description, copyright and About messages etc.
As there are localizable strings at module level, this can only be imported once localization is set up via languageHandler.initialize.
To access version information for programmatic version checks before languageHandler.initialize, use the buildVersion module which contains all the non-localizable version information such as major and minor version, and version string etc.
"""

from buildVersion import (
	copyrightYears,
	name,
	url,
	version,
	version_detailed,
)

longName = _("Lincoln Access Screen Reader")
description = _("A free and open source screen reader for Microsoft Windows")
copyright = _("Copyright (C) {years} Addison Graham").format(
	years=copyrightYears,
)
aboutMessage = _(
	# Translators: "About" dialog box message for Lincoln Access Screen Reader
	"""{longName} ({name})
Version: {version} ({version_detailed})
URL: {url}
{copyright}

{name} is based on the NVDA open-source project (see https://www.nvaccess.org/). It is not affiliated with or endorsed by NV Access.

This software does not collect student personal information for the author or for analytics. Third-party update and add-on catalog features that could contact external servers are turned off in the default configuration.

{name} is covered by the GNU General Public License (Version 2 or later).
You are free to share or change this software in any way you like as long as it is accompanied by the license and you make all source code available to anyone who wants it.
This applies to both original and modified copies of this software, plus any derivative works.
For further details, you can view the license from the Help menu.
It can also be viewed online at: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html and https://www.gnu.org/licenses/gpl-3.0.en.html""",  # noqa: E501 line too long
).format(
	longName=longName,
	name=name,
	version=version,
	version_detailed=version_detailed,
	url=url,
	copyright=copyright,
)
