#!coding:utf8

class User:
    def __init__(self):
        pass

    #注册类方法
    #1 用户名或密码是否合法
    def user_pass_illegal(self,username,password):
        pass

    #2 用户是否存在
    def user_esxits(self,username):
        pass

    #3 确认密码是否相同
    def check_pass(self,password,en-password):
        pass

    #4 注册提醒功能
    def register_notiy(self):
        pass

    #5 记录日志
    def register_log(self):
        pass

    #6 会话保持
    #登陆类方法
    #1 验证用户名是否存在 调用注册的方法
    #2 是否被激活 验证用户名和密码是否正确
    def user_isalive(self.username):
        pass
    def check_user_pass(self,username,password):
        #检查是否被激活
        if self.user_isalive:
            if password == en-password:#检查密码是否正确
                return True
    #3 异地登陆提醒
    def diff_ip(self):
        pass
    #4 登陆日志
    def login_log(self):
        pass
    #5 密码错误过多锁定
    def user_lock(self,username):
        pass

    #其它方法
    #1 验证验证码
    def check_code(self,code):
        pass
    #2 发送信息检测帐号
    def send_user_notiy(self,username):
        pass
    #3 触发更改密码
    def change_pass(self,username):
        pass
    #忘记密码
    def forget_pass(self,username):
        if self.send_user_notiy(username):
            if self.change_pass(username):
                return True

    #注册入口
    def register(self,username,password,en-password):
        if not self.user_pass_illegal(username,password):
            return False
        if not self.user_esxits(username):
            return False
        if not self.check_pass(password,en-password)
            return False
        try:#不管有没有执行成功，我们的用户注册功能正常
            if not self.register_notiy(username):
                return False
            if not self.register_log(register_log_content):
                return False
        except Exception, e:
            raise e
        finally:
            return True
            
    #登陆入口
    def login(self,username,password):
        if not self.user_esxits(username):
            return False
        if not self.user_isalive(username):
            return False
        if not check_user_pass(username,password):
            return Falsep
        if not self.user_lock(username):
            return False
        try:
            if self.diff_ip(username,ip):
                pass
        except Exception, e:
            raise e
        finally:
            pass
