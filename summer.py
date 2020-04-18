# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:02:11 2020

@author: sundar
"""
import asyncio
import json
import time
import aiohttp

async def worker(name, nums, session):
    print(f'worker-{name}')
    url = f'http://qrng.anu.edu.au/API/jsonI.php?length={nums}&type=uint16'
    response = await session.request(method='GET',url=url)
    value = await response.text()
    value = json.loads(value)
    return sum(value['data'])
    return value

async def main():
    #await asyncio.sleep(1)
    async with aiohttp.ClientSession() as session:
        response = await worker('bob',3,session)
        sums = await asyncio.gather(*(worker(f'w{i}',n,session) for i,n in enumerate(range(2,30))))
        print("response: ",response)
        print("sums: ",sums)
        
if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f'executed in {elapsed:0.2f} second')