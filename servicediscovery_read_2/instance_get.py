#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-instance.html
if __name__ == '__main__':
    """
	deregister-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/deregister-instance.html
	discover-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/discover-instances.html
	list-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-instances.html
	register-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/register-instance.html
    """

    parameter_display_string = """
    # service-id : The ID of the service that the instance is associated with.
    # instance-id : The ID of the instance that you want to get information about.
    """

    execute_two_parameter("servicediscovery", "get-instance", "service-id", "instance-id", parameter_display_string)