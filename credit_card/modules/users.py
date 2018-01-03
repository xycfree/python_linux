#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/2/17 17:11
# @Descript: 用户类模块
import os
import sys

from conf import errorcode
from conf import settings
from conf import templates
from dbhelper import dbapi
from modules import common
from modules.creditcard import CreditCard

reload(sys)
sys.setdefaultencoding('utf-8')

class Users(object):
    # 用户数据库
    __database = "{}.db".format(os.path.join(settings.DATABASE['dbpath'],settings.DATABASE['tables']['users']))

    def __init__(self):
        self.username = ""  # 登录名
        self.password = ""  # 登录密码
        self.bindcard = ""  # 绑定卡
        self.islogin = False  # 登录状态
        self.name = ""  # 姓名
        self.mobile = ""  # 手机
        self.islocked = 0  # 是否锁定
        self.role = "user"  # 账户权限
        self.trycount = 0  # 登录尝试次数
        self.isdel = 0  # 用户删除标识
        self.code = common.verification_code()
        self.dict_user = {}
        self.db_load()

    def db_load(self):
        self.dict_user = dbapi.load_data_from_db(self.__database)

    def _user_login(self,password, code):
        """用户登录验证模块,对用户对象进行判断,登录成功后返回一个新的用户对象
        :param password: 密码
        :param code: 验证码
        :return:
        """
        _password = common.encrypt(password)  # 密码加密为MD5
        for user, details in self.dict_user.items():

            if user == self.username and not details['isdel']:
                if details['islocked'] == 0: # 用户是否锁定,0:未锁定 1:锁定
                    if details['password'] == _password and code == self.code:
                        self.islogin = True
                        self.bindcard = details["bindcard"]
                        self.name = details["name"]
                        self.mobile = details["mobile"]
                        self.role = details["role"]
                        self.isdel = details["isdel"]
                        self.islocked = details["islocked"]
                        self.password = password
                        break
                    else:
                        # 密码错误,失败1次
                        self.trycount += 1
                else:
                    # 账户锁定了
                    self.islocked = 1

    def login(self):
        """用户登录过程函数,输入用户名,密码调用内容方法,_user_login方法进行登录验证"""
        while self.trycount < settings.ERROR_MAX_COUNT:
            self.username = raw_input("用户名: ")
            password = raw_input('密 码: ')
            common.show_message("验证码:{}".format(self.code), 'INFORMATION')
            check_code = raw_input("请输入验证码: ")

            if not self.user_exits:
                common.show_message('用户名不存在!', 'ERROR')
                continue

            # 调用用户登录方法登录
            self._user_login(password, check_code)

            #用户锁定,退出
            if self.islocked:
                common.show_message("该用户已被锁定,请联系管理员", 'ERROR')
                self.trycount = 0
                break

            if self.islogin:
                break
            else:
                common.show_message('用户名或密码错误!', 'NOTICE')
        else:
            self.islocked = 1
            self.dict_user[self.username]['islocked'] = self.islocked # 更新用户信息
            self.update_user()
            common.show_message('输入错误次数过多，请联系管理员', 'ERROR')

        self.trycount = 0  # 重试次数重置为0

    def update_user(self):
        """用户数据更新方法,用户修改信息、用户账户锁定、解锁等操作之后更新数据库文件"""
        try:
            '''
            _password = common.encrypt(self.password)
            self.dict_user[self.username]["password"] = _password
            self.dict_user[self.username]["islocked"] = self.islocked
            self.dict_user[self.username]["name"] = self.name
            self.dict_user[self.username]["mobile"] = self.mobile
            self.dict_user[self.username]["bindcard"] = self.bindcard
            self.dict_user[self.username]["isdel"] = self.isdel
            self.dict_user[self.username]["role"] = self.role
            '''
            # 写入数据库文件
            dbapi.write_db_json(self.dict_user, self.__database)
            return True
        except Exception as e:
            common.write_error_log(e)
            return False

    def create_user(self):
        """
        新创建一个用户,将用户数据同步写入到数据库文件
        :return:
        """
        self.dict_user[self.username] = dict(password=common.encrypt(self.password),
                                             name=self.name,
                                             mobile=self.mobile,
                                             bindcard=self.bindcard,
                                             role=self.role,
                                             islocked=0,
                                             isdel=0,
                                             )
        dbapi.write_db_json(self.dict_user, self.__database)

    def del_user(self):
        """
        删除用户,逻辑删除
        :return:
        """
        self.dict_user[self.username]["isdel"] = 1
        self.update_user()

    def unlock_user(self):
        """用户解锁"""
        self.dict_user[self.username]["islocked"] = 0
        self.update_user()

    def init_user_info(self):
        """创建用户,完善用户信息"""
        is_null_flag = True
        while is_null_flag:
            self.username = input("登录用户名(区分大小写): ").strip()
            if not self.username:
                common.show_message('用户名不能为空', "ERROR")
                continue
            elif self.user_exits:
                common.show_message('该用户名已存在', 'ERROR')
                continue
            else:
                is_null_flag = False
                continue
        self.name = common.input_msg("姓名:")
        self.password = common.input_msg("密码:")
        self.mobile = common.input_msg("手机:")
        self.role = common.input_msg("用户权限(user/admin):", ("admin", "user"))
        self.create_user()
        common.show_message("用户创建成功!", "NOTICE")

    """python中的staticmethod 主要是方便将外部函数集成到类体中,美化代码结构,重点在不需要类实例化的
       情况下调用方法。如果你去掉staticmethod,在方法中加self也可以通过实例化访问方法也是可以集成代码.
    """
    @staticmethod
    def user_auth(func):
        """用户登录验证装饰器,userobj为登录用户对象，未登录时可以传入一个空对象
        :param func: 被装饰的函数
        :return:
        """
        def login_check(self, userobj):
            if not userobj.islogin:
                common.show_message("用户未登录,请先登录系统", 'NOTICE')
                userobj.login()  # 登录
                if userobj.islogin:  # 登录成功
                    return func(self, userobj)
                else:
                    common.show_message('登录失败,请联系管理员', 'ERROR')
            else:
                return func(self, userobj)
        return login_check

    def bind_card(self, cardobj):
        """用户绑定信用卡，调用该方法绑卡时，先实例化卡对象，再判断卡是否有效
        :param cardobj: 信用卡对象
        :return: 成功 99999 / 失败 错误码
        """
        if self.username == cardobj.owner:
            self.bindcard = cardobj.cardno
            self.update_user()
            return errorcode.NO_ERROR
        else:
            return errorcode.CARD_OWNER_ERROR

    def logout(self):
        """注销当前用户，系统属性置空"""
        self.islogin = False
        self.bindcard = ""
        self.mobile = ""
        self.name = ""
        self.password = ""
        self.username = ""
        common.show_message("注销成功", "NOTICE")

    def modify_password(self):
        """个人中心，修改密码"""
        _not_null_flag = False
        try:
            while not _not_null_flag:
                _new_password = input('输入新密码: ').strip()
                _confirm_password = input('再次输入确认密码:').strip()
                if not _new_password or not _confirm_password:
                    common.show_message('密码不能为空,请重新输入', 'ERROR')
                    continue
                if _new_password != _confirm_password:
                    common.show_message('两次输入密码不一致,请重新输入!', 'ERROR')
                    continue
                _not_null_flag = True
            self.password = _new_password
            _password = common.encrypt(self.password)
            self.dict_user[self.username]['password'] = _password
            self.update_user()
            common.show_message('密码修改成功', 'INFORMATION')
            return True
        except Exception, e:
            common.write_error_log(e)
            return False

    @property #Python内置的@property装饰器就是负责把一个方法变成属性调用的
    def user_exits(self):
        """判断用户名是否存在,存在返回True,否则False"""
        if self.username in list(self.dict_user.keys()):
            return True
        else:
            return False

    def modify_user_info(self):
        """
        打印用户信息
        :return: 用户信息字符串
        """
        if self.islocked == 1:
            currstatus = "账户锁定"
        else:
            currstatus = "账户正常"
        frmuser = templates.user_info.format(
            username=self.username,
            name=self.name,
            mobile=self.mobile,
            bindcard=self.bindcard,
            role=self.role,
            islocked="是" if self.islocked == 1 else "否",
            isdel="是" if self.isdel == 1 else "否"
        )
        # 打印用户信息
        common.show_message(frmuser, "NOTICE")

        # 开始修改
        common.show_message("请输入新的资料,若不更新直接回车：", "NOTICE")
        new_name = raw_input("姓名({0}); ".format(self.name))
        new_mobile = raw_input("手机({0}): ".format(self.mobile))
        self.name = self.name if len(new_name) == 0 else new_name
        self.mobile = self.mobile if len(new_mobile) == 0 else new_mobile
        # 输入信用卡卡号
        _card_noerror = False
        while not _card_noerror:
            new_bindcard = raw_input("绑定卡({0}): ".format(self.bindcard))
            if len(new_bindcard) > 0:
                # 创建一个卡对象
                cardobj = CreditCard(new_bindcard)
                if not cardobj.card_is_exists:
                    common.show_message("您输入的卡号不存在!", "ERROR")

                elif cardobj.owner != self.username:
                    common.show_message("您输入的卡号非法,请联系系统管理员!", "ERROR")
                else:
                    # 都正确了
                    self.bindcard = new_bindcard
                    _card_noerror = True
            else:
                _card_noerror = True
        # 更新用户资料库变量
        self.dict_user[self.username]["name"] = self.name
        self.dict_user[self.username]["mobile"] = self.mobile
        self.dict_user[self.username]["bindcard"] = self.bindcard
        if self.update_user():
            common.show_message("信息更新成功!", "NOTICE")
        else:
            common.show_message("更新失败,查看日志!", "ERROR")

    def load_user_info(self):
        """
        根据用户名获取用户信息
        :return: 用户对象
        """
        if self.user_exits:
            user_detail = self.dict_user[self.username]
            self.name = user_detail["name"]
            self.bindcard = user_detail["bindcard"]
            self.islocked = user_detail["islocked"]
            self.role = user_detail["role"]
            self.isdel = user_detail["isdel"]
            self.mobile = user_detail["mobile"]
            return True
        else:
            return False