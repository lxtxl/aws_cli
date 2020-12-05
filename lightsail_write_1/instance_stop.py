#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/stop-instance.html
if __name__ == '__main__':
    """
	create-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-instances.html
	delete-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-instance.html
	get-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instance.html
	get-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instances.html
	reboot-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/reboot-instance.html
	start-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/start-instance.html
    """

    parameter_display_string = """
    # instance-name : The name of the instance (a virtual private server) to stop.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("lightsail", "stop-instance", "instance-name", add_option_dict)





