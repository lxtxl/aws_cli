#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-site : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/create-site.html
	delete-site : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/delete-site.html
	get-sites : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/networkmanager/get-sites.html
    """

    write_parameter("networkmanager", "update-site")