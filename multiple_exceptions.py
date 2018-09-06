def run_tasks(tasks, _failed_tasks=None):
    if _failed_tasks is None:
        _failed_tasks = []
    if tasks:
        task = tasks.pop(0)
        try:
            task()
        except Exception as err:
            _failed_tasks.append(err)
            raise err
        finally:
            run_tasks(tasks, _failed_tasks)
    elif _failed_tasks:
        raise Exception('exception(s) encountered while running tasks')

def f():
    1 / 0

def g():
    pass

def h():
    g()

def i():
    2 / 'a'

def j():
    pass


run_tasks([f, g, h, i, h])
