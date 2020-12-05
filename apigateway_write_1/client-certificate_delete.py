#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-client-certificate.html
if __name__ == '__main__':
    """
	generate-client-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/generate-client-certificate.html
	get-client-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-client-certificate.html
	get-client-certificates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-client-certificates.html
	update-client-certificate : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-client-certificate.html
    """

    parameter_display_string = """
    # client-certificate-id : [Required] The identifier of the  ClientCertificate resource to be deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("apigateway", "delete-client-certificate", "client-certificate-id", add_option_dict)





