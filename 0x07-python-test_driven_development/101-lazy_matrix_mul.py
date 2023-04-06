#!/usr/bin/python3
""" use numpy to multiply two matrices the lazy way"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
        """ Function that takes in 2 matrices and multiplies them
        Args:
            m_a: matrix 1
            m_b: matrix 2
        Return: the product of m_a and m_b
        """
        return np.matmul(m_a, m_b)
