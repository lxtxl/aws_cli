#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/create-medical-vocabulary.html
if __name__ == '__main__':
    """
	delete-medical-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-medical-vocabulary.html
	get-medical-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-medical-vocabulary.html
	list-medical-vocabularies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-medical-vocabularies.html
	update-medical-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/update-medical-vocabulary.html
    """

    parameter_display_string = """
    # vocabulary-name : The name of the custom vocabulary. This case-sensitive name must be unique within an AWS account. If you try to create a vocabulary with the same name as a previous vocabulary, you get a ConflictException error.
    # language-code : The language code for the language used for the entries in your custom vocabulary. The language code of your custom vocabulary must match the language code of your transcription job. US English (en-US) is the only language code available for Amazon Transcribe Medical.
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
    # vocabulary-file-uri : The location in Amazon S3 of the text file you use to define your custom vocabulary. The URI must be in the same AWS Region as the resource that youâre calling. Enter information about your VocabularyFileUri in the following format:

https://s3.<aws-region>.amazonaws.com/<bucket-name>/<keyprefix>/<objectkey>

The following is an example URI for a vocabulary file that is stored in Amazon S3:

https://s3.us-east-1.amazonaws.com/AWSDOC-EXAMPLE-BUCKET/vocab.txt

For more information about Amazon S3 object names, see Object Keys in the Amazon S3 Developer Guide .
For more information about custom vocabularies, see Medical Custom Vocabularies .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("transcribe", "create-medical-vocabulary", "vocabulary-name", "language-code", "vocabulary-file-uri", add_option_dict)
