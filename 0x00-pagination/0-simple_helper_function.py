#!/usr/bin/env python3
"""
index_range
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple:
    '''
    Returning tuple containing pagination start index and end index.
    '''
    return ((page_size * (page - 1)), page_size * page)