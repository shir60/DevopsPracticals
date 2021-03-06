from ansible.module_utils.basic import *

def is_user_exist(username):

  try:
    import pwd
    return (username in [entry.pw_name for entry in pwd.getpwall()])
	return (shellname in [entry.pw_shell for entry in pwd.getpwall() if entry.pw_name=="root"][0])
  except:
    module.fail_json(msg="Module pwd not found")

def main():
  module = AnsibleModule(argument_spec = dict(username = dict(required=True)))
  username = module.params.get("username")

  exists = is_user_exist(username)
  if exists:
    msg = "{0} is found".format(username)
	msg = " shell for {0} is {1}".format(username,shellname)
  else:
    msg = "{0} is not found".format(username)


  module.exit_json(changed=True, msg=msg)

main()
