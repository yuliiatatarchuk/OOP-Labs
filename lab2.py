import asyncio
import random
import time
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def connect(self, node):
        self.connections.append(node)
        node.connections.append(self)
class Router(Node):
    pass
class Packet:
    def __init__(self, src, dest, size, protocol):
        self.src = src
        self.dest = dest
        self.size = size
        self.protocol = protocol
        self.visited = []
class TCPProtocol:
    name = "TCP"
    @staticmethod
    async def transmit(src, dest, network):
        packet = Packet(src, dest, random.randint(200, 500), "TCP")
        await src.send(packet, network)

class UDPProtocol:
    name = "UDP"
    @staticmethod
    async def transmit(src, dest, network):
        packet = Packet(src, dest, random.randint(50, 200), "UDP")
        await src.send(packet, network)
async def simulate_packet_transfer():
    print("Packet sent")
    await asyncio.sleep(random.uniform(0.01, 0.1))
    print("Packet received")
asyncio.run(simulate_packet_transfer())

class Network:
    def __init__(self):
        self.nodes = []
        self.loss_rate = random.uniform(0.10, 0.15)
        self.packets_sent = 0
        self.packets_lost = 0
        self.total_time = 0

    async def simulate(self, protocol, packets=5):
        for _ in range(packets):
            src, dest = random.sample(self.nodes, 2)
            start = time.time()
            self.packets_sent += 1
            await protocol.transmit(src, dest, self)
            self.total_time += time.time() - start
    def analyze(self):
        avg_time = self.total_time / self.packets_sent
        loss = (self.packets_lost / self.packets_sent) * 100
        bandwidth = (self.packets_sent - self.packets_lost) / self.total_time

        print(f"Середній час передачі: {avg_time:.4f} с")
        print(f"Втрати пакетів: {loss:.2f}%")
        print(f"Пропускна здатність: {bandwidth:.2f} пак/с")


    def visualize(self):
        G = nx.Graph()
        for node in self.nodes:
            for conn in node.connections:
                G.add_edge(node.name, conn.name)
        nx.draw(G, with_labels=True, node_color="skyblue",
            node_size=2500, font_size=10)
        plt.title("Зіркова топологія")
        plt.show()

async def main():
    network_star = Network()
    router = Router("Router")
    pcs = [Node(f"PC{i}") for i in range(1, 5)]
    network_star.nodes = [router] + pcs

    for pc in pcs:
        router.connect(pc)

    await network_star.simulate(TCPProtocol, 25)
    network_star.analyze()
    network_star.visualize()

    network_bus = Network()
    pcs_bus = [Node(f"PC{i}") for i in range(1, 5)]
    network_bus.nodes = pcs_bus

    for i in range(len(pcs_bus) - 1):
        pcs_bus[i].connect(pcs_bus[i + 1])

    await network_bus.simulate(TCPProtocol, 25)
    network_bus.analyze()
    network_bus.visualize()

async def send(self, packet, network):
    await asyncio.sleep(random.uniform(0.05, 0.3))
    if random.random() < network.loss_rate:
        network.packets_lost += 1
        return
    await self.forward(packet, network)
Node.send = send

async def forward(self, packet, network):
    if self == packet.dest:
        return

    if self in packet.visited:
        return

    packet.visited.append(self)

    for node in self.connections:
        if node not in packet.visited:
            await node.send(packet, network)

Node.forward = forward
asyncio.run(main())

