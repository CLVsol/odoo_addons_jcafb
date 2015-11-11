#!/usr/bin/env python
# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2014-Today  Carlos Eduardo Vercelino - CLVsol                  #
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

import yaml

def survey_colunm(doc, yaml_out_file, xml_file, txt_file, key1, key2, key3, key4, question_type, question_id, collumn_sequence):

    _title_ = doc[key1][key2][key3][key4]['title'].encode("utf-8")
    _model_ = doc[key1][key2][key3][key4]['model']
    if collumn_sequence < 100:
        _id_ = question_id + '_0' + str(collumn_sequence / 10)
    else:
        _id_ = question_id + '_' + str(collumn_sequence / 10)
    _question_id_ = question_id
    _sequence_ = str(collumn_sequence)

    yaml_out_file.write('            %s:\n' % (_id_))
    yaml_out_file.write('                model: %s\n' % (_model_))
    yaml_out_file.write('                title: \'%s\'\n' % (_title_))

    _title_ = '[' + _id_ + '] ' + _title_

    txt_file.write('            %s\n' % (_title_))

    xml_file.write('                    <record model="%s" id="%s">\n' % (_model_, _id_))
    xml_file.write('                        <field name="title">%s</field>\n' % (_title_))
    xml_file.write('                        <field name="question_id" ref="%s"/>\n' % (_question_id_))
    #xml_file.write('                        <field name="sequence" eval="%s"/>\n' % (_sequence_))

    yaml_out_file.write('\n')

    xml_file.write('                    </record>\n')
    xml_file.write('\n')

def survey_answer(doc, yaml_out_file, xml_file, txt_file, key1, key2, key3, key4, question_type, question_id, answer_sequence):

    _answer_ = doc[key1][key2][key3][key4]['answer'].encode("utf-8")
    _model_ = doc[key1][key2][key3][key4]['model']
    if answer_sequence < 100:
        _id_ = question_id + '_0' + str(answer_sequence / 10)
    else:
        _id_ = question_id + '_' + str(answer_sequence / 10)
    _question_id_ = question_id
    _sequence_ = str(answer_sequence)

    yaml_out_file.write('            %s:\n' % (_id_))
    yaml_out_file.write('                model: %s\n' % (_model_))
    yaml_out_file.write('                answer: \'%s\'\n' % (_answer_))

    _answer_ = '[' + _id_ + '] ' + _answer_

    if  question_type == 'multiple_textboxes_diff_type':
        txt_file.write('            %s____________________________________\n' % (_answer_))
    else:
        txt_file.write('            %s\n' % (_answer_))

    xml_file.write('                    <record model="%s" id="%s">\n' % (_model_, _id_))
    xml_file.write('                        <field name="answer">%s</field>\n' % (_answer_))
    xml_file.write('                        <field name="question_id" ref="%s"/>\n' % (_question_id_))
    xml_file.write('                        <field name="sequence" eval="%s"/>\n' % (_sequence_))
    try:
        _type_ = doc[key1][key2][key3][key4]['type']
        yaml_out_file.write('                type: %s\n' % (_type_))
        xml_file.write('                        <field name="type">%s</field>\n' % (_type_))
    except Exception, e:
        pass

    yaml_out_file.write('\n')

    xml_file.write('                    </record>\n')
    xml_file.write('\n')

def survey_question(doc, yaml_out_file, xml_file, txt_file, key1, key2, key3, page_id, question_sequence):

    _question_ = doc[key1][key2][key3]['question'].encode("utf-8")
    _type_ = doc[key1][key2][key3]['type']
    _model_ = doc[key1][key2][key3]['model']
    if question_sequence < 100:
        _id_ = page_id + '_0' + str(question_sequence / 10)
    else:
        _id_ = page_id + '_' + str(question_sequence / 10)
    _page_id_ = page_id
    _sequence_ = str(question_sequence)
    _constr_mandatory_ = str(doc[key1][key2][key3]['constr_mandatory'])
    _constr_err_msg_ = doc[key1][key2][key3]['constr_err_msg'].encode("utf-8")

    yaml_out_file.write('        %s:\n' % (_id_))
    yaml_out_file.write('            model: %s\n' % (_model_))
    yaml_out_file.write('            question: \'%s\'\n' % (_question_))
    yaml_out_file.write('            type: %s\n' % (_type_))
    yaml_out_file.write('            constr_mandatory: %s\n' % (_constr_mandatory_))
    yaml_out_file.write('            constr_err_msg: \'%s\'\n' % (_constr_err_msg_))

    _question_ = '[' + _id_ + '] ' + _question_

    txt_file.write('        %s\n' % (_question_))
    txt_file.write('            (%s)\n' % (_type_))

    xml_file.write('                <record model="%s" id="%s">\n' % (_model_, _id_))
    xml_file.write('                    <field name="question">%s</field>\n' % (_question_))
    xml_file.write('                    <field name="type">%s</field>\n' % (_type_))
    xml_file.write('                    <field name="page_id" ref="%s"/>\n' % (_page_id_))
    xml_file.write('                    <field name="sequence" eval="%s"/>\n' % (_sequence_))
    xml_file.write('                    <field name="constr_mandatory">%s</field>\n' % (_constr_mandatory_))
    xml_file.write('                    <field name="constr_err_msg">%s</field>\n' % (_constr_err_msg_))

    _comments_allowed_ = 'False'
    _comments_message_ = ''
    try:
        _comments_allowed_ = str(doc[key1][key2][key3]['comments_allowed'])
        yaml_out_file.write('            comments_allowed: %s\n' % (_comments_allowed_))
        xml_file.write('                    <field name="comments_allowed">%s</field>\n' % (_comments_allowed_))
    except Exception, e:
        print '             Missing: "%s"' % (e)
    try:
        _comments_message_ = doc[key1][key2][key3]['comments_message'].encode("utf-8")
        yaml_out_file.write('            comments_message: \'%s\'\n' % (_comments_message_))
        xml_file.write('                    <field name="comments_message">%s</field>\n' % (_comments_message_))
    except Exception, e:
        print '             Missing: "%s"' % (e)

    try:
        _display_mode_ = doc[key1][key2][key3]['display_mode']
        yaml_out_file.write('            display_mode: %s\n' % (_display_mode_))
        xml_file.write('                    <field name="display_mode">%s</field>\n' % (_display_mode_))
    except Exception, e:
        print '             Missing: "%s"' % (e)
    
    try:
        _column_nb_ = doc[key1][key2][key3]['column_nb']
        yaml_out_file.write('            column_nb: %s\n' % (_column_nb_))
        xml_file.write('                    <field name="column_nb">%s</field>\n' % (_no_of_rows_))
    except Exception, e:
        pass

    yaml_out_file.write('\n')

    xml_file.write('                </record>\n')
    xml_file.write('\n')

    if  (_type_ == 'textbox') or \
        (_type_ == 'datetime'):
        txt_file.write('            ' + '____________________________________\n')

    # else:
    #     answer_sequence = 0
    #     for key4 in sorted(doc[key1][key2][key3].keys()):
    #         try:
    #             _model_ = doc[key1][key2][key3][key4]['model']
    #             print '            ', key4, _model_
    #             if _model_ == 'survey.answer':
    #                 answer_sequence += 10
    #                 survey_answer(doc, yaml_out_file, xml_file, txt_file, key1, key2, key3, key4, _type_, _id_, answer_sequence)
    #             if _model_ == 'survey.question.column.heading':
    #                 answer_sequence += 10
    #                 survey_colunm(doc, yaml_out_file, xml_file, txt_file, key1, key2, key3, key4, _type_, _id_, answer_sequence)
    #         except Exception, e:
    #             pass

    # try:
    #     _comments_allowed_ = doc[key1][key2][key3]['comments_allowed']
    #     if _comments_allowed_ == 'True':
    #         _comments_message_ = doc[key1][key2][key3]['comments_message'].encode("utf-8")
    #         txt_file.write('            %s____________________________________\n' % _comments_message_)
    # except Exception, e:
    #     pass
    if _comments_allowed_ == 'True':
        txt_file.write('            %s____________________________________\n' % _comments_message_)

def survey_page(doc, yaml_out_file, xml_file, txt_file, key1, key2, survey_id, page_sequence):

    _title_ = doc[key1][key2]['title'].encode("utf-8")
    _model_ = doc[key1][key2]['model']
    if page_sequence < 100:
        _id_ = survey_id + '_0' + str(page_sequence / 10)
    else:
        _id_ = survey_id + '_' + str(page_sequence / 10)
    _description_ = doc[key1][key2]['description'].encode("utf-8")
    _survey_id_ = key1
    _sequence_ = str(page_sequence)

    yaml_out_file.write('    %s:\n' % (_id_))
    yaml_out_file.write('        model: %s\n' % (_model_))
    yaml_out_file.write('        title: \'%s\'\n' % (_title_))
    yaml_out_file.write('        description: \'%s\'\n' % (_description_))
    yaml_out_file.write('\n')

    _title_ = '[' + _id_ + '] ' + _title_
    _description_ = '[' + _id_ + '] ' + _description_

    txt_file.write('    %s\n' % (_title_))

    xml_file.write('            <record model="%s" id="%s">\n' % (_model_, _id_))
    xml_file.write('                <field name="title">%s</field>\n' % (_title_))
    xml_file.write('                <field name="survey_id" ref="%s"/>\n' % (_survey_id_))
    xml_file.write('                <field name="sequence" eval="%s"/>\n' % (_sequence_))
    xml_file.write('                <field name="description">&lt;p&gt;%s&lt;/p&gt;</field>\n' % (_description_))
    xml_file.write('            </record>' + '\n')
    xml_file.write('\n')

    question_sequence = 0
    for key3 in sorted(doc[key1][key2].keys()):
        try:
            _model_ = doc[key1][key2][key3]['model']
            print '        ', key3, _model_
            if _model_ == 'survey.question':

                question_sequence += 10
                survey_question(doc, yaml_out_file, xml_file, txt_file, key1, key2, key3, _id_, question_sequence)
        except Exception, e:
            pass

def survey(doc, yaml_out_file, xml_file, txt_file, key1):

    _title_ = doc[key1]['title'].encode("utf-8")
    _model_ = doc[key1]['model']
    _id_ = key1
    _stage_id_ = doc[key1]['stage_id']
    _auth_required_ = doc[key1]['auth_required']
    _users_can_go_back_ = doc[key1]['users_can_go_back']
    _description_ = doc[key1]['description'].encode("utf-8")
    _thank_you_message_ = doc[key1]['thank_you_message'].encode("utf-8")

    yaml_out_file.write('%s:\n' % (key1))
    yaml_out_file.write('    model: %s\n' % (_model_))
    yaml_out_file.write('    title: \'%s\'\n' % (_title_))
    yaml_out_file.write('    stage_id: \'%s\'\n' % (_stage_id_))
    yaml_out_file.write('    auth_required: %s\n' % (_auth_required_))
    yaml_out_file.write('    users_can_go_back: %s\n' % (_users_can_go_back_))
    yaml_out_file.write('    description: %s\n' % (_description_))
    yaml_out_file.write('    thank_you_message: %s\n' % (_thank_you_message_))
    yaml_out_file.write('\n')

    _title_ = '[' + _id_ + '] ' + _title_
    _description_ = '[' + _id_ + '] ' + _description_

    txt_file.write('%s\n' % (_title_))
    
    xml_file.write('        <!-- %s -->\n' % (_title_))
    xml_file.write('        <record model="%s" id="%s">\n' % (_model_, _id_))
    xml_file.write('            <field name="title">%s</field>\n' % (_title_))
    xml_file.write('            <field name="stage_id" ref="%s"/>\n' % (_stage_id_))
    xml_file.write('            <field name="auth_required" eval="%s"/>\n' % (_auth_required_))
    xml_file.write('            <field name="users_can_go_back" eval="%s"/>\n' % (_users_can_go_back_))
    xml_file.write('            <field name="description">&lt;p&gt;%s&lt;/p&gt;</field>\n' % (_description_))
    xml_file.write('            <field name="thank_you_message">&lt;p&gt;%s&lt;/p&gt;</field>\n' % (_thank_you_message_))
    xml_file.write('        </record>\n')
    xml_file.write('\n')
    
    page_sequence = 0
    for key2 in sorted(doc[key1].keys()):
        try:
            _model_ = doc[key1][key2]['model']
            print '    ', key2, _model_
            if _model_ == 'survey.page':
                page_sequence += 10
                survey_page(doc, yaml_out_file, xml_file, txt_file, key1, key2, key1, page_sequence)
        except Exception, e:
            pass

def survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename):

    yaml_file = open(yaml_filename, 'r')
    doc = yaml.load(yaml_file)

    yaml_out_file = open(yaml_out_filename, "w")
    txt_file = open(txt_filename, "w")
    xml_file = open(xml_filename, "w")

    xml_file.write('<?xml version="1.0" encoding="utf-8"?>\n')
    xml_file.write('<openerp>\n')
    xml_file.write('    <data noupdate="1">\n')
    xml_file.write('\n')

    for key1 in sorted(doc.keys()):
        _model_ = doc[key1]['model']
        print key1, _model_
        if _model_ == 'survey.survey':
            survey(doc, yaml_out_file, xml_file, txt_file, key1)

    xml_file.write('    </data>\n')
    xml_file.write('</openerp>\n')

    yaml_file.close()
    yaml_out_file.close()
    txt_file.close()
    xml_file.close()

def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],[(t*1000,),1000,60,60])

if __name__ == '__main__':

    from time import time
    start = time()

    print '--> Executing survey_process_yaml.py ...'

    yaml_filename = 'survey_jcafb_FSE16.yaml'
    yaml_out_filename = 'survey_jcafb_FSE16_out.yaml'
    xml_filename = 'survey_jcafb_FSE16.xml'
    txt_filename = 'survey_jcafb_FSE16.txt'
    print '--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename)
    survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)

    # yaml_filename = 'survey_jcafb_ISE16.yaml'
    # yaml_out_filename = 'survey_jcafb_ISE16_out.yaml'
    # xml_filename = 'survey_jcafb_ISE16.xml'
    # txt_filename = 'survey_jcafb_ISE16.txt'
    # print '--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename)
    # survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)

    # yaml_filename = 'survey_jcafb_CSE16.yaml'
    # yaml_out_filename = 'survey_jcafb_CSE16_out.yaml'
    # xml_filename = 'survey_jcafb_CSE16.xml'
    # txt_filename = 'survey_jcafb_CSE16.txt'
    # print '--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename)
    # survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)

    # yaml_filename = 'survey_jcafb_QMD16.yaml'
    # yaml_out_filename = 'survey_jcafb_QMD16_out.yaml'
    # xml_filename = 'survey_jcafb_QMD16.xml'
    # txt_filename = 'survey_jcafb_QMD16.txt'
    # print '--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename)
    # survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)

    # yaml_filename = 'survey_jcafb_QAN16.yaml'
    # yaml_out_filename = 'survey_jcafb_QAN16_out.yaml'
    # xml_filename = 'survey_jcafb_QAN16.xml'
    # txt_filename = 'survey_jcafb_QAN16.txt'
    # print '--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename)
    # survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)

    # yaml_filename = 'survey_jcafb_QDH16.yaml'
    # yaml_out_filename = 'survey_jcafb_QDH16_out.yaml'
    # xml_filename = 'survey_jcafb_QDH16.xml'
    # txt_filename = 'survey_jcafb_QDH16.txt'
    # print '--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename)
    # survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)

    print '--> survey_process_yaml.py'
    print '--> Execution time:', secondsToStr(time() - start)