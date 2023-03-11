import maskpass


class Login():
    def __init__(self):
        self.u_id = int(input('Please Enter Your UID : \n'))
        self.pswd = maskpass.askpass('Please Enter Your Password : \n')
