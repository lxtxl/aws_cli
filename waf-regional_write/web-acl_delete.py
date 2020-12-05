#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	associate-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/associate-web-acl.html
	create-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/create-web-acl.html
	disassociate-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/disassociate-web-acl.html
	get-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-web-acl.html
	list-web-acls : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/list-web-acls.html
	update-web-acl : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/update-web-acl.html
    """

    write_parameter("waf-regional", "delete-web-acl")