#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/update-medical-vocabulary.html
if __name__ == '__main__':
    """
	create-medical-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/create-medical-vocabulary.html
	delete-medical-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-medical-vocabulary.html
	get-medical-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-medical-vocabulary.html
	list-medical-vocabularies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-medical-vocabularies.html
    """

    parameter_display_string = """
    # vocabulary-name : The name of the vocabulary to update. The name is case sensitive. If you try to update a vocabulary with the same name as a vocabulary youâve already made, you get a ConflictException error.
    # language-code : The language code of the language used for the entries in the updated vocabulary. US English (en-US) is the only valid language code in Amazon Transcribe Medical.
Possible values:

af-ZA
ar-AE
ar-SA
cy-GB
da-DK
de-CH
de-DE
en-AB
en-AU
en-GB
en-IE
en-IN
en-US
en-WL
es-ES
es-US
fa-IR
fr-CA
fr-FR
ga-IE
gd-GB
he-IL
hi-IN
id-ID
it-IT
ja-JP
ko-KR
ms-MY
nl-NL
pt-BR
pt-PT
ru-RU
ta-IN
te-IN
tr-TR
zh-CN
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("transcribe", "update-medical-vocabulary", "vocabulary-name", "language-code", add_option_dict)
