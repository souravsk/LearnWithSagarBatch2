# Obtain application specific password

sing-in to gmail account >> navigate to settings >> privacy and security settings

setup two step verification settings (because without two step verification we cannot generate application specific password)

after setting up two step verification setting in gmail account navigate back to security and privacy settings

click on application specific password >> give the name of the application in the drop down as Jenkins (google by default does not have any specific application password setting for Jenkins) >> this will generate password note down the password generated

Note : Since the Password has a overall control over you gmail account disclosing it may lead serious consequences



# Setup SMTP configuration for sending the gmail

navigate in the following path from dashboard after logging in manage Jenkins >> configure system >> scroll down to email notification section

enter the following parameters

smtp server : smtp.gmail.com
default user email suffix : @gmail.com
select advanced

check smtp authentication

username : (Your gmail id)
password : (application specific password generated from previous step)
check use SSL

SMTP port : 465
Reply to address : noreply@gmail.com(optional)
Charset : UTF-8 (by default it is UTF-8)
select Test configuration mail

Test e-mail recipient : <enter recipient email id >
click on test configuration which will send a test mail to the recipient e-mail id
