import asyncio
import random
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.future import select

Base = declarative_base()

class Node(Base):
    __tablename__ = 'nodes'
    id = Column(Integer, primary_key=True)
    ip_address = Column(String, unique=True, nullable=False)
    status = Column(String, default="unknown")

DATABASE_URL = "sqlite+aiosqlite:///network.db"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
async def add_nodes():
    async with AsyncSessionLocal() as session:
        nodes = [
            Node(ip_address=f"192.168.1.{i}")
            for i in range(1, 16)
        ]
        session.add_all(nodes)
        await session.commit()

async def get_nodes():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Node))
        return result.scalars().all()

async def check_node(node):
    await asyncio.sleep(random.uniform(0.5, 2))
    node.status = random.choice(["online", "offline"])
    return node

async def monitor_nodes():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Node))
        nodes = result.scalars().all()
        tasks = [check_node(node) for node in nodes]
        updated_nodes = await asyncio.gather(*tasks)
        for node in updated_nodes:
            await session.merge(node)
        await session.commit()
def print_nodes(nodes, title):
    print("\n", title)
    print("-" * 40)
    for node in nodes:
        print(f"{node.id} | {node.ip_address} | {node.status}")
async def main():
    await init_db()
    await add_nodes()
    nodes_before = await get_nodes()
    print_nodes(nodes_before, "Nodes before monitoring")
    await monitor_nodes()
    nodes_after = await get_nodes()
    print_nodes(nodes_after, "Nodes after monitoring")

asyncio.run(main())






