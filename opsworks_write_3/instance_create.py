#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/create-instance.html
if __name__ == '__main__':
    """
	assign-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks/assign-instance.html
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
    # stack-id : The stack ID.
    # layer-ids : An array that contains the instanceâs layer IDs.
(string)
    # instance-type : The instance type, such as t2.micro . For a list of supported instance types, open the stack in the console, choose Instances , and choose + Instance . The Size list contains the currently supported types. For more information, see Instance Families and Types . The parameter values that you use to specify the various types are in the API Name column of the Available Instance Types table.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("opsworks", "create-instance", "stack-id", "layer-ids", "instance-type", add_option_dict)
