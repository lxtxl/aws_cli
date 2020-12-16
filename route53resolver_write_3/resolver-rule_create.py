#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-rule.html
if __name__ == '__main__':
    """
	associate-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/associate-resolver-rule.html
	delete-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-resolver-rule.html
	disassociate-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/disassociate-resolver-rule.html
	get-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-rule.html
	list-resolver-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-rules.html
	update-resolver-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-resolver-rule.html
    """

    parameter_display_string = """
    # creator-request-id : A unique string that identifies the request and that allows failed requests to be retried without the risk of executing the operation twice. CreatorRequestId can be any unique string, for example, a date/time stamp.
    # rule-type : When you want to forward DNS queries for specified domain name to resolvers on your network, specify FORWARD .
When you have a forwarding rule to forward DNS queries for a domain to your network and you want Resolver to process queries for a subdomain of that domain, specify SYSTEM .
For example, to forward DNS queries for example.com to resolvers on your network, you create a rule and specify FORWARD for RuleType . To then have Resolver process queries for apex.example.com, you create a rule and specify SYSTEM for RuleType .
Currently, only Resolver can create rules that have a value of RECURSIVE for RuleType .
Possible values:

FORWARD
SYSTEM
RECURSIVE
    # domain-name : DNS queries for this domain name are forwarded to the IP addresses that you specify in TargetIps . If a query matches multiple Resolver rules (example.com and www.example.com), outbound DNS queries are routed using the Resolver rule that contains the most specific domain name (www.example.com).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("route53resolver", "create-resolver-rule", "creator-request-id", "rule-type", "domain-name", add_option_dict)
