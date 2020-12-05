#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-skill-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/delete-skill-group.html
	get-skill-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/get-skill-group.html
	search-skill-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/search-skill-groups.html
	update-skill-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/alexaforbusiness/update-skill-group.html
    """

    write_parameter("alexaforbusiness", "create-skill-group")