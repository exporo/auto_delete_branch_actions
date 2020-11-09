FROM python:3.7
ADD auto_delete_branches.py requirements.txt entrypoint.sh /
RUN pip install -r requirements.txt
ENTRYPOINT ["/entrypoint.sh"]