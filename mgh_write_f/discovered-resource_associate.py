#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	disassociate-discovered-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/disassociate-discovered-resource.html
	list-discovered-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgh/list-discovered-resources.html
    """

    write_parameter("mgh", "associate-discovered-resource")