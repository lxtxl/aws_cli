#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-reserved-elasticsearch-instance-offerings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-reserved-elasticsearch-instance-offerings.html
    """

    write_parameter("es", "purchase-reserved-elasticsearch-instance-offering")