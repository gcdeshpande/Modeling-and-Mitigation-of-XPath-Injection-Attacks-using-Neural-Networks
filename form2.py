#!/usr/bin/env python
print "Content-Type: text/HTML\n\n"

import cgi
#form = cgi.FieldStorage()


def check_login():
        form = cgi.FieldStorage()
        user = form.getfirst("username")
        password = form.getfirst("password")
        pwd = { 'user':    'password',
                'ta':      'ta',
        }
         
        if pwd.has_key(user):
                if password==pwd[user]:
                        print"You are now logged in"
                else:    
                        print "Invalid username or password\n"
                        form1()
        else:
                form1()

def form1():
   print """
        <html>
        <body>
        <FORM ACTION="form2.py" METHOD="POST">
        <P><FONT SIZE="5" COLOR="#990000">Login</FONT><BR>
        
        <TABLE BORDER="0" WIDTH="271">
        <TR>
        <TD WIDTH="48%">
                <P ALIGN="RIGHT">Username:
        </TD>
        <TD WIDTH="1%">&nbsp;</TD>
        <TD WIDTH="51%"><INPUT TYPE="TEXT" NAME="username" SIZE="12"></TD>
        </TR>
        <TR>
                <TD WIDTH="48%">
                        <P ALIGN="RIGHT">Password:
                </TD>
                <TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="51%"><INPUT TYPE="PASSWORD" NAME="password" SIZE="12"></TD>
                <INPUT TYPE = hidden NAME = "action\" VALUE = "display">
        </TR>
        <TR>
                <TD WIDTH="48%">&nbsp;</TD>
                <TD WIDTH="1%">&nbsp;</TD>
                <TD WIDTH="51%"><INPUT TYPE="SUBMIT" NAME="submit" VALUE="Login"><INPUT TYPE="RESET" NAME="Reset" VALUE="Clear"></TD>
        </TR>
</TABLE>
</FORM>"""

check_login()
print"</BODY></HTML>"
