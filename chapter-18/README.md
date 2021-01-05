<h2>Answers to the Practice Questions from chapter 18</h2>

<p>1. What is the protocol for sending email? For checking and receiving email?</p>
<h3><i>Answer</i></h3>
<p>SMTP(Simple Mail Transfer Protocol) and IMAP(Internet Message Access Protocol).</p>

<p>2. What four smtplib functions/methods must you call to log in to an SMTP server?</p>
<h3><i>Answer</i></h3>

```
import smtplib
smtpObj = smtplib.SMTP('smtp.example.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('mailid', 'password')
```

<p>3. What two imapclient functions/methods must you call to log in to an IMAP server?</p>
<h3><i>Answer</i></h3>

```
import imapclient
imapObj = imapclient.IMAPClient('imap.example.com', ssl=True)
imapObj.login('mailid', 'password')
```

<p>4. What kind of argument do you pass to imapObj.search()?</p>
<h3><i>Answer</i></h3>
<p>FROM, BEFORE, SEEN.</p>

<p>5. What do you do if your code gets an error message that says got more than 10000 bytes?</p>
<h3><i>Answer</i></h3>
<p>Disconnect and reconnect to the IMAP server and try again.</p>

```
import imaplib
imaplib._MAXLINE = 10000000
```

<p>6.  The imapclient module handles connecting to an IMAP server and finding emails. What is one module that handles reading the emails that imapclient collects?</p>
<h3><i>Answer</i></h3>
<p>pyzmail</p>

<p>7. When using the Gmail API, what are the credentials.json and token.json files?</p>
<h3><i>Answer</i></h3>
<p>token.json is used to access the Gmail account you entered in your python program and credentials.json file is used for the authentication purpose.</p>

<p>8. In the Gmail API, what’s the difference between “thread” and “message” objects?</p>
<h3><i>Answer</i></h3>
<p>The messages attribute contains a list of the GmailMessage objects that make up the thread.</p>

<p>9. Using ezgmail.search(), how can you find emails that have file attachments?</p>
<h3><i>Answer</i></h3>
<p>has:attachment</p>

<p>10. What three pieces of information do you need from Twilio before you can send text messages?</p>
<h3><i>Answer</i></h3>
<p>SID Number, Authentication Token, and Twilio Number.</p>
