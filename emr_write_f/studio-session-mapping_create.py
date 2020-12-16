#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-studio-session-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/delete-studio-session-mapping.html
	get-studio-session-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/get-studio-session-mapping.html
	list-studio-session-mappings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-studio-session-mappings.html
	update-studio-session-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/update-studio-session-mapping.html
    """

    write_parameter("emr", "create-studio-session-mapping")