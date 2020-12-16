#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-entity-recognizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-entity-recognizer.html
	describe-entity-recognizer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-entity-recognizer.html
	list-entity-recognizers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-entity-recognizers.html
    """

    write_parameter("comprehend", "delete-entity-recognizer")