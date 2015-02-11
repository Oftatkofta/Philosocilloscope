from subprocess import Popen, PIPE


def run(cmd):
  pid = Popen(cmd.split(" "),stdout=PIPE,stderr=PIPE)
  out,err = pid.communicate()
  res = pid.wait()
  return res,out,err


def run_speedtest():
  return run("/home/algol/workspace/speedtest-cli/speedtest_cli.py");



def go():
  res,out,err = run_speedtest()
  if not res:
    print out.split("\n")
    speed = filter(lambda x: "arduino" in x, out.split("\n"))[0][9:]
    return int(speed.split(".")[0])
  return None
