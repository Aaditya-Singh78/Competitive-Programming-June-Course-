# -*- coding: utf-8 -*-
"""540. Single Element in a Sorted Array

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_O2jTS98mmGwWxGZ5czYTxeeMQNr0xDn
"""

class Solution:
    def singleNonDuplicate(self, a: List[int]) -> int:
        
        #XOR
        s=0
        for i in a:
            s=s^i
        return s