#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-hsm : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/create-hsm.html
	delete-hsm : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/delete-hsm.html
	describe-hsm : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/describe-hsm.html
	list-hsms : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsm/list-hsms.html
    """

    write_parameter("cloudhsm", "modify-hsm")