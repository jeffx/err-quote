import os
import unittest
import quote
from errbot.backends.test import FullStackTest


class TestFileFunctions(unittest.TestCase):

    def test_get_quote(self):
        qv = quote.get_quote()
        self.assertEqual(qv['quote'], 'What gets measured, gets managed.')
        self.assertEqual(qv['attribution'], 'Peter Drucker')


class TestQuoteBotCommands(FullStackTest):

    def setUp(self):
        super(TestQuoteBotCommands, self).setUp(
            extra_plugin_dir='/home/jeffx/Projects/errbot/plugins',
            loglevel=50)

    def test_quote(self):
        self.assertCommand('!quote',
                           'What gets measured, gets managed.\n'
                           '    --Peter Drucker')

    def test_quote_add(self):
        self.assertCommand('!quote add If heavy metal bands ruled the world,'
                           ' we\'d be a lot better off;Bruce Dickinson',
                           'Quote added')

    def test_quote_add_no_attribution(self):
        self.assertCommand('!quote add I\'m a bad quote',
                           'Usage: !quote <quote>, <attribution>')

    def test_quote_add_usage(self):
        self.assertCommand('!quote add',
                           'Usage: !quote <quote>, <attribution>')

    def test_quote_add_quote_in_file(self):
        self.push_message('!quote add Message in file;Mary Sue')
        rv = self.pop_message()
        location = os.path.dirname(__file__)
        quote_file = "{}/data/quotes.txt".format(location)
        with open(quote_file, 'r') as fh:
            contents = fh.read().splitlines()
        assert contents[-1] == "Message in file;Mary Sue"
