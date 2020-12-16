#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/apply-pending-maintenance-action.html
if __name__ == '__main__':
    """
	describe-pending-maintenance-actions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/describe-pending-maintenance-actions.html
    """

    parameter_display_string = """
    # replication-instance-arn : The Amazon Resource Name (ARN) of the AWS DMS resource that the pending maintenance action applies to.
    # apply-action : The pending maintenance action to apply to this resource.
    # opt-in-type : A value that specifies the type of opt-in request, or undoes an opt-in request. You canât undo an opt-in request of type immediate .
Valid values:

immediate - Apply the maintenance action immediately.
next-maintenance - Apply the maintenance action during the next maintenance window for the resource.
undo-opt-in - Cancel any existing next-maintenance opt-in requests.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("dms", "apply-pending-maintenance-action", "replication-instance-arn", "apply-action", "opt-in-type", add_option_dict)
