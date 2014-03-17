#config
import time

verbose = True
time_res = 1000 * 60 * 60 #hours
min_time = time.time() * 1000 - time_res * 24
#time_res = 1000 * 60 # minutes
#where the local git repo is
local_dir = './pi_work'
#only want these files
file_extension='*py'

#variable for student's computers
host_ips = [ '192.168.0.12' ]
user_name = 'pi'
work_dir = '~/work'
