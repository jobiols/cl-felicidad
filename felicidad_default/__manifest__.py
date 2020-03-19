# -----------------------------------------------------------------------------
#
#    Copyright (C) 2020 jeo Software  (http://www.jeosoft.com.ar)
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
        # Repo externos
        'https://github.com/CybroOdoo/CybroAddons.git CybroOdoo-CybroAddons',
        'https://github.com/it-projects-llc/access-addons.git it-projects-llc-access-addons',
        'https://github.com/it-projects-llc/misc-addons.git it-projects-llc-misc-addons',
        'https://github.com/it-projects-llc/pos-addons.git it-projects-llc-pos-addons',
        'https://github.com/it-projects-llc/project.git it-projects-llc-project',
        'https://github.com/it-projects-llc/website-addons.git it-projects-llc-website-addons',
        'https://github.com/JayVora-SerpentCS/SerpentCS_Contributions.git JayVora-SerpentCS-SerpentCS_Contributions',
        'https://github.com/Vauxoo/addons-vauxoo.git Vauxoo-addons-vauxoo',
        'https://github.com/SythilTech/Odoo.git SythilTech-Odoo',
        'https://github.com/pledra/odoo-product-configurator.git pledra-odoo-product-configurator',
        'https://github.com/jobiols/rafi16jan-backend-theme.git jobiols-rafi16jan-backend-theme',
        'https://github.com/jobiols/odoo-addons.git jobiols-odoo-addons',
        'https://github.com/regaby/odoo-addons.git regaby-odoo-addons',
        # Repo Ingadhoc
        'https://github.com/ingadhoc/account-analytic.git ingadhoc-account-analytic',
        'https://github.com/ingadhoc/account-financial-tools.git ingadhoc-account-financial-tools',
        'https://github.com/ingadhoc/account-invoicing.git ingadhoc-account-invoicing',
        'https://github.com/ingadhoc/account-payment.git ingadhoc-account-payment',
        'https://github.com/ingadhoc/aeroo_reports.git ingadhoc-aeroo_reports',
        'https://github.com/ingadhoc/argentina-reporting.git ingadhoc-argentina-reporting',
        'https://github.com/ingadhoc/argentina-sale.git ingadhoc-argentina-sale',
        'https://github.com/ingadhoc/hr.git ingadhoc-hr',
        'https://github.com/ingadhoc/manufacture.git ingadhoc-manufacture',
        'https://github.com/ingadhoc/miscellaneous.git ingadhoc-miscellaneous',
        'https://github.com/ingadhoc/multi-company.git ingadhoc-multi-company',
        'https://github.com/ingadhoc/multi-store.git ingadhoc-multi-store',
        'https://github.com/ingadhoc/odoo-argentina.git ingadhoc-odoo-argentina',
        'https://github.com/ingadhoc/odoo-support.git ingadhoc-odoo-support',
        'https://github.com/ingadhoc/partner.git ingadhoc-partner',
        'https://github.com/ingadhoc/patches.git ingadhoc-patches',
        'https://github.com/ingadhoc/product.git ingadhoc-product',
        'https://github.com/ingadhoc/project.git ingadhoc-project',
        'https://github.com/ingadhoc/purchase.git ingadhoc-purchase',
        'https://github.com/ingadhoc/reporting-engine.git ingadhoc-reporting-engine',
        'https://github.com/ingadhoc/sale.git ingadhoc-sale',
        'https://github.com/ingadhoc/stock.git ingadhoc-stock',
        'https://github.com/ingadhoc/website.git ingadhoc-website',
        'https://github.com/ingadhoc/survey.git ingadhoc-survey',
        # Repo OCA
        'https://github.com/OCA/account-analytic.git OCA-account-analytic',
        'https://github.com/OCA/account-closing.git OCA-account-closing',
        'https://github.com/OCA/account-financial-reporting.git OCA-account-financial-reporting',
        'https://github.com/OCA/account-financial-tools.git OCA-account-financial-tools',
        'https://github.com/OCA/account-invoice-reporting.git OCA-account-invoice-reporting',
        'https://github.com/OCA/account-invoicing.git OCA-account-invoicing',
        'https://github.com/OCA/account-payment.git OCA-account-payment',
        'https://github.com/OCA/account-reconcile.git OCA-account-reconcile',
        'https://github.com/OCA/bank-payment.git OCA-bank-payment',
        'https://github.com/OCA/commission.git OCA-commission',
        'https://github.com/OCA/contract.git OCA-contract',
        'https://github.com/OCA/credit-control.git OCA-credit-control',
        'https://github.com/OCA/crm.git OCA-crm',
        'https://github.com/OCA/currency.git OCA-currency',
        'https://github.com/OCA/donation.git OCA-donation',
        'https://github.com/OCA/e-commerce.git OCA-e-commerce',
        'https://github.com/OCA/event.git OCA-event',
        'https://github.com/OCA/field-service.git OCA-field-service',
        'https://github.com/OCA/geospatial.git OCA-geospatial',
        'https://github.com/OCA/hr.git OCA-hr',
        'https://github.com/OCA/hr-timesheet.git OCA-hr-timesheet',
        'https://github.com/OCA/knowledge.git OCA-knowledge',
        'https://github.com/OCA/manufacture.git OCA-manufacture',
        'https://github.com/OCA/manufacture-reporting.git OCA-manufacture-reporting',
        'https://github.com/OCA/multi-company.git OCA-multi-company',
        'https://github.com/OCA/OpenUpgrade.git OCA-OpenUpgrade',
        'https://github.com/OCA/partner-contact.git OCA-partner-contact',
        'https://github.com/OCA/pos.git OCA-pos',
        'https://github.com/OCA/product-attribute.git OCA-product-attribute',
        'https://github.com/OCA/product-variant.git OCA-product-variant',
        'https://github.com/OCA/project.git OCA-project',
        'https://github.com/OCA/project-reporting.git OCA-project-reporting',
        'https://github.com/OCA/purchase-workflow.git OCA-purchase-workflow',
        'https://github.com/OCA/queue.git OCA-queue',
        'https://github.com/OCA/reporting-engine.git OCA-reporting-engine',
        'https://github.com/OCA/report-print-send.git OCA-report-print-send',
        'https://github.com/OCA/rma.git OCA-rma',
        'https://github.com/OCA/sale-reporting.git OCA-sale-reporting',
        'https://github.com/OCA/sale-workflow.git OCA-sale-workflow',
        'https://github.com/OCA/server-auth.git OCA-server-auth',
        'https://github.com/OCA/server-backend.git OCA-server-backend',
        'https://github.com/OCA/server-tools.git OCA-server-tools',
        'https://github.com/OCA/server-ux.git OCA-server-ux',
        'https://github.com/OCA/social.git OCA-social',
        'https://github.com/OCA/stock-logistics-barcode.git OCA-stock-logistics-barcode',
        'https://github.com/OCA/stock-logistics-reporting.git OCA-stock-logistics-reporting',
        'https://github.com/OCA/stock-logistics-warehouse.git OCA-stock-logistics-warehouse',
        'https://github.com/OCA/stock-logistics-workflow.git OCA-stock-logistics-workflow',
        'https://github.com/OCA/survey.git OCA-survey',
        'https://github.com/OCA/timesheet.git OCA-timesheet',
        'https://github.com/OCA/vertical-association.git OCA-vertical-association',
        'https://github.com/OCA/vertical-hotel.git OCA-vertical-hotel',
        'https://github.com/OCA/web.git OCA-web',
        'https://github.com/OCA/website.git OCA-website',
        'https://github.com/OCA/ddmrp.git OCA-ddmrp',
        'https://github.com/OCA/mis-builder.git OCA-mis-builder',
    ],

    'docker-images': [
        'odoo jobiols/odoo-jeo:11.0',
        'postgres postgres:11.1-alpine',
        'aeroo adhoc/aeroo-docs',
        'nginx nginx'
    ]
}
