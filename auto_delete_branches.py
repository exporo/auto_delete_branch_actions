import boto3
import os
import ast

cloudformation=boto3.client('cloudformation',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    region_name=os.environ['AWS_DEFAULT_REGION'])
stack_name=os.environ['STACK_NAME']

def find_branches():
    global cloudformation

    stacks_list = get_stack_list(cloudformation)
    
    if stacks_list != None:
        delete_stack(cloudformation,stacks_list)
    else:
        print('ERROR: Was unable to find any cloudformation stacks that match with {}'.format(stack_name)) 
        exit(0) 

def get_stack_list(cloudformation):
    global stack_name
    stack_list=[]
    try:
        stacks = cloudformation.list_stacks(
            StackStatusFilter=['CREATE_FAILED','CREATE_COMPLETE','ROLLBACK_FAILED','ROLLBACK_COMPLETE','DELETE_FAILED','UPDATE_COMPLETE','UPDATE_ROLLBACK_FAILED','UPDATE_ROLLBACK_COMPLETE','IMPORT_COMPLETE','IMPORT_ROLLBACK_FAILED','IMPORT_ROLLBACK_COMPLETE']
        )['StackSummaries']
        for stack in stacks:
            name = stack['StackName']
            if name.startswith(stack_name):
                if not name.startswith(stack_name+'-prod') and not name.startswith(stack_name+'-stage'):
                    stack_list.append(name)
        if str(stack_list) == '[]':
            return None 
        else:
            return stack_list

    except:
        print('ERROR: Was unable to get list of stacks')
        exit(1)
        
def delete_stack(cloudformation, stack_list):
    for stack in stack_list:
        try:
            cloudformation.delete_stack(StackName=stack)
        except:
            print('ERROR: Was unable to find delete the stack {}'.format(stack))
            exit(1)

find_branches()