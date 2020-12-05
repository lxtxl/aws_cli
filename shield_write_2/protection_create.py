#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/create-protection.html
if __name__ == '__main__':
    """
	delete-protection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/delete-protection.html
	describe-protection : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/describe-protection.html
	list-protections : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/list-protections.html
    """

    parameter_display_string = """
    # name : Friendly name for the Protection you are creating.
    # resource-arn : The ARN (Amazon Resource Name) of the resource to be protected.
The ARN should be in one of the following formats:

For an Application Load Balancer: ``arn:aws:elasticloadbalancing:region :account-id :loadbalancer/app/load-balancer-name /load-balancer-id ``
For an Elastic Load Balancer (Classic Load Balancer): ``arn:aws:elasticloadbalancing:region :account-id :loadbalancer/load-balancer-name ``
For an AWS CloudFront distribution: ``arn:aws:cloudfront::account-id :distribution/distribution-id ``
For an AWS Global Accelerator accelerator: ``arn:aws:globalaccelerator::account-id :accelerator/accelerator-id ``
For Amazon Route 53: ``arn:aws:route53:::hostedzone/hosted-zone-id ``
For an Elastic IP address: ``arn:aws:ec2:region :account-id :eip-allocation/allocation-id ``
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("shield", "create-protection", "name", "resource-arn", add_option_dict)
