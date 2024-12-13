import asyncio
import aiosqlite


async def async_fetchall():
  async with aiosqlite.connect("users.db") as db:
    async with db.execute("SELECT * FROM users") as cursor:
      rows = await cursor.fetchall()
      for row in rows:
        print(row)
      return rows

async def async_fetch_older_users():
  async with aiosqlite.connect("users.db") as db:
    async with db.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
      rows = await cursor.fetchall()
      for row in rows:
        print(row)
      return rows
    
async def fetch_CONCURRENTLY():
  results = await asyncio.gather(async_fetchall(), async_fetch_older_users())
  return results

if __name__ == "__main__":
  asyncio.run(fetch_CONCURRENTLY())