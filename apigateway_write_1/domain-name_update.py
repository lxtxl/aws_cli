#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-domain-name.html
if __name__ == '__main__':
    """
	create-domain-name : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-domain-name.html
	delete-domain-name : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-domain-name.html
	get-domain-name : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-domain-name.html
	get-domain-names : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-domain-names.html
    """

    parameter_display_string = """
    # domain-name : [Required] The name of the  DomainName resource to be changed.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("apigateway", "update-domain-name", "domain-name", add_option_dict)





