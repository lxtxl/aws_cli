#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/deregister-on-premises-instance.html
if __name__ == '__main__':
    """
	get-on-premises-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-on-premises-instance.html
	list-on-premises-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-on-premises-instances.html
	register-on-premises-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/register-on-premises-instance.html
    """

    parameter_display_string = """
    # instance-name : The name of the on-premises instance to deregister.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("deploy", "deregister-on-premises-instance", "instance-name", add_option_dict)





