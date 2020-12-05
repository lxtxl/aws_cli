#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-workflow.html
if __name__ == '__main__':
    """
	create-workflow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-workflow.html
	delete-workflow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-workflow.html
	get-workflow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-workflow.html
	list-workflows : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-workflows.html
    """

    parameter_display_string = """
    # name : Name of the workflow to be updated.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("glue", "update-workflow", "name", add_option_dict)





