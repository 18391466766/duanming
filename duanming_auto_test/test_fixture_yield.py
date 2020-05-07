# -*- coding:utf-8 -*-
import pytest

@pytest.fixture(scope='module')
#作用域： module是在模块之前执行，模块之后执行
def open():
    print("打开浏览器")
    yield
    print('执行teardown')
    print("关闭浏览器")
    pass

def test_search1(open):
    print('test_search1')
    raise NameError
    pass
def test_search2(open):
    print('test_search2')
    pass
def test_search3(open):
    print('test_search3')
    pass
if __name__=='__main__':
    pytest.main()


