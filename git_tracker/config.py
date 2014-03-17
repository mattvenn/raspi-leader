#config file
import time

verbose = True

#time_res is used for calculating syntax error bar widths
#time_res = 1000 * 60 * 60 #hours
time_res = 1000 * 60 #mins
min_time = time.time() * 1000 - time_res * 60

#where the local git repo will be created
local_dir = './pi_work'
#only these files will be added
file_extension='*py'

#variables for student's computers
host_ips = [ '192.168.0.12' ]
user_name = 'pi'
work_dir = '~/work'
