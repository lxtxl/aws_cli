#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/assign-instance.html
if __name__ == '__main__':
    """
	create-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-instance.html
	delete-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/delete-instance.html
	deregister-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/deregister-instance.html
	describe-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/describe-instances.html
	reboot-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/reboot-instance.html
	register-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/register-instance.html
	start-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/start-instance.html
	stop-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/stop-instance.html
	unassign-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/unassign-instance.html
	update-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/update-instance.html
    """

    parameter_display_string = """
    # instance-id : The instance ID.
    # layer-ids : The layer ID, which must correspond to a custom layer. You cannot assign a registered instance to a built-in layer.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("opsworks", "assign-instance", "instance-id", "layer-ids", add_option_dict)
