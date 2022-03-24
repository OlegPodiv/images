# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 11:29:45 2021

@author: atman
"""

import turtle as t
def go_snowy(lenght):
    if lenght < 5:
        t.forward(lenght)
    else:
        go_snowy(lenght / 3)
        t.left(60)
        go_snowy(lenght / 3)
        t.right(120)
        go_snowy(lenght / 3)
        t.left(60)
        go_snowy(lenght / 3)

t.speed(100)        
go_snowy(100)
t.right(120)
go_snowy(100)
t.right(120)
go_snowy(100)
        