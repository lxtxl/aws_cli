#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/create-service.html
if __name__ == '__main__':
    """
	delete-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/delete-service.html
	get-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-service.html
	list-services : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-services.html
	update-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/update-service.html
    """

    parameter_display_string = """
    # name : The name that you want to assign to the service.
If you want AWS Cloud Map to create an SRV record when you register an instance, and if youâre using a system that requires a specific SRV format, such as HAProxy , specify the following for Name :

Start the name with an underscore (_), such as _exampleservice
End the name with ._protocol , such as ._tcp

When you register an instance, AWS Cloud Map creates an SRV record and assigns a name to the record by concatenating the service name and the namespace name, for example:

_exampleservice._tcp.example.com
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("servicediscovery", "create-service", "name", add_option_dict)





