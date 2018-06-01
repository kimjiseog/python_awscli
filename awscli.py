import subprocess

a=subprocess.check_output('aws ec2 describe-instances --query Reservations[].Instances[].[PrivateIpAddress,PublicIpAddress,InstanceId,SubnetId,InstanceType,State.Name,KeyName,SecurityGroups,LaunchTime,Tags[?Key==`Name`].Value[]] --profile platform --output text', universal_newlines=True, shell=True)

print(a)
