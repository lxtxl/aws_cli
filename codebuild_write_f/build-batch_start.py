#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-build-batch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/delete-build-batch.html
	list-build-batches : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-build-batches.html
	retry-build-batch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/retry-build-batch.html
	stop-build-batch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/stop-build-batch.html
    """

    write_parameter("codebuild", "start-build-batch")