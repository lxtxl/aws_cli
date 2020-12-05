#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-intent.html
if __name__ == '__main__':
    """
	delete-intent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/delete-intent.html
	get-intents : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-intents.html
	put-intent : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-intent.html
    """

    parameter_display_string = """
    # name : The name of the intent. The name is case sensitive.
    # intent-version : The version of the intent.
    """

    execute_two_parameter("lex-models", "get-intent", "name", "intent-version", parameter_display_string)