<img width="1797" height="692" alt="image" src="https://github.com/user-attachments/assets/56746dae-3c00-491e-b208-33adbff37308" />

1. According to our understanding there was only 1 aws organization  which has  ccoe account and app accounts. we planned to have enabling Organizational cloud trail to Fetch info about ec2 instances using API calls. So the organization cloudtrail enabling will be scoped to this aws Organaization.
2. Problem: They have shows 2 Organisations.. Maybe more.. So the left side will contains CCOE account( which has Dedicated hosts) and application accounts. Right side will contain App accounts. If we enable the cloud trail @organizational level in the left -it will be scoped to left side aws organization only.
If ec2 is running on  right side its organizational cloud trail also should be enabled.. and how we connect these all instances at different organisations with DH in CCOE of different Organization. How we will get event Driven triggers to lambda? Lambda will be in CCOE account.
------------------------------------------------------------
Q. what Organizational CloudTrail actually does?
----------------------------------------------------------------
It records events like:
RunInstances
TerminateInstances
AllocateHosts
ReleaseHosts
Tag updates
RAM sharing

It records events on that aws Organization.

Q. solution:
-------------------------------
First, enable Organizational CloudTrail in every AWS organization so that all API activity (like EC2 instance launch, termination, host allocation, etc.) is captured for all accounts within that organization. Then, create EventBridge rules in each organization to forward those CloudTrail events to a central Event Bus in the CCOE account. The Lambda function attached to this central Event Bus will be triggered whenever events arrive. To allow the Lambda to fetch instance and host details from application accounts across different organizations, each application account must create an IAM role that trusts the CCOE Lambda execution role and grants read permissions (such as DescribeInstances and DescribeHosts). The CCOE Lambda role must also have permission to assume those roles, allowing it to securely collect required information across organizations.
