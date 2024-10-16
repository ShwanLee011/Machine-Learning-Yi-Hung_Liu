# -*- coding: utf-8 -*-
import numpy as np
from qpsolvers import solve_qp
import scipy.io
import math
#%% Quadratic problem
'''
1. 請參照qpsolvers的Documentation，將訓練資料矩陣化並調整成符合solve_qp的輸入格式。
2. solver請使用"clarabel"。如果出現問題請參考：https://github.com/qpsolvers/qpsolvers/blob/master/doc/installation.rst#open-source-solvers
3. 由於dual problem的求解演算法不同和精度差異，Matlab和Python的Alpha值會有差異
'''

# alpha = solve_qp(H, f,None,None,Aeq, beq, lb, ub, solver="clarabel")
    
'''
請以下列方法對alpha值進行處理，再接著求解bias'''

eps =   2.2204e-16
for i in range(alpha.size):
    if alpha[i] >= C - np.sqrt(eps):
        alpha[i] = C
        alpha[i] = np.round(alpha[i],6)
    elif  alpha[i] <= 0 + np.sqrt(eps):
        alpha[i] = 0
        alpha[i] = np.round(alpha[i],6)
    else:
        alpha[i] = np.round(alpha[i],6)
        print(f"support vector: alpha = {alpha[i]}")


#%% SVM accomplish，
'''
接續二次規劃所求得之alpha計算bias，即可得到SVM之模型。
此階段程式碼請自行實現。
'''
#%% Test
'''
利用上述步驟所訓練之SVM之模型建立決策函數，並將test代入得到決策結果。
此階段程式碼請自行實現。
'''