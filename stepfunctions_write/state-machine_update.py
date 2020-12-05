#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-state-machine : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/create-state-machine.html
	delete-state-machine : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/delete-state-machine.html
	describe-state-machine : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/describe-state-machine.html
	list-state-machines : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/stepfunctions/list-state-machines.html
    """

    write_parameter("stepfunctions", "update-state-machine")