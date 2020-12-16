#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	associate-resolver-query-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/associate-resolver-query-log-config.html
	create-resolver-query-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-query-log-config.html
	delete-resolver-query-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-resolver-query-log-config.html
	get-resolver-query-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-query-log-config.html
	list-resolver-query-log-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-query-log-configs.html
    """

    write_parameter("route53resolver", "disassociate-resolver-query-log-config")