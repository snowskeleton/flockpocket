from subprocess import run, PIPE
from common import textIO
from security import safe_command

# set the yum options
cmd = 'yum -q -y'

def update ():
    command = '%s update' % cmd
    result = safe_command.run(run, command.split(), stdout=PIPE, stderr=PIPE)

def install (pkg, quiet=False):
    print("(yum) Installing %s" % pkg)
    command = '%s install %s' % (cmd, pkg)
    try:
        result = safe_command.run(run, command.split(), stdout=PIPE, stderr=PIPE)
        result.check_returncode()
    except Exception as e:
        if not quiet:
            text = '**** ERROR ****\n%s' % result.stderr
            print(textIO.fail(textIO.indent(text, 4)))
        raise
