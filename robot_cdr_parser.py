import csv
from operator import itemgetter

legend = {"time":"0", "call_id":"1", "call_leg_id":"2", "leg_number":"3", "type":"4", "cgpn":"5", "cdpn":"6", "odpn":"7", "rgpn":"8", "cgpc":"9",
          "hostport":"10", "bye_from":"11", "bye_cause":"12", "call_start":"13", "voice_start":"14", "call_end":"15", "voice_duration":"16", "call_duration":"17", "gate":"18", "imsi":"19"}
cdr = {}

def param_to_id(name):
    if name.lower() in legend:
        return int(legend[name.lower()])
    else:
        raise AssertionError('Error name to id converting: input must be from list (case insensitive): \n%s' % legend.keys())

class cdr_pars:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    def __init__(self):
        self.__server_thread = None

    def readfile(self, path, filename):
        global str_cnt, records
        csvline = None
        with open(path+filename, 'rt') as f:
            try:
                csvline = csv.Sniffer().sniff(f.readline(), delimiters=';')
                f.seek(0)
                records = list(csv.reader(f, csvline))
                # rows counter
                str_cnt = len(records)
                print str_cnt, 'rows read from', path, '/', filename
                # convert rows to dict cdr[u00 - u(str_cnt)]
                for i in range(str_cnt):
                    cdr['u' + str(i)] = records[i]
            except csv.Error:
                print 'error'
        print cdr

    def search(self, name, col):
        s1 = []
        id = param_to_id(col)
        print 'Searching %s in column: %s (%s)\n' % (name, id, col)
        #   search
        for i in range(str_cnt):
            f1 = itemgetter(int(id))(itemgetter(i)(records))
            # by callID
            if name in f1:
                s1.append(i)
        print 'found in row(s): %s\n' % s1
        for x in s1: print x, cdr['u' + str(x)]
        return s1

    def unique(self, col):
        # print 'records debug:', records, '\n'
        unique = set()
        id = param_to_id(col)
        for i in range(len(records)):
            r = itemgetter(id)(itemgetter(i)(records))
            unique.add(r)
        output = list(unique)
        print 'unique %s(s): %s' % (col, output)
        return output
