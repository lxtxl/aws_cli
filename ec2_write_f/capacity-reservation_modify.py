#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	cancel-capacity-reservation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-capacity-reservation.html
	create-capacity-reservation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-capacity-reservation.html
	describe-capacity-reservations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-capacity-reservations.html
    """

    write_parameter("ec2", "modify-capacity-reservation")