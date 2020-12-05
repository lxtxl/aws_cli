#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-reserved-instances-exchange-quote : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-reserved-instances-exchange-quote.html
    """

    write_parameter("ec2", "accept-reserved-instances-exchange-quote")