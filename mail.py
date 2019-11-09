from flask import Flask
import os
from flask import send_from_directory
app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/<email>')
def send_mail(email):
   import smtplib
   from email.mime.text import MIMEText
   conn = smtplib.SMTP('smtpout.secureserver.net',587)
   conn.starttls()
   user_ID = ""
   user_PWD = ""
   conn.login(user_ID,user_PWD)
   # msg = MIMEText("Check")
   fp = open('content.txt', 'r')
   msg = MIMEText(fp.read())
   fp.close()
   msg['Subject'] = 'SOCIAL MEDIA ADVERTISING SERVICES'
   msg['From'] = "Social Matte " + user_ID
   msg['To'] = email
   # print(msg)
   conn.sendmail(user_ID,email,msg.as_string())
   conn.quit()
   return "SUCCESS"

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % (port))
    app.run(debug=False, port=port, host='0.0.0.0')
