#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-matchmaking-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-matchmaking-rule-set.html
	delete-matchmaking-rule-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/delete-matchmaking-rule-set.html
	describe-matchmaking-rule-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-matchmaking-rule-sets.html
    """

    write_parameter("gamelift", "validate-matchmaking-rule-set")