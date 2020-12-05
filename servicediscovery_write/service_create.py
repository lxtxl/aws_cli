#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/delete-service.html
	get-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-service.html
	list-services : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-services.html
	update-service : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/update-service.html
    """

    write_parameter("servicediscovery", "create-service")