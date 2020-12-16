#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	cancel-elasticsearch-service-software-update : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/cancel-elasticsearch-service-software-update.html
    """

    write_parameter("es", "start-elasticsearch-service-software-update")