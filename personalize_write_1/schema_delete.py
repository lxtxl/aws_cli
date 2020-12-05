#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/delete-schema.html
if __name__ == '__main__':
    """
	create-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/create-schema.html
	describe-schema : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-schema.html
	list-schemas : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/list-schemas.html
    """

    parameter_display_string = """
    # schema-arn : The Amazon Resource Name (ARN) of the schema to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("personalize", "delete-schema", "schema-arn", add_option_dict)





