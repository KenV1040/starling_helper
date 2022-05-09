from ast import arg
import logging
import dotenv
import argparse

def argparse():
    parser = argparse.ArgumentParser(description="This script handles automatic space transfer between certain transactions, and also automatic budgeting at payday")
    
    return parser.parse_args()

def main():
    logging.info("Script started...")
    args = argparse()


if __name__ == '__main__':
    main()

