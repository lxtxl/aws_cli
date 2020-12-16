#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/apply-pending-maintenance-action.html
if __name__ == '__main__':
    """
	describe-pending-maintenance-actions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune/describe-pending-maintenance-actions.html
    """

    parameter_display_string = """
    # resource-identifier : The Amazon Resource Name (ARN) of the resource that the pending maintenance action applies to. For information about creating an ARN, see Constructing an Amazon Resource Name (ARN) .
    # apply-action : The pending maintenance action to apply to this resource.
Valid values: system-update , db-upgrade
    # opt-in-type : A value that specifies the type of opt-in request, or undoes an opt-in request. An opt-in request of type immediate canât be undone.
Valid values:

immediate - Apply the maintenance action immediately.
next-maintenance - Apply the maintenance action during the next maintenance window for the resource.
undo-opt-in - Cancel any existing next-maintenance opt-in requests.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("neptune", "apply-pending-maintenance-action", "resource-identifier", "apply-action", "opt-in-type", add_option_dict)
