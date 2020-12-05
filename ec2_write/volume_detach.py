#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	attach-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-volume.html
	create-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-volume.html
	delete-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-volume.html
	describe-volumes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-volumes.html
	modify-volume : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-volume.html
    """

    write_parameter("ec2", "detach-volume")