import smtplib
sender = "500060649@stu.upes.ac.in"
receiver = "ishitasinghal08@gmail.com"

pswd = input("Enter passsowrd for gmail- 50060649@stu.upes.ac.in")

message = "Hey!  I have been sent via python!"

server = smtplib.SMPT('smtp.gmail.com', 587)
server.starttls()
server.login(sender, pswd)
print("CONGRATULATION")
print("Login successfull!!")

server.sendmail(sender, receiver, message)

print("Email has been succssfully sent to ", receiver)
