<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
 "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
 <head>
 <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
 <link href="/css/apsite.css" rel="stylesheet" media="all" type="text/css" title="Main stylesheet" />
 <meta name="author" content="Documentation Group" /><meta name="email" content="docs@httpd.apache.org" />
 <title>Download - The Apache HTTP Server Project</title>
 </head>
 <body>
 
 <div id="page-header">
 <p class="menu">&nbsp;</p>
 <p class="apache">&nbsp;</p>
 <a href="/">
 <img alt="" width="800" height="72" src="/images/httpd_logo_wide_new.png" />
 </a>
 </div>
 
 <!-- LEFT SIDE NAVIGATION -->
 <div id="apmenu">
 
 <h1 id="essentials">Essentials</h1>
<ul>
<li><a href="/ABOUT_APACHE.html">About</a></li>
<li><a href="http://www.apache.org/licenses/">License</a></li>
<li><a href="http://wiki.apache.org/httpd/FAQ">FAQ</a></li>
<li><a href="/security_report.html">Security Reports</a></li>
</ul>
<h1 id="downloading">Download!</h1>
<ul>
<li><a href="/download.cgi">From a Mirror</a></li>
</ul>
<h1 id="documentation"><a href="/docs/">Documentation</a></h1>
<ul>
<li><a href="/docs/2.4/">Version 2.4</a></li>
<li><a href="/docs/2.2/">Version 2.2</a></li>
<li><a href="/docs/2.0/">Version 2.0</a></li>
<li><a href="/docs/trunk/">Trunk (dev)</a></li>
<li><a href="http://wiki.apache.org/httpd/">Wiki</a></li>
</ul>
<h1 id="get-support">Get Support</h1>
<ul>
<li><a href="/support.html">Support</a></li>
</ul>
<h1 id="get-involved">Get Involved</h1>
<ul>
<li><a href="/lists.html">Mailing Lists</a></li>
<li><a href="/bug_report.html">Bug Reports</a></li>
<li><a href="/dev/">Developer Info</a></li>
</ul>
<h1 id="subprojects">Subprojects</h1>
<ul>
<li><a href="/docs-project/">Docs</a></li>
<li><a href="/test/">Test</a></li>
<li><a href="/test/flood/">Flood</a></li>
<li><a href="/apreq/">libapreq</a></li>
<li><a href="/modules">Modules</a></li>
<li><a href="/mod_fcgid/">mod_fcgid</a></li>
<li><a href="/mod_ftp/">mod_ftp</a></li>
</ul>
<h1 id="miscellaneous"><a href="/info/">Miscellaneous</a></h1>
<ul>
<li><a href="/contributors/">Contributors</a></li>
<li><a href="http://www.apache.org/foundation/thanks.html">Sponsors</a></li>
<li><a href="http://www.apache.org/foundation/sponsorship.html">Sponsorship</a></li>
</ul>
 
 </div>
 <!-- RIGHT SIDE INFORMATION -->
 <div id="apcontents">
 
 <h1 id="download">Downloading the Apache HTTP Server</h1>
<p>Use the links below to download the Apache HTTP Server from one of our
mirrors. You <strong>must</strong> <a href="#verify">verify the integrity</a> of the downloaded
files using signatures downloaded from our main distribution directory.</p>
<p>Only current recommended releases are available on the main distribution
site and its mirrors. Older releases, including the 1.3 and 2.0 families
of releases, are available from the 
<a href="http://archive.apache.org/dist/httpd/">archive download site</a>. </p>
<p>Stable Release - Latest Version:</p>
<ul>
<li><a href="#apache24">2.4.10</a> (released 2014-07-21)</li>
</ul>
<p>Legacy Release - 2.2 Branch:</p>
<ul>
<li><a href="#apache22">2.2.29</a> (released 2014-09-03)</li>
</ul>
<p>If you are downloading the Win32 distribution, please read these <a href="http://mirror.olnevhost.net/pub/apache//httpd/binaries/win32/README.html">important
notes</a>.</p>
<h1 id="mirror">Mirror</h1>
<p> The currently selected mirror is
<strong>http://mirror.olnevhost.net/pub/apache/</strong>. If you encounter a problem with this mirror, please select
another mirror. If all mirrors are failing, there are <em>backup</em> mirrors (at
the end of the mirrors list) that should be available.
<form action="/download.cgi" method="get" id="SelectMirror">Other
mirrors:<select name="Preferred"> <option
value="http://mirror.olnevhost.net/pub/apache/">http://mirror.olnevhost.net/pub/apache/</option><option
value="http://mirror.sdunix.com/apache/">http://mirror.sdunix.com/apache/</option><option
value="http://www.gtlib.gatech.edu/pub/apache/">http://www.gtlib.gatech.edu/pub/apache/</option><option
value="http://download.nextag.com/apache/">http://download.nextag.com/apache/</option><option
value="http://www.eng.lsu.edu/mirrors/apache/">http://www.eng.lsu.edu/mirrors/apache/</option><option
value="http://www.webhostingjams.com/mirror/apache/">http://www.webhostingjams.com/mirror/apache/</option><option
value="http://apache.arvixe.com/">http://apache.arvixe.com/</option><option
value="http://mirrors.advancedhosters.com/apache/">http://mirrors.advancedhosters.com/apache/</option><option
value="http://www.trieuvan.com/apache/">http://www.trieuvan.com/apache/</option><option
value="http://psg.mtu.edu/pub/apache/">http://psg.mtu.edu/pub/apache/</option><option
value="http://mirrors.gigenet.com/apache/">http://mirrors.gigenet.com/apache/</option><option
value="http://www.motorlogy.com/apache/">http://www.motorlogy.com/apache/</option><option
value="http://apache.mirrors.pair.com/">http://apache.mirrors.pair.com/</option><option
value="http://mirror.symnds.com/software/Apache/">http://mirror.symnds.com/software/Apache/</option><option
value="http://mirrors.ibiblio.org/apache/">http://mirrors.ibiblio.org/apache/</option><option
value="http://apache.mirrors.hoobly.com/">http://apache.mirrors.hoobly.com/</option><option
value="http://apache.cs.utah.edu/">http://apache.cs.utah.edu/</option><option
value="http://mirror.tcpdiag.net/apache/">http://mirror.tcpdiag.net/apache/</option><option
value="http://mirrors.sonic.net/apache/">http://mirrors.sonic.net/apache/</option><option
value="http://mirror.cc.columbia.edu/pub/software/apache/">http://mirror.cc.columbia.edu/pub/software/apache/</option><option
value="http://supergsego.com/apache/">http://supergsego.com/apache/</option><option
value="http://apache.spinellicreations.com/">http://apache.spinellicreations.com/</option><option
value="http://mirror.reverse.net/pub/apache/">http://mirror.reverse.net/pub/apache/</option><option
value="http://apache.osuosl.org/">http://apache.osuosl.org/</option><option
value="http://www.bizdirusa.com/mirrors/apache/">http://www.bizdirusa.com/mirrors/apache/</option><option
value="http://apache.petsads.us/">http://apache.petsads.us/</option><option
value="http://www.dsgnwrld.com/am/">http://www.dsgnwrld.com/am/</option><option
value="http://mirror.metrocast.net/apache/">http://mirror.metrocast.net/apache/</option><option
value="http://apache.claz.org/">http://apache.claz.org/</option><option
value="http://apache.mirrors.tds.net/">http://apache.mirrors.tds.net/</option><option
value="http://apache.tradebit.com/pub/">http://apache.tradebit.com/pub/</option><option
value="http://mirror.nexcess.net/apache/">http://mirror.nexcess.net/apache/</option><option
value="http://www.carfab.com/apachesoftware/">http://www.carfab.com/apachesoftware/</option><option
value="http://apache.mesi.com.ar/">http://apache.mesi.com.ar/</option><option
value="http://mirror.cogentco.com/pub/apache/">http://mirror.cogentco.com/pub/apache/</option><option
value="http://mirrors.koehn.com/apache/">http://mirrors.koehn.com/apache/</option><option
value="http://www.interior-dsgn.com/apache/">http://www.interior-dsgn.com/apache/</option><option
value="http://apache.mirrors.lucidnetworks.net/">http://apache.mirrors.lucidnetworks.net/</option>   <option
value="ftp://apache.mirrors.pair.com/">ftp://apache.mirrors.pair.com/</option><option
value="ftp://apache.mirrors.tds.net/pub/apache.org/">ftp://apache.mirrors.tds.net/pub/apache.org/</option><option
value="ftp://ftp.osuosl.org/pub/apache/">ftp://ftp.osuosl.org/pub/apache/</option><option
value="ftp://mirror.reverse.net/pub/apache/">ftp://mirror.reverse.net/pub/apache/</option><option
value="ftp://apache.cs.utah.edu/apache.org/">ftp://apache.cs.utah.edu/apache.org/</option>   <option
value="http://www.eu.apache.org/dist/">http://www.eu.apache.org/dist/ (backup)</option><option
value="http://www.us.apache.org/dist/">http://www.us.apache.org/dist/ (backup)</option> </select><input
type="submit" value="Change"></input></form>
You may also consult the <a href="http://www.apache.org/mirrors/">complete list of
mirrors</a>.</p>
<h1 id="apache24">Apache HTTP Server 2.4.10 (httpd): 2.4.10 is the latest available version <span>2014-07-21</span></h1>
<p>The Apache HTTP Server Project is pleased to
<a href="http://www.apache.org/dist/httpd/Announcement2.4.txt">announce</a> the
release of version 2.4.10 of the Apache HTTP Server ("Apache" and "httpd").
This version of Apache is our latest GA release of the new generation 2.4.x
branch of Apache HTTPD and represents fifteen years of innovation by the
project, and is recommended over all previous releases!</p>
<p>For details see the <a href="http://www.apache.org/dist/httpd/Announcement2.4.html">Official
Announcement</a> and
the <a href="http://mirror.olnevhost.net/pub/apache//httpd/CHANGES_2.4">CHANGES_2.4</a> and
<a href="http://mirror.olnevhost.net/pub/apache//httpd/CHANGES_2.4.10">CHANGES_2.4.10</a> lists</p>
<ul>
<li>
<p>Source: <a href="http://mirror.olnevhost.net/pub/apache//httpd/httpd-2.4.10.tar.bz2">httpd-2.4.10.tar.bz2</a>
[ <a href="http://www.apache.org/dist/httpd/httpd-2.4.10.tar.bz2.asc">PGP</a> ] [
<a href="http://www.apache.org/dist/httpd/httpd-2.4.10.tar.bz2.md5">MD5</a> ] [
<a href="http://www.apache.org/dist/httpd/httpd-2.4.10.tar.bz2.sha1">SHA1</a> ]</p>
</li>
<li>
<p>Source: <a href="http://mirror.olnevhost.net/pub/apache//httpd/httpd-2.4.10.tar.gz">httpd-2.4.10.tar.gz</a> [
<a href="http://www.apache.org/dist/httpd/httpd-2.4.10.tar.gz.asc">PGP</a> ] [
<a href="http://www.apache.org/dist/httpd/httpd-2.4.10.tar.gz.md5">MD5</a> ] [
<a href="http://www.apache.org/dist/httpd/httpd-2.4.10.tar.gz.sha1">SHA1</a> ]</p>
</li>
<li>
<p><a href="http://mirror.olnevhost.net/pub/apache//httpd/binaries/">Binaries</a> </p>
</li>
<li>
<p><a href="http://mirror.olnevhost.net/pub/apache//httpd/patches/">Security and official patches</a> </p>
</li>
<li>
<p><a href="http://mirror.olnevhost.net/pub/apache//httpd/">Other files</a> </p>
</li>
</ul>
<h1 id="apache22">Apache HTTP Server 2.2.29 (httpd) <span>2014-09-02</span></h1>
<p>The Apache HTTP Server Project is pleased to announce the release of Apache
HTTP Server (httpd) version 2.2.29.</p>
<p>For details see the <a href="http://www.apache.org/dist/httpd/Announcement2.2.html">Official
Announcement</a> and
the <a href="http://mirror.olnevhost.net/pub/apache//httpd/CHANGES_2.2">CHANGES_2.2</a> or condensed
<a href="http://mirror.olnevhost.net/pub/apache//httpd/CHANGES_2.2.29">CHANGES_2.2.29</a> lists</p>
<p>Add-in modules for Apache 2.0 are not compatible with Apache 2.2. If you
are running third party add-in modules, you must obtain modules compiled or
updated for Apache 2.2 from that third party, before you attempt to upgrade
from these previous versions. Modules compiled for Apache 2.2 should
continue to work for all 2.2.x releases.</p>
<ul>
<li>
<p>Source: <a href="http://mirror.olnevhost.net/pub/apache//httpd/httpd-2.2.29.tar.gz">httpd-2.2.29.tar.gz</a>
[ <a href="http://www.apache.org/dist/httpd/httpd-2.2.29.tar.gz.asc">PGP</a> ] [
<a href="http://www.apache.org/dist/httpd/httpd-2.2.29.tar.gz.md5">MD5</a> ] [
<a href="http://www.apache.org/dist/httpd/httpd-2.2.29.tar.gz.sha1">SHA1</a> ]</p>
</li>
<li>
<p>Source:
<a href="http://mirror.olnevhost.net/pub/apache//httpd/httpd-2.2.29.tar.bz2">httpd-2.2.29.tar.bz2</a> [
<a href="http://www.apache.org/dist/httpd/httpd-2.2.29.tar.bz2.asc">PGP</a> ] [
<a href="http://www.apache.org/dist/httpd/httpd-2.2.29.tar.bz2.md5">MD5</a> ] [
<a href="http://www.apache.org/dist/httpd/httpd-2.2.29.tar.bz2.sha1">SHA1</a> ]</p>
</li>
<li>
<p><a href="http://mirror.olnevhost.net/pub/apache//httpd/binaries/">Binaries</a> </p>
</li>
<li>
<p><a href="http://mirror.olnevhost.net/pub/apache//httpd/patches/">Security and official patches</a> </p>
</li>
<li>
<p><a href="http://mirror.olnevhost.net/pub/apache//httpd/">Other files</a> </p>
</li>
</ul>
<h1 id="mod_fcgid">Apache mod_fcgid FastCGI module for Apache HTTP Server released as 2.3.9 <span>2013-10-08</span></h1>
<p>The Apache Software Foundation and the Apache HTTP Server Project are
pleased to announce the release of version 2.3.9 of mod_fcgid, a FastCGI
implementation for Apache HTTP Server versions 2.2 and 2.4. This
version of mod_fcgid is a security release.</p>
<p>For information about this module subproject, see the <a href="http://httpd.apache.org/mod_fcgid/">mod_fcgid module
project page</a>.</p>
<ul>
<li>
<p>Source as gzip with LF line endings:
<a href="http://mirror.olnevhost.net/pub/apache//httpd/mod_fcgid/mod_fcgid-2.3.9.tar.gz">mod_fcgid-2.3.9.tar.gz</a>
[
<a href="http://www.apache.org/dist/httpd/mod_fcgid/mod_fcgid-2.3.9.tar.gz.asc">PGP</a>
] [
<a href="http://www.apache.org/dist/httpd/mod_fcgid/mod_fcgid-2.3.9.tar.gz.md5">MD5</a>
] [
<a href="http://www.apache.org/dist/httpd/mod_fcgid/mod_fcgid-2.3.9.tar.gz.sha1">SHA1</a>
]</p>
</li>
<li>
<p>Source as bz2 with LF line endings:
<a href="http://mirror.olnevhost.net/pub/apache//httpd/mod_fcgid/mod_fcgid-2.3.9.tar.bz2">mod_fcgid-2.3.9.tar.bz2</a>
[
<a href="http://www.apache.org/dist/httpd/mod_fcgid/mod_fcgid-2.3.9.tar.bz2.asc">PGP</a>
] [
<a href="http://www.apache.org/dist/httpd/mod_fcgid/mod_fcgid-2.3.9.tar.bz2.md5">MD5</a>
] [
<a href="http://www.apache.org/dist/httpd/mod_fcgid/mod_fcgid-2.3.9.tar.bz2.sha1">SHA1</a>
]</p>
</li>
<li>
<p>Win32, Netware or OS/2 Source with CR/LF line endings:
<a href="http://mirror.olnevhost.net/pub/apache//httpd/mod_fcgid/mod_fcgid-2.3.9-crlf.zip">mod_fcgid-2.3.9-crlf.zip</a>
[
<a href="http://www.apache.org/dist/httpd/mod_fcgid/mod_fcgid-2.3.9-crlf.zip.asc">PGP</a>
] [
<a href="http://www.apache.org/dist/httpd/mod_fcgid/mod_fcgid-2.3.9-crlf.zip.md5">MD5</a>
] [
<a href="http://www.apache.org/dist/httpd/mod_fcgid/mod_fcgid-2.3.9-crlf.zip.sha1">SHA1</a>
]</p>
</li>
</ul>
<h1 id="mod_ftp">Apache FTP module for Apache HTTP Server released as 0.9.6-beta <span>2008-10-08</span></h1>
<p>The Apache HTTP Server Project is pleased to announce the release of Apache
FTP module for Apache HTTP Server, version 0.9.6 as beta.</p>
<p>Users are encouraged to test and provide feedback on this beta release. For
information about this module subproject, see the <a href="http://httpd.apache.org/mod_ftp/">mod_ftp module project
page</a>.</p>
<ul>
<li>
<p>Source with LF line endings (bzip2 compressed):
<a href="http://mirror.olnevhost.net/pub/apache//httpd/mod_ftp/mod_ftp-0.9.6-beta.tar.bz2">mod_ftp-0.9.6-beta.tar.bz2</a>
[
<a href="http://www.apache.org/dist/httpd/mod_ftp/mod_ftp-0.9.6-beta.tar.bz2.asc">PGP</a>
] [
<a href="http://www.apache.org/dist/httpd/mod_ftp/mod_ftp-0.9.6-beta.tar.bz2.sha1">SHA1</a>
] [
<a href="http://www.apache.org/dist/httpd/mod_ftp/mod_ftp-0.9.6-beta.tar.bz2.md5">MD5</a>
]</p>
</li>
<li>
<p>Source with LF line endings (gzip compressed):
<a href="http://mirror.olnevhost.net/pub/apache//httpd/mod_ftp/mod_ftp-0.9.6-beta.tar.gz">mod_ftp-0.9.6-beta.tar.gz</a>
[
<a href="http://www.apache.org/dist/httpd/mod_ftp/mod_ftp-0.9.6-beta.tar.gz.asc">PGP</a>
] [
<a href="http://www.apache.org/dist/httpd/mod_ftp/mod_ftp-0.9.6-beta.tar.gz.sha1">SHA1</a>
] [
<a href="http://www.apache.org/dist/httpd/mod_ftp/mod_ftp-0.9.6-beta.tar.gz.md5">MD5</a>
]</p>
</li>
<li>
<p>Win32, Netware or OS/2 Source with CR/LF line endings:
<a href="http://mirror.olnevhost.net/pub/apache//httpd/mod_ftp/mod_ftp-0.9.6-beta-crlf.zip">mod_ftp-0.9.6-beta-crlf.zip</a>
[
<a href="http://www.apache.org/dist/httpd/mod_ftp/mod_ftp-0.9.6-beta-crlf.zip.asc">PGP</a>
] [
<a href="http://www.apache.org/dist/httpd/mod_ftp/mod_ftp-0.9.6-beta-crlf.zip.sha1">SHA1</a>
] [
<a href="http://www.apache.org/dist/httpd/mod_ftp/mod_ftp-0.9.6-beta-crlf.zip.md5">MD5</a>
]</p>
</li>
<li>
<p>Win32 binary build (unzip over the installed Apache 2.2 directory):
<a href="http://mirror.olnevhost.net/pub/apache//httpd/binaries/win32/mod_ftp-0.9.6-beta-win32-x86.zip">mod_ftp-0.9.6-beta-win32-x86.zip</a>
[
<a href="http://www.apache.org/dist/httpd/binaries/win32/mod_ftp-0.9.6-beta-win32-x86.zip.asc">PGP</a>
] [
<a href="http://www.apache.org/dist/httpd/binaries/win32/mod_ftp-0.9.6-beta-win32-x86.zip.sha1">SHA1</a>
] [
<a href="http://www.apache.org/dist/httpd/binaries/win32/mod_ftp-0.9.6-beta-win32-x86.zip.md5">MD5</a>
]</p>
</li>
</ul>
<h1 id="verify">Verify the integrity of the files</h1>
<p>It is essential that you verify the integrity of the downloaded files using
the PGP or MD5 signatures. Please read <a href="/dev/verification.html">Verifying Apache HTTP Server
Releases</a> for more information on why you should
verify our releases.</p>
<p>The PGP signatures can be verified using PGP or GPG. First download the
<a href="http://www.apache.org/dist/httpd/KEYS">KEYS</a> as well as the <code>asc</code>
signature file for the relevant distribution. Make sure you get these files
from the <a href="http://www.apache.org/dist/httpd/">main distribution directory</a> ,
rather than from a mirror. Then verify the signatures using</p>
<p><code>% pgpk -a KEYS<br></br>% pgpv httpd-2.2.0.tar.gz.asc<br></br></code>
<em>or</em> <br></br><code>% pgp -ka KEYS<br></br>% pgp
httpd-2.2.0.tar.gz.asc<br></br></code> <em>or</em> <br></br><code>% gpg --import
KEYS<br></br>% gpg --verify httpd-2.2.0.tar.gz.asc</code></p>
<ul>
<li>
<p>httpd-2.4.10.tar.* are signed by Jim Jagielski <code>791485A8</code> </p>
</li>
<li>
<p>httpd-2.2.29.tar.* are signed by William A Rowe Jr <code>9088F565(7F7214A7)</code> </p>
</li>
<li>
<p>httpd_2.4.10-netware-*.zip signed by Guenter Knauf <code>E55B0D0E(31D9665F)</code> </p>
</li>
<li>
<p>mod_fcgid-2.3.9.tar.* and mod_fcgid-2.3.9-crlf.zip are signed by Jeff
Trawick <code>39FF092C</code> </p>
</li>
<li>
<p>mod_ftp-0.9.6-beta* are signed by William A Rowe Jr <code>B55D9977(7F7214A7)</code> </p>
</li>
</ul>
<p>Alternatively, you can verify the MD5 signature on the files. A unix
program called <code>md5</code> or <code>md5sum</code> is included in many unix distributions. It
is also available as part of <a href="http://www.gnu.org/software/textutils/textutils.html">GNU
Textutils</a>. Windows
users can get binary md5 programs from <a href="http://www.fourmilab.ch/md5/">here</a>
, <a href="http://www.pc-tools.net/win32/freeware/console/">here</a> , or
<a href="http://www.slavasoft.com/fsum/">here</a>. An MD5 signature consists of 32 hex
characters, and a SHA1 signature consists of 40 hex characters. Ensure your
generated signature string matches the signature string published in the
files above.</p>
 
 <!-- FOOTER -->
 <div id="footer">
 
 <p>Copyright &copy; 1997-2014 The Apache Software Foundation.<br />
Apache HTTP Server, Apache, and the Apache feather logo are trademarks of The Apache Software Foundation.</p>
 
 </div>
 </div>
 </body>
 </html>
