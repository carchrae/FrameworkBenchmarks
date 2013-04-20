import subprocess
import sys
import setup_util

def start(args):
  setup_util.replace_text("play1/conf/application.conf", "jdbc:mysql:\/\/.*:3306", "jdbc:mysql://" + args.database_host + ":3306")
  subprocess.check_call("play1 start --%prod", shell=True, cwd="play1")
  return 0
def stop():
  try:
    subprocess.check_call("play1 stop", shell=True, cwd="play1")
    return 0
  except subprocess.CalledProcessError:
    return 1 
