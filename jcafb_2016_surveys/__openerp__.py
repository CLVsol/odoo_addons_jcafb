# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol                  #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU Affero General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU Affero General Public License for more details.                          #
#                                                                              #
# You should have received a copy of the GNU Affero General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
################################################################################

{
    'name': 'JCAF 2016 Surveys',
    'version': '1.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'description': '''
This module will install all the JCAF 2016 surveys.
    ''',
    'depends': [
        'survey',
        'clv_document',
        'clv_patient',
        'clv_family',
        ],
    'data': [
        # 'survey_jcafb_2016_data.xml',
        'FSE16/survey_jcafb_FSE16.xml',
        'ISE16/survey_jcafb_ISE16.xml',
        'CSE16/survey_jcafb_CSE16.xml',
        'QMD16/survey_jcafb_QMD16.xml',
        # 'LMD16/survey_jcafb_LMD16.xml',
        'QAN16/survey_jcafb_QAN16.xml',
        'QDH16/survey_jcafb_QDH16.xml',
        'ITM16/survey_jcafb_ITM16.xml',
        'clv_document_view.xml',
        'clv_patient_view.xml',
        'clv_family_view.xml',
        ],
    'test': [],
    'installable': True,
    'active': False,
}
