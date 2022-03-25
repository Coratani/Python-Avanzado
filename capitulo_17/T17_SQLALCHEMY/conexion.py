# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 11:13:55 2021

@author: zimiz
"""
from sqlalchemy import create_engine

engine = create_engine("sqlite:///minegocio.sqlite",echo=False)