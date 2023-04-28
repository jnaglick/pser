from .agent import FewShotAgent
from .prompts import DEFAULT_SYSTEM, DEFAULT_EXAMPLES

def user(query, text_to_summarize):
    return f"""
Given this query:
{query}
Give a very brief summary of the relevant information from this result:
{text_to_summarize}
If the result is not relevant, only output "<NOT_RELEVANT>".
""".strip()

class RelevenceSummaryAgent(FewShotAgent):
    def prompt(self, query, text_to_summarize):
        return DEFAULT_SYSTEM, DEFAULT_EXAMPLES, user(query, text_to_summarize)
