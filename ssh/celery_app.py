from celery import Celery
from web import create_app


def create_celery_app(app=None):
    app = app or create_app()
    celery = Celery(__name__, broker=app.config['CELERY_BROKER_URL'], backend=app.config['CELERY_RESULT_BACKEND'])
    celery.conf.update(app.config)
    Taskbase = celery.Task

    class ContextTask(Taskbase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return Taskbase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery, app

# celery,app = create_celery_app()
# list_of_tasks = ['ssh.tasks.ssh_tasks.run_commands_on_device']   # list of all the task to register
# celery.autodiscover_tasks(list_of_tasks, force=True)              # whenever create celery app here
                                   # you have to set autodiscover function here to tell him about the tasks for registry
