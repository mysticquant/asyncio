# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:25:21 2020

@author: sundar
"""
from random import randint
import time
import asyncio

def randn():
    time.sleep(3)
    return randint(1,10)

async def randn2():
    await asyncio.sleep(3)
    return randint(1,10)

def odds(start,stop):
    for odd in range(start,stop+1,2):
        yield odd

async def square_odds(start,stop):
    for odd in range(start,stop+1,2):
        await asyncio.sleep(2)
        yield odd **2
        
async def main():
    odd_values = [odd for odd in odds(3,15)]
    print(odd_values)
    odds2 = tuple(odds(21,29))
    print(odds2)
    
    start = time.perf_counter()
    #r = await randn2()
    #r = await asyncio.gather(randn2(),randn2(),randn2())
    r = await asyncio.gather(*(randn2() for _ in range(10)))
    elapsed = time.perf_counter() - start
    print("r:",r)
    print("took " ,elapsed)
    
    async for so in square_odds(11,17):
        print(so)

if __name__ == "__main__":
   asyncio.run( main() )