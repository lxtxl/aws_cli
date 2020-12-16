#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/create-firewall-policy.html
	delete-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/delete-firewall-policy.html
	describe-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/describe-firewall-policy.html
	list-firewall-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/list-firewall-policies.html
	update-firewall-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/update-firewall-policy.html
    """

    write_parameter("network-firewall", "associate-firewall-policy")