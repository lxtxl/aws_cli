#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-medical-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/create-medical-vocabulary.html
	get-medical-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/get-medical-vocabulary.html
	list-medical-vocabularies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-medical-vocabularies.html
	update-medical-vocabulary : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/update-medical-vocabulary.html
    """

    write_parameter("transcribe", "delete-medical-vocabulary")