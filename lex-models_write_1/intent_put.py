#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-intent.html
if __name__ == '__main__':
    """
	delete-intent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/delete-intent.html
	get-intent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-intent.html
	get-intents : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-intents.html
    """

    parameter_display_string = """
    # name : The name of the intent. The name is not case sensitive.
The name canât match a built-in intent name, or a built-in intent name with âAMAZON.â removed. For example, because there is a built-in intent called AMAZON.HelpIntent , you canât create a custom intent called HelpIntent .
For a list of built-in intents, see Standard Built-in Intents in the Alexa Skills Kit .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lex-models", "put-intent", "name", add_option_dict)





