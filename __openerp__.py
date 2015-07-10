# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2015- Oy Tawasta Technologies Ltd. (http://www.tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Sale Opportunity Connector',
    'category': 'Sale',
    'version': '0.1',
    'author': 'Oy Tawasta Technologies Ltd.',
    'website': 'http://www.tawasta.fi',
    'depends': [
        'crm',
        'crm_lead_to_sale',
        'sale',
    ],
    'description': '''
Sale Opportunity Connector
==================

Links Opportunity and sale to work together as seamlessly as possible


Features
========
* Adds sale actions to crm case stage
''',
    'data': [
        'views/crm_case_stage_form.xml',
        'views/crm_case_stage_tree.xml',
    ],
}
