模拟实现一个ATM + 购物商城程序

    额度 15000或自定义
    实现购物商城，买东西加入 购物车，调用信用卡接口结账
    可以提现，手续费5%
    每月22号出账单，每月10号为还款日，过期未还，按欠款总额 万分之5 每日计息
    支持多账户登录
    支持账户间转账
    记录每月日常消费流水
    提供还款接口
    ATM记录操作日志
    提供管理接口，包括添加账户、用户额度，冻结账户等。。。

因对本次作业的MVC结构没有思路，故研究分析了王松牛人的作业，现整理如下：

一、作业代码具体说明如下：


一、主程序day5_credit_card.py开始
   1、生成today今天的日期和星期数weekoftoday
   2、定义currusers：实例化modules下的users.py中的类Users
   3、初始化对账单report.create_statement_main()
       （1）、从database目录下的文件creditcard中读取信用卡列表
       （2）、循环列表调用 create_card_statement
       （3）、create_card_statement函数说明
            3.1 获取当前日期currday和today
            3.2 如果当天是22号出帐日：
              3.2.1 赋值startday,endday,startdate,enddate,statement_key出帐起始结束时间
              3.2.2 获取卡号对应的消费流水列表dbapi.load_bill_report(cardno, startdate, enddate)
              3.2.3 statement_dict的信息追加到信用卡帐单信息中。
   4、循环菜单
       （1）、判断用户是否登录，并输出相应用户信息
              未登录输出template.index_default_menu.format("", today, common.numtochr(weekoftoday))
              否则输出template.index_logined_menu.format("欢迎您: {0}".format(curruser.name), today,common.numtochr(weekoftoday))
       （2）、输出用户选择菜单
       （3）、输入5，则退出菜单
       （4）、输入1，首先加载当年用户信息curruser.db_load()，然后调用doshopping(curruser)
       （5）、输入2，首先加载当年用户信息curruser.db_load()，然后调用user_login(curruser, today, weekoftoday)
       （6）、输入3，调用card_center(curruser)信用卡中心
       （7）、输入4，调用manager(curruser)后台管理
   5、菜单1：doshopping商城函数
       （1）、实例化商城，调用shopping.Shopping()
       （2）、循环开始，输出商品菜单shoppobj.welcome_menu
       （3）、输入编号选择并赋值shop_cassify_id，并进行输入验证判断
       （4）、输入值为4，进行购物车商品显示shopping.Shopping.print_goods_list(shoppobj.shopping_cart)
              并显示common.show_message("当前购物车共有 {0} 件商品,合计 {1} 元）
       （5）、输入值为5，shoppobj.payfor_shopcart(userobj)，无错误，输出支付成功
       （6）、输入值为1-3，则调用shoppobj.get_goods_list_by_typeid()，显示商品分列表
       （7）、第二层循环开始，并显示指定商品分类下的所有商品列表(Shopping类静态方法)
              shopping.Shopping.print_goods_list(goods_list)
       （8）、选择商品编号goods_id,加入购物车，并对输入进行判断
            8.1 如果输入为q,返回上一层
            8.2 调用商品加入购物车函数shoppobj.add_shopping_card(goods_id)
            8.3 如果返回正确，则显示购物车所有商品信息shopping.Shopping.print_goods_list(shoppobj.shopping_cart)，并输出common.show_message("已将商品加入购物车!", "INFORMATION")
               第三层循环开始，显示“继续购物(y) or 返回上一级(q)”，
            8.4 如果返回失败，则输出common.show_message("添加购物车失败,请检查输入商品编号是否正确!", "ERROR")，并continue
   6、菜单2：user_login(curruser, today, weekoftoday)用户登录
       （1）、循环开始
       （2）、判断用户是否登录成功userobj.islogin，
            2.1 如果已经登录，则显示个人中心菜单 template.index_user_center.format(userobj.name, today, common.numtochr(weekoftoday))
            2.2 输出选择功能菜单，选择6，返回上级菜单
            2.3 如果选择1-5，则通过反射来执行，从 template 模块查找各按键对应的模块
                func_dict = template.user_center_func
            2.4 根据输出的数字，赋值相应的模块名称,modulepy = __import__(func_dict[_choose]["module"])
            2.5 如果选择的是1，2，5，则赋值modulesobj 、classobj、func
   7、菜单3：card_center(curruser)信用卡中心
       （1）、判断用户是否登录
            1.1 已登录，则重新load一下数据userobj.db_load()，并获取到绑定的信息卡信息cardno = userobj.bindcard
            1.2 获得信用卡对象card = CreditCard(cardno)
            1.3 如果未登录，则进行循环，让用户输入信用卡和密码进行认证
       （2）、显示登录输出菜单index_ATM，循环开始：
       （3）、输入common.input_msg("请选择功能: ", ("1", "2", "3", "4", "5"))
       （4）、如果输入是5，就返回上一层循环
       （5）、如果输入是1，则查看信用卡信息
       （6）、如果输入是2，则进行提现菜单
            6.1 如果card.frozenstatus状态是1，则提示“卡已冻结,请联系客服”
            6.2 否则提示“信用卡提现将收取 {0}% 的手续费!”
            6.3 循环开始，提示"请输入要提现的金额(q返回):"
            6.4 输入正确的话，提示输入信用卡密码进行确认
            6.5 执行提现函数card.fetch_money(float(cost), cardpasswd)，并根据返回结果进行输出相应信息
       （7）、如果输入是3，则进入转帐菜单
            7.1 如果card.frozenstatus状态是1，则提示“卡已冻结,请联系客服”
            7.2 否则提示“信用卡转帐将收取 {0}% 的手续费!”
            7.3 循环开始，提示"请输入要转账的卡号(q返回)"
            7.4 对卡号是数字，则生成一个trans_cardobj = CreditCard(trans_cardno)
            7.5 进行卡号判断存在的话，提示是转账的金额，
            7.6 如果金额正确并输入信用卡密码进行确认
            7.5 执行转帐函数card.translate_money(float(trans_cost), cardpasswd, trans_cardobj) ，并根据返回结果进行输出相应信息
       （8）、如果输入是4，则进入还款菜单
            8.1 调用card.recreate_statement()函数，更新一下对账单信息
            8.2 循环开始，获取对账单所有列表interest_list = card.load_statement_list()
            8.3 获取还未还款的记录并显示message_info = report.print_statement_list(card.cardno, interest_list)
            8.4 如果有要还款的记录，则显示具体帐单信息
            8.5 请选择还款的16位账单号，然后进行判断，
            8.6 输出正确，则显示指定单号的相应对账单信息report.print_statement_detail
            8.7 输入还款金额，并更新已还款金额 = 现在还的金额 + 已经还的金额
            8.8 需要还款数 = 消费总费用 + 利息 ，并判断是否已还清，如果还清则设置interest_list[i][pay_serno]["isfinished"] = 1
            8.9 如果未还清，则显示“您尚未全部还款,请在还款日前尽快还款!”
            8.10 将还款后的信息写入数据库更新dbapi.write_statement_list(card.cardno, interest_list)
            8.11 显示是否继续还款。
   8、菜单4：主菜单后台管理模块manager(userobj):
       （1）、用户是否登录，是否是角色是否是admin
       （2）、是admin,进入循环，显示template.index_admin
       （3）、选择菜单，输入1时，进入创建新用户调用User类中的init_user_info()函数
       （4）、选择菜单，输入2时，进入删除用户菜单调用get_users()函数
            4.1 get_users() 显示用户的信息,用户新建、删除、解锁用户时显示用户基本信息
            4.2 输入操作的用户名
            4.3 创建一个用户实例_deluser = Users()，并赋值_deluser.username = username
            4.4 _deluser.load_user_info()判断，如果用户名存在,load用户信息成功，显示用户信息，返回用户
            4.5 用户不存在，返回失败
            4.6 调用_user.del_user()，并显示删除用户成功
       （5）、选择菜单，输入3时，进行锁定用户菜单调用get_users()函数，方式同上
       （6）、选择菜单，输入4时，进入发行信用卡菜单
            6.1 调用newcard = fill_card_info()函数，填充信用卡资料信息，返回一个信用卡对象
            6.2 循环开始，输入卡号，并判断卡号是否存在，不存在退出循环
            6.3 在依次输入密码，额度等信息，并返回一个信用卡对象
       （7）、选择菜单，输入5时，进入冻结信用卡
            7.1 输入要操作卡号
            7.2 card = CreditCard(cardno)，实例化信用卡
            7.3 判断信用卡是否存在card.card_is_exists
            7.4 存在则输入卡信息，并在次确定是否冻结
            7.5 card.frozenstatus = 1设置卡的标志位，card.update_card()更新信用卡文件
       （8）、选择菜单，输入0时，返回上层菜单


二、包conf说明：
   1、errorcode.py介绍:
       定义系统错误代码表：NO_ERROR，USER_NOT_EXISTS，CARD_NOT_BINDED，BALANCE_NOT_ENOUGHT，CARD_OWNER_ERROR，CARD_PASS_ERROR
   2、settings.py介绍：定义一系列变量值
       2.1 定义程序文件主目录BASE_DIR，并加入环境变量
       2.2 定义数据库信息DATABASE
       2.3 定义日志文件存放路径LOG_PATH
       2.4 定义账单报表文件路径REPORT_PATH
       2.5 定义用户登录失败最大次数ERROR_MAX_COUNT
       2.6 定义日息费率EXPIRE_DAY_RATE
       2.7 定义转账、提现手续费FETCH_MONEY_RATE
       2.8 定义信用额度CREDIT_TOTAL
       2.9 定义每月账单日期STATEMENT_DAY
   3、template.py介绍：该模块用来定义系统的菜单模板
       3.1 主程序中的主菜单index_default_menu
       3.2 主程序中的用户登录后的显示菜单index_logined_menu
       3.3 主程序中的用户中心菜单index_user_center
       3.4 用户中心按键对应功能模块user_center_func
       3.5 购物模块的主菜单, menu 菜单在shopping模块中内部构造shopping_index_menu
       3.6 账单报表显示模板report_bill
       3.7 购物历史记录显示模板shopping_history
       3.8 后台管理模板index_admin
       3.9 ATM 管理模块index_ATM
       3.10 显示用户基本信息模板user_info
       3.11 显示信用卡基本信息模板card_info
       3.12 信用卡对账单列表模板report_statement_list
       3.13 信用卡对账单详细模板report_statement_detail

三、包database介绍：
   1、init_db.py介绍：
       1.1 定义商品列表_shopping_list
       1.2 定义用户列表_user_list
       1.3 定义信用卡列表_creditcard_list
       1.4 函数init_db_shoppingmark() 初始化购物商城数据表 shoppingmark.db
       1.5 函数init_db_users() 初始化用户数据表 users.db
       1.6 函数init_db_creditcard() 初始化信用卡数据表 creditcard.db
       1.7 执行init_database()，通过反射初始化数据表分别调用以上三个函数

四、包dbhelper介绍:
   1、dbapi.py介绍：
       1.1 函数append_db_json(contant, filename)，将信息以 json 格式写入数据表文件(追加)
       1.2 函数write_db_json(contant, filename)，将信息以 json 格式写入数据表文件（覆盖）
       1.3 函数load_data_from_db(tabename)，从指定的数据表中获取所有数据,通过 json 方式将数据返回
       1.4 函数load_bill_report(cardno, startdate, enddate)，从信用卡对账单中获取指定卡的对账信息数据, 获取某一个时间段内的数据
       1.5 函数load_shop_history(user, startdate, enddate)，查找报表记录中的指定用户的购物历史记录,将结果存入到列表中
       1.6 函数load_statement_list(cardno)，从对账单中获取记录
       1.7 函数write_statement_list(cardno, db_list)，将对账单记录写入对账单文件，更新


五、包modules介绍：
1、users.py介绍之类Users:
   1、定义私有变量：__database 值为database下的user.db
   2、定义用户的静态变量
   3、定义动态方法db_load(self.dict_user = dbapi.load_data_from_db(self.__database)),即调用dbapi模块中的load_data_from_db方法来展示用户信息
   4、定义login函数，输入用户名和密码
       （1）、调用user_exists，判断用户是否存在，不存在则使用common.show_message进行异常颜色输出。
       （2）、如存在则调用 用户登录模块_user_login ,首先对输入的密码参数进行md5计算_password = common.encrypt(password)，调用common模块中的encrypt函数，并进行用户信息的判断的赋值
       （3）、判断是否用户被锁定
       （4）、判断用户是否登录成功，成功则break退出，失败则输出异常信息
       （5）、连续三次登录失败，则设置用户锁定标识为1，并update_user更新到user.db
       （6）、重置trycount 重置次数
   5、update_user即为将dict_user用户列表信息进行回写文件
   6、定义用户存在函数user_exists、创建函数create_user、删除函数del_user、锁定函数unlock_user
   7、创建并init_user_info初始化用户信息，输入各种信息后，调用 create_user来生成用户
   8、定义静态方法user_auth，用于用户登录验证装饰器
   9、定义bind_card函数判断卡绑定
   10、注销用户函数logout，将系统属性置空
   11、个人中心 - 修改密码函数modify_password
   12、修改用户信息modify_user_info
       （1）、首先输出当前的用户信息
       （2）、输入新的用户信息
       （3）、输入新的信用卡信息，并创建一个新的卡对象，调用CreditCard模块：cardobj = CreditCard
       （4）、判断信用卡是否存在
       （5）、输入其他信息，并update_user回写文件
   13、根据用户名获取用户信息load_user_info


2、shopping.py之类Shopping：
   1、定义私有变量：__welcome_title 菜单标题、__database 数据库文件、__shop_report_file购物报表
   2、定义__init__: 特别定义方法
         （1）、获取数据表数据self._get_shop_market()
         （2）、购物商城欢迎菜单self._construct_title_menu()
   3、_get_shop_market方法：加载购物商品信息dbapi.load_data_from_db(shoppingmarket.db)
   4、_construct_title_menu方法：输出购物商城菜单
       self.welcome_menu = self.__welcome_title.format(menu="".join(_menu))
   5、get_goods_list_by_typeid方法：根据用户选择的商品分类编号,获取该分类下所有商品
   6、定义静态方法print_goods_list：列表中的商品信息输出到屏幕,商品列表或购物车商品列表
         （1）、输出商品信息标题
         （2）、循环输出商品具体信息
   7、定义方法add_shopping_card(self, goodsid)：根据商品编号加入购物车
         （1）、定义变量_goods_tuple ，即具体的商品列表
         （2）、开始查找输入的商品编号，并加入购物车列表中，并计算金额
         （3）、成功后break
         （4）、返回return 成功与否
   8、定义payfor_shopcart结算方法，并调用@Users.user_auth认证模块作装饰器
       购物车结算模块,功能包括：购物车付款、购物记录写入文件
         （1）、判断用户是否绑定信用卡，如无，则返回错误，有，则继续、
         （2）、实例化信用卡类cardobj = CreditCard(userobj.bindcard)
         （3）、判断信用卡余额是否大于购买金额，如果不够，输出额度不够，否则继续
         （4）、调用common.create_serialno()，生成一个流水号
         （5）、调用卡的支付模块进行支付cardobj.card_pay(self.shopping_cost, 1, serno)
                    支付扣款
                    记录消费流水对账单,将发生了费用还没有还款的账单信息写入文件 report_bill 中
                    更新信用卡可透支余额信息到数据库 creditcard.db
         （6）、记录购物流水shopping_record，并写入报表记录文件shopping_history
         （7）、购物结算完成后将对象的购物车清空shopping_cart.clear(), 购物车商品总价清0 ,待下次购物
         （8）、返回错误代码


3、creditcard.py之类CreditCard：
   1、指定数据表__database的表creditcard
   2、定义信用卡额度，信用卡透支余额，信用卡日息，提现手续费率，信用卡状态等变量
   3、定义_load_card_info函数，用户输入的卡号获取信用卡信息
   4、定义card_is_exists函数，判断输入的信用卡是否存在
   5、定义card_pay(self, cost, paytype, sereialno)函数，信用卡支付,从信用卡可透支余额中扣费
        （1）、根据传入的paytype的值，定义payfor的名称，例：1:消费、2:转账、3:提现、4:手续费
        （2）、支付扣款self.credit_balance -= cost
        （3）、定义_tmp_bill_record，记录消费流水对账单
        （4）、将消费流水对账单写回到文件report_bill
        （5）、更新信用卡可透支余额信息到数据库 creditcard.db
   6、定义新发行信用卡create_card函数，根据输入的卡号密码等信息并更新到creditcard.db
   7、定义信用卡更新update_card函数，根据输入的卡号密码等信息并更新到creditcard.db
   8、定义转账、提现时验证操作_pay_check函数，转账、提现时验证操作，判断卡的余额与支付密码是否正确。并   返回错误类型码
   9、定义提现函数fetch_money(self, count, passwd)
        （1）、根据传入的取现金额，计算取现+手续费总额
        （2）、调用_pay_check函数，根据返回值进行操作。
        （3）、如果返回值是errorcode.NO_ERROR，则调用card_pay函数将取现金额和手续费计帐，并回写文件
        （4）、并返回errorcode.NO_ERROR
   10、定义信用卡转账函数translate_money(self, trans_count, passwd, trans_cardobj)
        （1）、根据传入的转帐金额，计算转帐+手续费总额
        （2）、调用_pay_check函数，根据返回值进行操作。
        （3）、如果返回值是errorcode.NO_ERROR，则调用card_pay函数将转帐金额和手续费计帐，并回写文件
        （4）、并给对方卡充值,trans_cardobj.credit_balance += trans_count，并调用trans_cardobj.update_card()写入数据库文件
        （4）、并返回errorcode.NO_ERROR
   11、定义对账单列表数据函数load_statement_list，调用dbapi.load_statement_list(self.cardno)
   12、定义recreate_statement函数，实现今天的日期将当前卡的对账单重新生成,主要对过了还款日的账单重新生    成利息信息
        （1）、获取当前日期today
        （2）、获取卡的对账单信息card_statement = dbapi.load_statement_list(self.cardno)
        （3）、如果有记录，进行循环读取，并判断isfinished字段是否是1，是则加记录加到临时列表tmp_list
        （4）、未还款，则获取pdate还款时期，并判断是否过期
        （5）、如果过期则计算利息：record[k]["interest"] = v["total"] * settings.EXPIRE_DAY_RATE * day_delta
        （6）、将过期或非过期的记录都加到临时列表tmp_list
        （7）、将更新过的列表写入文件，替换原有信息dbapi.write_statement_list(self.cardno, tmp_list)

4、common.py介绍：
   1、函数verification_code()，用来生成一个4位的验证码，并返回验证码
   2、函数encrypt(string)，用来字符串加密
   3、函数write_log(content)，用来写错误日志
   4、函数get_chinese_num(uchar)，用来计算汉字的个数
   5、函数show_message(msg, msgtype)根据msgtype类型，对print函数进行封装，根据不同类型显示不同颜色
   6、函数create_serialno()，用来生成一个消费、转账、提款时的流水号，不重复
   7、函数numtochr(num_of_weekday)，将数字星期转换为中文数字
   8、函数input_msg(message, limit_value=tuple())，判断input输入的信息是否为空的公共检测函数,为空继续输入,不为空返回输入的信息
   9、函数input_date(msg, default_date)，对输入的日期进行判断是否正确 yyyy-mm-dd or yyyy-m-d

5、report.py介绍： 账单生成模块
   1、导入calendar，timedelta等模块
   2、函数get_date()，用来用户输入一个时间段,如果显示报表是要提供开始、结束日期,返回开始，结束时间
       2.1 调用common.input_date来生成一个开始日期startdate
       2.2 调用common.input_date来生成一个结束日期enddate
       2.3 返回一个时间的字典
   3、函数print_shopping_history(userobj)，个人中心 - 购物历史记录打印模块
   4、函数print_bill_history(userobj) ，个人中心-账单明细 打印模块
   5、函数create_card_statement(cardno)，生成信用卡对账单
   6、函数create_statement_main()，卡对账单初始化模块,从卡数据库文件中加载所有卡号，对所有卡调用生成对账单模块
   7、函数print_statement_list(cardno, list_info)，将卡号对应的未还款记录显示出来
   8、函数print_statement_detail(cardno, serino, details)，还款模块 - 用户选择还款的单号后，显示详细的还款对账单及流水信息

程序说明

二、ATM 模拟程序说明

系统主程序为根目录下的:day5_credit_card.py

1. 系统功能模块

Day5_ATM 模拟程序是在python3.0 环境下开发

2. 系统目录结构：

程序采用分层的方式编写,包括数据库访问层、数据库层(数据文件)、业务逻辑层（module 层），业务处理层（主程序）、

3．应用知识点：

a) 字典、列表、元组的操作

b) 文件的读写操作

c) 函数的应用

d) 类的使用

e) 装饰器、反射

三、代码如下：

1、主程序credit_card.py:


#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import os,sys

from datetime import date, datetime
from conf import template, errorcode
from conf import settings
from modules import shopping, common
from dbhelper import dbapi
from modules.users import Users
from modules.creditcard import CreditCard
from modules import report


def doshopping(userobj):
    """
    购物商城模块,进行购物部分的所有处理
    :param userobj:  一个用户对象,如果用户未登录，在支付模块会通过装饰器来登录
    :return:
    """
    # 实例化商城
    shoppobj = shopping.Shopping()
    # 选择商品类型
    exitflag = False
    while not exitflag:
        # 开始菜单
        print(shoppobj.welcome_menu)
        shop_cassify_id = input("请选择商品分类编号[1-3]: ").strip().lower()
        if not shop_cassify_id: continue
        if shop_cassify_id == "0":
            exitflag = True
            continue
        if int(shop_cassify_id) not in range(1, 6):
            common.show_message("请选择正确的商品类型编号!", "ERROR")

            continue
        elif shop_cassify_id == "4":
            # 查看购物车
            shopping.Shopping.print_goods_list(shoppobj.shopping_cart)
            common.show_message("当前购物车共有 {0} 件商品,合计 {1} 元 !".format(len(shoppobj.shopping_cart),
                                                                    shoppobj.shopping_cost), "INFORMATION")
            continue
        elif shop_cassify_id == "5":
            # 购物结算
            dealresult = shoppobj.payfor_shopcart(userobj)
            if dealresult == errorcode.NO_ERROR:
                common.show_message("支付完成!", "INFORMATION")

        else:
            # 获取用户选择的商品类型编号
            shoppobj.goods_classify_id = shop_cassify_id
            # 获得商品类型编号对应的商品列表
            goods_list = shoppobj.get_goods_list_by_typeid()

            if not goods_list:
                common.show_message("未找到商品信息！", "NOTICE")

                continue

            # 开始选择商品，添加到购物车
            choose_goods_flag = True
            while choose_goods_flag:
                # 显示指定商品分类下的所有商品列表(Shopping类静态方法)
                shopping.Shopping.print_goods_list(goods_list)
                goods_id = input("选择商品编号,加入购物车(q返回上一级): ").strip().lower()
                if not goods_id: continue
                # 返回上一级
                if goods_id == "q":
                    choose_goods_flag = False
                    continue
                else:
                    # 将选择商品加入购物车
                    result = shoppobj.add_shopping_card(goods_id)
                    if result:
                        # 添加成功,显示购物车所有商品信息
                        shopping.Shopping.print_goods_list(shoppobj.shopping_cart)
                        common.show_message("已将商品加入购物车!", "INFORMATION")

                        # 是否继续添加
                        nextflag = False
                        while not nextflag:
                            donext = input("继续购物(y) or 返回上一级(q):").strip().lower()
                            if donext == "y":
                                break
                            elif donext == "q":
                                choose_goods_flag = False
                                break
                            else:
                                continue
                    else:
                        # 添加购物车失败
                        common.show_message("添加购物车失败,请检查输入商品编号是否正确!", "ERROR")

                        continue


def user_login(userobj, today, weekoftoday):
    """
    主菜单的2号菜单登录系统模块
    :param userobj: 当前用户对象
    :param today: 菜单显示的日期
    :param weekoftoday: 菜单显示的星期
    :return:
    """
    quitflag = False
    while not quitflag:
        if userobj.islogin:
            # 如果用户已经登录,菜单功能2为个人中心,调用另一个菜单模板 index_user_center
            print(template.index_user_center.format(userobj.name, today, common.numtochr(weekoftoday)))
            _chooseflag = False
            while not _chooseflag:
                _choose = input("选择功能：")
                if _choose not in ("1", "2", "3", "4", "5", "6"):
                    common.show_message("选择正确的功能编号!", "ERROR")
                    continue
                else:
                    _chooseflag = True

            # 返回上级菜单
            if _choose == "6":
                quitflag = True
            else:
                # 根据用户按键开始处理,从 template 模块查找各按键对应的模块,通过反射来执行
                func_dict = template.user_center_func
                modulepy = __import__(func_dict[_choose]["module"])
                # 1,2,5号键为users类方法，
                if _choose in ('1', '2', '5'):
                    modulesobj = getattr(modulepy, "users")
                    classobj = getattr(modulesobj, "Users")
                    func = getattr(classobj, func_dict[_choose]["func"])

                else:
                    # 3,4为 report 模块的方法
                    modulesobj = getattr(modulepy, "report")
                    func = getattr(modulesobj, func_dict[_choose]["func"])

                func(userobj)
        else:
            # 用户未登录,调用 Users类的登录模块
            userobj.login()
            quitflag = True


def card_center(userobj):
    if userobj.islogin:
        # 重新load一下数据
        userobj.db_load()
        cardno = userobj.bindcard
        # 获得信用卡对象
        card = CreditCard(cardno)
    else:
        # 未登录信用卡
        input_flag = False
        while not input_flag:
            cardno = input("请输入信用卡卡号: ").strip().lower()
            if cardno.isnumeric():
                card = CreditCard(cardno)
                if card.card_is_exists:
                    pwd = input("请输入密码:")
                    if common.encrypt(pwd) == card.password:
                        common.show_message("登录成功", "NOTICE")
                        input_flag = True
                        continue
                else:
                    common.show_message("卡号不存在,请重新输入!", "ERROR")
                    continue
            else:
                common.show_message("卡号无效!", "ERROR")
                continue

    show_template = template.index_ATM
    quitflag = False
    while not quitflag:
        print(show_template.format(cardno=card.cardno))
        _choose = common.input_msg("请选择功能: ", ("1", "2", "3", "4", "5"))
        # 返回
        if _choose == "5":
            quitflag = True
            continue

        # 查看信用卡信息
        if _choose == "1":
            common.show_message(template.card_info.format(cardno=card.cardno,
                                                          owner=card.owner,
                                                          total=card.credit_total,
                                                          balance=card.credit_balance,
                                                          status="正常" if card.frozenstatus == 0 else "冻结"
                                                          ), "NOTICE")
        # 提现
        if _choose == "2":
            if card.frozenstatus == 1:
                common.show_message("卡已冻结,请联系客服!", "ERROR")
            else:
                common.show_message("信用卡提现将收取 {0}% 的手续费!".format(settings.FETCH_MONEY_RATE * 100), "NOTICE")
                quitflag = False
                while not quitflag:
                    cost = common.input_msg("请输入要提现的金额(q返回):")
                    if cost.isnumeric():
                        cardpasswd = common.input_msg("请输入信用卡密码:")
                        # 执行提现操作
                        exe_result = card.fetch_money(float(cost), cardpasswd)
                        if exe_result == errorcode.NO_ERROR:
                            common.show_message("已完成提现！", "NOTICE")
                        if exe_result == errorcode.BALANCE_NOT_ENOUGHT:
                            common.show_message("信用卡可透支余额不足!", "ERROR")
                        if exe_result == errorcode.CARD_PASS_ERROR:
                            common.show_message("信用卡密码错误!", "ERROR")
                    elif cost == "q":
                        quitflag = True
                        continue
                    else:
                        common.show_message("输入错误!", "ERROR")
        # 转账
        if _choose == "3":
            if card.frozenstatus == 1:
                common.show_message("此卡已冻结,请联系客服!", "ERROR")
            else:
                common.show_message("信用卡转账将收取 {0}% 的手续费!".format(settings.FETCH_MONEY_RATE * 100), "NOTICE")
                quitflag = False
                while not quitflag:
                    trans_cardno = common.input_msg("请输入要转账的卡号(q返回):")
                    if trans_cardno.isnumeric():
                        # 生成一个卡对象, 验证卡号是否存在
                        trans_cardobj = CreditCard(trans_cardno)

                        # 卡号不存在返回主菜单
                        if not trans_cardobj.card_is_exists:
                            common.show_message("卡号不存在,请确认!", "ERROR")
                            quitflag = True
                            continue
                        else:
                            # 卡号存在
                            trans_cost = common.input_msg("请输入要转账的金额: ")

                            # 如果输入的均为数字
                            if trans_cost.isnumeric():
                                comfirm = common.input_msg("确定要给卡号 {0} 转入人民币 {1} 元吗(y/n)?".format(trans_cardobj.cardno,
                                                                                                  trans_cost),
                                                           ("y", "n"))
                                if comfirm == "y":
                                    cardpasswd = common.input_msg("请输入信用卡密码:")

                                    # 执行转账操作
                                    exe_result = card.translate_money(float(trans_cost), cardpasswd, trans_cardobj)

                                    if exe_result == errorcode.NO_ERROR:
                                        common.show_message("转账完成！", "NOTICE")
                                    if exe_result == errorcode.BALANCE_NOT_ENOUGHT:
                                        common.show_message("信用卡可透支余额不足!", "ERROR")
                                    if exe_result == errorcode.CARD_PASS_ERROR:
                                        common.show_message("信用卡密码错误!", "ERROR")
                            else:
                                common.show_message("输入错误!", "ERROR")

                    elif trans_cardno == "q":
                        quitflag = True
                        continue
                    else:
                        common.show_message("输入错误!", "ERROR")

        # 还款
        if _choose == "4":
            # 更新一下对账单信息
            card.recreate_statement()

            quitflag = False
            while not quitflag:
                # 获取对账单所有列表
                interest_list = card.load_statement_list()
                # 获取还未还款的记录并显示
                message_info = report.print_statement_list(card.cardno, interest_list)

                # 如果有要还款的记录
                if len(message_info) > 0:
                    common.show_message(message_info, "NOTICE")
                    # 输入要还款的单号
                    serino_list = list()
                    for order in interest_list:
                        serino_list.append(list(order.keys())[0])
                    serino_list.append("q")
                    pay_serno = common.input_msg("请选择还款的16位账单号(q退出)：", tuple(serino_list))

                    if pay_serno == "q":
                        quitflag = True
                        continue
                    else:
                        for i in range(len(interest_list)):
                            for k, details in interest_list[i].items():
                                if k == pay_serno:
                                    # 显示指定单号的相信对账单信息
                                    common.show_message(report.print_statement_detail(card.cardno,
                                                                                      pay_serno,
                                                                                      details),
                                                        "NOTICE")
                                    pay_fee = common.input_msg("请输入还款金额:")
                                    if pay_fee.isnumeric():
                                        # 更新已还款金额 = 现在还的金额 + 已经还的金额
                                        total_payed = details["payed"] + float(pay_fee)
                                        interest_list[i][pay_serno]["payed"] = total_payed

                                        # 全还了吗？需要还款数 = 消费总费用 + 利息
                                        need_pay = details["total"] + details["interest"]
                                        if total_payed >= need_pay:
                                            # 还款数大于等于需要还款数，则更新已还款字段信息
                                            interest_list[i][pay_serno]["isfinished"] = 1
                                        else:
                                            # 没全部还款
                                            common.show_message("您尚未全部还款,请在还款日前尽快还款!", "NOTICE")
                                        # 将还款后的信息写入数据库更新
                                        dbapi.write_statement_list(card.cardno, interest_list)

                                        # 还款成功
                                        common.show_message("还款成功", "NOTICE")
                                        # 是否继续
                                        iscontinue = common.input_msg("继续还款吗(y/n)?", ("y", "n"))
                                        if iscontinue == "n":
                                            quitflag = True

                                    else:
                                        common.show_message("输入数据不正确，请重新输入!", "ERROR")
                else:
                    common.show_message("无账单信息！", "NOTICE")
                    quitflag = True


def get_users():
    """
    显示用户的信息,用户新建、删除、解锁用户时显示用户基本信息
    :return:
    """
    username = common.input_msg("请输入用户名:")
    # 创建一个用户实例
    _deluser = Users()
    _deluser.username = username
    # 如果用户名存在,load用户信息成功
    if _deluser.load_user_info():
        # 先显示一下用户的信息
        common.show_message(template.user_info.format(username=_deluser.username,
                                                      name=_deluser.name,
                                                      mobile=_deluser.mobile,
                                                      role=_deluser.role,
                                                      isdel="否" if _deluser.isdel == 0 else "是",
                                                      islocked="否" if _deluser.islocked == 0 else "是",
                                                      bindcard=_deluser.bindcard)
                            , "NOTICE")
        return _deluser
    else:
        common.show_message("用户名不存在!", "ERROR")
        return False


def fill_card_info():
    """
    填充信用卡资料信息
    :return: 返回一个信用卡对象
    """
    retry_flag = False
    while not retry_flag:
        cardno = common.input_msg("请输入卡号:")
        cardobj = CreditCard(cardno)
        if cardobj.card_is_exists:
            common.show_message("卡号已存在,请重新输入卡号", "ERROR")
            continue
        else:
            retry_flag = True
            continue

    cardobj.password = common.input_msg("请输入密码:")
    cardobj.credit_total = common.input_msg("信用额度(default:{0}):".format(cardobj.credit_total))
    cardobj.credit_balance = cardobj.credit_total
    cardobj.owner = common.input_msg("所有者:")
    return cardobj


def manager(userobj):
    """
    主菜单后台管理模块
    :param userobj: 当前登录用户对象
    :return:
    """
    if userobj.islogin:
        if userobj.role == "admin":
            quit_flag = False
            while not quit_flag:
                _show_template = template.index_admin
                print(_show_template.format(username=userobj.name))
                _choose = input("选择操作功能: ").strip().lower()
                # 创建新用户
                if _choose == "1":
                    _newuser = Users()
                    # 调用初始化用户函数创建新用户
                    _newuser.init_user_info()
                # 删除用户
                if _choose == "2":
                    _user = get_users()
                    if _user:
                        confirm = common.input_msg("确定要删除此用户吗(y/n)?", ("y", "n"))
                        if confirm == "y":
                            _user.del_user()
                            common.show_message("用户删除成功!", "NOTICE")
                # 解锁用户
                if _choose == "3":
                    _user = get_users()
                    if _user:
                        confirm = common.input_msg("确认解锁吗(y/n)?", ("y", "n"))
                        if confirm == "y":
                            _user.unlock_user()
                            common.show_message("用户解锁成功!", "NOTICE")
                # 发行信用卡
                if _choose == "4":
                    newcard = fill_card_info()
                    newcard.create_card()
                    common.show_message("发卡成功!", "NOTICE")

                # 冻结信用卡
                if _choose == "5":
                    cardno = common.input_msg("输入卡号:")
                    card = CreditCard(cardno)
                    if not card.card_is_exists:
                        common.show_message("卡号不存在", "ERROR")
                    else:
                        # 调用模板显示卡信息
                        common.show_message(template.card_info.format(cardno=card.cardno,
                                                                      owner=card.owner,
                                                                      total=card.credit_total,
                                                                      balance=card.credit_balance,
                                                                      status="正常" if card.frozenstatus == 0 else "冻结"
                                                                      ), "INFORMATION")
                        confirm = common.input_msg("确认要冻结此卡吗(y/n)?", ("y", "n"))
                        if confirm == "y":
                            card.frozenstatus = 1
                            card.update_card()
                            common.show_message("此卡已冻结!", "NOTICE")
                # 退出
                if _choose == "0":
                    quit_flag = True
        else:
            # 不是 admin 角色无权限
            common.show_message("权限不够!", "ERROR")
    else:
        common.show_message("请先登录系统!", "NOTICE")
        userobj.login()


if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    weekoftoday = date.weekday(datetime.now())
    curruser = Users()

    # 初始化对账单
    report.create_statement_main()

    # --------    开始主程序   -------------------
    exitflag = False
    while not exitflag:
        # 如果用户登录了，显示登录的界面; 未登录显示未登录的界面
        if not curruser.islogin:
            print(template.index_default_menu.format("", today, common.numtochr(weekoftoday)))
        else:
            print(template.index_logined_menu.format("欢迎您: {0}".format(curruser.name), today,
                                                     common.numtochr(weekoftoday)))

        choose = common.input_msg("选择功能编号[1-5]: ", ("1", "2", "3", "4", "5")).strip()
        if choose == "5":
            exitflag = True
            continue

        # 1 购物商城
        if choose == "1":
            curruser.db_load()
            doshopping(curruser)

        # 2 用户登录
        if choose == "2":
            curruser.db_load()
            user_login(curruser, today, weekoftoday)

        # 3 信用卡管理
        if choose == "3":
            card_center(curruser)

        # 4 后台管理
        if choose == "4":
            manager(curruser)

credit_card

2、配置文件包conf下代码：

2.1  参数配置文件settings.py：


#!/usr/bin/env python

import os,sys

# 程序文件主目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加环境变量
sys.path.append(BASE_DIR)

# 数据库信息
DATABASE = dict(engineer="file", dbpath=os.path.join(BASE_DIR, "database"), tables={"users": "users",
                                                                                    "shopping": "shoppingmark",
                                                                                    "creditcard": "creditcard"
                                                                                    })

# 日志文件存放路径
LOG_PATH = os.path.join(BASE_DIR, "logs")
# 账单报表文件路径
REPORT_PATH = os.path.join(BASE_DIR, "report")
# 用户登录失败最大次数
ERROR_MAX_COUNT = 3
# 日息费率
EXPIRE_DAY_RATE = 0.0005
# 转账、提现手续费
FETCH_MONEY_RATE = 0.05
# 信用额度
CREDIT_TOTAL = 10000
# 每月账单日期(默认每月22日为账单日)
STATEMENT_DAY = 6

settings

2.2  界面显示模板文件templates.py：


#!/usr/bin/env python
"""
该模块用来定义系统的菜单模板
"""
# 主程序中的主菜单

index_default_menu = '''
-------------------------------------------------------------------------
                             ATM 模拟程序

{0}                                        今天 {1}   星期{2}
-------------------------------------------------------------------------
【1】进入商城 【2】登录系统 【3】信用卡中心 【4】后台管理 【5】退出系统
'''

# 主程序中的用户登录后的显示菜单

index_logined_menu = '''
-------------------------------------------------------------------------
                             ATM 模拟程序

{0}                                        今天 {1}   星期{2}
-------------------------------------------------------------------------
【1】进入商城 【2】用户中心 【3】信用卡中心 【4】后台管理 【5】退出系统
'''

# 主程序中的用户中心菜单

index_user_center = '''
-------------------------------------------------------------------------
                                用户中心

当前用户:{0}                                   今天 {1}   星期{2}
-------------------------------------------------------------------------
【1】修改密码 【2】修改资料 【3】我的账单 【4】购物记录 【5】注销 【6】返回

'''

# 用户中心按键对应功能模块
user_center_func = {
    "1": {"module": "modules.users", "func": "modify_password"},
    "2": {"module": "modules.users", "func": "modify_user_info"},
    "3": {"module": "modules.report", "func": "print_bill_history"},
    "4": {"module": "modules.report", "func": "print_shopping_history"},
    "5": {"module": "modules.users", "func": "logout"}
}

# 购物模块的主菜单, menu 菜单在shopping模块中内部构造

shopping_index_menu = '''
    ==================================================================================
    =                                                                                =
    =                                 信用卡购物商城                                  =
    =                                                                                =
    ==================================================================================

    {menu}
    '''

# 账单报表显示模板
report_bill = '''
------------------------------------------------------------------------------
                                 用户中心 - 账单明细

卡号:{cardno}                           账单时间:{startdate} 至 {enddate}
------------------------------------------------------------------------------
     交易时间        交易类型        交易金额           流水号
{billdetail}

'''

# 购物历史记录显示模板
shopping_history = '''
------------------------------------------------------------------------------
                                  用户中心 - 购物明细

用户:{username}                           购物时间:{startdate} 至 {enddate}
------------------------------------------------------------------------------
'''

# 后台管理模板
index_admin = '''
------------------------------------------------------------------------------
                               后台管理

用户:{username}
------------------------------------------------------------------------------
【1】创建用户               【2】删除用户         【3】解锁用户
【4】发行信用卡             【5】冻结信用卡       【0】退出后台管理
'''

# ATM 管理模块
index_ATM = '''
------------------------------------------------------------------------------
                               信用卡管理中心

卡号:{cardno}
------------------------------------------------------------------------------
【1】我的信用卡    【2】提现    【3】转账     【4】还款    【5】返回
'''

# 显示用户基本信息模板
user_info = '''
------------------------------------------------------------------------------
                               用户基本信息

用 户 名:{username}        姓    名:{name}               手    机:{mobile}
用户权限:{role}            是否锁定:{islocked}           是否删除:{isdel}
信用卡号:{bindcard}
------------------------------------------------------------------------------
'''

# 显示信用卡基本信息模板
card_info = '''
-----------------------------------------------------------------------------------
                               信用卡基本信息

卡号:{cardno}   所有人:{owner}  信用额度:{total}  剩余额度:{balance} 状态:{status}
-----------------------------------------------------------------------------------
'''
report_statement_list = '''
----------------------------------------------------------------------------------
                                信用卡对账单列表
卡号:{cardno}
----------------------------------------------------------------------------------
    账单号            还款日        应还款        已还款
{show_msg}
'''

report_statement_detail = '''
---------------------------------------------------------------------------------------
                               信用卡对账单

卡号：{cardno}                                          账单编号:{serino}
---------------------------------------------------------------------------------------
  账单日            账单日期范围              还款日       应还款     已还款     利息
{billdate}    {sdate} 至 {edate}     {pdate}    {total}     {payed}     {interest}
---------------------------------------------------------------------------------------
账单明细：
     交易时间        交易类型        交易金额           流水号
{details}
'''

templates.py

2.3  错误代码文件errorcode.py：


#!/usr/bin/env python
"""
系统错误代码表
"""
NO_ERROR = 99999               # 系统正常返回
USER_NOT_EXISTS = 10000        # 用户名不存在
CARD_NOT_BINDED = 10001        # 用户未绑定信用卡
BALANCE_NOT_ENOUGHT = 10002    # 信用卡余额不足
CARD_OWNER_ERROR = 10003       # 绑定卡时输入的卡号与卡的所有人不一致
CARD_PASS_ERROR = 10004        # 信用卡密码错误

errorcode

3、数据库database下代码：

3.1  初如化数据模块init_db.py：


#!/usr/bin/env python
import json,os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings
from modules import common

# 初始化数据表
_shopping_list = {
    "1": {"typename": "食品生鲜", "product": (
        {"no": "0001", "name": "进口牛奶 欧德堡(Oldenburger)1L*12", "price": 95},
        {"no": "0002", "name": "乐虎氨基酸维生素功能饮料250ML*24罐", "price": 120},
        {"no": "0003", "name": "意大利进口 Ferrero Rocher费列罗巧克力(盒)", "price": 205},
        {"no": "0004", "name": "品湖韵阳澄湖大闸蟹礼券1388型 8只", "price": 458},
        {"no": "0005", "name": "三胖蛋 正宗内蒙原味大瓜子218g*6桶/礼", "price": 168},
        {"no": "0006", "name": "臻味山珍礼盒 吉年纳福1600g干菌山珍大礼包", "price": 256}
    )},
    "2": {"typename": "数码产品", "product": (
        {"no": "1001", "name": "佳能（Canon） EOS 6D 单反机身（不含镜头） 家庭套餐", "price": 9326},
        {"no": "1002", "name": "360安全路由P1 3mm纤薄设计 大户型智能无线路由器", "price": 89},
        {"no": "1003", "name": "小米 4c 高配版 全网通 白色 移动联通电信", "price": 1499},
        {"no": "1004", "name": "华为（HUAWEI）荣耀手环zero 经典黑短", "price": 399},
        {"no": "1005", "name": "步步高（BBK）家教机S2 香槟金 32G ", "price": 3468},
        {"no": "1006", "name": "Apple MacBook Air 13.3英寸笔记本电脑", "price": 6988}
    )},
    "3": {"typename": "男装女装", "product": (
        {"no": "2001", "name": "伊莲娜2016新款连衣裙英伦格子针织连衣裙假两件裙加厚", "price": 163},
        {"no": "2002", "name": "Maxchic玛汐2016春时尚分割修身圆领修身长袖连衣裙", "price": 235},
        {"no": "2003", "name": "2015新冬款加厚加绒牛仔裤女保暖小脚裤大码弹力铅笔裤", "price": 169},
        {"no": "2004", "name": "秋冬新款青年男士休闲连帽羽绒服男韩版修身短款外套", "price": 319},
        {"no": "2005", "name": "AAPE秋冬季新款 时尚潮牌猿人头袖英文字母印花男士休闲", "price": 298},
        {"no": "2006", "name": "2015秋冬新款加绒保暖套头卫衣 15541707 BC17灰花灰", "price": 159}
    )}
}

_user_list = {
    "test": {"password": "12345", "name": "测试", "mobile": "13511111111", "islocked": 0, "bindcard": "1001012345",
             "role": "user", "isdel": 0},
    "super": {"password": "12345", "name": "Admin", "mobile": "15257157418", "islocked": 0, "bindcard": "1001010002",
              "role": "admin", "isdel": 0}
}

_creditcard_list = {
    "1001012345": {"password": "12345", "credit_total": 10000, "credit_balance": 10000,
                   "owner": "test", "frozenstatus": 0},
    "1001010002": {"password": "12345", "credit_total": 10000, "credit_balance": 10000,
                   "owner": "super", "frozenstatus": 0}
}


# 初始化购物商城数据表 shopping_list.db
def init_db_shoppingmark():
    _db_file = os.path.join(settings.DATABASE['dbpath'], "shoppingmark.db")
    with open(_db_file, "w+") as f:
        f.write(json.dumps(_shopping_list))


# 初始化用户数据表 user_list.db
def init_db_users():
    _db_file = os.path.join(settings.DATABASE['dbpath'], "users.db")
    with open(_db_file, "w+") as fu:
        for k, v in _user_list.items():
            # 获得用户设置的密码
            tmppassword = _user_list[k]['password']
            # 对密码进行加密
            encrypassword = common.encrypt(tmppassword)
            # 修改明文密码
            _user_list[k]['password'] = encrypassword
        fu.write(json.dumps(_user_list))


# 初始化信用卡数据表 creditcard.db
def init_db_creditcard():
    _db_file = os.path.join(settings.DATABASE['dbpath'], "creditcard.db")
    with open(_db_file, "w+") as fc:
        for k, v in _creditcard_list.items():
            tmppassword = _creditcard_list[k]['password']
            encrypassword = common.encrypt(tmppassword)
            _creditcard_list[k]['password'] = encrypassword
        fc.write(json.dumps(_creditcard_list))


# 初始化数据表
def init_database():
    tables = list(settings.DATABASE['tables'].values())  # 数据表名称列表
    database = settings.DATABASE['dbpath']  # 数据表存放路径
    for _table in tables:
        # 如果表不存在
        if not os.path.exists(os.path.join(database, "{0}.db".format(_table))):
            print("Table {0}.db create successfull".format(_table))
            # 通过反射初始化数据表

            if hasattr(sys.modules[__name__], "init_db_{0}".format(_table)):
                init_func = getattr(sys.modules[__name__], "init_db_{0}".format(_table))
                init_func()
            else:
                common.write_error_log("init table {0} failed,no function init_db_{0} found".format(_table))


if __name__ == "__main__":
    init_database()

init_db

执行init_db脚本可生成json格式的users.db、shoppingmark.db和creditcard.db

内容如下：

3.2  数据文件：


{"test": {"isdel": 0, "name": "\u6d4b\u8bd5", "password": "8ad8dd76a16dca9ffcfc970a807a6378", "islocked": 0, "role": "user", "bindcard": "1001012345", "mobile": "13511111111"}, "super": {"isdel": 0, "name": "Admin", "password": "8ad8dd76a16dca9ffcfc970a807a6378", "islocked": 0, "role": "admin", "bindcard": "1001010002", "mobile": "15257157418"}}

users


{"2": {"product": [{"no": "1001", "name": "\u4f73\u80fd\uff08Canon\uff09 EOS 6D \u5355\u53cd\u673a\u8eab\uff08\u4e0d\u542b\u955c\u5934\uff09 \u5bb6\u5ead\u5957\u9910", "price": 9326}, {"no": "1002", "name": "360\u5b89\u5168\u8def\u7531P1 3mm\u7ea4\u8584\u8bbe\u8ba1 \u5927\u6237\u578b\u667a\u80fd\u65e0\u7ebf\u8def\u7531\u5668", "price": 89}, {"no": "1003", "name": "\u5c0f\u7c73 4c \u9ad8\u914d\u7248 \u5168\u7f51\u901a \u767d\u8272 \u79fb\u52a8\u8054\u901a\u7535\u4fe1", "price": 1499}, {"no": "1004", "name": "\u534e\u4e3a\uff08HUAWEI\uff09\u8363\u8000\u624b\u73afzero \u7ecf\u5178\u9ed1\u77ed", "price": 399}, {"no": "1005", "name": "\u6b65\u6b65\u9ad8\uff08BBK\uff09\u5bb6\u6559\u673aS2 \u9999\u69df\u91d1 32G ", "price": 3468}, {"no": "1006", "name": "Apple MacBook Air 13.3\u82f1\u5bf8\u7b14\u8bb0\u672c\u7535\u8111", "price": 6988}], "typename": "\u6570\u7801\u4ea7\u54c1"}, "1": {"product": [{"no": "0001", "name": "\u8fdb\u53e3\u725b\u5976 \u6b27\u5fb7\u5821(Oldenburger)1L*12", "price": 95}, {"no": "0002", "name": "\u4e50\u864e\u6c28\u57fa\u9178\u7ef4\u751f\u7d20\u529f\u80fd\u996e\u6599250ML*24\u7f50", "price": 120}, {"no": "0003", "name": "\u610f\u5927\u5229\u8fdb\u53e3 Ferrero Rocher\u8d39\u5217\u7f57\u5de7\u514b\u529b(\u76d2)", "price": 205}, {"no": "0004", "name": "\u54c1\u6e56\u97f5\u9633\u6f84\u6e56\u5927\u95f8\u87f9\u793c\u52381388\u578b 8\u53ea", "price": 458}, {"no": "0005", "name": "\u4e09\u80d6\u86cb \u6b63\u5b97\u5185\u8499\u539f\u5473\u5927\u74dc\u5b50218g*6\u6876/\u793c", "price": 168}, {"no": "0006", "name": "\u81fb\u5473\u5c71\u73cd\u793c\u76d2 \u5409\u5e74\u7eb3\u798f1600g\u5e72\u83cc\u5c71\u73cd\u5927\u793c\u5305", "price": 256}], "typename": "\u98df\u54c1\u751f\u9c9c"}, "3": {"product": [{"no": "2001", "name": "\u4f0a\u83b2\u5a1c2016\u65b0\u6b3e\u8fde\u8863\u88d9\u82f1\u4f26\u683c\u5b50\u9488\u7ec7\u8fde\u8863\u88d9\u5047\u4e24\u4ef6\u88d9\u52a0\u539a", "price": 163}, {"no": "2002", "name": "Maxchic\u739b\u6c502016\u6625\u65f6\u5c1a\u5206\u5272\u4fee\u8eab\u5706\u9886\u4fee\u8eab\u957f\u8896\u8fde\u8863\u88d9", "price": 235}, {"no": "2003", "name": "2015\u65b0\u51ac\u6b3e\u52a0\u539a\u52a0\u7ed2\u725b\u4ed4\u88e4\u5973\u4fdd\u6696\u5c0f\u811a\u88e4\u5927\u7801\u5f39\u529b\u94c5\u7b14\u88e4", "price": 169}, {"no": "2004", "name": "\u79cb\u51ac\u65b0\u6b3e\u9752\u5e74\u7537\u58eb\u4f11\u95f2\u8fde\u5e3d\u7fbd\u7ed2\u670d\u7537\u97e9\u7248\u4fee\u8eab\u77ed\u6b3e\u5916\u5957", "price": 319}, {"no": "2005", "name": "AAPE\u79cb\u51ac\u5b63\u65b0\u6b3e \u65f6\u5c1a\u6f6e\u724c\u733f\u4eba\u5934\u8896\u82f1\u6587\u5b57\u6bcd\u5370\u82b1\u7537\u58eb\u4f11\u95f2", "price": 298}, {"no": "2006", "name": "2015\u79cb\u51ac\u65b0\u6b3e\u52a0\u7ed2\u4fdd\u6696\u5957\u5934\u536b\u8863 15541707 BC17\u7070\u82b1\u7070", "price": 159}], "typename": "\u7537\u88c5\u5973\u88c5"}}

shoppingmarket


{"1001010002": {"credit_total": 10000, "owner": "super", "password": "8ad8dd76a16dca9ffcfc970a807a6378", "frozenstatus": 0, "credit_balance": 275}, "1001012345": {"credit_total": 10000, "owner": "test", "password": "8ad8dd76a16dca9ffcfc970a807a6378", "frozenstatus": 0, "credit_balance": 9537}}

creditcard

4、数据访问层dbhelper下的dbapi.py：

数据访问层模块，读写数据


#!/usr/bin/env python
"""
__author: super
数据库访问层：
1 提供从数据文件、报表文件中读取数据的接口
2 将数据写入到数据文件的接口
"""
import os,json
from conf import settings
from modules.common import write_error_log,write_log


def append_db_json(contant, filename):
    """
    将信息以 json 格式写入数据表文件(追加)
    :param contant: 要写入的 json 格式内容
    :param filename: 要写入的数据表文件名
    :return: 无返回
    """
    try:
        with open(filename, 'a+') as fa:
            fa.write(json.dumps(contant))
            fa.write("\n")
    except Exception as e:
        write_error_log(e)


def write_db_json(contant, filename):
    """
    将信息以 json 格式写入数据表文件（覆盖）
    :param contant: 写入的json数据内容
    :param filename: 要写入的文件名
    :return: 无返回结果
    """
    try:
        with open(filename, 'w+') as fw:
            fw.write(json.dumps(contant))
    except Exception as e:
        write_error_log(e)


def load_data_from_db(tabename):
    """
    从指定的数据表中获取所有数据,通过 json 方式将数据返回
    :param tabename: 数据文件名
    :return: 返回所有结果
    """
    try:
        with open(tabename, 'r+') as f:
            return json.load(f)
    except Exception as e:
        write_error_log(e)


def load_bill_report(cardno, startdate, enddate):
    """
    从信用卡对账单中获取指定卡的对账信息数据, 获取某一个时间段内的数据
    :param enddate: 查询记录的结束日期
    :param startdate: 查询记录的开始日期
    :param cardno: 信用卡卡号
    :return: 信用卡对账单数据 ,返回结果为 list 数据类型
    """
    r_file = os.path.join(settings.REPORT_PATH, "report_bill")
    result = []
    try:
        with open(r_file, "r+") as f:
            for line in f:
                _record = json.loads(line)
                if _record["cardno"] == cardno:
                    if startdate <= _record["starttime"] <= enddate:
                        result.append(_record)
        return result
    except Exception as e:
        write_error_log(e)


def load_shop_history(user, startdate, enddate):
    """
    查找报表记录中的指定用户的购物历史记录,将结果存入到列表中
    :param user:  用户名
    :param startdate: 开始日期
    :param enddate: 结束日期
    :return: 结果 dict_list
    """
    _file = os.path.join(settings.REPORT_PATH, "shopping_history")
    result = list()
    try:
        with open(_file, "r") as f:
            for line in f:
                _record = json.loads(line)
                # 如果找到指定用户记录
                if list(_record.keys())[0] == user:
                    if list(_record.values())[0]["time"] >= startdate <= enddate:
                        result.append(_record)
        return result
    except Exception as e:
        write_error_log("dbapi > load_shop_history > {0}".format(e))


def load_statement_list(cardno):
    """
    从对账单中获取记录,
    :param cardno: 对账单文件
    :return: 返回一个列表
    """
    file = os.path.join(settings.REPORT_PATH, "statement_{0}".format(cardno))
    result_list = list()
    try:
        if os.path.isfile(file):
            with open(file, 'r+') as f:
                for line in f:
                    statement = json.loads(line)
                    result_list.append(statement)
        return result_list
    except Exception as e:
        write_error_log("dbapi > load_statement_list > {0}".format(e))


def write_statement_list(cardno, db_list):
    """
    将对账单记录写入对账单文件，更新
    :param cardno: 对账单的卡号
    :param db_list: 新的对账信息列表
    :return:
    """
    file = os.path.join(settings.REPORT_PATH, "statement_{0}".format(cardno))
    with open(file, 'w+') as f:
        for newrecord in db_list:
            f.write(json.dumps(newrecord))
            f.write("\n")

dbapi

5、业务逻辑层modules下代码：

5.1 公共函数模块common.py：


#!/usr/bin/env python
import hashlib,random,os,time,logging

from datetime import datetime, date
from conf import settings



def verification_code():
    """
    生成一个4位的验证码
    :return:  返回验证码
    """
    _code = list()
    for i in range(4):
        ra = random.randrange(4)
        if i == ra:
            _code.append(chr(random.randrange(97, 122)))
        else:
            _code.append(str(i))
    result = ''.join(_code)
    return result


def encrypt(string):
    """
    字符串加密函数
    :param string: 待加密的字符串
    :return:  返回加密过的字符串
    """
    ha = hashlib.md5(b'oldboy')
    ha.update(string.encode('utf-8'))
    result = ha.hexdigest()
    return result


def write_error_log(content):
    """
    写错误日志
    :param content: 日志信息
    :return: 无返回，写入文件 error.log
    """
    _content = "\n{0} : {1} ".format(datetime.now().strftime("%Y-%m-%d %X"), content)
    _filename = os.path.join(settings.LOG_PATH, "errlog.log")
    with open(_filename, "a+") as fa:
        fa.write(_content)

def write_log(content,levelname):
    """
    写正常登录，退出，转帐，取现日志
    :param content: 日志信息
    :return: 无返回，写入文件 sysinfo.log
    """
    _filename = os.path.join(settings.LOG_PATH, "sysinfo.log")
    logging.basicConfig(level=logging.INFO,
                encoding = "UTF-8",
                format='%(asctime)s %(levelname)s %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S %p',
                filename=_filename,
                filemode='a+')
    if levelname == 'debug':
        logging.debug(content)
    elif levelname == 'info':
        logging.info(content)
    elif levelname == 'warning':
        logging.warning(content)
    elif levelname == 'error':
        logging.error(content)
    elif levelname == 'critical':
        logging.critical(content)
    else:
        show_message('输入错误',"ERROR")



# 获取汉字个数
def get_chinese_num(uchar):
    i = 0
    for utext in uchar:
        if u'\u4e00' <= utext <= u'\u9fa5':
            i += 1
    return i


def show_message(msg, msgtype):
    """
    对print函数进行封装，根据不同类型显示不同颜色
    :param msg:  显示的消息体
    :param msgtype:  消息类型
    :return: 返回格式化过的内容
    """
    if msgtype == "NOTICE":
        show_msg = "\n\033[1;33m{0}\033[0m\n".format(msg)
    elif msgtype == "ERROR":
        show_msg = "\n\033[1;31m{0}\033[0m\n".format(msg)
    elif msgtype == "INFORMATION":
        show_msg = "\n\033[1;32m{0}\033[0m\n".format(msg)
    else:
        show_msg = "\n{0}\n".format(msg)
    print(show_msg)


def create_serialno():
    """
    生成一个消费、转账、提款时的流水号，不重复
    :return: 流水号
    """
    serno = "{0}{1}".format(datetime.now().strftime("%Y%m%d%H%M%S"), str(int(time.time())))
    return serno


def numtochr(num_of_weekday):
    """
    将数字星期转换为中文数字
    :param num_of_weekday: 星期几的数字字符( 0,1,2,3,4,5,6)
    :return: 中文 星期几
    """
    chrtuple = ( '一', '二', '三', '四', '五', '六','日')
    num = int(num_of_weekday)
    return chrtuple[num]


def input_msg(message, limit_value=tuple()):
    """
    判断input输入的信息是否为空的公共检测函数,为空继续输入,不为空返回输入的信息
    :param limit_value: 对输入的值有限制,必须为limit_value的值;ex:("admin","user")
    :param message: input()函数的提示信息
    :return: 返回输入的信息
    """
    is_null_flag = True
    while is_null_flag:
        input_value = input(message).strip().lower()
        if not input_value:
            show_message("输入不能为空!", "ERROR")
            continue
        elif len(limit_value) > 0:
            if input_value not in limit_value:
                show_message("输入的值不正确,请重新输入!", "ERROR")
                continue
            else:
                is_null_flag = False
        else:
            is_null_flag = False
            continue
    return input_value

def input_date(msg, default_date):
    """
    对输入的日期进行判断是否正确 yyyy-mm-dd or yyyy-m-d
    :param msg:输入提示信息
    :param default_date: 默认日期
    :return:返回日期 str类型
    """
    check_flag = False
    while not check_flag:
        strdate = input(msg).strip()
        if not strdate:
            strdate = default_date

        try:
            date_list = strdate.split("-")
            result = date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
            check_flag = True
        except ValueError:
            show_message("输入日期不合法,请重新输入!", "ERROR")
            continue
    return result.strftime("%Y-%m-%d")

common

5.2 用户类模块users.py：


#!/usr/bin/env python
import os
from conf import settings, errorcode, template
from modules import common
from modules.creditcard import CreditCard
from dbhelper import dbapi


class Users(object):
    # 用户数据库
    __database = "{0}.db".format(os.path.join(settings.DATABASE['dbpath'], settings.DATABASE["tables"]["users"]))

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


    def _user_login(self, password,code):
        """
        用户登录验证模块,对用户对象进行判断,登录成功后返回一个新的用户对象
        :return:
        """
        # 对输入的密码加密
        _password = common.encrypt(password)

        for user, details in self.dict_user.items():
            # 找到用户名
            if user == self.username and not details["isdel"]:
                # 是否被锁定
                if details["islocked"] == 0:
                    # 账户未锁定,验证密码
                    if details["password"] == _password and code == self.code:
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
        """
        用户登录过程函数，输入用户名和密码后调用内部方法 _user_login进行登录验证
        :return:
        """
        while self.trycount < settings.ERROR_MAX_COUNT:
            self.username = input("用户名: ")
            password = input("密  码: ")
            common.show_message("验证码：{0}".format(self.code),"INFORMATION")
            check_code = input("请输入验证码:")

            if not self.user_exists:
                common.show_message("用户名不存在！", "ERROR")
                continue

            # 调用用户登录方法进行登录
            self._user_login(password,check_code)

            # 用户锁定就直接退出
            if self.islocked:
                common.show_message("该用户已被锁定,请联系系统管理员！", "ERROR")
                self.trycount = 0

                break

            # 登录成功 退出登录
            if self.islogin:
                break
            else:
                common.show_message("用户名密码错误", "NOTICE")
        else:
            # 失败3次了还输? 锁了你
            self.islocked = 1

            # 更新用户信息
            self.dict_user[self.username]["islocked"] = self.islocked
            self.update_user()
            common.show_message("输入错误次数过多,请联系系统管理员!", "ERROR")

        # 将用户的登录尝试次数恢复初始值 0
        self.trycount = 0

    def update_user(self):
        """
        用户数据更新方法,用户修改信息、用户账户锁定、解锁等操作之后更新数据库文件
        :return:
        """
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

    @property
    def user_exists(self):
        """
        判断用户名是否存在,用户注册时判断，存在返回True, 否则返回False
        :return: True / False
        """
        if self.username in list(self.dict_user.keys()):
            return True
        else:
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
        self.dict_user[self.username]["islocked"] = 0
        self.update_user()

    def init_user_info(self):
        """
        创建用户，完善用户资料信息
        :return:
        """
        is_null_flag = True
        while is_null_flag:
            self.username = input("登录用户名(小写字母）:").strip().lower()
            if not self.username:
                common.show_message("用户名不能为空", "ERROR")
                continue
            elif self.user_exists:
                common.show_message("该用户名已存在", "ERROR")
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

    @staticmethod
    def user_auth(func):
        """
        用户登录验证装饰器, userobj 为登录用户对象,未登录时可以传入一个空对象
        :param func: 被装饰的函数
        :return:
        """

        def login_check(self, userobj):
            # 用户还未登录
            if not userobj.islogin:
                common.show_message("用户未登录,请先登录系统！", "NOTICE")

                # 开始用户登录
                userobj.login()
                # 登录成功了吗
                if userobj.islogin:
                    return func(self, userobj)
                else:
                    common.show_message("登录失败,请联系系统管理员!", "ERROR")

            else:
                return func(self, userobj)

        return login_check

    def bind_card(self, cardobj):
        """
        用户绑定信用卡,调用该方法绑定卡时,先实例化卡对象,再判断卡是否有效(卡是否存在、卡密码是否正确)
        :param cardobj: 信用卡对象
        :return: 成功 99999 / 失败 错误码
        """
        # 判断用户输入的卡号和实际卡号所有人是不是一致的
        if self.username == cardobj.owner:
            self.bindcard = cardobj.cardno
            self.update_user()
            return errorcode.NO_ERROR
        else:
            return errorcode.CARD_OWNER_ERROR

    def logout(self):
        """
        注销当前用户,将系统属性置空
        :return:
        """
        self.islogin = False
        self.bindcard = ""
        self.mobile = ""
        self.name = ""
        self.password = ""
        self.username = ""
        common.show_message("注销成功", "NOTICE")

    def modify_password(self):
        """
        个人中心 - 修改密码
        :return:
        """
        _not_null_flag = False
        try:
            while not _not_null_flag:
                _new_password = input("输入新密码: ").strip()
                _confirm_password = input("再次输入确认密码:").strip()
                if not _new_password or not _confirm_password:
                    common.show_message("密码不能为空,请重新输入!", "ERROR")
                    continue
                if _new_password != _confirm_password:
                    common.show_message("两次输入密码不一致,请重新输入!", "NOTICE")
                    continue
                _not_null_flag = True
            self.password = _new_password
            _password = common.encrypt(self.password)
            self.dict_user[self.username]["password"] = _password
            self.update_user()
            common.show_message("密码修改成功!", "INFORMATIOM")
            return True
        except Exception as e:
            common.write_error_log(e)
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
        frmuser = template.user_info.format(
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
        new_name = input("姓名({0}); ".format(self.name))
        new_mobile = input("手机({0}): ".format(self.mobile))
        self.name = self.name if len(new_name) == 0 else new_name
        self.mobile = self.mobile if len(new_mobile) == 0 else new_mobile
        # 输入信用卡卡号
        _card_noerror = False
        while not _card_noerror:
            new_bindcard = input("绑定卡({0}): ".format(self.bindcard))
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
        if self.user_exists:
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

users

5.3 购物类模块shopping.py：


#!/usr/bin/env python
import os
from datetime import datetime
from conf import settings, errorcode, template
from modules.users import Users
from modules.creditcard import CreditCard
from modules import common
from dbhelper import dbapi


class Shopping(object):
    # 购物商城界面
    __welcome_title = template.shopping_index_menu
    # 购物商城商品数据库
    __database = "{0}.db".format(os.path.join(settings.DATABASE['dbpath'], settings.DATABASE["tables"]["shopping"]))
    # 购物记录报表存放文件
    __shop_report_file = os.path.join(settings.REPORT_PATH, "shopping_history")

    def __init__(self):
        # 存放购物车列表
        self.shopping_cart = []
        # 购物总费用
        self.shopping_cost = 0
        # 用户选择的商品分类 key
        self.goods_classify_id = ""
        # 数据表中所有商品信息
        self.shop_market = dict()
        # 购物商城欢迎菜单
        self.welcome_menu = ""

        self._get_shop_market()  # 获取数据表数据
        self._construct_title_menu()  # 购物商城欢迎菜单

    def _get_shop_market(self):
        """
        获取购物商城所有商品信息,存入类字段(shop_market)
        :return:  self.shop_market
        """
        self.shop_market = dbapi.load_data_from_db(self.__database)

    def _construct_title_menu(self):
        """
        构建欢迎菜单,存入类字段(welcome_menu)
        :return: self.welcome_menu
        """
        _menu = []
        keys = list(self.shop_market.keys())
        # 按类型编号排序
        keys.sort()
        for goods_type_id in keys:
            goods_type_name = self.shop_market[goods_type_id]['typename']
            _menu.append("[{0}] {1}   ".format(goods_type_id, goods_type_name))
        _menu.append("[{0}] {1}   ".format("4", "查看购物车"))
        _menu.append("[{0}] {1}   ".format("5", "购物结算"))
        _menu.append("[{0}] {1}   ".format("0", "退出商城"))
        self.welcome_menu = self.__welcome_title.format(menu="".join(_menu))

    def get_goods_list_by_typeid(self):
        """
        根据用户选择的商品分类编号,获取该分类下所有商品,返回结果为tuple
        :return:  返回tuple类型: 指定分类商品下的所有商品信息
        """
        if self.goods_classify_id not in list(self.shop_market.keys()):
            return None
        else:
            return self.shop_market[self.goods_classify_id]['product']

    @staticmethod
    def print_goods_list(goods_list):
        """
        将goods_list列表中的商品信息输出到屏幕,商品列表或购物车商品列表
        :param goods_list: 要打印的商品信息，类型为tuple
        :return: 输出到屏幕
        """
        _goodlist = goods_list
        print("|{0}|{1}|{2}|".format('商品编号'.center(11), '商品名称'.center(50), '商品价格(RMB)'.center(10)))
        print('%s' % '-' * 95)

        for goods in _goodlist:
            chinese_num = common.get_chinese_num(goods['name'])
            len_name = len(goods['name'])
            space_str = (55 - len_name - chinese_num) * " "
            print('| %-12s | %s |%15s|' % (goods['no'], goods['name'] + space_str, str(goods['price'])))

    def add_shopping_card(self, goodsid):
        """
        根据用户输入的商品编号，将商品编号加入购物车，如果商品编号不存在返回False,添加成功返回True
        :param goodsid: 商品编号
        :return: 成功 True / 失败 False
        """
        exist_flag = False
        # 从商品列表中获取指定类型的所有商品信息(tuple)
        _goods_tuple = self.shop_market[self.goods_classify_id]['product']

        # 开始查找输入的商品编号
        for goods in _goods_tuple:
            if goods['no'] == goodsid:
                self.shopping_cart.append(goods)
                self.shopping_cost += goods['price']
                exist_flag = True
                break
        return exist_flag

    @Users.user_auth
    def payfor_shopcart(self, userobj):
        """
        购物车结算模块,功能包括：购物车付款、购物记录写入文件、
        :param kwargs: 字典参数 {cost=购物车金额, userobj=用户对象}
        :return:
        """
        # 判断用户有没有绑定信用卡
        if not userobj.bindcard:
            # 用户没有绑定信用卡,直接返回错误，在外层绑卡
            return errorcode.CARD_NOT_BINDED
        else:
            # 用户绑定了信用卡了, 获取信用卡信息(实例化对象)
            cardobj = CreditCard(userobj.bindcard)
            # 卡余额够吗
            if cardobj.credit_balance < self.shopping_cost:
                common.show_message("您的信用卡本月额度不够! ", "NOTICE")
                return errorcode.BALANCE_NOT_ENOUGHT
            else:
                # 生成一个流水号
                serno = common.create_serialno()
                # 调用卡的支付模块进行支付
                cardobj.card_pay(self.shopping_cost, 1, serno)
                # 记录购物流水
                shopping_record = {userobj.username: {"time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                                                      "cost": self.shopping_cost,
                                                      "serno": serno,
                                                      "detail": self.shopping_cart}}
                # 写入报表记录文件
                dbapi.append_db_json(shopping_record, self.__shop_report_file)

                # 购物结算完成后将对象的购物车清空, 购物车商品总价清0 ,待下次购物
                self.shopping_cart.clear()
                self.shopping_cost = 0
                return errorcode.NO_ERROR

shopping

5.4 信用卡类模块creditcard.py：


#!/usr/bin/env python
import os
from datetime import datetime, date, timedelta
from conf import settings, errorcode
from modules import common
from dbhelper import dbapi


class CreditCard(object):
    __database = "{0}.db".format(os.path.join(settings.DATABASE['dbpath'], settings.DATABASE["tables"]["creditcard"]))

    def __init__(self, cardno):
        # 信用卡卡号
        self.cardno = cardno
        # 信用卡密码
        self.password = ""
        # 卡所有者
        self.owner = ""
        # 信用卡额度
        self.credit_total = settings.CREDIT_TOTAL
        # 信用卡透支余额
        self.credit_balance = settings.CREDIT_TOTAL
        # 信用卡日息
        self.dayrate = settings.EXPIRE_DAY_RATE
        # 提现手续费率
        self.feerate = settings.FETCH_MONEY_RATE
        # 所有信用卡数据
        self.credit_card = {}
        # 信用卡是否存在标识
        #self.card_is_exists = True
        # 信用卡状态(是否冻结)
        self.frozenstatus = 0

        # 获取卡的信息
        self._load_card_info()

    def _load_card_info(self):
        """
        根据用户输入的卡号获取信用卡信息,如果卡号不存在就返回False
        :return: 信用卡对象
        """
        exists_flag = False
        self.credit_card = dbapi.load_data_from_db(self.__database)
        for key, items in self.credit_card.items():
            if key == self.cardno:
                self.password = self.credit_card[self.cardno]['password']
                self.credit_total = self.credit_card[self.cardno]['credit_total']
                self.credit_balance = self.credit_card[self.cardno]['credit_balance']
                self.owner = self.credit_card[self.cardno]['owner']
                self.frozenstatus = self.credit_card[self.cardno]['frozenstatus']

                exists_flag = True
                break
        #self.card_is_exists = exists_flag


    @property
    def card_is_exists(self):
        if self.cardno in list(self.credit_card.keys()):
            return True
        else:
            return False


    def card_pay(self, cost, paytype, sereialno):
        """
        信用卡支付,从信用卡可透支余额中扣费
        :param sereialno: 流水号
        :param cost: 消费金额 float类型
        :param paytype: 消费类型 int类型  ( 1:消费、2:转账、3:提现、4:手续费 ) 对于2,3类型的支付要扣手续费,单记录一条流水单
        :return:
        """
        if paytype == 1:
            payfor = "消费"
        elif paytype == 2:
            payfor = "转账"
        elif paytype == 3:
            payfor = "提现"
        elif paytype == 4:
            payfor = "手续费"
        else:
            payfor = "未知"

        # 支付扣款
        self.credit_balance -= cost

        # 记录消费流水对账单,将发生了费用还没有还款的账单信息写入文件 report_bill 中
        _tmp_bill_record = dict(cardno="{0}".format(self.cardno),
                                starttime=datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M"),
                                payfor=payfor,
                                cost=cost,
                                serialno=sereialno)
        dbapi.append_db_json(_tmp_bill_record, os.path.join(settings.REPORT_PATH, "report_bill"))

        # 更新信用卡可透支余额信息到数据库 creditcard.db
        self.credit_card[self.cardno]["credit_balance"] = self.credit_balance
        dbapi.write_db_json(self.credit_card, self.__database)

    def create_card(self):
        """
        新发行一张行用卡
        :return:
        """
        password = common.encrypt(self.password)
        self.credit_card[self.cardno] = dict(password=password,
                                             credit_total=self.credit_total,
                                             credit_balance=self.credit_balance,
                                             owner=self.owner,
                                             frozenstatus=self.frozenstatus)
        # 保存到数据库
        dbapi.write_db_json(self.credit_card, self.__database)

    def update_card(self):
        password = common.encrypt(self.password)
        self.credit_card[self.cardno]["password"] = password
        self.credit_card[self.cardno]["owner"] = self.owner
        self.credit_card[self.cardno]["credit_total"] = self.credit_total
        self.credit_card[self.cardno]["credit_balance"] = self.credit_balance
        self.credit_card[self.cardno]["frozenstatus"] = self.frozenstatus
        # 写入数据库
        dbapi.write_db_json(self.credit_card, self.__database)

    def _pay_check(self, cost, password):
        """
        转账、提现时验证操作，判断卡的余额与支付密码是否正确。并返回错误类型码
        :param cost:  转账、提现金额（包含手续费）
        :param password: 支付密码
        :return: 错误码
        """
        totalfee = cost
        # 提现金额及手续费和大于余额,
        if totalfee > self.credit_balance:
            return errorcode.BALANCE_NOT_ENOUGHT
        elif common.encrypt(password) != self.password:
            return errorcode.CARD_PASS_ERROR
        else:
            return errorcode.NO_ERROR

    def fetch_money(self, count, passwd):
        """
        提现
        :param count: 提现金额
        :param passwd:信用卡提现密码
        :return: 返回错误类型码
        """
        totalfee = count + count * self.feerate
        check_result = self._pay_check(totalfee, passwd)
        if check_result == errorcode.NO_ERROR:
            # 扣取提现金额并写入数据库，生成账单
            self.card_pay(count, 3, common.create_serialno())
            # 扣取手续费并写入数据库, 生成账单
            self.card_pay(count * self.feerate, 4, common.create_serialno())
            return errorcode.NO_ERROR
        else:
            return check_result

    def translate_money(self, trans_count, passwd, trans_cardobj):
        """
        信用卡转账模块
        :param trans_count: 要转账的金额
        :param passwd: 信用卡密码
        :param trans_cardobj: 对方卡号对应的卡对象
        :return: 转账结果
        """
        totalfee = trans_count + trans_count * self.feerate
        check_result = self._pay_check(totalfee, passwd)
        if check_result == errorcode.NO_ERROR:
            # 先扣款，生成消费流水账单
            self.card_pay(trans_count, 2, common.create_serialno())
            # 扣手续费, 生成消费流水账单
            self.card_pay(trans_count * self.feerate, 4, common.create_serialno())
            # 给对方卡充值,并写入数据库文件
            trans_cardobj.credit_balance += totalfee
            trans_cardobj.update_card()
            return errorcode.NO_ERROR
        else:
            return check_result

    def load_statement_list(self):
        """
        获取要还款的对账单列表数据，仅包含对账单号、还款日、应还款额、已还款额
        :return: 对账单列表
        """
        # 获取要显示的信息
        list_info = dbapi.load_statement_list(self.cardno)
        return list_info

    def recreate_statement(self):
        """
        根据今天的日期将当前卡的对账单重新生成,主要对过了还款日的账单重新生成利息信息
        :return:
        """
        # 获取当前日期
        today = datetime.strptime(date.today().strftime("%Y-%m-%d"), "%Y-%m-%d")
        # 获取所有卡的对账单信息
        card_statement = dbapi.load_statement_list(self.cardno)
        tmp_list = list()
        # 如果有记录
        if len(card_statement) > 0:
            for record in card_statement:
                for k, v in record.items():
                    # 如果已经还款了,将对账单放入临时列表中
                    if v["isfinished"] == 1:
                        tmp_list.append(record)
                    else:
                        # 还未还款? 获取还款日期
                        pay_day = datetime.strptime(v["pdate"], "%Y-%m-%d")
                        # 如果还款日大于当前日期,无利息
                        day_delta = (today - pay_day).days
                        if day_delta > 0:
                            # 过了还款日了，计算利息 = 总费用 * 日息 * 超过天数
                            interest = v["total"] * settings.EXPIRE_DAY_RATE * day_delta
                            # 更新利息信息记录
                            record[k]["interest"] = interest
                            # 将更新过的记录写入临时列表
                            tmp_list.append(record)
                        else:
                            # 没有过还款日直接写入临时列表
                            tmp_list.append(record)
            # 都处理完了，将更新过的列表写入文件，替换原有信息
            dbapi.write_statement_list(self.cardno, tmp_list)
        else:
            # 此卡没有对账单记录
            pass

creditcard

5.5 报表模块report.py：


#!/usr/bin/env python
"""
账单生成模块：
1 从report_bill中便利所有流水记录，获取所有卡号
2 将卡号存放到列表中
3 对列表进行集合类型转换
4 根据集合中的唯一的卡号信息，每个卡号生成一个文件 cardno_startdate_enddate报表文件,文件中存放字典信息对账单
5 将对账的费用统计信息接入一个统计文件 ,包括字段：卡号、对应详单文件名、账单日期、还款日期、应还款金额、已还款金额、
{"detail":{[],[]}
 "
"""
import calendar
import os
from datetime import datetime, timedelta
from datetime import date
from dbhelper import dbapi
from conf import template
from conf import settings
from modules import common
from modules.shopping import Shopping


def get_date():
    """
    用户输入一个时间段,如果显示报表是要提供开始、结束日期,返回开始，结束时间
    :return: 字典格式,{"start":startdate, "end": enddate}
    """
    startdate = common.input_date("输入查询开始日期(yyyy-mm-dd)[default:2016-01-01]: ", "2016-01-01")
    enddate = common.input_date("输入查询结束日期(yyyy-mm-dd)[default: today]: ", date.today().strftime("%Y-%m-%d"))
    return {"start": startdate, "end": enddate}


def print_shopping_history(userobj):
    """
    个人中心 - 购物历史记录打印模块
    :param userobj:    用户对象
    :return:  显示指定时间段的购物历史记录
    """
    date_between = get_date()
    start = date_between["start"]
    end = date_between["end"]
    # 通过dbapi获得要查询的记录列表,结果为dict_list类型
    history_list = dbapi.load_shop_history(userobj.username, start, end)
    # 获取模板文件样式
    _template = template.shopping_history
    common.show_message(_template.format(username=userobj.username,
                                         startdate=start,
                                         enddate=end), "NOTICE")

    if not history_list:
        common.show_message("无购物记录!", "NOTICE")
    else:
        for record in history_list:
            # 获取消费信息
            _tmprec = list(record.values())[0]
            common.show_message("\n流水号:{0}       时间:{1}     消费金额：{2}\n".format(_tmprec["serno"],
                                                                               _tmprec["time"],
                                                                               _tmprec["cost"]), "NOTICE")
            # 调用Shopping的类方法打印详单
            Shopping.print_goods_list(_tmprec["detail"])


def print_bill_history(userobj):
    """
    个人中心-账单明细 打印模块
    :param userobj: 用户对象
    :return:
    """
    dates = get_date()
    startdate = dates["start"]
    enddate = dates["end"]
    # 保存所有账单流水的记录列表,数据为一个字符串
    msglist = list()
    # 获取显示模板
    _template = template.report_bill
    # 获取符合条件的账单明细记录(dict_list 类型)
    _recordlist = dbapi.load_bill_report(userobj.bindcard, startdate, enddate)
    for record in _recordlist:
        tmpmsg = "{time}      {costtype}  {cost}     {crdno}".format(time=record["starttime"],
                                                                     costtype=record["payfor"].ljust(10),
                                                                     cost=str(record["cost"]).ljust(6),
                                                                     crdno=record["serialno"])
        msglist.append(tmpmsg)
    # 填充模板并打印
    common.show_message(_template.format(cardno=userobj.bindcard,
                                         startdate=startdate,
                                         enddate=enddate,
                                         billdetail="\n".join(msglist)
                                         ), "NOTICE")


def create_card_statement(cardno):
    """
    生成信用卡对账单
    :param cardno:卡号
    :return:
    """
    # 获得当前时间
    currday = datetime.now().strftime("%Y-%m-%d")
    today = date.today().day

    # 如果是账单日22号 开始生成账单
    if today == settings.STATEMENT_DAY:
        # 生成对账单数据库中存放对账单数据的字典 key

        startday = (datetime.now() + timedelta(days=-30)).strftime("%Y%m{0}".format(settings.STATEMENT_DAY))
        endday = datetime.now().strftime("%Y%m%d")
        statement_key = "{start}{end}".format(start=startday, end=endday)


        # 从对账单流水中计算出要还款的金额
        startdate = (datetime.now() + timedelta(days=-30)).strftime("%Y-%m-{0} 00:00:00".format(settings.STATEMENT_DAY))
        enddate = (datetime.now()  + timedelta(days=1)).strftime("%Y-%m-%d 00:00:00")
        # 获取卡号对应的消费流水记录列表
        bill_list = dbapi.load_bill_report(cardno, startdate, enddate)

        statement_total = 0.00
        # 如果有消费记录,生成对账单
        if len(bill_list) > 0:
            for bill in bill_list:
                # 获取一个对账单日期的消费总费用
                statement_total += bill["cost"]

            # 获取还款日期 下个月10号
            statement_pdate = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-10")

            # 生成对账单的统计数据字典{"2016012220160222":{"账单日":currday,
            #                                             "账单范围":startdate至enddate,
            #                                             "账单金额":statement_bill,
            #                                             "已还款":0,
            #                                             "还款日":pdate
            #                                             "已还完":0}}

            statement_dict = {statement_key: {"billdate": currday,
                                              "startdate": startdate,
                                              "enddate": enddate,
                                              "total": statement_total,
                                              "payed": 0,
                                              "pdate": statement_pdate,
                                              "interest": 0,
                                              "isfinished": 0}}
            # 对账单文件名
            file_name = os.path.join(settings.REPORT_PATH, "statement_{0}".format(cardno))
            # 写入文件
            dbapi.append_db_json(statement_dict, file_name)



def create_statement_main():
    """
    卡对账单初始化模块,从卡数据库文件中加载所有卡号，对所有卡调用生成对账单模块
    :return:
    """
    _database = "{0}.db".format(os.path.join(settings.DATABASE['dbpath'], settings.DATABASE["tables"]["creditcard"]))
    card_list = dbapi.load_data_from_db(_database)
    cards = list(card_list.keys())
    for cardno in cards:

        create_card_statement(cardno)


def print_statement_list(cardno, list_info):
    """
    将卡号对应的未还款记录显示出来，
    :param cardno: 卡号
    :param list_info: 信用卡对账单信息
    :return: 无返回
    """
    # 获取显示模板
    show_template = template.report_statement_list
    tmpstrlist = list()

    # 如果获取到了对账单数据
    if len(list_info) > 0:
        for record in list_info:
            for k, v in record.items():
                # 如果还未全部还完款
                if v["isfinished"] == 0:
                    tmpmsg = "{sno}{pdate}{spay}{payed}".format(sno=k.ljust(20),
                                                                pdate=v["pdate"].ljust(13),
                                                                spay=str(v["total"]).ljust(13),
                                                                payed=str(v["payed"]))
                    tmpstrlist.append(tmpmsg)
        tmpstrlist.append("您目前共有 {0} 个账单".format(len(tmpstrlist)))
        # 填充模板,将填充后的魔板信息返回
        result = show_template.format(cardno=cardno, show_msg="\n".join(tmpstrlist))
        return result
    else:
        return ""


def print_statement_detail(cardno, serino, details):
    """
    还款模块 - 用户选择还款的单号后，显示详细的还款对账单及流水信息
    :param cardno: 信用卡卡号
    :param serino: 对账单编号
    :param statement_list: 对账单列表
    :return: 返回填充后的模板信息
    """
    # 获取显示模板
    show_template = template.report_statement_detail
    # 获取指定编号的详细信息
    _billdate = details["billdate"]  # 账单日
    _sdate = details["startdate"]  # 账单开始日期
    _edate = details["enddate"]  # 账单结束日期
    _total = details["total"]  # 费用总额
    _payed = details["payed"]  # 已还款金额
    _pdate = details["pdate"]  # 还款日
    _interest = details["interest"]  # 利息

    # 获取详细的流水清单
    _flows = list()
    _recordlist = dbapi.load_bill_report(cardno, _sdate, _edate)
    for info in _recordlist:
        tmpmsg = "{time}      {costtype}  {cost}     {crdno}".format(time=info["starttime"],
                                                                     costtype=info["payfor"].ljust(10),
                                                                     cost=str(info["cost"]).ljust(6),
                                                                     crdno=info["serialno"])
        _flows.append(tmpmsg)

    # 填充模板
    result_message = show_template.format(cardno=cardno,
                                          serino=serino,
                                          billdate=_billdate,
                                          sdate=_sdate[0:10],
                                          edate=_edate[0:10],
                                          pdate=_pdate,
                                          total=_total,
                                          payed=_payed,
                                          interest=_interest,
                                          details="\n".join(_flows))
    return result_message

report

6、报表目录report下生成的文件：

6.1 消费流水记录report_bill：


{"serialno": "201603061903271457262207", "cost": 463, "payfor": "\u6d88\u8d39", "cardno": "1001012345", "starttime": "2016-03-06 19:03"}
{"serialno": "201603061903331457262213", "cost": 0, "payfor": "\u6d88\u8d39", "cardno": "1001012345", "starttime": "2016-03-06 19:03"}
{"serialno": "201603062148271457272107", "payfor": "\u6d88\u8d39", "starttime": "2016-03-06 21:48", "cost": 9725, "cardno": "1001010002"}
{"serialno": "201603062148351457272115", "payfor": "\u6d88\u8d39", "starttime": "2016-03-06 21:48", "cost": 0, "cardno": "1001010002"}

report_bill

6.2 购物历史记录shopping_history


{"test": {"time": "2016-03-06 19:03", "detail": [{"price": 95, "name": "\u8fdb\u53e3\u725b\u5976 \u6b27\u5fb7\u5821(Oldenburger)1L*12", "no": "0001"}, {"price": 205, "name": "\u610f\u5927\u5229\u8fdb\u53e3 Ferrero Rocher\u8d39\u5217\u7f57\u5de7\u514b\u529b(\u76d2)", "no": "0003"}, {"price": 163, "name": "\u4f0a\u83b2\u5a1c2016\u65b0\u6b3e\u8fde\u8863\u88d9\u82f1\u4f26\u683c\u5b50\u9488\u7ec7\u8fde\u8863\u88d9\u5047\u4e24\u4ef6\u88d9\u52a0\u539a", "no": "2001"}], "cost": 463, "serno": "201603061903271457262207"}}
{"test": {"time": "2016-03-06 19:03", "detail": [], "cost": 0, "serno": "201603061903331457262213"}}
{"super": {"serno": "201603062148271457272107", "time": "2016-03-06 21:48", "cost": 9725, "detail": [{"price": 9326, "no": "1001", "name": "\u4f73\u80fd\uff08Canon\uff09 EOS 6D \u5355\u53cd\u673a\u8eab\uff08\u4e0d\u542b\u955c\u5934\uff09 \u5bb6\u5ead\u5957\u9910"}, {"price": 399, "no": "1004", "name": "\u534e\u4e3a\uff08HUAWEI\uff09\u8363\u8000\u624b\u73afzero \u7ecf\u5178\u9ed1\u77ed"}]}}
{"super": {"serno": "201603062148351457272115", "time": "2016-03-06 21:48", "cost": 0, "detail": []}}

shopping_history

6.3 对帐单statement_卡号：


{"201602620160306": {"payed": 0, "pdate": "2016-04-10", "total": 9725.0, "startdate": "2016-02-6 00:00:00", "interest": 0, "isfinished": 0, "enddate": "2016-03-07 00:00:00", "billdate": "2016-03-06"}}

statement_id

7、日志文件目录logs：

7.1 错误日志记录errlog.log


2016-02-08 18:43:09 : Expecting value: line 1 column 113 (char 112)
2016-02-10 15:35:52 : 'dict' object has no attribute 'key'
2016-02-10 15:38:19 : 'dict' object has no attribute 'key'
2016-02-10 15:41:33 : 'dict' object has no attribute 'key'
2016-02-10 15:45:49 : 'dict' object has no attribute 'key'
2016-02-10 15:49:35 : dbapi > load_shop_history > 'dict' object has no attribute 'key'
2016-02-16 09:27:52 : [Errno 2] No such file or directory: '1001012345'
2016-02-16 09:41:54 : [Errno 2] No such file or directory: '1001012345'
2016-02-16 09:50:20 : dbapi > load_statement_list > Extra data: line 1 column 203 - line 1 column 405 (char 202 - 404)
2016-02-16 09:56:42 : dbapi > load_statement_list > Extra data: line 1 column 203 - line 1 column 405 (char 202 - 404)
2016-03-16 12:23:15 : dbapi > load_statement_list > Extra data: line 1 column 208 - line 2 column 1 (char 207 - 410)
2016-03-16 12:31:06 : dbapi > load_statement_list > Extra data: line 1 column 208 - line 2 column 1 (char 207 - 410)
2016-03-05 14:36:51 : dbapi > load_statement_list > Expecting value: line 2 column 1 (char 1)
2016-03-06 18:34:44 : [Errno 2] No such file or directory: 'D:\\python\\pycharm\\python34\\day5\\CreditCard\\database\\users.db'
2016-03-06 18:34:44 : [Errno 2] No such file or directory: 'D:\\python\\pycharm\\python34\\day5\\CreditCard\\database\\creditcard.db'
2016-03-06 18:35:09 : [Errno 2] No such file or directory: 'D:\\python\\pycharm\\python34\\day5\\CreditCard\\database\\users.db'
2016-03-06 18:35:09 : [Errno 2] No such file or directory: 'D:\\python\\pycharm\\python34\\day5\\CreditCard\\database\\creditcard.db'
2016-03-06 18:42:06 : [Errno 2] No such file or directory: '__database'
2016-03-06 18:42:38 : [Errno 2] No such file or directory: '__database'
2016-03-06 18:42:55 : [Errno 2] No such file or directory: '__database'
2016-03-06 18:43:51 : [Errno 2] No such file or directory: '__database'
2016-03-06 18:44:21 : name 'json' is not defined
2016-03-06 18:46:08 : name 'json' is not defined
2016-03-06 18:48:03 : name 'json' is not defined
2016-03-06 18:48:10 : name 'json' is not defined
2016-03-06 18:48:47 : name 'json' is not defined
2016-03-06 18:49:02 : name 'json' is not defined
2016-03-06 18:49:11 : name 'json' is not defined
2016-03-06 18:50:52 : name 'json' is not defined

errlog.log