import threading
import watchfiles

watch_event = threading.Event()


def watch_for_changes(dir_to_watch, callback):
    for changes in watchfiles.watch(dir_to_watch):
        if watch_event.is_set():
            print('watching stopped.')
            break

        for change in changes:
            print(f'file changed: {change[1]}')
            callback()


def start_watch_thread(dir_to_watch, callback):
    watch_thread = threading.Thread(
        target=watch_for_changes,
        args=(dir_to_watch, callback),
    )
    watch_thread.daemon = True
    watch_thread.start()


def stop_watch_thread():
    watch_event.set()
