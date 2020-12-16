#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/delete-endpoint-group.html
	describe-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-endpoint-group.html
	list-endpoint-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-endpoint-groups.html
	update-endpoint-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-endpoint-group.html
    """

    write_parameter("globalaccelerator", "create-endpoint-group")