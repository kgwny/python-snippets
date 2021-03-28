import boto3

# create client
ec2_client = boto3.client('ec2')

# describe
ec2_data = ec2_client.describe_instances()

for reservation in ec2_data['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'])
