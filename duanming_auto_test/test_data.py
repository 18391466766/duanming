# -*- coding:utf-8 -*-
import pytest
import yaml
class TestData:
    #参数可以为str、tuple、list
    @pytest.mark.parametrize(["a","b"],yaml.safe_load(open("./test_data.yaml")))
    def test_data(self,a,b):
        print(a+b)