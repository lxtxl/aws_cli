#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-approval-rule-template.html
if __name__ == '__main__':
    """
	create-approval-rule-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-approval-rule-template.html
	get-approval-rule-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-approval-rule-template.html
	list-approval-rule-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-approval-rule-templates.html
    """

    parameter_display_string = """
    # approval-rule-template-name : The name of the approval rule template to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("codecommit", "delete-approval-rule-template", "approval-rule-template-name", add_option_dict)





