import re

icinga2_constants = [
  'NodeName',
  'ZoneName',
  'ConfigDir',
  'DataDir',
  'LogDir',
  'CacheDir',
  'SpoolDir',
  'InitRunDir',
  'ZonesDir',
  'PluginContribDir',
  'OK',
  'Warning',
  'Critical',
  'Up',
  'Down',
]

def check_constants(value):
  '''
  Quotes values that do not represent icinga2 constants
  '''
  if type(value) is int:
    return value

  pattern = re.compile(r'^(?:\d+(ms|s|m|h|d)?|host\.vars.*)$')
  if value in icinga2_constants or pattern.match(value):
    return value

  return '"{}"'.format(value)


def check_key_format(key, prefix):
  """
  Check if a key needs quoting.
  E.g. attributes in CheckCommands that are actually flags ("--foo")
  require this.
  """
  if prefix:
    return prefix + key

  if key[:1] == '-':
    return '"{}"'.format(key)

  return key


class FilterModule(object):
  '''
  custom jinja2 filters for working with icinga2
  '''

  def filters(self):
    return {
      'constants': check_constants,
      'icinga_vars': check_constants,
      'icingakey': check_key_format,
    }
