import re

icinga2_keywords = [
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
  'Problem',
  'Acknowledgement',
  'Recovery',
  'Custom',
  'FlappingStart',
  'FlappingEnd',
  'DowntimeStart',
  'DowntimeEnd',
  'DowntimeRemoved',
]

def check_keywords(value, iterator=None):
  """
  Quotes values that do not represent icinga2 keywords or match
  specific types or patterns, such as those representing host variables.
  Also leaves values unquoted that have appeared as keys or values in loops.
  """
  if type(value) is int:
    return value

  if type(iterator) is dict and (value == iterator['key'] or value == iterator['value']):
    return value

  pattern = re.compile(r'^(?:\d+(ms|s|m|h|d)?|host\.vars.*)$')
  if value in icinga2_keywords or pattern.match(value):
    return value

  return '"{}"'.format(value)


def check_key_format(key, prefix):
  """
  Check if a key needs quoting or prefixing.
  E.g. attributes in CheckCommands that are actually flags ("--foo")
  require to be quoted.
  """
  if prefix:
    return prefix + key

  if key[:1] == '-':
    return '"{}"'.format(key)

  return key


class FilterModule(object):
  """
  custom jinja2 filters for working with icinga2
  """

  def filters(self):
    return {
      'icinga_vars': check_keywords,
      'icingakey': check_key_format,
    }
