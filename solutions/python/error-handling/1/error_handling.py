def handle_error_by_throwing_exception():
    raise Exception("An error occurred")


def handle_error_by_returning_none(input_data):
    if input_data.isdigit():
        return int(input_data)
    else:
        return None


def handle_error_by_returning_tuple(input_data):
    if input_data.isdigit():
        return True, int(input_data)
    else:
        return False, input_data


def filelike_objects_are_closed_on_exception(filelike_object):
    filelike_object.open()
    try:
        filelike_object.do_something()
        filelike_object.close()
    except Exception:
        filelike_object.close()
        raise Exception("An error occured while doing something")
