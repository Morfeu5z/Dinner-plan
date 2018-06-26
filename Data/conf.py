from os import environ as ENV
import os


ENV['syspath'] = os.getcwd()

# DataBase configurations
ENV['dlogin'] = ENV.get('slogin') if 'slogin' in ENV else "sergiy1998"
ENV['dpaswd'] = ENV.get('spaswd') if 'spaswd' in ENV else "hspybxeR98>"
ENV['dbase'] = "dinnerplan"
ENV['dhost'] = "trashpanda.pwsz.nysa.pl"