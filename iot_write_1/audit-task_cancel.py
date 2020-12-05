#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/cancel-audit-task.html
if __name__ == '__main__':
    """
	describe-audit-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-audit-task.html
	list-audit-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-audit-tasks.html
    """

    parameter_display_string = """
    # task-id : The ID of the audit you want to cancel. You can only cancel an audit that is âIN_PROGRESSâ.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iot", "cancel-audit-task", "task-id", add_option_dict)





