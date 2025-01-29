from phi.agent import Agent
from phi.model.groq import Groq

agent = Agent(
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    markdown=True
)

agent.print_response("Share a 2 sentence horror story.")