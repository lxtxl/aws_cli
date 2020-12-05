#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-text-translation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/describe-text-translation-job.html
	list-text-translation-jobs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/list-text-translation-jobs.html
	start-text-translation-job : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/start-text-translation-job.html
    """

    write_parameter("translate", "stop-text-translation-job")