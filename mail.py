import smtplib                                                                                                                                                 
                                                                                                                                                               
server =  smtplib.SMTP('smtp.gmail.com', 587)                                                                                                                  
server.starttls()                                                                                                                                              
server.login("USERNAME/EMAIL ADDRESS", "PASSWORD")                                                                                                             
                                                                                                                                                               
msg = "Test"                                                                                                                                                   
server.sendmail("FROM EMAIL ADDRESS OR NAME", "TO EMAIL ADDRESS", msg)                                                                                         
server.quit()       

