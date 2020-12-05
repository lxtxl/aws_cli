#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/delete-entity-recognizer.html
if __name__ == '__main__':
    """
	create-entity-recognizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-entity-recognizer.html
	describe-entity-recognizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-entity-recognizer.html
	list-entity-recognizers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-entity-recognizers.html
    """

    parameter_display_string = """
    # entity-recognizer-arn : The Amazon Resource Name (ARN) that identifies the entity recognizer.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("comprehend", "delete-entity-recognizer", "entity-recognizer-arn", add_option_dict)





