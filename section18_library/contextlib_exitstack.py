import contextlib


def is_ok_job():
    try:
        print('do something')
        raise Exception('error')
        return True
    except Exception:
        return False


def clean_up():
    print('clean up')


def clean_up2():
    print('clean up2')


with contextlib.ExitStack() as stack:
    stack.callback(clean_up)
    stack.callback(clean_up2)

    @stack.callback
    def clean_up3():
        print('clean up3')

    is_ok = is_ok_job()
    print('more task')

    if is_ok:
        stack.pop_all()
