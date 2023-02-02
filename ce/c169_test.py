"""
Filename Pattern
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-filename-pattern.html
      https://www.codeeval.com/open_challenges/169/
"""

import unittest
from c169 import solution


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('bh1770.h', solution('*7* johab.py gen_probe.ko palmtx.h macpath.py tzp dm-dirty-log.h bh1770.h pktloc faillog.8.gz zconf.gperf'))

    def test_provided_2(self):
        self.assertEqual('IBM1008_420.so', solution('*[0123456789]*[auoei]* IBM1008_420.so zfgrep limits.conf.5.gz tc.h ilogb.3.gz limits.conf CyrAsia-TerminusBold28x14.psf.gz nf_conntrack_sip.ko DistUpgradeViewNonInteractive.pyc NFKDQC'))

    def test_provided_3(self):
        self.assertEqual('menu_no_no.utf-8.vim', solution('*.??? max_user_watches arptables.h net_namespace Kannada.pl menu_no_no.utf-8.vim shtags.1 unistd_32_ia32.h gettext-tools.mo ntpdate.md5sums linkat.2.gz'))

    def test_provided_4(self):
        self.assertEqual('-', solution('*.pdf OldItali.pl term.log plymouth-upstart-bridge rand.so libipw.ko jisfreq.pyc impedance-analyzer xmon.h 1.5.0.3.txt bank'))

    def test_provided_5(self):
        self.assertEqual('groff-base.conffiles', solution('g*.* 56b8a0b6.0 sl.vim digctl.h groff-base.conffiles python-software-properties.md5sums CountryInformation.py use_zero_page session-noninteractive d2i_RSAPublicKey.3ssl.gz container-detect.log.4.gz'))

    def test_provided_6(self):
        self.assertEqual('46b2fd3b.0 libip6t_frag.so', solution('*[0123456789]* keyboard.h machinecheck 46b2fd3b.0 libip6t_frag.so timer_defs.h nano-menu.xpm NI vim-keys.conf setjmp.h memcg'))


if __name__ == '__main__':
    unittest.main()
