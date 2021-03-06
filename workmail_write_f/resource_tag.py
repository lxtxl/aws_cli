#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-resource.html
	delete-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-resource.html
	describe-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-resource.html
	list-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-resources.html
	untag-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/untag-resource.html
	update-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-resource.html
    """

    write_parameter("workmail", "tag-resource")