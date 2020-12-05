#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-placement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/create-placement.html
	describe-placement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/describe-placement.html
	list-placements : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/list-placements.html
	update-placement : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot1click-projects/update-placement.html
    """

    write_parameter("iot1click-projects", "delete-placement")