# -*- coding:utf-8 -*-
import pytest
#
# @pytest.fixture()
#
# def login():
#     print("这是一个登录方法")
def test_case1(login):
    print("test_case1，需要登录")
    pass

def test_case2():
    print("test_case2，不需要登录")
    pass

def test_case3(login):
    print("test_case3，也需要登录")
    pass
if __name__=='__main__':
    pytest.main()
