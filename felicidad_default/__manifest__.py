# -----------------------------------------------------------------------------
#
#    Copyright (C) 2019  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------
{
    'name': 'felicidad',
    'version': '11.0.0.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Default Application',
    'summary': 'Customization for felicidad',
    'author': 'jeo Software',
    'depends': [
        # basic applications
        #'sale_management',
        #'account_invoicing',
        #'purchase',

        # minimum modules for argentinian localizacion + utilities + fixes
        # 'standard_depends',
    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    #
    # Here begins docker-odoo-environment manifest
    # --------------------------------------------
    # manifest version
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'Enterprise': False,

    # port where odoo starts serving pages
    'port': '8069',

    'git-repos': [
        'https://github.com/jobiols/cl-felicidad.git',
        'https://github.com/it-projects-llc/access-addons.git it-projects-llc-access-addons',
    ],

    # example images version 2
    'docker-images': [
        'odoo jobiols/odoo-jeo:11.0',
        'postgres postgres:11.1-alpine',
        'aeroo adhoc/aeroo'
    ]
}
