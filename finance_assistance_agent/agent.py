from google.adk.agents import LlmAgent

finance_assistance_agent = LlmAgent(
    name="finance_assistance_agent",
    model="gemini-2.5-flash",
    description="An agent that provides financial assistance and advice to users.",
    instruction="""You are a helpful and knowledgeable financial assistant.
You can provide advice on budgeting, saving, investing, and other financial topics.
Always provide accurate and up-to-date information.""",
)

root_agent = finance_assistance_agent