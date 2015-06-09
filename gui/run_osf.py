import os, sys
import threading




def run(command, wb=False):
	file_name = command + '.command'
	file_name = file_name.replace(' ', '_')
	command = ('cd desktop/osf.io; ' if not wb else 'cd desktop/waterbutler') + command
	cmd = 'echo "{cmd}" > {f}; chmod +x {f}; open {f}'.format(cmd=command, f=file_name)
	os.system(cmd)

def inv(process):
	command = 'invoke {}'.format(process)
	run(command)

def start_osf(wb=True):
	os.chdir('osf.io')
	os.system('workon osf')
	inv('mongo')
	inv('mailserver')
	inv('rabbitmq')
	inv('celery_worker')
	inv('elasticsearch')
	inv('assets -dw')
	if wb: inv('server --port 5001')
	inv('server')
	os.chdir('..')

def start_waterbutler():
	os.chdir('waterbutler')
	os.system('workon waterbutler')
	inv('server')
	os.chdir('..')

def fix_limits():
	print('fixing process limits...')
	os.system('sudo launchctl limit maxproc 8096 8096')
	print('fixing file limits...')
	os.system('sudo launchctl limit maxfiles 80096 80096')
	print('fixing sustem limits')
	os.system('ulimit -n 8096')
	os.system('ulimit -u 1024')

if __name__ == '__main__':
	fix_limits()
	start_osf()
	start_waterbutler()