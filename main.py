import argparse
import os
import logging.handlers
import sys
import starling_controller
from dotenv import load_dotenv

# Initiate logger
log = logging.getLogger('ken.starlingHelper')
log.setLevel(logging.WARNING)

console_handler = logging.StreamHandler()  # sys.stderr
console_handler.setLevel(logging.CRITICAL)  # set later by set_log_level_from_verbose() in interactive sessions
console_handler.setFormatter(logging.Formatter('[%(levelname)s](%(name)s): %(message)s'))
log.addHandler(console_handler)

# Create a logging file and make sure it logs to file as well.
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


# Function to start the budgeting part.
def budget():
    load_dotenv()
    star_ctrl = starling_controller.StarlingCtrl(authorised=True, session_token=os.getenv('PAT'))
    print(star_ctrl.get_accounts())


def interface():
    log.info('Running interface now...')
    user_input = 0
    while user_input != -1:
        print('Starling Helper')
        print('1: Budget')
        print('2: Exit')
        try:
            user_input = int(input('Pick a number: '))
            if user_input == 1:
                budget()
            else:
                user_input = -1
                log.info('Bye!')
        except ValueError:
            log.warning('Please enter in a number')
        except Exception as e:
            if log.level == logging.DEBUG:
                raise e
            else:
                log.error('Unknown user input from interface')
                sys.exit()


def main():
    # Init the argument parser.
    parser = argparse.ArgumentParser(
        description="This script handles automatic space transfer between certain transactions, and also automatic "
                    "budgeting at payday")
    parser.add_argument('-v', '--verbose', action="count", help="verbose level... repeat up to three times.")

    set_log_level_from_verbose(parser.parse_args())

    log.info('Scrip started')
    interface()


if __name__ == '__main__':
    main()
