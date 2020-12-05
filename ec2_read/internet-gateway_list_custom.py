#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import read_no_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-internet-gateways.html
if __name__ == '__main__':
    """
	attach-internet-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-internet-gateway.html
	create-internet-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-internet-gateway.html
	delete-internet-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-internet-gateway.html
	detach-internet-gateway : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-internet-gateway.html
    """

    parameter_num = len(sys.argv)

    if parameter_num != 3:
        print("config value is not exist")
        print("Usage: python {} <config> <template>".format(sys.argv[0]))
        sys.exit(1)

    profile_name = sys.argv[1]
    template_name = sys.argv[2]

    if template_name == "base":
        output_name = "table"
        query_name = """\"
            InternetGateways[*].[
                InternetGatewayId,
                Attachments[0].State,
                Attachments[0].VpcId,
                Tags[?Key=='Name'].Value|[0]      
            ]        
        \""""
    elif template_name == "uid":
        output_name = "text"
        query_name = """\"
            InternetGateways[*].[
                InternetGatewayId      
            ]        
        \""""

    change_query_name = query_name.replace("\n", "")
    change_query_name = change_query_name.replace(" ", "")

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # custom parameter
    add_option_dict["output"] = output_name
    add_option_dict["query"] = change_query_name

    read_no_parameter(profile_name, "ec2", "describe-internet-gateways", add_option_dict)
