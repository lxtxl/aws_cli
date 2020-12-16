#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-conference-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/create-conference-provider.html
	delete-conference-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-conference-provider.html
	get-conference-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-conference-provider.html
	list-conference-providers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/list-conference-providers.html
    """

    write_parameter("alexaforbusiness", "update-conference-provider")