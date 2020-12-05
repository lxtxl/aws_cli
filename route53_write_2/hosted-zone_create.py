#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-hosted-zone.html
if __name__ == '__main__':
    """
	delete-hosted-zone : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-hosted-zone.html
	get-hosted-zone : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-hosted-zone.html
	list-hosted-zones : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-hosted-zones.html
    """

    parameter_display_string = """
    # name : The name of the domain. Specify a fully qualified domain name, for example, www.example.com . The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats www.example.com (without a trailing dot) and www.example.com. (with a trailing dot) as identical.
If youâre creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of NameServers that CreateHostedZone returns in DelegationSet .
    # caller-reference : A unique string that identifies the request and that allows failed CreateHostedZone requests to be retried without the risk of executing the operation twice. You must use a unique CallerReference string every time you submit a CreateHostedZone request. CallerReference can be any unique string, for example, a date/time stamp.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53", "create-hosted-zone", "name", "caller-reference", add_option_dict)
