#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-load-balancer.html
if __name__ == '__main__':
    """
	delete-load-balancer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/delete-load-balancer.html
	describe-load-balancers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancers.html
    """

    parameter_display_string = """
    # load-balancer-name : The name of the load balancer.
This name must be unique within your set of load balancers for the region, must have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and cannot begin or end with a hyphen.
    # listeners : The listeners.
For more information, see Listeners for Your Classic Load Balancer in the Classic Load Balancers Guide .
(structure)

Information about a listener.
For information about the protocols and the ports supported by Elastic Load Balancing, see Listeners for Your Classic Load Balancer in the Classic Load Balancers Guide .
Protocol -> (string)

The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.

LoadBalancerPort -> (integer)

The port on which the load balancer is listening. On EC2-VPC, you can specify any port from the range 1-65535. On EC2-Classic, you can specify any port from the following list: 25, 80, 443, 465, 587, 1024-65535.

InstanceProtocol -> (string)

The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.
If the front-end protocol is TCP or SSL, the back-end protocol must be TCP or SSL. If the front-end protocol is HTTP or HTTPS, the back-end protocol must be HTTP or HTTPS.
If there is another listener with the same InstancePort whose InstanceProtocol is secure, (HTTPS or SSL), the listenerâs InstanceProtocol must also be secure.
If there is another listener with the same InstancePort whose InstanceProtocol is HTTP or TCP, the listenerâs InstanceProtocol must be HTTP or TCP.

InstancePort -> (integer)

The port on which the instance is listening.

SSLCertificateId -> (string)

The Amazon Resource Name (ARN) of the server certificate.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elb", "create-load-balancer", "load-balancer-name", "listeners", add_option_dict)
