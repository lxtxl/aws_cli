#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-event-source-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/delete-event-source-mapping.html
	get-event-source-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/get-event-source-mapping.html
	list-event-source-mappings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/list-event-source-mappings.html
	update-event-source-mapping : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-event-source-mapping.html
    """

    write_parameter("lambda", "create-event-source-mapping")