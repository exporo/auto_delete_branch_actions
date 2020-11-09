# Linking Hosted Zones

## Summary
This repo creates a docker image that can be used by CircleCI and DockerCompose, as well as a Github Action that can be used in Github Workflows. It deletes all non-stage and non-production cloudformation stacks of a given name. This helps reduce cost of AWS and time that it takes to clean up cloudformation stacks.

## When updating
Make sure you run the following commands when updating the action:
```
git add --all
git commit -m 'Updating action'
git push --follow-tags -u origin master
```

## Requirements
 - Only that the role has adequete permissions to delete the branch

## Examples to add to pipeline
### Example use for Github Actions
For Github Actions, these actions is best to be left as a standalone workflow. In the following example, this workflow runs every 3 days.
#### As a workflow
```
name: Auto-delete branch every 3 days

on: 
  schedule:
      - cron: '0 0 */3 * *'

jobs:
  delete_ranch:
    name: Delete Branches Stack
    runs-on: ubuntu-latest
    steps:
      - name: Links Hosted Zone to Root Account
        uses: exporo/auto-delete-branches@v1
        with:
          AWS_DEFAULT_REGION: eu-central-1
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_KEY }}
          STACK_NAME: TestingStackName
          ACCOUNT_ID: 1234567890
```