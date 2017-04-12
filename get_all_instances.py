import boto3

def get_regions():
    client = boto3.client('ec2')
    region_response = client.describe_regions()
    regions = [region['RegionName'] for region in region_response['Regions']]
    return regions

for region in get_regions():
    client = boto3.client('ec2', region_name= region)
    resp = client.describe_instances()
    for m in resp['Reservations']:
        inst = m['Instances']
        for n in inst:
            print n['InstanceId'], region