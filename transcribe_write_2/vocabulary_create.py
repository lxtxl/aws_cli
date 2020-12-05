#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/create-vocabulary.html
if __name__ == '__main__':
    """
	delete-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-vocabulary.html
	get-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-vocabulary.html
	list-vocabularies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-vocabularies.html
	update-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/update-vocabulary.html
    """

    parameter_display_string = """
    # vocabulary-name : The name of the vocabulary. The name must be unique within an AWS account. The name is case sensitive. If you try to create a vocabulary with the same name as a previous vocabulary you will receive a ConflictException error.
    # language-code : The language code of the vocabulary entries.
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
    write_two_parameter("transcribe", "create-vocabulary", "vocabulary-name", "language-code", add_option_dict)
