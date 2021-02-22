import sys


def plain_progress_monitor(handler, interactive: bool = True):
    if interactive:
        # move back to the beginning of the line
        sys.stdout.write('\r')
    sys.stdout.write(f'{handler.progress.percentage}%')
