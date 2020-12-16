#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-template-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-template-alias.html
	describe-template-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-template-alias.html
	update-template-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-template-alias.html
    """

    write_parameter("quicksight", "delete-template-alias")