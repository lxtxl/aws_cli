#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/translate-text.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # text : The text to translate. The text string can be a maximum of 5,000 bytes long. Depending on your character set, this may be fewer than 5,000 characters.
    # source-language-code : The language code for the language of the source text. The language must be a language supported by Amazon Translate. For a list of language codes, see  what-is-languages .
To have Amazon Translate determine the source language of your text, you can specify auto in the SourceLanguageCode field. If you specify auto , Amazon Translate will call Amazon Comprehend to determine the source language.
    # target-language-code : The language code requested for the language of the target text. The language must be a language supported by Amazon Translate.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("translate", "translate-text", "text", "source-language-code", "target-language-code", add_option_dict)
