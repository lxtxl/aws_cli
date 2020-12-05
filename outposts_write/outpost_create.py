#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-outpost : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/delete-outpost.html
	get-outpost : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/get-outpost.html
	list-outposts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/list-outposts.html
    """

    write_parameter("outposts", "create-outpost")