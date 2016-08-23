# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 13:57:17 2016

@author: karol
"""
from sympy import plot_implicit, And, Eq, symbols
from sympy.solvers import solve

madera, aluminio = symbols('madera aluminio')

frm = madera - 6
fra = aluminio - 4
frv = madera*6 + aluminio*8 - 48
fgt = madera*180 + aluminio*90

e1 = Eq(madera - 6, 0)
e3 = Eq(madera*6 + aluminio*8 - 48, 0)


sol = solve([Eq(frm, 0), Eq(frv, 0)], [madera, aluminio])
val_opt = fgt.subs(sol)


plot = plot_implicit(And(frm <= 0, fra <= 0, frv <= 0), (madera, -1, 10),
                     (aluminio, -1, 10), line_color='orange', show=False)
plot.extend(plot_implicit(Eq(fgt, val_opt), (madera, -1, 10),
                          (aluminio, -1, 10), line_color='blue', show=False))
plot.show()
