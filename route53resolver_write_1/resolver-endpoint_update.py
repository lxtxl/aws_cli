#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-resolver-endpoint.html
if __name__ == '__main__':
    """
	create-resolver-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-endpoint.html
	delete-resolver-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-resolver-endpoint.html
	get-resolver-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-endpoint.html
	list-resolver-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-endpoints.html
    """

    parameter_display_string = """
    # resolver-endpoint-id : The ID of the Resolver endpoint that you want to update.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("route53resolver", "update-resolver-endpoint", "resolver-endpoint-id", add_option_dict)





