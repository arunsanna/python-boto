import boto3
import sys

#Need to iterate over regions
def get_regions():
    client = boto3.client('ec2')
    region_response = client.describe_regions()
    regions = [region['RegionName'] for region in region_response['Regions']]
    return regions
    #return "us-east-1"

#print get_regions()
tagkey = "Owner"
tagvalue = ['arun.sanna']

def get_my_amis():
    print 'scanning the AMI under owner '+tagvalue[0]
    for region in get_regions():
        client = boto3.client('ec2', region_name= region)
        resp = client.describe_images(Filters=[{'Name': 'tag:'+tagkey, 'Values': tagvalue}])
        for m in resp['Images']:
            image_id = m['ImageId']
            tags =  m['Tags']
            for tag in tags:
                if tag['Key'] == 'Name':
                    ami_name = tag['Value']
                else:
                    ami_name = 'No_Name'
                if tag['Key'] == 'ExpirationDate':
                    ami_expiration = tag['Value']
                else:
                    ami_expiration = 'No_Expiration'
                if tag['Key'] == 'Project':
                    ami_project = tag['Value']
                else:
                    ami_project = 'No_Project'

            if decision('Deregister the AMI',image_id,ami_name,ami_project,ami_expiration):
                print "Cleanup "+image_id
                client.deregister_image(ImageId=image_id)
            else:
                print "skip cleanup "+image_id

def decision(question,id,name,project,expiration):
    while "the answer is invalid":
        reply = str(raw_input(question+' '+id+name+' '+project+' '+expiration+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False

def get_my_snapshots():
    print 'scanning the snapshots under owner '+tagkey
    for region in get_regions():
        client = boto3.client('ec2', region_name= region)
    resp = client.describe_snapshots(Filters=[
        {'Name': 'tag:'+tagkey, 'Values': tagvalue}
    ])
    for m in resp['Snapshots']:
        tags =  m['Tags']
        for tag in tags:
            if tag['Key'] == 'Name':
                print region+' '+tag['Value']
                if tag['Key'] == 'ExpirationDate':
                    print 'Expiration Date '+tag['Value']

def get_my_instances():
    print 'scanning the Instances under owner '+tagkey
    for region in get_regions():
        client = boto3.client('ec2', region_name= region)
    resp = client.describe_instances(
        Filters=[{'Name': 'tag:'+tagkey, 'Values': tagvalue}])
    for m in resp['Reservations']:
        inst = m['Instances']
        for n in inst:
            #print n['InstanceId'], region, n['State']['Name']
            print n['Tags']['Key']

# calling the funtions
get_my_amis()
#get_my_snapshots()
#get_my_instances()