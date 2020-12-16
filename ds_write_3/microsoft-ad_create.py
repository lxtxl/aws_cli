#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/create-microsoft-ad.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # name : The fully qualified domain name for the AWS Managed Microsoft AD directory, such as corp.example.com . This name will resolve inside your VPC only. It does not need to be publicly resolvable.
    # password : The password for the default administrative user named Admin .
If you need to change the password for the administrator account, you can use the  ResetUserPassword API call.
    # vpc-settings : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ds", "create-microsoft-ad", "name", "password", "vpc-settings", add_option_dict)
