#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/create-vocabulary-filter.html
if __name__ == '__main__':
    """
	delete-vocabulary-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-vocabulary-filter.html
	get-vocabulary-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-vocabulary-filter.html
	list-vocabulary-filters : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-vocabulary-filters.html
	update-vocabulary-filter : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/update-vocabulary-filter.html
    """

    parameter_display_string = """
    # vocabulary-filter-name : The vocabulary filter name. The name must be unique within the account that contains it. If you try to create a vocabulary filter with the same name as another vocabulary filter, you get a ConflictException error.
    # language-code : The language code of the words in the vocabulary filter. All words in the filter must be in the same language. The vocabulary filter can only be used with transcription jobs in the specified language.
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
    write_two_parameter("transcribe", "create-vocabulary-filter", "vocabulary-filter-name", "language-code", add_option_dict)
