# print("✅ Starting marketing agent...")

# from typing import List
# # from agents import create_crew
# from crewai import Agent, Crew, Process, Task
# from crewai.project import CrewBase, agent, crew, task

# # Uncomment the following line to use an example of a custom tool
# # from marketing_posts.tools.custom_tool import MyCustomTool
# from pydantic import BaseModel, Field

# from .tools import get_tools


# class MarketStrategy(BaseModel):
#     """Market strategy model"""

#     name: str = Field(..., description="Name of the market strategy")
#     tactics: List[str] = Field(
#         ..., description="List of tactics to be used in the market strategy"
#     )
#     channels: List[str] = Field(
#         ..., description="List of channels to be used in the market strategy"
#     )
#     KPIs: List[str] = Field(
#         ..., description="List of KPIs to be used in the market strategy"
#     )


# class CampaignIdea(BaseModel):
#     """Campaign idea model"""

#     name: str = Field(..., description="Name of the campaign idea")
#     description: str = Field(..., description="Description of the campaign idea")
#     audience: str = Field(..., description="Audience of the campaign idea")
#     channel: str = Field(..., description="Channel of the campaign idea")


# class CampaignIdeas(BaseModel):
#     title: str = Field(..., description="A title for list of ideas")
#     ideas: List[CampaignIdea] = Field(..., description="List of campaign ideas")


# class Copy(BaseModel):
#     """Copy model"""

#     title: str = Field(..., description="Title of the copy")
#     body: str = Field(..., description="Body of the copy")


# @CrewBase
# class MarketingPostsCrew:
#     """MarketingPosts crew"""

#     agents_config = "config/agents.yaml"
#     tasks_config = "config/tasks.yaml"

#     @agent
#     def lead_market_analyst(self) -> Agent:
#         return Agent(
#             config=self.agents_config["lead_market_analyst"],  # type: ignore
#             tools=get_tools(),
#             verbose=True,
#         )

#     @agent
#     def chief_marketing_strategist(self) -> Agent:
#         return Agent(
#             config=self.agents_config["chief_marketing_strategist"],  # type: ignore
#             tools=get_tools(),
#             verbose=True,
#         )

#     @agent
#     def creative_content_creator(self) -> Agent:
#         return Agent(
#             config=self.agents_config["creative_content_creator"],  # type: ignore
#             verbose=True,
#         )

#     @task
#     def research_task(self) -> Task:
#         return Task(
#             config=self.tasks_config["research_task"],  # type: ignore
#             agent=self.lead_market_analyst(),
#         )

#     @task
#     def project_understanding_task(self) -> Task:
#         return Task(
#             config=self.tasks_config["project_understanding_task"],  # type: ignore
#             agent=self.chief_marketing_strategist(),
#         )

#     @task
#     def marketing_strategy_task(self) -> Task:
#         return Task(
#             config=self.tasks_config["marketing_strategy_task"],  # type: ignore
#             agent=self.chief_marketing_strategist(),
#             output_json=MarketStrategy,
#         )

#     @task
#     def campaign_idea_task(self) -> Task:
#         return Task(
#             config=self.tasks_config["campaign_idea_task"],  # type: ignore
#             agent=self.creative_content_creator(),
#             output_json=CampaignIdeas,
#         )

#     @task
#     def copy_creation_task(self) -> Task:
#         return Task(
#             config=self.tasks_config["copy_creation_task"],  # type: ignore
#             agent=self.creative_content_creator(),
#             context=[self.marketing_strategy_task(), self.campaign_idea_task()],
#             output_json=Copy,
#         )

#     @crew
#     def crew(self) -> Crew:
#         """Creates the MarketingPosts crew"""
#         return Crew(
#             agents=self.agents,  # type: ignore - Automatically created by the @agent decorator
#             tasks=self.tasks,  # type: ignore - Automatically created by the @task decorator
#             process=Process.sequential,
#             verbose=True,
#             # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
#         )




# if __name__ == "__main__":
#     print("✅ Crew is starting...")
#     crew = MarketingPostsCrew().crew()
#     crew.kickoff()



# import logging
# import os
# import sys
# from typing import Any, List
# import yaml

# from crewai import Agent, Crew, Process, Task
# from crewai.project import CrewBase, agent, crew, task
# from pydantic import BaseModel, Field

# from .tools import get_tools # Assuming this is your tools.py

# logging.getLogger("LiteLLM").setLevel(logging.WARNING) # Keep your existing logging config


# # --- Your Pydantic Models (KEEP THEM AS THEY ARE) ---
# class MarketStrategy(BaseModel):
#     """Market strategy model"""
#     name: str = Field(..., description="Name of the market strategy")
#     tactics: List[str] = Field(..., description="List of tactics to be used in the market strategy")
#     channels: List[str] = Field(..., description="List of channels to be used in the market strategy")
#     KPIs: List[str] = Field(..., description="List of KPIs to be used in the market strategy")


# class CampaignIdea(BaseModel):
#     """Campaign idea model"""
#     name: str = Field(..., description="Name of the campaign idea")
#     description: str = Field(..., description="Description of the campaign idea")
#     audience: str = Field(..., description="Audience of the campaign idea")
#     channel: str = Field(..., description="Channel of the campaign idea")


# class CampaignIdeas(BaseModel):
#     title: str = Field(..., description="A title for list of ideas")
#     ideas: List[CampaignIdea] = Field(..., description="List of campaign ideas")


# class Copy(BaseModel):
#     """Copy model"""
#     title: str = Field(..., description="Title of the copy")
#     body: str = Field(..., description="Body of the copy")
# # --- End Pydantic Models ---


# @CrewBase
# class MarketingPostsCrew:
#     """MarketingPosts crew"""

#     agents_config = "config/agents.yaml"
#     tasks_config = "config/tasks.yaml"

#     @agent
#     def lead_market_analyst(self) -> Agent:
#         return Agent(
#             config=self.agents_config["lead_market_analyst"],  # type: ignore
#             tools=get_tools(),
#             verbose=True,
#         )

#     @agent
#     def chief_marketing_strategist(self) -> Agent:
#         return Agent(
#             config=self.agents_config["chief_marketing_strategist"],  # type: ignore
#             tools=get_tools(),
#             verbose=True,
#         )

#     @agent
#     def creative_content_creator(self) -> Agent:
#         return Agent(
#             config=self.agents_config["creative_content_creator"],  # type: ignore
#             verbose=True,
#         )

#     # NEW AGENT: Chief Creative Director for final consolidation
#     @agent
#     def chief_creative_director(self) -> Agent:
#         return Agent(
#             config=self.agents_config["chief_creative_director"], # type: ignore
#             verbose=True,
#         )

#     # --- Tasks (modified to ensure context flow and explicit output_json) ---
#     @task
#     def research_task(self) -> Task:
#         return Task(
#             config=self.tasks_config["research_task"],  # type: ignore
#             agent=self.lead_market_analyst(),
#             output_json=dict, # Explicitly set output_json to dict for structured output
#         )

#     @task
#     def project_understanding_task(self) -> Task:
#         return Task(
#             config=self.tasks_config["project_understanding_task"],  # type: ignore
#             agent=self.chief_marketing_strategist(),
#             output_json=dict, # Explicitly set output_json to dict for structured output
#         )

#     @task
#     def marketing_strategy_task(self) -> Task:
#         return Task(
#             config=self.tasks_config["marketing_strategy_task"],  # type: ignore
#             agent=self.chief_marketing_strategist(),
#             context=[self.research_task(), self.project_understanding_task()], # Pass context explicitly
#             output_json=MarketStrategy,
#         )

#     @task
#     def campaign_idea_task(self) -> Task:
#         return Task(
#             config=self.tasks_config["campaign_idea_task"],  # type: ignore
#             agent=self.creative_content_creator(),
#             context=[self.marketing_strategy_task()], # Pass strategy as context
#             output_json=CampaignIdeas,
#         )

#     @task
#     def copy_creation_task(self) -> Task:
#         return Task(
#             config=self.tasks_config["copy_creation_task"],  # type: ignore
#             agent=self.creative_content_creator(),
#             context=[self.campaign_idea_task(), self.marketing_strategy_task()], # Pass both as context
#             output_json=List[Copy], # Expecting a list of Copy objects
#         )

#     # --- NEW: Final Task to Consolidate Outputs for Streamlit ---
#     @task
#     def consolidate_output_task(self) -> Task:
#         return Task(
#             description=(
#                 "Review the comprehensive marketing strategy, creative campaign ideas, and marketing copies generated by the crew. "
#                 "Consolidate all this information into a single, comprehensive JSON object. "
#                 "Ensure the output JSON includes the following top-level keys: "
#                 "'marketing_strategy' (a dictionary conforming to the MarketStrategy model), "
#                 "'campaign_ideas' (a dictionary conforming to the CampaignIdeas model), and "
#                 "'marketing_copies' (a list of dictionaries, each conforming to the Copy model). "
#                 "Present the gathered research summary and project understanding in a 'research_summary' key as a string."
#                 "Do NOT include any additional thoughts or conversational text in the final JSON output, just the structured data."
#             ),
#             agent=self.chief_creative_director(), # Assign to the Chief Creative Director for final review
#             context=[
#                 self.research_task(),
#                 self.project_understanding_task(),
#                 self.marketing_strategy_task(),
#                 self.campaign_idea_task(),
#                 self.copy_creation_task()
#             ],
#             output_json=dict, # The output will be a single dictionary containing all sub-outputs
#             human_input=False,
#             expected_output=(
#                 "A single JSON object with keys: 'research_summary' (string), "
#                 "'project_understanding' (string), 'marketing_strategy' (MarketStrategy dict), "
#                 "'campaign_ideas' (CampaignIdeas dict), and 'marketing_copies' (List[Copy] of dicts)."
#             )
#         )


#     @crew
#     def crew(self) -> Crew:
#         """Creates the MarketingPosts crew"""
#         return Crew(
#             agents=self.agents,  # type: ignore
#             tasks=[
#                 self.research_task(),
#                 self.project_understanding_task(),
#                 self.marketing_strategy_task(),
#                 self.campaign_idea_task(),
#                 self.copy_creation_task(),
#                 self.consolidate_output_task() # This is now the final task in the sequence
#             ],
#             process=Process.sequential,
#             verbose=True,
#         )


# # IMPORTANT: Comment out or remove this __main__ block
# # It will prevent the crew from running automatically when imported by Streamlit.
# # if __name__ == "__main__":
# #     print("✅ Crew is starting...")
# #     crew = MarketingPostsCrew().crew()
# #     crew.kickoff()



# import logging
# from typing import List
# from pydantic import BaseModel, Field

# from crewai import Agent, Crew, Process, Task
# from crewai.project import CrewBase, agent, crew, task

# from .tools import get_tools

# logging.getLogger("LiteLLM").setLevel(logging.WARNING)

# # ---------------- Pydantic Models ---------------- #

# class MarketStrategy(BaseModel):
#     name: str
#     tactics: List[str]
#     channels: List[str]
#     KPIs: List[str]

# class CampaignIdea(BaseModel):
#     name: str
#     description: str
#     audience: str
#     channel: str

# class CampaignIdeas(BaseModel):
#     title: str
#     ideas: List[CampaignIdea]

# class Copy(BaseModel):
#     title: str
#     body: str

# class CopyList(BaseModel):
#     __root__: List[Copy]

# class ResearchOutput(BaseModel):
#     research_summary: str

# class ProjectUnderstandingOutput(BaseModel):
#     project_description: str

# class ConsolidatedOutput(BaseModel):
#     research_summary: str
#     project_understanding: str
#     marketing_strategy: MarketStrategy
#     campaign_ideas: CampaignIdeas
#     marketing_copies: List[Copy]

# # ---------------- Crew Class ---------------- #

# @CrewBase
# class MarketingPostsCrew:
#     agents_config = "config/agents.yaml"
#     tasks_config = "config/tasks.yaml"

#     @agent
#     def lead_market_analyst(self) -> Agent:
#         return Agent(
#             config=self.agents_config["lead_market_analyst"],  # type: ignore
#             tools=get_tools(),
#             verbose=True,
#         )

#     @agent
#     def chief_marketing_strategist(self) -> Agent:
#         return Agent(
#             config=self.agents_config["chief_marketing_strategist"],  # type: ignore
#             tools=get_tools(),
#             verbose=True,
#         )

#     @agent
#     def creative_content_creator(self) -> Agent:
#         return Agent(
#             config=self.agents_config["creative_content_creator"],  # type: ignore
#             verbose=True,
#         )

#     @agent
#     def chief_creative_director(self) -> Agent:
#         return Agent(
#             config=self.agents_config["chief_creative_director"],  # type: ignore
#             verbose=True,
#         )

#     @task
#     def research_task(self) -> Task:
#         return Task(
#             config=self.tasks_config["research_task"],  # type: ignore
#             agent=self.lead_market_analyst(),
#             output_json=ResearchOutput,
#         )

#     @task
#     def project_understanding_task(self) -> Task:
#         return Task(
#             config=self.tasks_config["project_understanding_task"],  # type: ignore
#             agent=self.chief_marketing_strategist(),
#             output_json=ProjectUnderstandingOutput,
#         )

#     @task
#     def marketing_strategy_task(self) -> Task:
#         return Task(
#             config=self.tasks_config["marketing_strategy_task"],  # type: ignore
#             agent=self.chief_marketing_strategist(),
#             context=[self.research_task(), self.project_understanding_task()],
#             output_json=MarketStrategy,
#         )

#     @task
#     def campaign_idea_task(self) -> Task:
#         return Task(
#             config=self.tasks_config["campaign_idea_task"],  # type: ignore
#             agent=self.creative_content_creator(),
#             context=[self.marketing_strategy_task()],
#             output_json=CampaignIdeas,
#         )

#     @task
#     def copy_creation_task(self) -> Task:
#         return Task(
#             config=self.tasks_config["copy_creation_task"],  # type: ignore
#             agent=self.creative_content_creator(),
#             context=[self.campaign_idea_task(), self.marketing_strategy_task()],
#             output_json=CopyList,
#         )

#     @task
#     def consolidate_output_task(self) -> Task:
#         return Task(
#             description=(
#                 "Review the comprehensive marketing strategy, creative campaign ideas, and marketing copies generated by the crew. "
#                 "Consolidate all this information into a single, comprehensive JSON object. "
#                 "Ensure the output JSON includes the following top-level keys: "
#                 "'marketing_strategy', 'campaign_ideas', 'marketing_copies', "
#                 "'research_summary', and 'project_understanding'."
#             ),
#             agent=self.chief_creative_director(),
#             context=[
#                 self.research_task(),
#                 self.project_understanding_task(),
#                 self.marketing_strategy_task(),
#                 self.campaign_idea_task(),
#                 self.copy_creation_task()
#             ],
#             output_json=ConsolidatedOutput,
#             human_input=False,
#             expected_output=(
#                 "A single JSON object with keys: 'research_summary' (string), "
#                 "'project_understanding' (string), 'marketing_strategy' (MarketStrategy dict), "
#                 "'campaign_ideas' (CampaignIdeas dict), and 'marketing_copies' (List[Copy] of dicts)."
#             )
#         )

#     @crew
#     def crew(self) -> Crew:
#         return Crew(
#             agents=[
#                 self.lead_market_analyst(),
#                 self.chief_marketing_strategist(),
#                 self.creative_content_creator(),
#                 self.chief_creative_director(),
#             ],
#             tasks=[
#                 self.research_task(),
#                 self.project_understanding_task(),
#                 self.marketing_strategy_task(),
#                 self.campaign_idea_task(),
#                 self.copy_creation_task(),
#                 self.consolidate_output_task(),
#             ],
#             process=Process.sequential,
#             verbose=True,
#         )




import logging
from typing import List
from pydantic import BaseModel, Field

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from .tools import get_tools

logging.getLogger("LiteLLM").setLevel(logging.WARNING)

# --------- Pydantic Models --------- #

class MarketStrategy(BaseModel):
    name: str
    tactics: List[str]
    channels: List[str]
    KPIs: List[str]

class CampaignIdea(BaseModel):
    name: str
    description: str
    audience: str
    channel: str

class CampaignIdeas(BaseModel):
    title: str
    ideas: List[CampaignIdea]

class Copy(BaseModel):
    title: str
    body: str

class CopyList(BaseModel):  # ✅ Wrapper for list of Copy
    copies: List[Copy]

class ResearchOutput(BaseModel):
    research_summary: str

class ProjectUnderstandingOutput(BaseModel):
    project_description: str

class ConsolidatedOutput(BaseModel):
    research_summary: str
    project_understanding: str
    marketing_strategy: MarketStrategy
    campaign_ideas: CampaignIdeas
    marketing_copies: List[Copy]  # ✅ Still valid because it's wrapped

# --------- Crew Definition --------- #

@CrewBase
class MarketingPostsCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def lead_market_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["lead_market_analyst"],
            tools=get_tools(),
            verbose=True,
        )

    @agent
    def chief_marketing_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config["chief_marketing_strategist"],
            tools=get_tools(),
            verbose=True,
        )

    @agent
    def creative_content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config["creative_content_creator"],
            verbose=True,
        )

    @agent
    def chief_creative_director(self) -> Agent:
        return Agent(
            config=self.agents_config["chief_creative_director"],
            verbose=True,
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
            agent=self.lead_market_analyst(),
            output_json=ResearchOutput,
        )

    @task
    def project_understanding_task(self) -> Task:
        return Task(
            config=self.tasks_config["project_understanding_task"],
            agent=self.chief_marketing_strategist(),
            output_json=ProjectUnderstandingOutput,
        )

    @task
    def marketing_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config["marketing_strategy_task"],
            agent=self.chief_marketing_strategist(),
            context=[self.research_task(), self.project_understanding_task()],
            output_json=MarketStrategy,
        )

    @task
    def campaign_idea_task(self) -> Task:
        return Task(
            config=self.tasks_config["campaign_idea_task"],
            agent=self.creative_content_creator(),
            context=[self.marketing_strategy_task()],
            output_json=CampaignIdeas,
        )

    @task
    def copy_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config["copy_creation_task"],
            agent=self.creative_content_creator(),
            context=[self.campaign_idea_task(), self.marketing_strategy_task()],
            output_json=CopyList,  # ✅ Fix: must be BaseModel
        )

    @task
    def consolidate_output_task(self) -> Task:
        return Task(
            description=(
                "Review all generated content and consolidate it into a single structured JSON with keys: "
                "'research_summary', 'project_understanding', 'marketing_strategy', "
                "'campaign_ideas', and 'marketing_copies'."
            ),
            agent=self.chief_creative_director(),
            context=[
                self.research_task(),
                self.project_understanding_task(),
                self.marketing_strategy_task(),
                self.campaign_idea_task(),
                self.copy_creation_task(),
            ],
            output_json=ConsolidatedOutput,
            human_input=False,
            expected_output=(
                "A JSON with keys: 'research_summary', 'project_understanding', "
                "'marketing_strategy', 'campaign_ideas', and 'marketing_copies'."
            )
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=[
                self.research_task(),
                self.project_understanding_task(),
                self.marketing_strategy_task(),
                self.campaign_idea_task(),
                self.copy_creation_task(),
                self.consolidate_output_task(),
            ],
            process=Process.sequential,
            verbose=True,
        )
