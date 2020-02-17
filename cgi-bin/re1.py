import re

#address = re.compile('[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)', re.UNICODE)

candidates = [
    u'first.last@example.com',
    u'first.last+category@gmail.com',
    u'valid-address@mail.example.com',
    u'not-valid@example.foo',
    ]

for candidate in candidates:
    print
    print 'Candidate:', candidate
    match = re.search('[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)', candidate)
    if match:
        print '  Matches'
    else:
        print '  No match'
