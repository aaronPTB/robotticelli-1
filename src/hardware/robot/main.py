import os
import time

import conf
from hardware.robot.com import *
from hardware.robot.server import *
from hardware.robot.step import *

## TODO: ADD STANDBY UNTIL BOTH MOTORS CAN BE FOUND

def main():
	pid = os.fork()
	## Executed in the new process
	if pid == 0:
		app.run(host='0.0.0.0')

	## Main process
	else:
		if conf.LMOTOR_IP != '0.0.0.0':
			print("Waiting for LMOTOR ({0})".format(conf.LMOTOR_IP))

			while not test_connection(conf.LMOTOR_IP):
				print("waiting...")
				time.sleep(1)

			print("Successfully connected to LMOTOR")
		else:
			print("LMOTOR not configured... skipping.")

		if conf.RMOTOR_IP != '0.0.0.0':
			print("Waiting for RMOTOR ({0})".format(conf.RMOTOR_IP))

			while not test_connection(conf.RMOTOR_IP):
				print("waiting...")
				time.sleep(1)

			print("Successfully connected to RMOTOR")
		else:
			print("RMOTOR not configured... skipping.")

		## Entry point
		print("Initializing robot")
		request_step(0)
