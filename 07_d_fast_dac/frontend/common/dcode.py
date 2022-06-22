from typing import List
from os import path, environ
from dataclasses import dataclass, asdict

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
# '/Users/onesixx/my/git/dash_01f/07_d_fast_dac'


@dataclass
class DType_CD:
    Comparison: str = 'C'
    Period: str = 'P'

# print(asdict(DType()))


@dataclass
class Bank_CD:
    Bank1: str = '1'
    Bank2: str = '2'
    Bank3: str = '3'

# print(asdict(Bank_CD()))
# {'Bank1': '1', 'Bank2': '2', 'Bank3': '3'}
# {v: k for k, v in asdict(Bank_CD()).items()}
