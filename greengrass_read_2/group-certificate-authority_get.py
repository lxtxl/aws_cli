#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/get-group-certificate-authority.html
if __name__ == '__main__':
    """
	create-group-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/create-group-certificate-authority.html
	list-group-certificate-authorities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrass/list-group-certificate-authorities.html
    """

    parameter_display_string = """
    # certificate-authority-id : The ID of the certificate authority.
    # group-id : The ID of the Greengrass group.
    """

    execute_two_parameter("greengrass", "get-group-certificate-authority", "certificate-authority-id", "group-id", parameter_display_string)