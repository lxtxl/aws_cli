#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-notebook-instance.html
if __name__ == '__main__':
    """
	delete-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/delete-notebook-instance.html
	describe-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-notebook-instance.html
	list-notebook-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-notebook-instances.html
	start-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/start-notebook-instance.html
	stop-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/stop-notebook-instance.html
	update-notebook-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-notebook-instance.html
    """

    parameter_display_string = """
    # notebook-instance-name : The name of the new notebook instance.
    # instance-type : The type of ML compute instance to launch for the notebook instance.
Possible values:

ml.t2.medium
ml.t2.large
ml.t2.xlarge
ml.t2.2xlarge
ml.t3.medium
ml.t3.large
ml.t3.xlarge
ml.t3.2xlarge
ml.m4.xlarge
ml.m4.2xlarge
ml.m4.4xlarge
ml.m4.10xlarge
ml.m4.16xlarge
ml.m5.xlarge
ml.m5.2xlarge
ml.m5.4xlarge
ml.m5.12xlarge
ml.m5.24xlarge
ml.c4.xlarge
ml.c4.2xlarge
ml.c4.4xlarge
ml.c4.8xlarge
ml.c5.xlarge
ml.c5.2xlarge
ml.c5.4xlarge
ml.c5.9xlarge
ml.c5.18xlarge
ml.c5d.xlarge
ml.c5d.2xlarge
ml.c5d.4xlarge
ml.c5d.9xlarge
ml.c5d.18xlarge
ml.p2.xlarge
ml.p2.8xlarge
ml.p2.16xlarge
ml.p3.2xlarge
ml.p3.8xlarge
ml.p3.16xlarge
    # role-arn : When you send any requests to AWS resources from the notebook instance, Amazon SageMaker assumes this role to perform tasks on your behalf. You must grant this role necessary permissions so Amazon SageMaker can perform these tasks. The policy must allow the Amazon SageMaker service principal (sagemaker.amazonaws.com) permissions to assume this role. For more information, see Amazon SageMaker Roles .

Note
To be able to pass this role to Amazon SageMaker, the caller of this API must have the iam:PassRole permission.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("sagemaker", "create-notebook-instance", "notebook-instance-name", "instance-type", "role-arn", add_option_dict)
