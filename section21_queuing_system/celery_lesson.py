from unittest import result
import celery_tasks

# result = celery_tasks.build_server.delay()
# result = celery_tasks.build_servers_with_cleanup.delay()
result = celery_tasks.deploy_customer_server.delay()
print('doing...')
print(result)
