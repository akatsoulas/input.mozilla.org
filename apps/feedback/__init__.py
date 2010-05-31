# Applications, shamelessly snagged from AMO
class FIREFOX:
    id = 1
    short = 'firefox'
    pretty = 'Firefox'
    guid = '{ec8030f7-c20a-464f-9b0e-13a3a9e97384}'

class MOBILE:
    id = 60
    short = 'mobile'
    pretty = 'Mobile'
    guid = '{a23983c0-fd0e-11dc-95ff-0800200c9a66}'

UA_PATTERN_FIREFOX = (
    r'^Mozilla.*(Firefox|Minefield|Namoroka|Shiretoko|GranParadiso|BonEcho|'
    'Iceweasel|Fennec|MozillaDeveloperPreview)\/([^\s]*).*$')
UA_PATTERN_MOBILE = r'^Mozilla.*(Fennec)\/([^\s]*)$'

# Order is important: Since Fennec is Firefox too, it'll match the second
# pattern as well, so we must detect it first.
BROWSERS = (
    (MOBILE, UA_PATTERN_MOBILE),
    (FIREFOX, UA_PATTERN_FIREFOX),
)

# Operating Systems
class WINDOWS:
    pretty = 'Windows'
    short = 'win'
    ua_pattern = 'Win32'

class OSX:
    pretty = 'Mac OS X'
    short = 'mac'
    ua_pattern = 'Mac'

class LINUX:
    pretty = 'Linux'
    short = 'linux'
    ua_pattern = 'Linux'

class OS_OTHER:
    pretty = 'Other'
    short = 'other'
    ua_pattern = None

OSES = (WINDOWS, OSX, LINUX)
OS_PATTERNS = [ (o.ua_pattern, o.short) for o in OSES ]