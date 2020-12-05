#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/deregister-instance.html
if __name__ == '__main__':
    """
	discover-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/discover-instances.html
	get-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-instance.html
	list-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-instances.html
	register-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/register-instance.html
    """

    parameter_display_string = """
    # service-id : The ID of the service that the instance is associated with.
    # instance-id : The value that you specified for Id in the RegisterInstance request.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("servicediscovery", "deregister-instance", "service-id", "instance-id", add_option_dict)
