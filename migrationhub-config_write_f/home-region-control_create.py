#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-home-region-controls : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhub-config/describe-home-region-controls.html
    """

    write_parameter("migrationhub-config", "create-home-region-control")