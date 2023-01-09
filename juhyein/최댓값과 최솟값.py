#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(s):
    s = s.split()
    for i in range(len(s)) : s[i] = int(s[i])
    s = sorted(s)
    answer = str(s[0])+" "+str(s[-1])
    return answer

