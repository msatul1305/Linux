import asyncio

async def fetch_data():
  print("start fetching")
  await asyncio.sleep(2)
  print("done fetching")
  return {'data': 1}

async def print_numbers():
  for i in range(10):
    print(i)
    await asyncio.sleep(0.5)

async def main():
  task2 = asyncio.create_task(print_numbers())
  await fetch_data()

  await task2

asyncio.run(main())
