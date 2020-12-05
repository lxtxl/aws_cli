#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-hosted-zones-by-vpc.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # vpc-id : The ID of the Amazon VPC that you want to list hosted zones for.
    # vpc-region : For the Amazon VPC that you specified for VPCId , the AWS Region that you created the VPC in.
Possible values:

us-east-1
us-east-2
us-west-1
us-west-2
eu-west-1
eu-west-2
eu-west-3
eu-central-1
ap-east-1
me-south-1
us-gov-west-1
us-gov-east-1
us-iso-east-1
us-isob-east-1
ap-southeast-1
ap-southeast-2
ap-south-1
ap-northeast-1
ap-northeast-2
ap-northeast-3
eu-north-1
sa-east-1
ca-central-1
cn-north-1
af-south-1
eu-south-1
    """

    execute_two_parameter("route53", "list-hosted-zones-by-vpc", "vpc-id", "vpc-region", parameter_display_string)