import argparse
import os
import logging.handlers
import dotenv

# Initiate logger
log = logging.getLogger('ken.starlingHelper')
log.setLevel(logging.WARNING)

console_handler = logging.StreamHandler()  # sys.stderr
console_handler.setLevel(logging.CRITICAL)  # set later by set_log_level_from_verbose() in interactive sessions
console_handler.setFormatter(logging.Formatter('[%(levelname)s](%(name)s): %(message)s'))
log.addHandler(console_handler)

if not os.path.exists('logs'): os.mkdir('logs')

log_file_handler = logging.handlers.TimedRotatingFileHandler('logs/args.log', when='M', interval=2)
log_file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s](%(name)s:%(funcName)s:%(lineno)d): %('
                                                'message)s'))
log_file_handler.setLevel(logging.DEBUG)
log.addHandler(log_file_handler)


def set_log_level_from_verbose(args):
    if not args.verbose:
        console_handler.setLevel('ERROR')
    elif args.verbose == 1:
        console_handler.setLevel('WARNING')
    elif args.verbose == 2:
        console_handler.setLevel('INFO')
    elif args.verbose >= 3:
        console_handler.setLevel('DEBUG')
    else:
        log.critical("UNEXPLAINED NEGATIVE COUNT!")


def main():
    # Init the argument parser.
    parser = argparse.ArgumentParser(
        description="This script handles automatic space transfer between certain transactions, and also automatic "
                    "budgeting at payday")
    parser.add_argument('-v', '--verbose', action="count", help="verbose level... repeat up to three times.")

    set_log_level_from_verbose(parser.parse_args())

    log.info('Scrip started')
    log.warning('hi world')


if __name__ == '__main__':
    main()
