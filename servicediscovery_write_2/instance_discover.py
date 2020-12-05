#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/discover-instances.html
if __name__ == '__main__':
    """
	deregister-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/deregister-instance.html
	get-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-instance.html
	list-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-instances.html
	register-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/register-instance.html
    """

    parameter_display_string = """
    # namespace-name : The name of the namespace that you specified when you registered the instance.
    # service-name : The name of the service that you specified when you registered the instance.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("servicediscovery", "discover-instances", "namespace-name", "service-name", add_option_dict)
