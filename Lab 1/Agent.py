from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
import asyncio

class HelloAgent(Agent):
    class HelloBehaviour(OneShotBehaviour):
        async def run(self):
            print("Hello! My first SPADE agent is running.")
            await self.agent.stop()

    async def setup(self):
        print("Agent starting...")
        self.add_behaviour(self.HelloBehaviour())

async def main():
    agent = HelloAgent("agent1@localhost", "agentpass")
    await agent.start()
    await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
