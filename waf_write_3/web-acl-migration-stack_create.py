#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-web-acl-migration-stack.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # web-acl-id : The UUID of the WAF Classic web ACL that you want to migrate to WAF v2.
    # s3-bucket-name : The name of the Amazon S3 bucket to store the CloudFormation template in. The S3 bucket must be configured as follows for the migration:

The bucket name must start with aws-waf-migration- . For example, aws-waf-migration-my-web-acl .
The bucket must be in the Region where you are deploying the template. For example, for a web ACL in us-west-2, you must use an Amazon S3 bucket in us-west-2 and you must deploy the template stack to us-west-2.
The bucket policies must permit the migration process to write data. For listings of the bucket policies, see the Examples section.
    # ignore-unsupported-type | --no-ignore-unsupported-type : Indicates whether to exclude entities that canât be migrated or to stop the migration. Set this to true to ignore unsupported entities in the web ACL during the migration. Otherwise, if AWS WAF encounters unsupported entities, it stops the process and throws an exception.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("waf", "create-web-acl-migration-stack", "web-acl-id", "s3-bucket-name", "ignore-unsupported-type | --no-ignore-unsupported-type", add_option_dict)
