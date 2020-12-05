#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/disassociate-web-acl.html
if __name__ == '__main__':
    """
	associate-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/associate-web-acl.html
	create-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-web-acl.html
	delete-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/delete-web-acl.html
	get-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-web-acl.html
	list-web-acls : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-web-acls.html
	update-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-web-acl.html
    """

    parameter_display_string = """
    # resource-arn : The ARN (Amazon Resource Name) of the resource from which the web ACL is being removed, either an application load balancer or Amazon API Gateway stage.
The ARN should be in one of the following formats:

For an Application Load Balancer: ``arn:aws:elasticloadbalancing:region :account-id :loadbalancer/app/load-balancer-name /load-balancer-id ``
For an Amazon API Gateway stage: ``arn:aws:apigateway:region ::/restapis/api-id /stages/stage-name ``
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("waf-regional", "disassociate-web-acl", "resource-arn", add_option_dict)





