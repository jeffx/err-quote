import os
import random
from errbot import BotPlugin, botcmd


def add_quote(args):
    location = os.path.dirname(__file__)
    quote_file = "{}/data/quotes.txt".format(location)
    quote = args[0].strip()
    attribute = args[1].strip()
    with open(quote_file, 'a') as fh:
        fh.write("{};{}\n".format(quote, attribute))


def get_file_entries(filename):
    with open(filename) as fh:
        for count, line in enumerate(fh):
            pass
    return count


def get_quote():
    location = os.path.dirname(__file__)
    quote_file = "{}/data/quotes.txt".format(location)
    quote_return = dict()
    number_of_quotes = get_file_entries(quote_file)
    if number_of_quotes == 0:
        quote_num = 0
    else:
        number_of_quotes = number_of_quotes + 1
        quote_num = random.randrange(number_of_quotes)
    with open(quote_file, 'r') as fh:
        for count, line in enumerate(fh):
            if count == quote_num:
                quote = line
            elif count > quote_num:
                break
    quote = quote.rstrip()
    split_value = quote.split(';')

    quote_return['quote'] = split_value[0]
    quote_return['attribution'] = split_value[1]
    return quote_return


class Quote(BotPlugin):

    """An Err plugin for getting a quote"""
    min_err_version = '3.2.1'
    max_err_version = '3.2.1'

    @botcmd(split_args_with=None, template='quote_display')
    def quote(self, mess, args):
        """Get a quote from the database and display it"""
        return get_quote()

    @botcmd(split_args_with=';')
    def quote_add(self, mess, args):
        """Add a quote to the database"""
        if len(args) != 2:
            return "Usage: !quote <quote>, <attribution>"
        add_quote(args)
        return "Quote added"
