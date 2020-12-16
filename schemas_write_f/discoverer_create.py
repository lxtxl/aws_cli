#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-discoverer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/delete-discoverer.html
	describe-discoverer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/describe-discoverer.html
	list-discoverers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/list-discoverers.html
	start-discoverer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/start-discoverer.html
	stop-discoverer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/stop-discoverer.html
	update-discoverer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/schemas/update-discoverer.html
    """

    write_parameter("schemas", "create-discoverer")