#!/bin/bash
#This if statement is for use of github actions.
if [ -z "$AWS_DEFAULT_REGION" ]
then
    if [ -z "$INPUT_REGION" ]
    then
        echo "Could not find value for AWS_DEFAULT_REGION"
        exit 1
    else
        export AWS_DEFAULT_REGION=$INPUT_REGION
    fi
fi
if [ -z "$AWS_ACCESS_KEY_ID" ]
then

    if [ -z "$INPUT_ACCESS" ]
    then
        echo "Could not find value for AWS_ACCESS_KEY_ID"
        exit 1
    else
        export AWS_ACCESS_KEY_ID=$INPUT_ACCESS
    fi
fi
if [ -z "$AWS_SECRET_ACCESS_KEY" ]
then
    if [ -z "$INPUT_SECRET" ]
    then
        echo "Could not find value for AWS_SECRET_ACCESS_KEY"
        exit 1
    else
        export AWS_SECRET_ACCESS_KEY=$INPUT_SECRET
    fi
fi
if [ -z "$STACK_NAME" ]
then
    if [ -z "$INPUT_STACKNAME" ]
    then
        echo "Could not find value for STACK_NAME"
        exit 1
    else
        export STACK_NAME=$INPUT_STACKNAME
    fi
fi

#Makes sure script is executable
chmod u+x /auto_delete_branches.py

#Runs python script
python /auto_delete_branches.py