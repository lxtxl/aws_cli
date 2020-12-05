#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-server-certificate.html
if __name__ == '__main__':
    """
	get-server-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-server-certificate.html
	list-server-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-server-certificates.html
	update-server-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-server-certificate.html
	upload-server-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/upload-server-certificate.html
    """

    parameter_display_string = """
    # server-certificate-name : The name of the server certificate you want to delete.
This parameter allows (through its regex pattern ) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: _+=,.@-
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iam", "delete-server-certificate", "server-certificate-name", add_option_dict)





