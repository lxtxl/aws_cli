#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-document.html
if __name__ == '__main__':
    """
	get-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/get-document.html
	update-document : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/update-document.html
    """

    parameter_display_string = """
    # document-id : The ID of the document.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("workdocs", "delete-document", "document-id", add_option_dict)





