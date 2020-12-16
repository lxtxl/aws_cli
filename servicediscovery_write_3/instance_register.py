#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/register-instance.html
if __name__ == '__main__':
    """
	deregister-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/deregister-instance.html
	discover-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/discover-instances.html
	get-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-instance.html
	list-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-instances.html
    """

    parameter_display_string = """
    # service-id : The ID of the service that you want to use for settings for the instance.
    # instance-id : An identifier that you want to associate with the instance. Note the following:

If the service that is specified by ServiceId includes settings for an SRV record, the value of InstanceId is automatically included as part of the value for the SRV record. For more information, see DnsRecord > Type .
You can use this value to update an existing instance.
To register a new instance, you must specify a value that is unique among instances that you register by using the same service.
If you specify an existing InstanceId and ServiceId , AWS Cloud Map updates the existing DNS records, if any. If thereâs also an existing health check, AWS Cloud Map deletes the old health check and creates a new one.


Note
The health check isnât deleted immediately, so it will still appear for a while if you submit a ListHealthChecks request, for example.
    # attributes : A string map that contains the following information for the service that you specify in ServiceId :

The attributes that apply to the records that are defined in the service.
For each attribute, the applicable value.

Supported attribute keys include the following:

AWS_ALIAS_DNS_NAME

If you want AWS Cloud Map to create an Amazon Route 53 alias record that routes traffic to an Elastic Load Balancing load balancer, specify the DNS name that is associated with the load balancer. For information about how to get the DNS name, see âDNSNameâ in the topic AliasTarget in the Route 53 API Reference .
Note the following:

The configuration for the service that is specified by ServiceId must include settings for an A record, an AAAA record, or both.
In the service that is specified by ServiceId , the value of RoutingPolicy must be WEIGHTED .
If the service that is specified by ServiceId includes HealthCheckConfig settings, AWS Cloud Map will create the Route 53 health check, but it wonât associate the health check with the alias record.
Auto naming currently doesnât support creating alias records that route traffic to AWS resources other than Elastic Load Balancing load balancers.
If you specify a value for AWS_ALIAS_DNS_NAME , donât specify values for any of the AWS_INSTANCE attributes.


AWS_EC2_INSTANCE_ID
HTTP namespaces only. The Amazon EC2 instance ID for the instance. If the AWS_EC2_INSTANCE_ID attribute is specified, then the only other attribute that can be specified is AWS_INIT_HEALTH_STATUS . When the AWS_EC2_INSTANCE_ID attribute is specified, then the AWS_INSTANCE_IPV4 attribute will be filled out with the primary private IPv4 address.
AWS_INIT_HEALTH_STATUS

If the service configuration includes HealthCheckCustomConfig , you can optionally use AWS_INIT_HEALTH_STATUS to specify the initial status of the custom health check, HEALTHY or UNHEALTHY . If you donât specify a value for AWS_INIT_HEALTH_STATUS , the initial status is HEALTHY .

AWS_INSTANCE_CNAME

If the service configuration includes a CNAME record, the domain name that you want Route 53 to return in response to DNS queries, for example, example.com .
This value is required if the service specified by ServiceId includes settings for an CNAME record.

AWS_INSTANCE_IPV4

If the service configuration includes an A record, the IPv4 address that you want Route 53 to return in response to DNS queries, for example, 192.0.2.44 .
This value is required if the service specified by ServiceId includes settings for an A record. If the service includes settings for an SRV record, you must specify a value for AWS_INSTANCE_IPV4 , AWS_INSTANCE_IPV6 , or both.

AWS_INSTANCE_IPV6

If the service configuration includes an AAAA record, the IPv6 address that you want Route 53 to return in response to DNS queries, for example, 2001:0db8:85a3:0000:0000:abcd:0001:2345 .
This value is required if the service specified by ServiceId includes settings for an AAAA record. If the service includes settings for an SRV record, you must specify a value for AWS_INSTANCE_IPV4 , AWS_INSTANCE_IPV6 , or both.

AWS_INSTANCE_PORT

If the service includes an SRV record, the value that you want Route 53 to return for the port.
If the service includes HealthCheckConfig , the port on the endpoint that you want Route 53 to send requests to.
This value is required if you specified settings for an SRV record or a Route 53 health check when you created the service.

Custom attributes

You can add up to 30 custom attributes. For each key-value pair, the maximum length of the attribute name is 255 characters, and the maximum length of the attribute value is 1,024 characters. The total size of all provided attributes (sum of all keys and values) must not exceed 5,000 characters.
key -> (string)
value -> (string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("servicediscovery", "register-instance", "service-id", "instance-id", "attributes", add_option_dict)
