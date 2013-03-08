#!/usr/bin/python
# script to make a nightly build with git
from subprocess import Popen as Run
from subprocess import PIPE, STDOUT
from sys import argv
from datetime import datetime

args = dict()
for arg in argv:
	arg_splt = arg.split('=')
	if len(arg_splt) == 2:
		args[str(arg_splt[0])] = str(arg_splt[1])

logfile = 'nightly.log'
if 'logfile' in args:
	logfile = args['logfile']
logfile = open(logfile, 'a+')

def iso_update():
	global logfile
	# now = datetime.now()
	cmd = str('python pyiso.py')
	# need to change working dir, but can't use Popen because we need to wait for exit
	# so just change dir then go back
	upd = Run(cmd, cwd='./pyiso',shell=True, stdout=logfile)
	upd.wait()

	# elapsed = datetime.now() - now
	# print str('%d secs, elapsed time' % (elapsed.total_seconds()))

def git_push():
	global args, logfile
	# parse arguments into a dictionary
	b='branch'
	r='remote'

	# first make sure we are on the correct branch (use -B to set the build to this start point)
	if b in args:
		branch = args['branch']
	else:
		branch = 'nightly'

	catch = None
	catch = Run(str('git branch'), shell=True, stdout=PIPE)
	catch.wait()

	# store current branch, to switch back
	prev_branch = branch
	catch_p = str(catch.stdout.read())
	catch_p = catch_p.splitlines()
	print len(catch_p)
	for p in catch_p:
		if '*' in p:
			p_splt = p.partition(' ')
			prev_branch = p_splt[2]

	# checkout branch
	proc = Run(str('git checkout -B %s' % (branch)), shell=True, stdout=logfile)
	proc.wait()

	# stage all files for commit
	proc = Run(str('git add . '), shell=True, stdout=logfile)
	proc.wait()

	commit_message = str('Nightly commit for %s' % (datetime.today().strftime('%Y-%m-%d')))
	if 'message' in args:
		commit_message = args['message']

	# commit all files with a message stating the build is for today
	proc = Run(str('git commit -m \"%s\" ' % (commit_message)), shell=True, stdout=logfile)
	proc.wait()

	# push commit to the origin (or specified remote branch name)
	if r in args:
		remote = args['remote']
	else:
		remote = 'origin'

	proc = Run(str('git push %s %s ' % (remote,branch)), shell=True, stdout=logfile)
	proc.wait()

	proc = Run(str('git checkout %s ') % (prev_branch), shell=True, stdout=logfile)
	proc.wait()


iso_update()
git_push()
logfile.close()
exit(0)