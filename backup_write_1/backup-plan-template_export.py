#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/export-backup-plan-template.html
if __name__ == '__main__':
    """
	list-backup-plan-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-backup-plan-templates.html
    """

    parameter_display_string = """
    # backup-plan-id : Uniquely identifies a backup plan.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("backup", "export-backup-plan-template", "backup-plan-id", add_option_dict)





