import re

RE_STACK_ID = re.compile(r"""
    arn:aws:cloudformation:
    (?P<region>[\w-]+):        # region
    (?P<account_id>\d{12})     # account_id
    :stack/
    (?P<stack_name>[\w-]+)/    #stack_name
    [\w-]+""", re.VERBOSE)

s1 = ('arn:aws:cloudformation:us-east-2:123456789012:stack/'
      'mystack-mynestedstack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786')

s2 = ('arn:aws:cloudformation:us-east-1:888456789012:stack/'
      'mystack-mynestedstack-sggfrhxhum7w/f449b250-b969-11e0-a185-5081d0136786')

for s in [s1, s2]:
    m = RE_STACK_ID.match(s)

    if m:
        print('-' * 60)
        print('Go next')
        print(m)
        print(m.group())
        print('Region:', m.group('region'))
        print('account ID:', m.group('account_id'))
        print('stack name:', m.group('stack_name'))
    else:
        raise Exception('Error!')
