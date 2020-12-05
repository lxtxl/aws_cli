#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-flow-definition.html
if __name__ == '__main__':
    """
	create-flow-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-flow-definition.html
	describe-flow-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-flow-definition.html
	list-flow-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-flow-definitions.html
    """

    parameter_display_string = """
    # flow-definition-name : The name of the flow definition you are deleting.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sagemaker", "delete-flow-definition", "flow-definition-name", add_option_dict)





