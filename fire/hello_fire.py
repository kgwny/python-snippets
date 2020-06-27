import fire

def hello(name):
    return 'Hello {name}!'.format(name=name)

if __name__ == '__main__':
    fire.Fire()

# see
# https://github.com/google/python-fire/blob/master/docs/guide.md

#$ python hello_fire.py 
#
#NAME
#    hello_fire.py
#
#SYNOPSIS
#    hello_fire.py GROUP | COMMAND
#
#GROUPS
#    GROUP is one of the following:
#
#     fire
#       The Python Fire module.
#
#COMMANDS
#    COMMAND is one of the following:
#
#     hello
#

#$ python hello_fire.py hello World
#Hello World!
