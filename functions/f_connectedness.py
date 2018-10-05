# import required modules
import numpy as np
import pandas as pd


# connectedness

def var_p_to_var_1(ai_list):
    """
    :param ai_list: the Coef calculated
    :return: the coef of VAR1
    """
    ar1_coef = np.zeros((7, 1))
    for coef_i in ai_list:
        ar1_coef = np.column_stack((ar1_coef, coef_i))
    ar1_coef = np.delete(ar1_coef, 0, 1)
    nrow = ar1_coef.shape[0]
    lag = len(ai_list)
    n = nrow * lag
    ar1_coef_down = np.identity(n)
    ar1_coef_down = np.delete(ar1_coef_down, np.s_[(n-nrow):n], 0)
    ar1_coef = np.vstack((ar1_coef, ar1_coef_down))
    return ar1_coef


def ar1_coef_to_psi(coef, h=5):
    """
    :param coef: the coef estimated
    :param h: the period of predicted future from now
    :return: The mechanism of periods to periods
    """
    n = coef.shape[0]
    lag = coef.shape[1]/n
    i_k = np.identity(n)
    zeros = np.zeros((n, coef.shape[1]-n))
    j = np.column_stack((i_k, zeros))
    ai_list = []
    for i in range(1, int(lag) + 1):
        ai_list.append(coef[:, 0:n])
        coef = np.delete(coef, np.s_[0:7], 1)
    ar1_coef = var_p_to_var_1(ai_list)
    psi = []
    psi.append(i_k)
    big_i = np.identity(ar1_coef.shape[1])
    for i in range(2, h+2):
        big_i = np.dot(big_i, ar1_coef)
        psi.append(np.dot(np.dot(j, big_i), j.transpose()))
    return psi


def theta(coef, sigma_hat, h=5):
    p = np.linalg.cholesky(sigma_hat)
    n = coef.shape[0]
    matrix = np.zeros(shape=(n, n))
    row, col = np.diag_indices(matrix.shape[0])
    matrix[row, col] = np.diagonal(p)
    inv = np.linalg.inv(matrix).transpose()
    psi = ar1_coef_to_psi(coef, h)
    theta_unit = []
    theta_std = []
    for i in range(0, (h+1)):  # must use append
        theta_std.append(np.dot(psi[i], p))
        theta_unit.append(np.dot(np.dot(psi[i], p), inv))
    return theta_unit, theta_std


def generalized_variance_decomp(m, coef, sigma_hat, h=5):
    n = coef.shape[0]
    i_k = np.identity(n)
    m_i = i_k[:, (m-1)]
    psi = ar1_coef_to_psi(coef, h)
    theta_value = theta(coef, sigma_hat, h)[1]
    diag = np.diagonal(sigma_hat)
    inv_sigma2 = 1/diag
    # i = 0
    den = []
    num = []
    decomp = []
    den_fill = (np.linalg.
                multi_dot((m_i, theta_value[0], theta_value[0].T,
                          m_i[np.newaxis].T)))
    den.append(den_fill)
    num_fill = np.square(np.linalg.multi_dot((m_i, psi[0], sigma_hat)))
    num.append(num_fill)
    decomp.append(num_fill * inv_sigma2 / den_fill)
    for l in range(1, h):
        den_fill = den[l-1] + (np.linalg.
                               multi_dot((m_i, theta_value[l], theta_value[l].T,
                                          m_i[np.newaxis].T)))
        den.append(den_fill)
        num_fill = (np.square(np.linalg.multi_dot((m_i, psi[l], sigma_hat))) +
                    num[l-1])
        num.append(num_fill)
        decomp.append(num_fill*inv_sigma2/den_fill)
    return decomp


class Connectedness:
    def __init__(self, coef, sigma_hat):

        # the varilables required to lauch this class
        self.Coef = coef
        self.Sigma_hat = sigma_hat

        # return the Full_Connectedness
        self.full_connectedness = None

    def f_full_connectedness(self, h=5):

        coef = self.Coef
        sigma_hat = self.Sigma_hat

        n = coef.shape[0]
        connetedeness = []
        for i in range(1, (n + 1)):
            target = generalized_variance_decomp(i, coef, sigma_hat, h)[h - 1]
            connetedeness.append(target)
        connetedeness = np.array(connetedeness).T
        for i in range(0, n):  # first time modification to 1
            connetedeness[i] = connetedeness[i] / np.sum(connetedeness[i])
        connetedeness = connetedeness.T
        for i in range(0, n):  # second time modification to 1
            connetedeness[i] = connetedeness[i] / np.sum(connetedeness[i])
        from_other = []
        for i in range(0, len(connetedeness)):
            connectedness_value = connetedeness[i]
            from_other_value = 1 - connectedness_value[i]
            from_other.append(from_other_value)
        to_other = []
        for i in range(0, len(connetedeness)):
            connectedness = np.array(connetedeness).T[i]
            to_other_value = np.sum(connectedness) - connectedness[i]
            to_other.append(to_other_value)
        spill_over = np.sum(from_other) / n
        np.matrix(from_other).transpose()
        up = np.concatenate((np.matrix(connetedeness), np.matrix(from_other).transpose()), axis=1)
        down = np.concatenate((np.matrix(to_other), np.matrix(spill_over)), axis=1)
        connetedeness_table = np.concatenate((up, down), axis=0)

        self.full_connectedness = pd.DataFrame(connetedeness_table)