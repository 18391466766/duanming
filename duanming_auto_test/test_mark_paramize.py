# -*- coding:utf-8 -*-
import pytest
import sys

@pytest.mark.parametrize("test_input,expected ",[("3+5",8),("2+5",7),("7*5",30)])
def test_eval(test_input,expected):
    #eval 将字符串str当成有效的表达式来求值，并返回结果
    assert eval(test_input) == expected


#参数组合
@pytest.mark.parametrize("x",[1,2])
@pytest.mark.parametrize("y",[8,10,11])
def test_foo(x,y):
    print(f"测试数据组合x：{x},y：{y}")


#方法名作为参数
test_user_data = ['Tome','Jerry']
@pytest.fixture(scope='module')
def login_r(request):
    #这里接受并传入的参数
    user = request.param
    print(f"\n 打开首页准备登录，登录用户：{user}")
    return user
#indirect=True,可以把传过来的参数当函数来执行
@pytest.mark.parametrize("login_r",test_user_data,indirect=True)
#@pytest.mark.skip("此次用例不执行")
#@pytest.mark.skipif(sys.platform == 'darwin',reason='不再macos上执行')
@pytest.mark.xfail
def test_login(login_r):
    a = login_r
    print(f"测试用例中login的返回值：{a}")
    assert a!=""
    raise NameError

if __name__ == "__main__":
    pytest.main('-v')