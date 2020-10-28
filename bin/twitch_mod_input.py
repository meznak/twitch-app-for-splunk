import sys
import requests
import logging
from splunklib.modularinput import *


class MI(Script):

    def get_scheme(self):
        scheme = Scheme("Twitch Input")
        scheme.description = 'Collect Twitch channel stats'
        scheme.use_external_validation = True
        scheme.use_single_instance = True

        username_arg = Argument('username')
        username_arg.data_type = Argument.data_type_string
        username_arg.description = 'Your Twitch username'
        scheme.add_argument(username_arg)

        # TODO: Add password

        return scheme

    def validate_input(self, validation_definition):
        logging.info("Validating input")
        username = validation_definition.parameters['username']
        logging.debug(f'username: {username}')
        if len(username) < 1:
            raise ValueError('Username is required')

        # TODO: Validate username
        # TODO: Validate credentials

    def stream_events(self, inputs, ew):
        for input_name, input_item in inputs.inputs.iteritems():
            username = str(input_item['username'])
            do_work(input_name, ew, username)


def do_work(input_name, ew, username):
    EventWriter.log(ew, EventWriter.INFO,
                    f'Started Twitch queries for {username}')

    # TODO: Make queries
    # TODO: Write events


if __name__ == '__main__':
    MI().run(sys.argv)
