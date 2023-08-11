#!/usr/bin/python3
'''
Module for class City.
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
    City class inherits from BaseModel.

    Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    '''
    state.id = ""
    name = ""