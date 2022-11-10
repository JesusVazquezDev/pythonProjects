#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:41:50 2022

@author: jesusvazquez
"""

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    # FIXME: The following line will throw ValueError exception.
    #        Insert try/except blocks to catch the exception.
    try:
        age = int(parts[1]) + 1
        print(f'{name} {age}')
    except ValueError:
        print(f'{name} {0}')
    
    # Get next line
    parts = input().split()
    name = parts[0]