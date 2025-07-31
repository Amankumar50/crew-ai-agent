# # # # # # # import streamlit as st
# # # # # # # import os
# # # # # # # import json
# # # # # # # from dotenv import load_dotenv

# # # # # # # # Load environment variables from .env file (for SERPER_API_KEY)
# # # # # # # load_dotenv()

# # # # # # # # Import your CrewAI MarketingPostsCrew
# # # # # # # # Adjust this import path if your crew.py is not directly importable from 'app'
# # # # # # # from marketing_posts.crew import MarketingPostsCrew

# # # # # # # # --- Read API Keys ---
# # # # # # # # Serper API Key from environment variable (passed by docker-compose environment)
# # # # # # # serper_api_key = os.getenv('SERPER_API_KEY')

# # # # # # # # OpenAI API Key from Docker Secret
# # # # # # # openai_api_key = None
# # # # # # # openai_secret_path = "/run/secrets/openai-api-key"
# # # # # # # if os.path.exists(openai_secret_path):
# # # # # # #     try:
# # # # # # #         with open(openai_secret_path, "r") as f:
# # # # # # #             openai_api_key = f.read().strip()
# # # # # # #     except Exception as e:
# # # # # # #         st.error(f"Error reading OpenAI secret: {e}")
# # # # # # #         st.stop() # Stop execution if secret cannot be read
# # # # # # # else:
# # # # # # #     st.error(f"OpenAI secret file not found at {openai_secret_path}. Please ensure it's mounted correctly.")
# # # # # # #     st.stop() # Stop execution if secret not found

# # # # # # # # Set environment variables for CrewAI tools/LLMs if they expect them this way
# # # # # # # # CrewAI tools often pick them up automatically if set in os.environ
# # # # # # # os.environ['SERPER_API_KEY'] = serper_api_key if serper_api_key else ''
# # # # # # # os.environ['OPENAI_API_KEY'] = openai_api_key if openai_api_key else ''

# # # # # # # # Basic validation
# # # # # # # if not serper_api_key:
# # # # # # #     st.error("SERPER_API_KEY is not set. Please check your .env file and docker-compose.openai.yaml.")
# # # # # # #     st.stop()
# # # # # # # if not openai_api_key:
# # # # # # #     st.error("OPENAI_API_KEY is not set. Please ensure the 'secret.openai-api-key' file exists and is mounted.")
# # # # # # #     st.stop()

# # # # # # # # --- Streamlit App Layout ---
# # # # # # # st.set_page_config(layout="wide")

# # # # # # # st.title("🚀 AI Marketing Studio")
# # # # # # # st.markdown("---")

# # # # # # # st.header("Define Your Project")

# # # # # # # # Input fields for customer_domain and project_description
# # # # # # # customer_domain = st.text_input(
# # # # # # #     "Customer Domain (e.g., example.com)",
# # # # # # #     placeholder="e.g., crewai.com",
# # # # # # #     key="customer_domain_input"
# # # # # # # )

# # # # # # # project_description = st.text_area(
# # # # # # #     "Project Description (Provide details about the product/service, goals, target audience, etc.)",
# # # # # # #     height=200,
# # # # # # #     placeholder="e.g., CrewAI, a leading provider of multi-agent systems, aims to revolutionize marketing automation for its enterprise clients. This project involves developing an innovative marketing strategy to showcase CrewAI's advanced AI-driven solutions, emphasizing ease of use, scalability, and integration capabilities. The campaign will target tech-savvy decision-makers in medium to large enterprises, highlighting success stories and the transformative potential of CrewAI's platform.",
# # # # # # #     key="project_description_input"
# # # # # # # )

# # # # # # # st.markdown("---")

# # # # # # # if st.button("Generate Marketing Campaign", type="primary"):
# # # # # # #     if not customer_domain or not project_description:
# # # # # # #         st.error("Please provide both a Customer Domain and Project Description to generate the campaign.")
# # # # # # #     else:
# # # # # # #         st.subheader("Generating Campaign...")
# # # # # # #         st.info("The AI Marketing Crew is at work! This might take a few minutes as they perform research and formulate the strategy.")

# # # # # # #         # Prepare inputs for the CrewAI kickoff
# # # # # # #         inputs = {
# # # # # # #             "customer_domain": customer_domain,
# # # # # # #             "project_description": project_description
# # # # # # #         }

# # # # # # #         # Initialize and run the CrewAI
# # # # # # #         try:
# # # # # # #             with st.spinner("CrewAI is thinking..."):
# # # # # # #                 # The kickoff will now return the consolidated JSON from consolidate_output_task
# # # # # # #                 crew_result_json_string = MarketingPostsCrew().crew().kickoff(inputs=inputs)

# # # # # # #             st.success("Campaign Generation Complete!")
# # # # # # #             st.markdown("---")

# # # # # # #             st.header("✨ Generated Marketing Campaign")

# # # # # # #             # Parse the JSON output from the CrewAI result
# # # # # # #             try:
# # # # # # #                 results_dict = json.loads(crew_result_json_string)

# # # # # # #                 # Display Marketing Strategy
# # # # # # #                 st.subheader("📊 Marketing Strategy")
# # # # # # #                 if "marketing_strategy" in results_dict and results_dict["marketing_strategy"]:
# # # # # # #                     strategy = results_dict["marketing_strategy"]
# # # # # # #                     st.markdown(f"**Name:** {strategy.get('name', 'N/A')}")
# # # # # # #                     st.markdown("**Tactics:**")
# # # # # # #                     for tactic in strategy.get('tactics', []):
# # # # # # #                         st.markdown(f"- {tactic}")
# # # # # # #                     st.markdown("**Channels:**")
# # # # # # #                     for channel in strategy.get('channels', []):
# # # # # # #                         st.markdown(f"- {channel}")
# # # # # # #                     st.markdown("**KPIs:**")
# # # # # # #                     for kpi in strategy.get('KPIs', []):
# # # # # # #                         st.markdown(f"- {kpi}")
# # # # # # #                 else:
# # # # # # #                     st.info("No detailed marketing strategy found in the output.")

# # # # # # #                 st.markdown("---")

# # # # # # #                 # Display Campaign Ideas
# # # # # # #                 st.subheader("💡 Creative Campaign Ideas")
# # # # # # #                 if "campaign_ideas" in results_dict and results_dict["campaign_ideas"] and results_dict["campaign_ideas"].get('ideas'):
# # # # # # #                     campaign_ideas = results_dict["campaign_ideas"]["ideas"]
# # # # # # #                     st.markdown(f"**Title:** {results_dict['campaign_ideas'].get('title', 'N/A')}")
# # # # # # #                     for i, idea in enumerate(campaign_ideas):
# # # # # # #                         st.markdown(f"**Campaign {i+1}: {idea.get('name', 'N/A')}**")
# # # # # # #                         st.markdown(f"**Description:** {idea.get('description', 'N/A')}")
# # # # # # #                         st.markdown(f"**Audience:** {idea.get('audience', 'N/A')}")
# # # # # # #                         st.markdown(f"**Channel:** {idea.get('channel', 'N/A')}")
# # # # # # #                         st.markdown("---")
# # # # # # #                 else:
# # # # # # #                     st.info("No creative campaign ideas found in the output.")

# # # # # # #                 st.markdown("---")

# # # # # # #                 # Display Marketing Copies
# # # # # # #                 st.subheader("✍️ Marketing Copies")
# # # # # # #                 if "marketing_copies" in results_dict and results_dict["marketing_copies"]:
# # # # # # #                     marketing_copies = results_dict["marketing_copies"]
# # # # # # #                     for i, copy_item in enumerate(marketing_copies): # Renamed 'copy' to 'copy_item' to avoid conflict with Copy class
# # # # # # #                         st.markdown(f"**Copy {i+1}: {copy_item.get('title', 'N/A')}**")
# # # # # # #                         st.write(copy_item.get('body', 'N/A'))
# # # # # # #                         st.markdown("---")
# # # # # # #                 else:
# # # # # # #                     st.info("No marketing copies found in the output.")

# # # # # # #             except json.JSONDecodeError:
# # # # # # #                 st.error("Failed to parse JSON output from CrewAI. Raw output below:")
# # # # # # #                 st.code(crew_result_json_string)
# # # # # # #             except Exception as e:
# # # # # # #                 st.error(f"An error occurred while processing CrewAI output: {e}")
# # # # # # #                 st.exception(e)

# # # # # # #         except Exception as e:
# # # # # # #             st.error(f"An error occurred during CrewAI execution: {e}")
# # # # # # #             st.exception(e) # Show full traceback for debugging

# # # # # # # st.markdown("---")
# # # # # # # st.caption("Powered by CrewAI and Streamlit")


# # # # # # import streamlit as st
# # # # # # import os
# # # # # # import json
# # # # # # from dotenv import load_dotenv

# # # # # # # Load environment variables from .env file (for SERPER_API_KEY)
# # # # # # load_dotenv()

# # # # # # # Import your CrewAI MarketingPostsCrew
# # # # # # # The import path changes because streamlit_app.py is now inside marketing_posts
# # # # # # from marketing_posts.crew import MarketingPostsCrew # This remains valid if crew.py is sibling

# # # # # # # --- Read API Keys ---
# # # # # # # Serper API Key from environment variable (passed by docker-compose environment)
# # # # # # serper_api_key = os.getenv('SERPER_API_KEY')

# # # # # # # OpenAI API Key from Docker Secret
# # # # # # openai_api_key = None
# # # # # # # The path to the secret changes if the base WORKDIR changes, but /run/secrets is standard
# # # # # # openai_secret_path = "/run/secrets/openai-api-key"
# # # # # # if os.path.exists(openai_secret_path):
# # # # # #     try:
# # # # # #         with open(openai_secret_path, "r") as f:
# # # # # #             openai_api_key = f.read().strip()
# # # # # #     except Exception as e:
# # # # # #         st.error(f"Error reading OpenAI secret: {e}")
# # # # # #         st.stop() # Stop execution if secret cannot be read
# # # # # # else:
# # # # # #     st.error(f"OpenAI secret file not found at {openai_secret_path}. Please ensure it's mounted correctly.")
# # # # # #     st.stop() # Stop execution if secret not found

# # # # # # # Set environment variables for CrewAI tools/LLMs if they expect them this way
# # # # # # # CrewAI tools often pick them up automatically if set in os.environ
# # # # # # os.environ['SERPER_API_KEY'] = serper_api_key if serper_api_key else ''
# # # # # # os.environ['OPENAI_API_KEY'] = openai_api_key if openai_api_key else ''

# # # # # # # Basic validation
# # # # # # if not serper_api_key:
# # # # # #     st.error("SERPER_API_KEY is not set. Please check your .env file and docker-compose.openai.yaml.")
# # # # # #     st.stop()
# # # # # # if not openai_api_key:
# # # # # #     st.error("OPENAI_API_KEY is not set. Please ensure the 'secret.openai-api-key' file exists and is mounted.")
# # # # # #     st.stop()

# # # # # # # --- Streamlit App Layout ---
# # # # # # st.set_page_config(layout="wide")

# # # # # # st.title("🚀 AI Marketing Studio")
# # # # # # st.markdown("---")

# # # # # # st.header("Define Your Project")

# # # # # # # Input fields for customer_domain and project_description
# # # # # # customer_domain = st.text_input(
# # # # # #     "Customer Domain (e.g., example.com)",
# # # # # #     placeholder="e.g., crewai.com",
# # # # # #     key="customer_domain_input"
# # # # # # )

# # # # # # project_description = st.text_area(
# # # # # #     "Project Description (Provide details about the product/service, goals, target audience, etc.)",
# # # # # #     height=200,
# # # # # #     placeholder="e.g., CrewAI, a leading provider of multi-agent systems, aims to revolutionize marketing automation for its enterprise clients. This project involves developing an innovative marketing strategy to showcase CrewAI's advanced AI-driven solutions, emphasizing ease of use, scalability, and integration capabilities. The campaign will target tech-savvy decision-makers in medium to large enterprises, highlighting success stories and the transformative potential of CrewAI's platform.",
# # # # # #     key="project_description_input"
# # # # # # )

# # # # # # st.markdown("---")

# # # # # # if st.button("Generate Marketing Campaign", type="primary"):
# # # # # #     if not customer_domain or not project_description:
# # # # # #         st.error("Please provide both a Customer Domain and Project Description to generate the campaign.")
# # # # # #     else:
# # # # # #         st.subheader("Generating Campaign...")
# # # # # #         st.info("The AI Marketing Crew is at work! This might take a few minutes as they perform research and formulate the strategy.")

# # # # # #         # Prepare inputs for the CrewAI kickoff
# # # # # #         inputs = {
# # # # # #             "customer_domain": customer_domain,
# # # # # #             "project_description": project_description
# # # # # #         }

# # # # # #         # Initialize and run the CrewAI
# # # # # #         try:
# # # # # #             with st.spinner("CrewAI is thinking..."):
# # # # # #                 # The kickoff will now return the consolidated JSON from consolidate_output_task
# # # # # #                 crew_result_json_string = MarketingPostsCrew().crew().kickoff(inputs=inputs)

# # # # # #             st.success("Campaign Generation Complete!")
# # # # # #             st.markdown("---")

# # # # # #             st.header("✨ Generated Marketing Campaign")

# # # # # #             # Parse the JSON output from the CrewAI result
# # # # # #             try:
# # # # # #                 results_dict = json.loads(crew_result_json_string)

# # # # # #                 # Display Marketing Strategy
# # # # # #                 st.subheader("📊 Marketing Strategy")
# # # # # #                 if "marketing_strategy" in results_dict and results_dict["marketing_strategy"]:
# # # # # #                     strategy = results_dict["marketing_strategy"]
# # # # # #                     st.markdown(f"**Name:** {strategy.get('name', 'N/A')}")
# # # # # #                     st.markdown("**Tactics:**")
# # # # # #                     for tactic in strategy.get('tactics', []):
# # # # # #                         st.markdown(f"- {tactic}")
# # # # # #                     st.markdown("**Channels:**")
# # # # # #                     for channel in strategy.get('channels', []):
# # # # # #                         st.markdown(f"- {channel}")
# # # # # #                     st.markdown("**KPIs:**")
# # # # # #                     for kpi in strategy.get('KPIs', []):
# # # # # #                         st.markdown(f"- {kpi}")
# # # # # #                 else:
# # # # # #                     st.info("No detailed marketing strategy found in the output.")

# # # # # #                 st.markdown("---")

# # # # # #                 # Display Campaign Ideas
# # # # # #                 st.subheader("💡 Creative Campaign Ideas")
# # # # # #                 if "campaign_ideas" in results_dict and results_dict["campaign_ideas"] and results_dict["campaign_ideas"].get('ideas'):
# # # # # #                     campaign_ideas = results_dict["campaign_ideas"]["ideas"]
# # # # # #                     st.markdown(f"**Title:** {results_dict['campaign_ideas'].get('title', 'N/A')}")
# # # # # #                     for i, idea in enumerate(campaign_ideas):
# # # # # #                         st.markdown(f"**Campaign {i+1}: {idea.get('name', 'N/A')}**")
# # # # # #                         st.markdown(f"**Description:** {idea.get('description', 'N/A')}")
# # # # # #                         st.markdown(f"**Audience:** {idea.get('audience', 'N/A')}")
# # # # # #                         st.markdown(f"**Channel:** {idea.get('channel', 'N/A')}")
# # # # # #                         st.markdown("---")
# # # # # #                 else:
# # # # # #                     st.info("No creative campaign ideas found in the output.")

# # # # # #                 st.markdown("---")

# # # # # #                 # Display Marketing Copies
# # # # # #                 st.subheader("✍️ Marketing Copies")
# # # # # #                 if "marketing_copies" in results_dict and results_dict["marketing_copies"]:
# # # # # #                     marketing_copies = results_dict["marketing_copies"]
# # # # # #                     for i, copy_item in enumerate(marketing_copies):
# # # # # #                         st.markdown(f"**Copy {i+1}: {copy_item.get('title', 'N/A')}**")
# # # # # #                         st.write(copy_item.get('body', 'N/A'))
# # # # # #                         st.markdown("---")
# # # # # #                 else:
# # # # # #                     st.info("No marketing copies found in the output.")

# # # # # #             except json.JSONDecodeError:
# # # # # #                 st.error("Failed to parse JSON output from CrewAI. Raw output below:")
# # # # # #                 st.code(crew_result_json_string)
# # # # # #             except Exception as e:
# # # # # #                 st.error(f"An error occurred while processing CrewAI output: {e}")
# # # # # #                 st.exception(e)

# # # # # #         except Exception as e:
# # # # # #             st.error(f"An error occurred during CrewAI execution: {e}")
# # # # # #             st.exception(e) # Show full traceback for debugging

# # # # # # st.markdown("---")
# # # # # # st.caption("Powered by CrewAI and Streamlit")


# # # # # import streamlit as st
# # # # # import os
# # # # # from dotenv import load_dotenv

# # # # # # Load environment variables from .env for local dev
# # # # # load_dotenv()

# # # # # from marketing_posts.crew import MarketingPostsCrew

# # # # # # --- Read API Keys ---
# # # # # serper_api_key = os.getenv('SERPER_API_KEY')
# # # # # openai_secret_path = "/run/secrets/openai-api-key"
# # # # # openai_api_key = None

# # # # # if os.path.exists(openai_secret_path):
# # # # #     try:
# # # # #         with open(openai_secret_path, "r") as f:
# # # # #             openai_api_key = f.read().strip()
# # # # #     except Exception as e:
# # # # #         st.error(f"Error reading OpenAI secret: {e}")
# # # # #         st.stop()
# # # # # else:
# # # # #     st.error(f"OpenAI secret file not found at {openai_secret_path}. Please ensure it's mounted correctly.")
# # # # #     st.stop()

# # # # # # Set environment variables for CrewAI
# # # # # os.environ["SERPER_API_KEY"] = serper_api_key or ""
# # # # # os.environ["OPENAI_API_KEY"] = openai_api_key or ""

# # # # # # Validate presence of keys
# # # # # if not serper_api_key:
# # # # #     st.error("SERPER_API_KEY is missing. Check .env or Docker config.")
# # # # #     st.stop()
# # # # # if not openai_api_key:
# # # # #     st.error("OPENAI_API_KEY is missing. Ensure the Docker secret is correctly mounted.")
# # # # #     st.stop()

# # # # # # --- Streamlit UI ---
# # # # # st.set_page_config(layout="wide")
# # # # # st.title("🚀 AI Marketing Studio")
# # # # # st.markdown("---")
# # # # # st.header("Define Your Project")

# # # # # customer_domain = st.text_input("Customer Domain", placeholder="e.g., crewai.com")
# # # # # project_description = st.text_area("Project Description", height=200)

# # # # # st.markdown("---")

# # # # # if st.button("Generate Marketing Campaign", type="primary"):
# # # # #     if not customer_domain or not project_description:
# # # # #         st.error("Please provide both Customer Domain and Project Description.")
# # # # #     else:
# # # # #         st.subheader("Generating Campaign...")
# # # # #         st.info("The AI Marketing Crew is at work...")

# # # # #         inputs = {
# # # # #             "customer_domain": customer_domain,
# # # # #             "project_description": project_description
# # # # #         }

# # # # #         try:
# # # # #             with st.spinner("CrewAI is generating your campaign..."):
# # # # #                 result = MarketingPostsCrew().crew().kickoff(inputs=inputs)

# # # # #             # ✅ result is already a dict-like object
# # # # #             results_dict = result.model_dump()

# # # # #             st.success("✅ Campaign Generated!")
# # # # #             st.markdown("---")
# # # # #             st.header("✨ Generated Marketing Campaign")

# # # # #             # Research Summary
# # # # #             st.subheader("📚 Research Summary")
# # # # #             st.markdown(results_dict.get("research_summary", "Not available."))

# # # # #             # Project Understanding
# # # # #             st.subheader("🧠 Project Understanding")
# # # # #             st.markdown(results_dict.get("project_understanding", "Not available."))

# # # # #             st.markdown("---")

# # # # #             # Marketing Strategy
# # # # #             st.subheader("📊 Marketing Strategy")
# # # # #             strategy = results_dict.get("marketing_strategy")
# # # # #             if strategy:
# # # # #                 st.markdown(f"**Name:** {strategy.get('name', 'N/A')}")
# # # # #                 st.markdown("**Tactics:**")
# # # # #                 for t in strategy.get("tactics", []):
# # # # #                     st.markdown(f"- {t}")
# # # # #                 st.markdown("**Channels:**")
# # # # #                 for c in strategy.get("channels", []):
# # # # #                     st.markdown(f"- {c}")
# # # # #                 st.markdown("**KPIs:**")
# # # # #                 for k in strategy.get("KPIs", []):
# # # # #                     st.markdown(f"- {k}")
# # # # #             else:
# # # # #                 st.info("Marketing strategy not found.")

# # # # #             st.markdown("---")

# # # # #             # Campaign Ideas
# # # # #             st.subheader("💡 Creative Campaign Ideas")
# # # # #             ideas_obj = results_dict.get("campaign_ideas", {})
# # # # #             ideas_list = ideas_obj.get("ideas", [])
# # # # #             st.markdown(f"**Title:** {ideas_obj.get('title', 'N/A')}")
# # # # #             if ideas_list:
# # # # #                 for i, idea in enumerate(ideas_list):
# # # # #                     st.markdown(f"**Campaign {i+1}: {idea.get('name', 'N/A')}**")
# # # # #                     st.markdown(f"**Description:** {idea.get('description', 'N/A')}")
# # # # #                     st.markdown(f"**Audience:** {idea.get('audience', 'N/A')}")
# # # # #                     st.markdown(f"**Channel:** {idea.get('channel', 'N/A')}")
# # # # #                     st.markdown("---")
# # # # #             else:
# # # # #                 st.info("No campaign ideas found.")

# # # # #             # Marketing Copies
# # # # #             st.subheader("✍️ Marketing Copies")
# # # # #             copies = results_dict.get("marketing_copies", [])
# # # # #             if copies:
# # # # #                 for i, copy_item in enumerate(copies):
# # # # #                     st.markdown(f"**Copy {i+1}: {copy_item.get('title', 'N/A')}**")
# # # # #                     st.write(copy_item.get("body", "N/A"))
# # # # #                     st.markdown("---")
# # # # #             else:
# # # # #                 st.info("No marketing copies found.")

# # # # #         except Exception as e:
# # # # #             st.error(f"An error occurred during CrewAI execution: {e}")
# # # # #             st.exception(e)

# # # # # st.markdown("---")
# # # # # st.caption("Powered by CrewAI and Streamlit")



# # # # import streamlit as st
# # # # import os
# # # # import json
# # # # from dotenv import load_dotenv

# # # # # Load .env for local SERPER key (during dev)
# # # # load_dotenv()

# # # # from marketing_posts.crew import MarketingPostsCrew

# # # # # --- Read API Keys ---
# # # # serper_api_key = os.getenv('SERPER_API_KEY')

# # # # # Read OpenAI API key from Docker Secret (or fallback)
# # # # openai_secret_path = "/run/secrets/openai-api-key"
# # # # openai_api_key = None
# # # # if os.path.exists(openai_secret_path):
# # # #     try:
# # # #         with open(openai_secret_path, "r") as f:
# # # #             openai_api_key = f.read().strip()
# # # #     except Exception as e:
# # # #         st.error(f"Error reading OpenAI secret: {e}")
# # # #         st.stop()
# # # # else:
# # # #     st.error(f"OpenAI secret file not found at {openai_secret_path}. Please ensure it's mounted correctly.")
# # # #     st.stop()

# # # # # Set environment variables
# # # # os.environ["SERPER_API_KEY"] = serper_api_key or ""
# # # # os.environ["OPENAI_API_KEY"] = openai_api_key or ""

# # # # if not serper_api_key:
# # # #     st.error("SERPER_API_KEY is missing. Check .env or docker config.")
# # # #     st.stop()
# # # # if not openai_api_key:
# # # #     st.error("OPENAI_API_KEY is missing. Ensure the Docker secret is correctly mounted.")
# # # #     st.stop()

# # # # # --- Streamlit UI ---
# # # # st.set_page_config(layout="wide")
# # # # st.title("🚀 AI Marketing Studio")
# # # # st.markdown("---")
# # # # st.header("Define Your Project")

# # # # customer_domain = st.text_input(
# # # #     "Customer Domain (e.g., example.com)",
# # # #     placeholder="e.g., crewai.com",
# # # #     key="customer_domain_input"
# # # # )

# # # # project_description = st.text_area(
# # # #     "Project Description",
# # # #     height=200,
# # # #     placeholder="Describe the product, goals, audience, etc.",
# # # #     key="project_description_input"
# # # # )

# # # # st.markdown("---")

# # # # if st.button("Generate Marketing Campaign", type="primary"):
# # # #     if not customer_domain or not project_description:
# # # #         st.error("Please provide both Customer Domain and Project Description.")
# # # #     else:
# # # #         st.subheader("Generating Campaign...")
# # # #         st.info("The AI Marketing Crew is at work...")

# # # #         inputs = {
# # # #             "customer_domain": customer_domain,
# # # #             "project_description": project_description
# # # #         }

# # # #         try:
# # # #             with st.spinner("CrewAI is generating your campaign..."):
# # # #                 crew_output = MarketingPostsCrew().crew().kickoff(inputs=inputs)

# # # #             # ✅ Extract dict from CrewOutput object
# # # #             results_dict = crew_output.result

# # # #             st.success("✅ Campaign Generated!")
# # # #             st.markdown("---")

# # # #             st.header("✨ Generated Marketing Campaign")

# # # #             # Display Research Summary
# # # #             st.subheader("📚 Research Summary")
# # # #             st.markdown(results_dict.get("research_summary", "Not available."))

# # # #             # Display Project Understanding
# # # #             st.subheader("🧠 Project Understanding")
# # # #             st.markdown(results_dict.get("project_understanding", "Not available."))

# # # #             st.markdown("---")

# # # #             # Display Marketing Strategy
# # # #             st.subheader("📊 Marketing Strategy")
# # # #             strategy = results_dict.get("marketing_strategy")
# # # #             if strategy:
# # # #                 st.markdown(f"**Name:** {strategy.get('name', 'N/A')}")
# # # #                 st.markdown("**Tactics:**")
# # # #                 for t in strategy.get("tactics", []):
# # # #                     st.markdown(f"- {t}")
# # # #                 st.markdown("**Channels:**")
# # # #                 for c in strategy.get("channels", []):
# # # #                     st.markdown(f"- {c}")
# # # #                 st.markdown("**KPIs:**")
# # # #                 for k in strategy.get("KPIs", []):
# # # #                     st.markdown(f"- {k}")
# # # #             else:
# # # #                 st.info("Marketing strategy not found.")

# # # #             st.markdown("---")

# # # #             # Display Campaign Ideas
# # # #             st.subheader("💡 Creative Campaign Ideas")
# # # #             ideas_obj = results_dict.get("campaign_ideas", {})
# # # #             ideas_list = ideas_obj.get("ideas", [])
# # # #             st.markdown(f"**Title:** {ideas_obj.get('title', 'N/A')}")
# # # #             if ideas_list:
# # # #                 for i, idea in enumerate(ideas_list):
# # # #                     st.markdown(f"**Campaign {i+1}: {idea.get('name', 'N/A')}**")
# # # #                     st.markdown(f"**Description:** {idea.get('description', 'N/A')}")
# # # #                     st.markdown(f"**Audience:** {idea.get('audience', 'N/A')}")
# # # #                     st.markdown(f"**Channel:** {idea.get('channel', 'N/A')}")
# # # #                     st.markdown("---")
# # # #             else:
# # # #                 st.info("No campaign ideas found.")

# # # #             # Display Marketing Copies
# # # #             st.subheader("✍️ Marketing Copies")
# # # #             copies = results_dict.get("marketing_copies", [])
# # # #             if copies:
# # # #                 for i, copy_item in enumerate(copies):
# # # #                     st.markdown(f"**Copy {i+1}: {copy_item.get('title', 'N/A')}**")
# # # #                     st.write(copy_item.get("body", "N/A"))
# # # #                     st.markdown("---")
# # # #             else:
# # # #                 st.info("No marketing copies found.")

# # # #         except Exception as e:
# # # #             st.error(f"An error occurred during CrewAI execution: {e}")
# # # #             st.exception(e)

# # # # st.markdown("---")
# # # # st.caption("Powered by CrewAI and Streamlit")



# # # import streamlit as st
# # # import os
# # # from dotenv import load_dotenv
# # # import json

# # # # Load environment variables from .env (for local SERPER key during development)
# # # load_dotenv()

# # # from marketing_posts.crew import MarketingPostsCrew

# # # # --- Read API Keys ---
# # # serper_api_key = os.getenv('SERPER_API_KEY')

# # # # Read OpenAI API key from Docker Secret (or fallback for local dev)
# # # openai_secret_path = "/run/secrets/openai-api-key"
# # # openai_api_key = None
# # # if os.path.exists(openai_secret_path):
# # #     try:
# # #         with open(openai_secret_path, "r") as f:
# # #             openai_api_key = f.read().strip()
# # #     except Exception as e:
# # #         st.error(f"Error reading OpenAI secret: {e}")
# # #         st.stop()
# # # else:
# # #     st.error(f"OpenAI secret file not found at {openai_secret_path}. Please ensure it's mounted correctly.")
# # #     st.stop()

# # # # Set required environment variables
# # # os.environ["SERPER_API_KEY"] = serper_api_key or ""
# # # os.environ["OPENAI_API_KEY"] = openai_api_key or ""

# # # if not serper_api_key:
# # #     st.error("SERPER_API_KEY is missing. Check .env or docker config.")
# # #     st.stop()
# # # if not openai_api_key:
# # #     st.error("OPENAI_API_KEY is missing. Ensure the Docker secret is correctly mounted.")
# # #     st.stop()

# # # # --- Streamlit UI ---
# # # st.set_page_config(layout="wide")
# # # st.title("🚀 AI Marketing Studio")
# # # st.markdown("---")
# # # st.header("Define Your Project")

# # # customer_domain = st.text_input(
# # #     "Customer Domain (e.g., example.com)",
# # #     placeholder="e.g., crewai.com",
# # #     key="customer_domain_input"
# # # )

# # # project_description = st.text_area(
# # #     "Project Description",
# # #     height=200,
# # #     placeholder="Describe the product, goals, audience, etc.",
# # #     key="project_description_input"
# # # )

# # # st.markdown("---")

# # # if st.button("Generate Marketing Campaign", type="primary"):
# # #     if not customer_domain or not project_description:
# # #         st.error("Please provide both Customer Domain and Project Description.")
# # #     else:
# # #         st.subheader("Generating Campaign...")
# # #         st.info("The AI Marketing Crew is at work...")

# # #         inputs = {
# # #             "customer_domain": customer_domain,
# # #             "project_description": project_description
# # #         }


# # #         try:
# # #             with st.spinner("CrewAI is generating your campaign..."):
# # #                 crew_output = MarketingPostsCrew().crew().kickoff(inputs=inputs)

# # #                 # 🔍 Debug output
# # #                 st.write("📦 Output type:", type(crew_output))
# # #                 st.write("📚 Attributes:", dir(crew_output))

# # #                 # ✅ Correct way to get the final structured result
# # #                 results_dict = crew_output.final_task.output

# # #             st.success("✅ Campaign Generated!")
# # #             st.markdown("---")
# # #             st.header("✨ Generated Marketing Campaign")

# # #             # Display Research Summary
# # #             st.subheader("📚 Research Summary")
# # #             st.markdown(results_dict.get("research_summary", "Not available."))

# # #             # Display Project Understanding
# # #             st.subheader("🧠 Project Understanding")
# # #             st.markdown(results_dict.get("project_understanding", "Not available."))

# # #             # ... (rest of your result rendering code remains unchanged)


# # #         # try:
# # #         #     with st.spinner("CrewAI is generating your campaign..."):
# # #         #         crew_output = MarketingPostsCrew().crew().kickoff(inputs=inputs)
# # #         #         results_dict = crew_output.result  # ✅ Correct way to access final result

# # #         #     st.success("✅ Campaign Generated!")
# # #         #     st.markdown("---")
# # #         #     st.header("✨ Generated Marketing Campaign")

# # #         #     # Research Summary
# # #         #     st.subheader("📚 Research Summary")
# # #         #     st.markdown(results_dict.get("research_summary", "Not available."))

# # #         #     # Project Understanding
# # #         #     st.subheader("🧠 Project Understanding")
# # #         #     st.markdown(results_dict.get("project_understanding", "Not available."))

# # #         #     st.markdown("---")

# # #             # Marketing Strategy
# # #             st.subheader("📊 Marketing Strategy")
# # #             strategy = results_dict.get("marketing_strategy")
# # #             if strategy:
# # #                 st.markdown(f"**Name:** {strategy.get('name', 'N/A')}")
# # #                 st.markdown("**Tactics:**")
# # #                 for t in strategy.get("tactics", []):
# # #                     st.markdown(f"- {t}")
# # #                 st.markdown("**Channels:**")
# # #                 for c in strategy.get("channels", []):
# # #                     st.markdown(f"- {c}")
# # #                 st.markdown("**KPIs:**")
# # #                 for k in strategy.get("KPIs", []):
# # #                     st.markdown(f"- {k}")
# # #             else:
# # #                 st.info("Marketing strategy not found.")

# # #             st.markdown("---")

# # #             # Campaign Ideas
# # #             st.subheader("💡 Creative Campaign Ideas")
# # #             ideas_obj = results_dict.get("campaign_ideas", {})
# # #             ideas_list = ideas_obj.get("ideas", [])
# # #             st.markdown(f"**Title:** {ideas_obj.get('title', 'N/A')}")
# # #             if ideas_list:
# # #                 for i, idea in enumerate(ideas_list):
# # #                     st.markdown(f"**Campaign {i+1}: {idea.get('name', 'N/A')}**")
# # #                     st.markdown(f"**Description:** {idea.get('description', 'N/A')}")
# # #                     st.markdown(f"**Audience:** {idea.get('audience', 'N/A')}")
# # #                     st.markdown(f"**Channel:** {idea.get('channel', 'N/A')}")
# # #                     st.markdown("---")
# # #             else:
# # #                 st.info("No campaign ideas found.")

# # #             # Marketing Copies
# # #             st.subheader("✍️ Marketing Copies")
# # #             copies = results_dict.get("marketing_copies", [])
# # #             if copies:
# # #                 for i, copy_item in enumerate(copies):
# # #                     st.markdown(f"**Copy {i+1}: {copy_item.get('title', 'N/A')}**")
# # #                     st.write(copy_item.get("body", "N/A"))
# # #                     st.markdown("---")
# # #             else:
# # #                 st.info("No marketing copies found.")

# # #         except Exception as e:
# # #             st.error(f"An error occurred during CrewAI execution: {e}")
# # #             st.exception(e)

# # # st.markdown("---")
# # # st.caption("Powered by CrewAI and Streamlit")



# # import streamlit as st
# # import os
# # import json
# # from dotenv import load_dotenv

# # # Load .env for local SERPER key (optional in dev)
# # load_dotenv()

# # from marketing_posts.crew import MarketingPostsCrew

# # # Read environment keys
# # serper_api_key = os.getenv("SERPER_API_KEY")

# # # Read OpenAI key from Docker Secret
# # openai_api_key = None
# # secret_path = "/run/secrets/openai-api-key"
# # if os.path.exists(secret_path):
# #     try:
# #         with open(secret_path, "r") as f:
# #             openai_api_key = f.read().strip()
# #     except Exception as e:
# #         st.error(f"Error reading OpenAI secret: {e}")
# #         st.stop()
# # else:
# #     st.error(f"OpenAI secret file not found at {secret_path}.")
# #     st.stop()

# # # Set environment variables
# # os.environ["SERPER_API_KEY"] = serper_api_key or ""
# # os.environ["OPENAI_API_KEY"] = openai_api_key or ""

# # if not serper_api_key:
# #     st.error("SERPER_API_KEY is missing.")
# #     st.stop()
# # if not openai_api_key:
# #     st.error("OPENAI_API_KEY is missing.")
# #     st.stop()

# # # UI
# # st.set_page_config(layout="wide")
# # st.title("🚀 AI Marketing Studio")
# # st.markdown("---")
# # st.header("Define Your Project")

# # customer_domain = st.text_input(
# #     "Customer Domain (e.g., example.com)",
# #     placeholder="e.g., crewai.com",
# #     key="customer_domain_input"
# # )

# # project_description = st.text_area(
# #     "Project Description",
# #     height=200,
# #     placeholder="Describe the product, goals, audience, etc.",
# #     key="project_description_input"
# # )

# # st.markdown("---")

# # if st.button("Generate Marketing Campaign", type="primary"):
# #     if not customer_domain or not project_description:
# #         st.error("Please provide both Customer Domain and Project Description.")
# #     else:
# #         st.subheader("Generating Campaign...")
# #         st.info("The AI Marketing Crew is at work...")

# #         inputs = {
# #             "customer_domain": customer_domain,
# #             "project_description": project_description
# #         }

# #         try:
# #             with st.spinner("CrewAI is generating your campaign..."):
# #                 crew_output = MarketingPostsCrew().crew().kickoff(inputs=inputs)

# #                 # Debug info
# #                 st.write("📦 Output type:", type(crew_output))
# #                 st.write("📚 Available Attributes:", dir(crew_output))

# #                 # ✅ Safely extract final result as dictionary
# #                 results_dict = crew_output.json_dict or {}

# #             st.success("✅ Campaign Generated!")
# #             st.markdown("---")
# #             st.header("✨ Generated Marketing Campaign")

# #             st.subheader("📚 Research Summary")
# #             st.markdown(results_dict.get("research_summary", "Not available."))

# #             st.subheader("🧠 Project Understanding")
# #             st.markdown(results_dict.get("project_understanding", "Not available."))

# #             st.markdown("---")
# #             st.subheader("📊 Marketing Strategy")
# #             strategy = results_dict.get("marketing_strategy")
# #             if strategy:
# #                 st.markdown(f"**Name:** {strategy.get('name', 'N/A')}")
# #                 st.markdown("**Tactics:**")
# #                 for t in strategy.get("tactics", []):
# #                     st.markdown(f"- {t}")
# #                 st.markdown("**Channels:**")
# #                 for c in strategy.get("channels", []):
# #                     st.markdown(f"- {c}")
# #                 st.markdown("**KPIs:**")
# #                 for k in strategy.get("KPIs", []):
# #                     st.markdown(f"- {k}")
# #             else:
# #                 st.info("Marketing strategy not found.")

# #             st.markdown("---")
# #             st.subheader("💡 Creative Campaign Ideas")
# #             ideas_obj = results_dict.get("campaign_ideas", {})
# #             ideas_list = ideas_obj.get("ideas", [])
# #             st.markdown(f"**Title:** {ideas_obj.get('title', 'N/A')}")
# #             if ideas_list:
# #                 for i, idea in enumerate(ideas_list):
# #                     st.markdown(f"**Campaign {i+1}: {idea.get('name', 'N/A')}**")
# #                     st.markdown(f"**Description:** {idea.get('description', 'N/A')}")
# #                     st.markdown(f"**Audience:** {idea.get('audience', 'N/A')}")
# #                     st.markdown(f"**Channel:** {idea.get('channel', 'N/A')}")
# #                     st.markdown("---")
# #             else:
# #                 st.info("No campaign ideas found.")

# #             st.subheader("✍️ Marketing Copies")
# #             copies = results_dict.get("marketing_copies", [])
# #             if copies:
# #                 for i, copy_item in enumerate(copies):
# #                     st.markdown(f"**Copy {i+1}: {copy_item.get('title', 'N/A')}**")
# #                     st.write(copy_item.get("body", "N/A"))
# #                     st.markdown("---")
# #             else:
# #                 st.info("No marketing copies found.")

# #         except Exception as e:
# #             st.error(f"❌ An error occurred: {e}")
# #             st.exception(e)

# # st.markdown("---")
# # st.caption("Powered by CrewAI and Streamlit")



# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# from marketing_posts.crew import MarketingPostsCrew

# # Load environment variables
# load_dotenv()

# # Read API keys
# serper_api_key = os.getenv("SERPER_API_KEY")

# openai_secret_path = "/run/secrets/openai-api-key"
# openai_api_key = None
# if os.path.exists(openai_secret_path):
#     try:
#         with open(openai_secret_path, "r") as f:
#             openai_api_key = f.read().strip()
#     except Exception as e:
#         st.error(f"Error reading OpenAI secret: {e}")
#         st.stop()
# else:
#     st.error(f"OpenAI secret not found at {openai_secret_path}.")
#     st.stop()

# os.environ["SERPER_API_KEY"] = serper_api_key or ""
# os.environ["OPENAI_API_KEY"] = openai_api_key or ""

# if not serper_api_key:
#     st.error("SERPER_API_KEY is missing.")
#     st.stop()
# if not openai_api_key:
#     st.error("OPENAI_API_KEY is missing.")
#     st.stop()

# # Streamlit UI
# st.set_page_config(layout="wide")
# st.title("🚀 AI Marketing Studio")
# st.markdown("---")
# st.header("Define Your Project")

# customer_domain = st.text_input(
#     "Customer Domain (e.g., example.com)",
#     placeholder="e.g., crewai.com"
# )

# project_description = st.text_area(
#     "Project Description",
#     height=200,
#     placeholder="Describe the product, goals, audience, etc."
# )

# st.markdown("---")

# if st.button("Generate Marketing Campaign", type="primary"):
#     if not customer_domain or not project_description:
#         st.error("Please provide both Customer Domain and Project Description.")
#     else:
#         st.subheader("Generating Campaign...")
#         st.info("The AI Marketing Crew is at work...")

#         inputs = {
#             "customer_domain": customer_domain,
#             "project_description": project_description
#         }

#         try:
#             with st.spinner("CrewAI is generating your campaign..."):
#                 crew_output = MarketingPostsCrew().crew().kickoff(inputs=inputs)
#                 results_dict = crew_output.json_dict or {}

#             st.success("✅ Campaign Generated!")
#             st.markdown("---")
#             st.header("✨ Generated Marketing Campaign")

#             st.subheader("📚 Research Summary")
#             st.markdown(results_dict.get("research_summary", "Not available."))

#             st.subheader("🧠 Project Understanding")
#             st.markdown(results_dict.get("project_understanding", "Not available."))

#             st.markdown("---")
#             st.subheader("📊 Marketing Strategy")
#             strategy = results_dict.get("marketing_strategy")
#             if strategy:
#                 st.markdown(f"**Name:** {strategy.get('name', 'N/A')}")
#                 st.markdown("**Tactics:**")
#                 for t in strategy.get("tactics", []):
#                     st.markdown(f"- {t}")
#                 st.markdown("**Channels:**")
#                 for c in strategy.get("channels", []):
#                     st.markdown(f"- {c}")
#                 st.markdown("**KPIs:**")
#                 for kpi in strategy.get("KPIs", []):
#                     st.markdown(f"- {kpi}")
#             else:
#                 st.info("Marketing strategy not found.")

#             st.markdown("---")
#             st.subheader("💡 Creative Campaign Ideas")
#             ideas_obj = results_dict.get("campaign_ideas", {})
#             ideas_list = ideas_obj.get("ideas", [])
#             st.markdown(f"**Title:** {ideas_obj.get('title', 'N/A')}")
#             if ideas_list:
#                 for i, idea in enumerate(ideas_list):
#                     st.markdown(f"**Campaign {i+1}: {idea.get('name', 'N/A')}**")
#                     st.markdown(f"**Description:** {idea.get('description', 'N/A')}")
#                     st.markdown(f"**Audience:** {idea.get('audience', 'N/A')}")
#                     st.markdown(f"**Channel:** {idea.get('channel', 'N/A')}")
#                     st.markdown("---")
#             else:
#                 st.info("No campaign ideas found.")

#             st.subheader("✍️ Marketing Copies")
#             copies = results_dict.get("marketing_copies", [])
#             if copies:
#                 for i, copy_item in enumerate(copies):
#                     st.markdown(f"**Copy {i+1}: {copy_item.get('title', 'N/A')}**")
#                     st.write(copy_item.get("body", "N/A"))
#                     st.markdown("---")
#             else:
#                 st.info("No marketing copies found.")

#         except Exception as e:
#             st.error(f"❌ An error occurred: {e}")
#             st.exception(e)

# st.markdown("---")
# st.caption("Powered by CrewAI and Streamlit")


# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# from marketing_posts.crew import MarketingPostsCrew
# import streamlit.components.v1 as components

# # Load .env for local development
# load_dotenv()

# # --- Read API Keys ---
# serper_api_key = os.getenv('SERPER_API_KEY')
# openai_secret_path = "/run/secrets/openai-api-key"
# openai_api_key = None
# if os.path.exists(openai_secret_path):
#     try:
#         with open(openai_secret_path, "r") as f:
#             openai_api_key = f.read().strip()
#     except Exception as e:
#         st.error(f"Error reading OpenAI secret: {e}")
#         st.stop()
# else:
#     st.error(f"OpenAI secret file not found at {openai_secret_path}. Please ensure it's mounted correctly.")
#     st.stop()

# # Set env vars for CrewAI agents/tools
# os.environ["SERPER_API_KEY"] = serper_api_key or ""
# os.environ["OPENAI_API_KEY"] = openai_api_key or ""

# if not serper_api_key or not openai_api_key:
#     st.error("Required API keys are missing.")
#     st.stop()

# # --- Streamlit Layout ---
# st.set_page_config(layout="wide")
# st.title("🚀 AI Marketing Studio")
# st.markdown("---")
# st.header("Define Your Project")

# customer_domain = st.text_input("Customer Domain", placeholder="e.g., ai-startup.com")
# project_description = st.text_area("Project Description", height=200, placeholder="Describe your product, goals, and target audience.")

# st.markdown("---")

# # Embed Workflow Diagram
# st.subheader("🗺️ Campaign Generation Workflow")

# svg_output = """
# <svg width="100%" height="380">
#   <style>
#     .step { font: 14px sans-serif; }
#     .box { fill: #f0f0f0; stroke: #aaa; stroke-width: 1; rx: 5; ry: 5; }
#     .line { stroke: #555; stroke-width: 1.5; marker-end: url(#arrow); }
#   </style>
#   <defs>
#     <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
#       <path d="M0,0 L0,6 L9,3 z" fill="#555" />
#     </marker>
#   </defs>

#   <rect x="20" y="20" width="270" height="40" class="box"/>
#   <text x="30" y="45" class="step">📝 User Input (Domain + Description)</text>

#   <rect x="20" y="80" width="270" height="40" class="box"/>
#   <text x="30" y="105" class="step">🔍 lead_market_analyst (Serper)</text>

#   <rect x="300" y="80" width="270" height="40" class="box"/>
#   <text x="310" y="105" class="step">🧠 chief_marketing_strategist (OpenAI)</text>

#   <rect x="160" y="150" width="270" height="40" class="box"/>
#   <text x="175" y="175" class="step">📊 Marketing Strategy</text>

#   <rect x="160" y="220" width="270" height="40" class="box"/>
#   <text x="175" y="245" class="step">💡 Campaign Ideas</text>

#   <rect x="160" y="290" width="270" height="40" class="box"/>
#   <text x="175" y="315" class="step">✍️ Marketing Copies</text>

#   <rect x="460" y="290" width="270" height="40" class="box"/>
#   <text x="470" y="315" class="step">🎯 Final JSON Output</text>

#   <line x1="140" y1="60" x2="140" y2="80" class="line"/>
#   <line x1="280" y1="110" x2="300" y2="110" class="line"/>
#   <line x1="240" y1="120" x2="240" y2="150" class="line"/>
#   <line x1="280" y1="190" x2="280" y2="220" class="line"/>
#   <line x1="280" y1="260" x2="280" y2="290" class="line"/>
#   <line x1="400" y1="310" x2="460" y2="310" class="line"/>
# </svg>
# """

# components.html(svg_output, height=400)

# st.markdown("---")

# if st.button("Generate Marketing Campaign", type="primary"):
#     if not customer_domain or not project_description:
#         st.error("Please provide both Customer Domain and Project Description.")
#     else:
#         st.subheader("Generating Campaign...")
#         st.info("The AI Marketing Crew is at work...")

#         inputs = {
#             "customer_domain": customer_domain,
#             "project_description": project_description
#         }

#         try:
#             with st.spinner("CrewAI is thinking..."):
#                 crew_output = MarketingPostsCrew().crew().kickoff(inputs=inputs)
#                 results_dict = crew_output.json_dict  # ✅ Accessing structured output

#             st.success("✅ Campaign Generated!")
#             st.markdown("---")

#             st.header("✨ Generated Marketing Campaign")

#             # Research Summary
#             st.subheader("📚 Research Summary")
#             st.markdown(results_dict.get("research_summary", "Not available."))

#             # Project Understanding
#             st.subheader("🧠 Project Understanding")
#             st.markdown(results_dict.get("project_understanding", "Not available."))

#             st.markdown("---")

#             # Marketing Strategy
#             st.subheader("📊 Marketing Strategy")
#             strategy = results_dict.get("marketing_strategy")
#             if strategy:
#                 st.markdown(f"**Name:** {strategy.get('name', 'N/A')}")
#                 st.markdown("**Tactics:**")
#                 for t in strategy.get("tactics", []):
#                     st.markdown(f"- {t}")
#                 st.markdown("**Channels:**")
#                 for c in strategy.get("channels", []):
#                     st.markdown(f"- {c}")
#                 st.markdown("**KPIs:**")
#                 for k in strategy.get("KPIs", []):
#                     st.markdown(f"- {k}")
#             else:
#                 st.info("Marketing strategy not found.")

#             st.markdown("---")

#             # Campaign Ideas
#             st.subheader("💡 Creative Campaign Ideas")
#             ideas_obj = results_dict.get("campaign_ideas", {})
#             ideas_list = ideas_obj.get("ideas", [])
#             st.markdown(f"**Title:** {ideas_obj.get('title', 'N/A')}")
#             if ideas_list:
#                 for i, idea in enumerate(ideas_list):
#                     st.markdown(f"**Campaign {i+1}: {idea.get('name', 'N/A')}**")
#                     st.markdown(f"**Description:** {idea.get('description', 'N/A')}")
#                     st.markdown(f"**Audience:** {idea.get('audience', 'N/A')}")
#                     st.markdown(f"**Channel:** {idea.get('channel', 'N/A')}")
#                     st.markdown("---")
#             else:
#                 st.info("No campaign ideas found.")

#             # Marketing Copies
#             st.subheader("✍️ Marketing Copies")
#             copies = results_dict.get("marketing_copies", [])
#             if copies:
#                 for i, copy_item in enumerate(copies):
#                     st.markdown(f"**Copy {i+1}: {copy_item.get('title', 'N/A')}**")
#                     st.write(copy_item.get("body", "N/A"))
#                     st.markdown("---")
#             else:
#                 st.info("No marketing copies found.")

#         except Exception as e:
#             st.error(f"❌ An error occurred: {e}")
#             st.exception(e)

# st.markdown("---")
# st.caption("📡 Powered by CrewAI, OpenAI, Serper & Streamlit")


# Gemni code 

# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# from marketing_posts.crew import MarketingPostsCrew
# import streamlit.components.v1 as components

# # Load environment variables from .env
# load_dotenv()

# # --- API Keys ---
# serper_api_key = os.getenv("SERPER_API_KEY")
# openai_secret_path = "/run/secrets/openai-api-key"
# openai_api_key = None
# if os.path.exists(openai_secret_path):
#     try:
#         with open(openai_secret_path, "r") as f:
#             openai_api_key = f.read().strip()
#     except Exception as e:
#         st.error(f"Error reading OpenAI secret: {e}")
#         st.stop()
# else:
#     st.error("OpenAI secret file not found.")
#     st.stop()

# # Set API keys for environment
# os.environ["SERPER_API_KEY"] = serper_api_key or ""
# os.environ["OPENAI_API_KEY"] = openai_api_key or ""

# if not serper_api_key or not openai_api_key:
#     st.error("Missing API keys. Check .env and secrets.")
#     st.stop()

# # --- Streamlit UI ---
# st.set_page_config(layout="wide")
# st.title("🚀 AI Marketing Studio")
# st.markdown("---")
# st.header("Define Your Project")

# customer_domain = st.text_input("Customer Domain", placeholder="e.g., startup.com")
# project_description = st.text_area("Project Description", height=200, placeholder="Describe your product, goals, and audience.")

# st.markdown("---")

# if st.button("Generate Marketing Campaign", type="primary"):
#     if not customer_domain or not project_description:
#         st.error("Please provide both inputs.")
#     else:
#         st.subheader("Generating Campaign...")
#         st.info("The AI Marketing Crew is at work...")

#         inputs = {"customer_domain": customer_domain, "project_description": project_description}

#         try:
#             with st.spinner("Running CrewAI..."):
#                 crew_output_obj = MarketingPostsCrew().crew().kickoff(inputs=inputs) # Renamed to avoid confusion

#                 # Access the final consolidated JSON from the crew_output_obj
#                 # Assuming the last task (consolidate_output_task) outputs a dict
#                 results_dict = crew_output_obj.json_dict # Access the dict from CrewOutput

#                 # --- CORRECTED ACCESS TO TASK OUTPUTS ---
#                 # Iterate through the raw outputs of each task to get their string representation
#                 task_outputs = {}
#                 full_task_outputs = {}
#                 if hasattr(crew_output_obj, 'tasks_output') and isinstance(crew_output_obj.tasks_output, list):
#                     for i, task_result in enumerate(crew_output_obj.tasks_output):
#                         # Task results in tasks_output are already the direct output from the task
#                         # If output_json was a BaseModel, task_result is a BaseModel instance
#                         # If output_json was dict, task_result is a dict
#                         # If no output_json, task_result is a string

#                         # Convert to string and handle potential large outputs
#                         task_content = ""
#                         if isinstance(task_result, (dict, list)):
#                             task_content = json.dumps(task_result, indent=2)
#                         elif hasattr(task_result, 'model_dump_json'): # Pydantic v2
#                             task_content = task_result.model_dump_json(indent=2)
#                         elif hasattr(task_result, 'json'): # Pydantic v1
#                             task_content = task_result.json(indent=2)
#                         else: # Fallback for raw string output or other types
#                             task_content = str(task_result)

#                         # Store for display
#                         task_outputs[f"Step {i+1}"] = task_content[:300] + "..." if len(task_content) > 300 else task_content
#                         full_task_outputs[f"Step {i+1}"] = task_content
#                 else:
#                     st.warning("Could not retrieve individual task outputs from CrewAI's result object.")
#                     # Fallback to display the final output if individual task outputs are not available
#                     # This means the SVG tooltips might not work perfectly without task_outputs

#             # SVG with tooltips
#             st.subheader("🗺️ Agent Flow with Outputs (Hover Tooltips)")
#             # ... (your existing SVG code here, ensure it uses task_outputs) ...
#             svg = f"""
#             <svg width="100%" height="450">
#               <style>
#                 .step {{ font: 14px sans-serif; }}
#                 .box {{ fill: #f0f0f0; stroke: #aaa; stroke-width: 1; rx: 5; ry: 5; }}
#                 .line {{ stroke: #555; stroke-width: 1.5; marker-end: url(#arrow); }}
#               </style>
#               <defs>
#                 <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
#                   <path d="M0,0 L0,6 L9,3 z" fill="#555" />
#                 </marker>
#               </defs>

#               <rect x="20" y="20" width="270" height="40" class="box"/>
#               <title>{task_outputs.get("Step 1", "No output")}</title>
#               <text x="30" y="45" class="step">🔍 Lead Market Analyst</text>

#               <rect x="320" y="20" width="270" height="40" class="box"/>
#               <title>{task_outputs.get("Step 2", "No output")}</title>
#               <text x="330" y="45" class="step">🧠 Chief Marketing Strategist</text>

#               <rect x="170" y="90" width="270" height="40" class="box"/>
#               <title>{task_outputs.get("Step 3", "No output")}</title>
#               <text x="180" y="115" class="step">📊 Marketing Strategy</text>

#               <rect x="170" y="160" width="270" height="40" class="box"/>
#               <title>{task_outputs.get("Step 4", "No output")}</title>
#               <text x="180" y="185" class="step">💡 Campaign Idea</text>

#               <rect x="170" y="230" width="270" height="40" class="box"/>
#               <title>{task_outputs.get("Step 5", "No output")}</title>
#               <text x="180" y="255" class="step">✍️ Copy Creation</text>

#               <rect x="470" y="230" width="270" height="40" class="box"/>
#               <title>{task_outputs.get("Step 6", "No output")}</title>
#               <text x="480" y="255" class="step">🎯 Consolidate Output</text>

#               <line x1="290" y1="40" x2="320" y2="40" class="line"/>
#               <line x1="155" y1="60" x2="155" y2="90" class="line"/>
#               <line x1="455" y1="60" x2="455" y2="90" class="line"/>
#               <line x1="305" y1="130" x2="305" y2="160" class="line"/>
#               <line x1="305" y1="200" x2="305" y2="230" class="line"/>
#               <line x1="440" y1="250" x2="470" y2="250" class="line"/>
#             </svg>
#             """
#             components.html(svg, height=470)

#             st.markdown("### 📋 View Full Step Outputs")
#             for step, content in full_task_outputs.items():
#                 with st.expander(f"{step} Output"):
#                     st.code(content)

#             # -- Final Campaign Output --
#             st.markdown("---")
#             st.header("✨ Generated Marketing Campaign")

#             # Display Research Summary and Project Understanding
#             st.subheader("📚 Research Summary")
#             st.markdown(results_dict.get("research_summary", "Not available."))

#             st.subheader("🧠 Project Understanding")
#             st.markdown(results_dict.get("project_understanding", "Not available."))

#             st.markdown("---")
#             st.subheader("📊 Marketing Strategy")
#             strategy = results_dict.get("marketing_strategy")
#             if strategy:
#                 st.markdown(f"**Name:** {strategy.get('name', 'N/A')}")
#                 st.markdown("**Tactics:**")
#                 for t in strategy.get("tactics", []):
#                     st.markdown(f"- {t}")
#                 st.markdown("**Channels:**")
#                 for c in strategy.get("channels", []):
#                     st.markdown(f"- {c}")
#                 st.markdown("**KPIs:**")
#                 for k in strategy.get("KPIs", []):
#                     st.markdown(f"- {k}")
#             else:
#                 st.info("Strategy not found.")

#             st.markdown("---")
#             st.subheader("💡 Creative Campaign Ideas")
#             ideas_obj = results_dict.get("campaign_ideas", {})
#             ideas_list = ideas_obj.get("ideas", [])
#             st.markdown(f"**Title:** {ideas_obj.get('title', 'N/A')}")
#             for i, idea in enumerate(ideas_list):
#                 st.markdown(f"**Campaign {i+1}: {idea.get('name', '')}**")
#                 st.markdown(f"**Description:** {idea.get('description', '')}")
#                 st.markdown(f"**Audience:** {idea.get('audience', '')}")
#                 st.markdown(f"**Channel:** {idea.get('channel', '')}")
#                 st.markdown("---")

#             st.subheader("✍️ Marketing Copies")
#             copies = results_dict.get("marketing_copies", [])
#             for i, copy_item in enumerate(copies):
#                 st.markdown(f"**Copy {i+1}: {copy_item.get('title', '')}**")
#                 st.write(copy_item.get("body", ""))
#                 st.markdown("---")

#         except Exception as e:
#             st.error("❌ Error running CrewAI:")
#             st.exception(e)

# st.markdown("---")
# st.caption("🔗 Powered by CrewAI, OpenAI, Serper & Streamlit")
# docker compose -f compose.openai.yaml up --build



# Gemni -2
# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# from marketing_posts.crew import MarketingPostsCrew
# import streamlit.components.v1 as components

# # Load environment variables from .env
# load_dotenv()

# # --- API Keys ---
# serper_api_key = os.getenv("SERPER_API_KEY")
# openai_secret_path = "/run/secrets/openai-api-key"
# openai_api_key = None
# if os.path.exists(openai_secret_path):
#     try:
#         with open(openai_secret_path, "r") as f:
#             openai_api_key = f.read().strip()
#     except Exception as e:
#         st.error(f"Error reading OpenAI secret: {e}")
#         st.stop()
# else:
#     st.error("OpenAI secret file not found.")
#     st.stop()

# # Set API keys for environment
# os.environ["SERPER_API_KEY"] = serper_api_key or ""
# os.environ["OPENAI_API_KEY"] = openai_api_key or ""

# if not serper_api_key or not openai_api_key:
#     st.error("Missing API keys. Check .env and secrets.")
#     st.stop()

# # --- Streamlit UI ---
# st.set_page_config(layout="wide")
# st.title("🚀 AI Marketing Studio")
# st.markdown("---")
# st.header("Define Your Project")

# customer_domain = st.text_input("Customer Domain", placeholder="e.g., startup.com")
# project_description = st.text_area("Project Description", height=200, placeholder="Describe your product, goals, and audience.")

# st.markdown("---")

# if st.button("Generate Marketing Campaign", type="primary"):
#     if not customer_domain or not project_description:
#         st.error("Please provide both inputs.")
#     else:
#         st.subheader("Generating Campaign...")
#         st.info("The AI Marketing Crew is at work! This might take a few minutes as they perform research and formulate the strategy.")

#         inputs = {"customer_domain": customer_domain, "project_description": project_description}

#         try:
#             with st.spinner("Running CrewAI..."):
#                 # crew_output_obj will contain the result of the LAST task (consolidate_output_task)
#                 # and also the outputs of all previous tasks in its .tasks_output attribute
#                 crew_final_output = MarketingPostsCrew().crew().kickoff(inputs=inputs)

#                 # Access the final consolidated JSON from the crew_final_output
#                 # The .json_dict attribute is for the *final* task's parsed JSON output
#                 results_dict = crew_final_output.json_dict if hasattr(crew_final_output, 'json_dict') else json.loads(str(crew_final_output))


#                 # --- CORRECTED ACCESS TO INDIVIDUAL TASK OUTPUTS ---
#                 task_outputs = {} # For SVG tooltips (shortened)
#                 full_task_outputs = {} # For expanders (full content)

#                 # Check if crew_final_output has the tasks_output attribute (newer CrewAI versions)
#                 if hasattr(crew_final_output, 'tasks_output') and isinstance(crew_final_output.tasks_output, list):
#                     # Define the human-readable names for each step based on the order in crew.py
#                     # Make sure this order matches the `tasks` list in your `crew.py`'s `crew()` method
#                     task_names_ordered = [
#                         "Lead Market Analyst (Research)",
#                         "Chief Marketing Strategist (Project Understanding)",
#                         "Chief Marketing Strategist (Marketing Strategy)",
#                         "Creative Content Creator (Campaign Idea)",
#                         "Creative Content Creator (Copy Creation)",
#                         "Chief Creative Director (Consolidate Output)"
#                     ]

#                     for i, task_result_item in enumerate(crew_final_output.tasks_output):
#                         step_name = f"Step {i+1}: {task_names_ordered[i]}" if i < len(task_names_ordered) else f"Step {i+1}"

#                         # Convert task_result_item to string/JSON for display
#                         task_content = ""
#                         if isinstance(task_result_item, (dict, list)):
#                             task_content = json.dumps(task_result_item, indent=2)
#                         elif hasattr(task_result_item, 'model_dump_json'): # Pydantic v2 BaseModels
#                             task_content = task_result_item.model_dump_json(indent=2)
#                         elif hasattr(task_result_item, 'json'): # Pydantic v1 BaseModels
#                             task_content = task_result_item.json(indent=2)
#                         else: # Fallback for raw string output or other types
#                             task_content = str(task_result_item)

#                         # Store for display in SVG (shortened) and expander (full)
#                         task_outputs[f"Step {i+1}"] = task_content[:300] + "..." if len(task_content) > 300 else task_content
#                         full_task_outputs[f"Step {i+1}"] = task_content
#                 else:
#                     st.warning("Could not retrieve individual task outputs. Showing final output only.")
#                     # Fallback if tasks_output is not available
#                     task_outputs = {"Step 1": str(crew_final_output)[:300] + "..."} # Just put final output as step 1
#                     full_task_outputs = {"Step 1": str(crew_final_output)}


#             # SVG with tooltips
#             st.subheader("🗺️ Agent Flow with Outputs (Hover Tooltips)")
#             svg = f"""
#             <svg width="100%" height="450">
#               <style>
#                 .step {{ font: 14px sans-serif; }}
#                 .box {{ fill: #f0f0f0; stroke: #aaa; stroke-width: 1; rx: 5; ry: 5; }}
#                 .line {{ stroke: #555; stroke-width: 1.5; marker-end: url(#arrow); }}
#               </style>
#               <defs>
#                 <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
#                   <path d="M0,0 L0,6 L9,3 z" fill="#555" />
#                 </marker>
#               </defs>

#               <rect x="20" y="20" width="270" height="40" class="box"/>
#               <title>{task_outputs.get("Step 1", "No output available")}</title>
#               <text x="30" y="45" class="step">🔍 Lead Market Analyst (Research)</text>

#               <rect x="320" y="20" width="270" height="40" class="box"/>
#               <title>{task_outputs.get("Step 2", "No output available")}</title>
#               <text x="330" y="45" class="step">🧠 Chief Marketing Strategist (Understanding)</text>

#               <rect x="170" y="90" width="270" height="40" class="box"/>
#               <title>{task_outputs.get("Step 3", "No output available")}</title>
#               <text x="180" y="115" class="step">📊 Chief Marketing Strategist (Strategy)</text>

#               <rect x="170" y="160" width="270" height="40" class="box"/>
#               <title>{task_outputs.get("Step 4", "No output available")}</title>
#               <text x="180" y="185" class="step">💡 Creative Content Creator (Campaign)</text>

#               <rect x="170" y="230" width="270" height="40" class="box"/>
#               <title>{task_outputs.get("Step 5", "No output available")}</title>
#               <text x="180" y="255" class="step">✍️ Creative Content Creator (Copy)</text>

#               <rect x="470" y="230" width="270" height="40" class="box"/>
#               <title>{task_outputs.get("Step 6", "No output available")}</title>
#               <text x="480" y="255" class="step">🎯 Chief Creative Director (Consolidate)</text>

#               <line x1="290" y1="40" x2="320" y2="40" class="line"/>
#               <line x1="155" y1="60" x2="155" y2="90" class="line"/>
#               <line x1="455" y1="60" x2="455" y2="90" class="line"/>
#               <line x1="305" y1="130" x2="305" y2="160" class="line"/>
#               <line x1="305" y1="200" x2="305" y2="230" class="line"/>
#               <line x1="440" y1="250" x2="470" y2="250" class="line"/>
#             </svg>
#             """
#             components.html(svg, height=470)

#             st.markdown("### 📋 View Full Step Outputs")
#             for step, content in full_task_outputs.items():
#                 with st.expander(f"{step} Output"):
#                     st.code(content)

#             # -- Final Campaign Output --
#             st.markdown("---")
#             st.header("✨ Generated Marketing Campaign")

#             # Display Research Summary and Project Understanding
#             st.subheader("📚 Research Summary")
#             st.markdown(results_dict.get("research_summary", "Not available."))

#             st.subheader("🧠 Project Understanding")
#             st.markdown(results_dict.get("project_understanding", "Not available."))

#             st.markdown("---")
#             st.subheader("📊 Marketing Strategy")
#             strategy = results_dict.get("marketing_strategy")
#             if strategy:
#                 st.markdown(f"**Name:** {strategy.get('name', 'N/A')}")
#                 st.markdown("**Tactics:**")
#                 for t in strategy.get("tactics", []):
#                     st.markdown(f"- {t}")
#                 st.markdown("**Channels:**")
#                 for c in strategy.get("channels", []):
#                     st.markdown(f"- {c}")
#                 st.markdown("**KPIs:**")
#                 for k in strategy.get("KPIs", []):
#                     st.markdown(f"- {k}")
#             else:
#                 st.info("Strategy not found.")

#             st.markdown("---")
#             st.subheader("💡 Creative Campaign Ideas")
#             ideas_obj = results_dict.get("campaign_ideas", {})
#             ideas_list = ideas_obj.get("ideas", [])
#             st.markdown(f"**Title:** {ideas_obj.get('title', 'N/A')}")
#             for i, idea in enumerate(ideas_list):
#                 st.markdown(f"**Campaign {i+1}: {idea.get('name', '')}**")
#                 st.markdown(f"**Description:** {idea.get('description', '')}")
#                 st.markdown(f"**Audience:** {idea.get('audience', '')}")
#                 st.markdown(f"**Channel:** {idea.get('channel', '')}")
#                 st.markdown("---")

#             st.subheader("✍️ Marketing Copies")
#             copies = results_dict.get("marketing_copies", [])
#             for i, copy_item in enumerate(copies):
#                 st.markdown(f"**Copy {i+1}: {copy_item.get('title', '')}**")
#                 st.write(copy_item.get("body", ""))
#                 st.markdown("---")

#         except Exception as e:
#             st.error("❌ Error running CrewAI:")
#             st.exception(e)

# st.markdown("---")
# st.caption("🔗 Powered by CrewAI, OpenAI, Serper & Streamlit")


# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# from marketing_posts.crew import MarketingPostsCrew
# import streamlit.components.v1 as components

# # Load environment variables from .env
# load_dotenv()

# # --- API Keys ---
# serper_api_key = os.getenv("SERPER_API_KEY")
# openai_secret_path = "/run/secrets/openai-api-key"
# openai_api_key = None
# if os.path.exists(openai_secret_path):
#     try:
#         with open(openai_secret_path, "r") as f:
#             openai_api_key = f.read().strip()
#     except Exception as e:
#         st.error(f"Error reading OpenAI secret: {e}")
#         st.stop()
# else:
#     st.error("OpenAI secret file not found.")
#     st.stop()

# # Set API keys for environment
# os.environ["SERPER_API_KEY"] = serper_api_key or ""
# os.environ["OPENAI_API_KEY"] = openai_api_key or ""

# if not serper_api_key or not openai_api_key:
#     st.error("Missing API keys. Check .env and secrets.")
#     st.stop()

# # --- Static Descriptions for SVG Tooltips ---
# # These descriptions are fixed and describe the purpose of each step/agent
# static_step_descriptions = {
#     "Step 1": "Performs domain-specific market research based on the customer domain and industry trends.",
#     "Step 2": "Interprets the project goal and research to design a strategic marketing plan.",
#     "Step 3": "Uses context from earlier steps to create a tactical marketing strategy.",
#     "Step 4": "Generates creative campaign ideas using the strategy from step 3.",
#     "Step 5": "Uses ideas + strategy to write multiple marketing copies.",
#     "Step 6": "Reviews and consolidates all outputs (research_summary, project_understanding, marketing_strategy, campaign_ideas, marketing_copies) into one clean JSON result for UI consumption."
# }

# # --- Streamlit UI ---
# st.set_page_config(layout="wide")
# st.title("🚀 AI Marketing Studio")
# st.markdown("---")
# st.header("Define Your Project")

# customer_domain = st.text_input("Customer Domain", placeholder="e.g., startup.com")
# project_description = st.text_area("Project Description", height=200, placeholder="Describe your product, goals, and audience.")

# st.markdown("---")

# if st.button("Generate Marketing Campaign", type="primary"):
#     if not customer_domain or not project_description:
#         st.error("Please provide both inputs.")
#     else:
#         st.subheader("Generating Campaign...")
#         st.info("The AI Marketing Crew is at work! This might take a few minutes as they perform research and formulate the strategy.")

#         inputs = {"customer_domain": customer_domain, "project_description": project_description}

#         try:
#             with st.spinner("Running CrewAI..."):
#                 # crew_final_output will contain the result of the LAST task (consolidate_output_task)
#                 # and also the outputs of all previous tasks in its .tasks_output attribute
#                 crew_final_output = MarketingPostsCrew().crew().kickoff(inputs=inputs)

#                 # Access the final consolidated JSON from the crew_final_output
#                 results_dict = crew_final_output.json_dict if hasattr(crew_final_output, 'json_dict') else json.loads(str(crew_final_output))

#                 # --- Extracting Individual Task Outputs for Expanders ---
#                 # This logic populates `full_task_outputs` with the actual content
#                 full_task_outputs = {}
#                 if hasattr(crew_final_output, 'tasks_output') and isinstance(crew_final_output.tasks_output, list):
#                     # Define the human-readable names for each step based on the order in crew.py
#                     # Make sure this order matches the `tasks` list in your `crew.py`'s `crew()` method
#                     task_names_ordered = [
#                         "Lead Market Analyst (Research)",
#                         "Chief Marketing Strategist (Project Understanding)",
#                         "Chief Marketing Strategist (Marketing Strategy)",
#                         "Creative Content Creator (Campaign Idea)",
#                         "Creative Content Creator (Copy Creation)",
#                         "Chief Creative Director (Consolidate Output)"
#                     ]

#                     for i, task_result_item in enumerate(crew_final_output.tasks_output):
#                         step_name_key = f"Step {i+1}" # Key for both static and dynamic outputs
#                         full_step_title = f"{step_name_key}: {task_names_ordered[i]}" if i < len(task_names_ordered) else f"{step_name_key}"

#                         # Convert task_result_item to string/JSON for display
#                         task_content = ""
#                         if isinstance(task_result_item, (dict, list)):
#                             task_content = json.dumps(task_result_item, indent=2)
#                         elif hasattr(task_result_item, 'model_dump_json'): # Pydantic v2 BaseModels
#                             task_content = task_result_item.model_dump_json(indent=2)
#                         elif hasattr(task_result_item, 'json'): # Pydantic v1 BaseModels
#                             task_content = task_result_item.json(indent=2)
#                         else: # Fallback for raw string output or other types
#                             task_content = str(task_result_item)

#                         full_task_outputs[full_step_title] = task_content
#                 else:
#                     st.warning("Could not retrieve individual task outputs. Showing final output only in expander.")
#                     full_task_outputs["Final Consolidated Output"] = str(crew_final_output) # Fallback

#             # --- SVG Diagram Generation ---
#             st.subheader("🗺️ Agent Flow with Outputs (Hover Tooltips)")
#             svg = f"""
#             <svg width="100%" height="450">
#               <style>
#                 .step {{ font: 14px sans-serif; }}
#                 .box {{ fill: #f0f0f0; stroke: #aaa; stroke-width: 1; rx: 5; ry: 5; }}
#                 .line {{ stroke: #555; stroke-width: 1.5; marker-end: url(#arrow); }}
#               </style>
#               <defs>
#                 <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
#                   <path d="M0,0 L0,6 L9,3 z" fill="#555" />
#                 </marker>
#               </defs>

#               <rect x="20" y="20" width="270" height="40" class="box"/>
#               <title>{static_step_descriptions.get("Step 1", "Description not available.")}</title>
#               <text x="30" y="45" class="step">🔍 Lead Market Analyst (Research)</text>

#               <rect x="320" y="20" width="300" height="40" class="box"/>
#               <title>{static_step_descriptions.get("Step 2", "Description not available.")}</title>
#               <text x="330" y="45" class="step">🧠 Chief Marketing Strategist (Understanding)</text>

#               <rect x="170" y="90" width="270" height="40" class="box"/>
#               <title>{static_step_descriptions.get("Step 3", "Description not available.")}</title>
#               <text x="180" y="115" class="step">📊 Chief Marketing Strategist (Strategy)</text>

#               <rect x="170" y="160" width="270" height="40" class="box"/>
#               <title>{static_step_descriptions.get("Step 4", "Description not available.")}</title>
#               <text x="180" y="185" class="step">💡 Creative Content Creator (Campaign)</text>

#               <rect x="170" y="230" width="270" height="40" class="box"/>
#               <title>{static_step_descriptions.get("Step 5", "Description not available.")}</title>
#               <text x="180" y="255" class="step">✍️ Creative Content Creator (Copy)</text>

#               <rect x="470" y="230" width="270" height="40" class="box"/>
#               <title>{static_step_descriptions.get("Step 6", "Description not available.")}</title>
#               <text x="480" y="255" class="step">🎯 Chief Creative Director (Consolidate)</text>

#               <line x1="290" y1="40" x2="320" y2="40" class="line"/>
#               <line x1="455" y1="60" x2="305" y2="90" class="line"/>
#               <line x1="155" y1="60" x2="155" y2="90" class="line"/>

#               <line x1="305" y1="130" x2="305" y2="160" class="line"/>
#               <line x1="305" y1="200" x2="305" y2="230" class="line"/>

#               <line x1="155" y1="60" x2="470" y2="250" class="line"/>
#               <line x1="455" y1="60" x2="470" y2="250" class="line"/>
#               <line x1="305" y1="130" x2="470" y2="250" class="line"/>
#               <line x1="305" y1="200" x2="470" y2="250" class="line"/>
#               <line x1="305" y1="250" x2="470" y2="250" class="line"/>

#             </svg>
#             """
#             components.html(svg, height=470)

#             st.markdown("### 📋 View Full Step Outputs")
#             # Loop through full_task_outputs which has full content
#             for step_title, content in full_task_outputs.items():
#                 with st.expander(f"{step_title} Output"):
#                     st.code(content)

#             # -- Final Campaign Output --
#             st.markdown("---")
#             st.header("✨ Generated Marketing Campaign")

#             # Display Research Summary and Project Understanding
#             st.subheader("📚 Research Summary")
#             st.markdown(results_dict.get("research_summary", "Not available."))

#             st.subheader("🧠 Project Understanding")
#             st.markdown(results_dict.get("project_understanding", "Not available."))

#             st.markdown("---")
#             st.subheader("📊 Marketing Strategy")
#             strategy = results_dict.get("marketing_strategy")
#             if strategy:
#                 st.markdown(f"**Name:** {strategy.get('name', 'N/A')}")
#                 st.markdown("**Tactics:**")
#                 for t in strategy.get("tactics", []):
#                     st.markdown(f"- {t}")
#                 st.markdown("**Channels:**")
#                 for c in strategy.get("channels", []):
#                     st.markdown(f"- {c}")
#                 st.markdown("**KPIs:**")
#                 for k in strategy.get("KPIs", []):
#                     st.markdown(f"- {k}")
#             else:
#                 st.info("Strategy not found.")

#             st.markdown("---")
#             st.subheader("💡 Creative Campaign Ideas")
#             ideas_obj = results_dict.get("campaign_ideas", {})
#             ideas_list = ideas_obj.get("ideas", [])
#             st.markdown(f"**Title:** {ideas_obj.get('title', 'N/A')}")
#             for i, idea in enumerate(ideas_list):
#                 st.markdown(f"**Campaign {i+1}: {idea.get('name', '')}**")
#                 st.markdown(f"**Description:** {idea.get('description', '')}")
#                 st.markdown(f"**Audience:** {idea.get('audience', '')}")
#                 st.markdown(f"**Channel:** {idea.get('channel', '')}")
#                 st.markdown("---")

#             st.subheader("✍️ Marketing Copies")
#             copies = results_dict.get("marketing_copies", [])
#             for i, copy_item in enumerate(copies):
#                 st.markdown(f"**Copy {i+1}: {copy_item.get('title', '')}**")
#                 st.write(copy_item.get("body", ""))
#                 st.markdown("---")

#         except Exception as e:
#             st.error("❌ Error running CrewAI:")
#             st.exception(e)

# st.markdown("---")
# st.caption("🔗 Powered by CrewAI, OpenAI, Serper & Streamlit")




#Gemni 3
# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# from marketing_posts.crew import MarketingPostsCrew
# import streamlit.components.v1 as components

# # Load environment variables from .env
# load_dotenv()

# # --- API Keys ---
# serper_api_key = os.getenv("SERPER_API_KEY")
# openai_secret_path = "/run/secrets/openai-api-key"
# openai_api_key = None
# if os.path.exists(openai_secret_path):
#     try:
#         with open(openai_secret_path, "r") as f:
#             openai_api_key = f.read().strip()
#     except Exception as e:
#         st.error(f"Error reading OpenAI secret: {e}")
#         st.stop()
# else:
#     st.error("OpenAI secret file not found.")
#     st.stop()

# # Set API keys for environment
# os.environ["SERPER_API_KEY"] = serper_api_key or ""
# os.environ["OPENAI_API_KEY"] = openai_api_key or ""

# if not serper_api_key or not openai_api_key:
#     st.error("Missing API keys. Check .env and secrets.")
#     st.stop()

# # --- Static Descriptions for SVG Tooltips (always used for hover text) ---
# static_step_descriptions = {
#     "Step 1": "Performs domain-specific market research based on the customer domain and industry trends.",
#     "Step 2": "Interprets the project goal and research to design a strategic marketing plan.",
#     "Step 3": "Uses context from earlier steps to create a tactical marketing strategy.",
#     "Step 4": "Generates creative campaign ideas using the strategy from step 3.",
#     "Step 5": "Uses ideas + strategy to write multiple marketing copies.",
#     "Step 6": "Reviews and consolidates all outputs (research_summary, project_understanding, marketing_strategy, campaign_ideas, marketing_copies) into one clean JSON result for UI consumption."
# }

# # --- Streamlit UI ---
# st.set_page_config(layout="wide")
# st.title("🚀 AI Marketing Studio")
# st.markdown("---")

# st.header("Define Your Project")

# customer_domain = st.text_input("Customer Domain", placeholder="e.g., startup.com", key="customer_domain_input")
# project_description = st.text_area("Project Description", height=200, placeholder="Describe your product, goals, and audience.", key="project_description_input")

# st.markdown("---")

# # Initialize full_task_outputs for pre-loading and dynamic updates
# # This will be used for the expanders.
# if 'full_task_outputs' not in st.session_state:
#     st.session_state.full_task_outputs = {f"Step {i+1}: Description" : "Click 'Generate' to see the full output for this step." for i in range(6)}

# # --- SVG Diagram (always displayed) ---
# st.subheader("🗺️ Agent Flow Diagram (Hover for Static Descriptions)")
# svg = f"""
# <svg width="100%" height="450">
#   <style>
#     .step {{ font: 14px sans-serif; }}
#     .box {{ fill: #f0f0f0; stroke: #aaa; stroke-width: 1; rx: 5; ry: 5; }}
#     .line {{ stroke: #555; stroke-width: 1.5; marker-end: url(#arrow); }}
#     .tooltip {{
#         font: 12px sans-serif;
#         background: #333;
#         color: #fff;
#         padding: 5px;
#         border-radius: 3px;
#         display: none; /* Hidden by default */
#         position: absolute;
#         pointer-events: none; /* Allow events to pass through */
#     }}
#   </style>
#   <defs>
#     <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
#       <path d="M0,0 L0,6 L9,3 z" fill="#555" />
#     </marker>
#   </defs>

#   <rect id="step1" x="20" y="20" width="270" height="40" class="box"/>
#   <title>{static_step_descriptions["Step 1"]}</title>
#   <text x="30" y="45" class="step">🔍 Lead Market Analyst (Research)</text>

#   <rect id="step2" x="320" y="20" width="270" height="40" class="box"/>
#   <title>{static_step_descriptions["Step 2"]}</title>
#   <text x="330" y="45" class="step">🧠 Chief Marketing Strategist (Understanding)</text>

#   <rect id="step3" x="170" y="90" width="270" height="40" class="box"/>
#   <title>{static_step_descriptions["Step 3"]}</title>
#   <text x="180" y="115" class="step">📊 Chief Marketing Strategist (Strategy)</text>

#   <rect id="step4" x="170" y="160" width="270" height="40" class="box"/>
#   <title>{static_step_descriptions["Step 4"]}</title>
#   <text x="180" y="185" class="step">💡 Creative Content Creator (Campaign)</text>

#   <rect id="step5" x="170" y="230" width="270" height="40" class="box"/>
#   <title>{static_step_descriptions["Step 5"]}</title>
#   <text x="180" y="255" class="step">✍️ Creative Content Creator (Copy)</text>

#   <rect id="step6" x="470" y="230" width="270" height="40" class="box"/>
#   <title>{static_step_descriptions["Step 6"]}</title>
#   <text x="480" y="255" class="step">🎯 Chief Creative Director (Consolidate)</text>

#   <line x1="290" y1="40" x2="320" y2="40" class="line"/>

#   <line x1="155" y1="60" x2="155" y2="90" class="line"/>

#   <line x1="455" y1="60" x2="305" y2="90" class="line"/>

#   <line x1="305" y1="130" x2="305" y2="160" class="line"/>

#   <line x1="305" y1="130" x2="305" y2="230" class="line"/>

#   <line x1="305" y1="200" x2="305" y2="230" class="line"/>

#   <line x1="155" y1="60" x2="470" y2="250" class="line"/>
#   <line x1="455" y1="60" x2="470" y2="250" class="line"/>
#   <line x1="305" y1="130" x2="470" y2="250" class="line"/>
#   <line x1="305" y1="200" x2="470" y2="250" class="line"/>
#   <line x1="305" y1="250" x2="470" y2="250" class="line"/>

# </svg>
# """
# components.html(svg, height=470) # Display SVG immediately

# # --- Generate Button and Dynamic Output Section ---
# if st.button("Generate Marketing Campaign", type="primary"):
#     if not customer_domain or not project_description:
#         st.error("Please provide both inputs.")
#     else:
#         st.subheader("Generating Campaign...")
#         st.info("The AI Marketing Crew is at work! This might take a few minutes as they perform research and formulate the strategy.")

#         inputs = {"customer_domain": customer_domain, "project_description": project_description}

#         try:
#             with st.spinner("Running CrewAI..."):
#                 crew_final_output = MarketingPostsCrew().crew().kickoff(inputs=inputs)

#                 results_dict = crew_final_output.json_dict if hasattr(crew_final_output, 'json_dict') else json.loads(str(crew_final_output))

#                 # Populate full_task_outputs with actual dynamic content after generation
#                 st.session_state.full_task_outputs = {} # Reset for new run
#                 if hasattr(crew_final_output, 'tasks_output') and isinstance(crew_final_output.tasks_output, list):
#                     task_names_ordered = [
#                         "Lead Market Analyst (Research)",
#                         "Chief Marketing Strategist (Project Understanding)",
#                         "Chief Marketing Strategist (Marketing Strategy)",
#                         "Creative Content Creator (Campaign Idea)",
#                         "Creative Content Creator (Copy Creation)",
#                         "Chief Creative Director (Consolidate Output)"
#                     ]

#                     for i, task_result_item in enumerate(crew_final_output.tasks_output):
#                         full_step_title = f"Step {i+1}: {task_names_ordered[i]}" if i < len(task_names_ordered) else f"Step {i+1}"

#                         task_content = ""
#                         if isinstance(task_result_item, (dict, list)):
#                             task_content = json.dumps(task_result_item, indent=2)
#                         elif hasattr(task_result_item, 'model_dump_json'):
#                             task_content = task_result_item.model_dump_json(indent=2)
#                         elif hasattr(task_result_item, 'json'):
#                             task_content = task_result_item.json(indent=2)
#                         else:
#                             task_content = str(task_result_item)

#                         st.session_state.full_task_outputs[full_step_title] = task_content
#                 else:
#                     st.session_state.full_task_outputs["Final Consolidated Output"] = str(crew_final_output)

#             st.success("Campaign Generation Complete!")
#             st.markdown("---")

#             # --- Display Full Step Outputs (Dynamic Content) ---
#             st.markdown("### 📋 View Full Step Outputs")
#             # Loop through st.session_state.full_task_outputs which has full content
#             for step_title, content in st.session_state.full_task_outputs.items():
#                 with st.expander(f"{step_title} Output"):
#                     st.code(content)

#             # --- Final Campaign Output ---
#             st.markdown("---")
#             st.header("✨ Generated Marketing Campaign")

#             st.subheader("📚 Research Summary")
#             st.markdown(results_dict.get("research_summary", "Not available."))

#             st.subheader("🧠 Project Understanding")
#             st.markdown(results_dict.get("project_understanding", "Not available."))

#             st.markdown("---")
#             st.subheader("📊 Marketing Strategy")
#             strategy = results_dict.get("marketing_strategy")
#             if strategy:
#                 st.markdown(f"**Name:** {strategy.get('name', 'N/A')}")
#                 st.markdown("**Tactics:**")
#                 for t in strategy.get("tactics", []):
#                     st.markdown(f"- {t}")
#                 st.markdown("**Channels:**")
#                 for c in strategy.get("channels", []):
#                     st.markdown(f"- {c}")
#                 st.markdown("**KPIs:**")
#                 for k in strategy.get("KPIs", []):
#                     st.markdown(f"- {k}")
#             else:
#                 st.info("Strategy not found.")

#             st.markdown("---")
#             st.subheader("💡 Creative Campaign Ideas")
#             ideas_obj = results_dict.get("campaign_ideas", {})
#             ideas_list = ideas_obj.get("ideas", [])
#             st.markdown(f"**Title:** {ideas_obj.get('title', 'N/A')}")
#             for i, idea in enumerate(ideas_list):
#                 st.markdown(f"**Campaign {i+1}: {idea.get('name', '')}**")
#                 st.markdown(f"**Description:** {idea.get('description', '')}")
#                 st.markdown(f"**Audience:** {idea.get('audience', '')}")
#                 st.markdown(f"**Channel:** {idea.get('channel', '')}")
#                 st.markdown("---")

#             st.subheader("✍️ Marketing Copies")
#             copies = results_dict.get("marketing_copies", [])
#             for i, copy_item in enumerate(copies):
#                 st.markdown(f"**Copy {i+1}: {copy_item.get('title', '')}**")
#                 st.write(copy_item.get("body", ""))
#                 st.markdown("---")

#         except Exception as e:
#             st.error("❌ Error running CrewAI:")
#             st.exception(e)

# st.markdown("---")
# st.caption("🔗 Powered by CrewAI, OpenAI, Serper & Streamlit")


# Gemni Code(3rd)
# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# from marketing_posts.crew import MarketingPostsCrew
# import streamlit.components.v1 as components

# # Load environment variables from .env
# load_dotenv()

# # --- API Keys ---
# # FIX: Corrected typo from "SERPER_API:KEY" to "SERPER_API_KEY"
# serper_api_key = os.getenv("SERPER_API_KEY") 
# openai_secret_path = "/run/secrets/openai-api-key"
# openai_api_key = None
# if os.path.exists(openai_secret_path):
#     try:
#         with open(openai_secret_path, "r") as f:
#             openai_api_key = f.read().strip()
#     except Exception as e:
#         st.error(f"Error reading OpenAI secret: {e}")
#         st.stop()
# else:
#     st.error("OpenAI secret file not found.")
#     st.stop()

# # Set API keys for environment (ensure these are set for CrewAI tools)
# # These lines ensure that the environment variables are available for tools that
# # might implicitly read from os.environ.
# os.environ["SERPER_API_KEY"] = serper_api_key if serper_api_key else ''
# os.environ["OPENAI_API_KEY"] = openai_api_key if openai_api_key else ''

# # Basic validation (now should pass if keys are present)
# if not serper_api_key:
#     st.error("SERPER_API_KEY is not set. Please check your .env file and docker-compose.openai.yaml.")
#     st.stop()
# if not openai_api_key:
#     st.error("OPENAI_API_KEY is not set. Please ensure the 'secret.openai-api-key' file exists and is mounted.")
#     st.stop()

# # --- Rest of your Streamlit app code (no changes needed below this block) ---
# # --- Static Descriptions for SVG Tooltips (always used for hover text) ---
# static_step_descriptions = {
#     "step1": "Performs domain-specific market research based on the customer domain and industry trends.",
#     "step2": "Interprets the project goal and research to design a strategic marketing plan.",
#     "step3": "Uses context from earlier steps to create a tactical marketing strategy.",
#     "step4": "Generates creative campaign ideas using the strategy from step 3.",
#     "step5": "Uses ideas + strategy to write multiple marketing copies.",
#     "step6": "Reviews and consolidates all outputs (research_summary, project_understanding, marketing_strategy, campaign_ideas, marketing_copies) into one clean JSON result for UI consumption."
# }

# # Convert Python dict to JSON string for JavaScript
# static_descriptions_json = json.dumps(static_step_descriptions)


# # --- Streamlit UI ---
# st.set_page_config(layout="wide")
# st.title("🚀 AI Marketing Studio")
# st.markdown("---")

# st.header("Define Your Project")

# customer_domain = st.text_input("Customer Domain", placeholder="e.g., startup.com", key="customer_domain_input")
# project_description = st.text_area("Project Description", height=200, placeholder="Describe your product, goals, and audience.", key="project_description_input")

# st.markdown("---")

# # Initialize full_task_outputs for pre-loading and dynamic updates
# # Keys here match the step IDs in the SVG (e.g., "step1", "step2")
# if 'full_task_outputs' not in st.session_state:
#     st.session_state.full_task_outputs = {f"step{i+1}": "Click 'Generate' to see the full output for this step." for i in range(6)}

# # --- SVG Diagram (always displayed) with JS tooltips ---
# svg = f"""
# <svg width="100%" height="450">
#   <style>
#     .step {{ font: 14px sans-serif; }}
#     .box {{ fill: #f0f0f0; stroke: #aaa; stroke-width: 1; rx: 5; ry: 5; cursor: pointer; }} /* Added cursor:pointer */
#     .line {{ stroke: #555; stroke-width: 1.5; marker-end: url(#arrow); }}
#     #custom-tooltip {{
#         position: absolute;
#         display: none;
#         background-color: rgba(0, 0, 0, 0.8);
#         color: white;
#         padding: 5px 10px;
#         border-radius: 5px;
#         font-size: 12px;
#         pointer-events: none; /* Allows mouse events to pass through to elements below */
#         z-index: 1000; /* Ensure it's on top */
#         white-space: normal; /* CHANGE: Allow text to wrap */
#         max-width: 400px; /* INCREASED: Max width to allow more text before wrapping, or remove for no limit */
#         overflow: visible; /* CHANGE: Allow content to be fully visible */
#         text-overflow: clip; /* CHANGE: Prevent ellipsis */
#     }}
#   </style>
#   <defs>
#     <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
#       <path d="M0,0 L0,6 L9,3 z" fill="#555" />
#     </marker>
#   </defs>

#   <rect id="step1" x="20" y="20" width="270" height="40" class="box"/>
#   <text x="30" y="45" class="step">🔍 Lead Market Analyst (Research)</text>

#   <rect id="step2" x="320" y="20" width="270" height="40" class="box"/>
#   <text x="330" y="45" class="step">🧠 Chief Marketing Strategist (Understanding)</text>

#   <rect id="step3" x="170" y="90" width="270" height="40" class="box"/>
#   <text x="180" y="115" class="step">📊 Chief Marketing Strategist (Strategy)</text>

#   <rect id="step4" x="170" y="160" width="270" height="40" class="box"/>
#   <text x="180" y="185" class="step">💡 Creative Content Creator (Campaign)</text>

#   <rect id="step5" x="170" y="230" width="270" height="40" class="box"/>
#   <text x="180" y="255" class="step">✍️ Creative Content Creator (Copy)</text>

#   <rect id="step6" x="470" y="230" width="270" height="40" class="box"/>
#   <text x="480" y="255" class="step">🎯 Chief Creative Director (Consolidate)</text>

#   <line x1="290" y1="40" x2="320" y2="40" class="line"/>

#   <line x1="155" y1="60" x2="155" y2="90" class="line"/>

#   <line x1="455" y1="60" x2="305" y2="90" class="line"/>

#   <line x1="305" y1="130" x2="305" y2="160" class="line"/>

#   <line x1="305" y1="130" x2="305" y2="230" class="line"/>

#   <line x1="305" y1="200" x2="305" y2="230" class="line"/>

#   <line x1="155" y1="60" x2="470" y2="250" class="line"/>
#   <line x1="455" y1="60" x2="470" y2="250" class="line"/>
#   <line x1="305" y1="130" x2="470" y2="250" class="line"/>
#   <line x1="305" y1="200" x2="470" y2="250" class="line"/>
#   <line x1="305" y1="250" x2="470" y2="250" class="line"/>

# </svg>
# <div id="custom-tooltip"></div>
# <script>
#     const descriptions = {static_descriptions_json}; // Injected from Python
#     const tooltip = document.getElementById('custom-tooltip');

#     document.querySelectorAll('.box').forEach(box => {{
#         box.addEventListener('mouseover', (e) => {{
#             const id = e.target.id;
#             const text = descriptions[id];
#             if (text) {{
#                 tooltip.innerHTML = text;
#                 tooltip.style.display = 'block';
#                 // Position tooltip relative to the hovered element, or mouse position
#                 tooltip.style.left = (e.pageX + 10) + 'px';
#                 tooltip.style.top = (e.pageY + 10) + 'px';
#             }}
#         }});

#         box.addEventListener('mouseout', () => {{
#             tooltip.style.display = 'none';
#         }});

#         // For touch devices (long press) or ensuring a click also shows/hides
#         box.addEventListener('click', (e) => {{
#             const id = e.target.id;
#             const text = descriptions[id];
#             if (text && tooltip.style.display === 'none') {{
#                 tooltip.innerHTML = text;
#                 tooltip.style.display = 'block';
#                 tooltip.style.left = (e.pageX + 10) + 'px';
#                 tooltip.style.top = (e.pageY + 10) + 'px';
#             }} else {{
#                 tooltip.style.display = 'none';
#             }}
#         }});
#     }});
# </script>
# """
# components.html(svg, height=470) # Display SVG immediately

# # --- Generate Button and Dynamic Output Section ---
# if st.button("Generate Marketing Campaign", type="primary"):
#     if not customer_domain or not project_description:
#         st.error("Please provide both inputs.")
#     else:
#         st.subheader("Generating Campaign...")
#         st.info("The AI Marketing Crew is at work! This might take a few minutes as they perform research and formulate the strategy.")

#         inputs = {"customer_domain": customer_domain, "project_description": project_description}

#         try:
#             with st.spinner("Running CrewAI..."):
#                 crew_final_output = MarketingPostsCrew().crew().kickoff(inputs=inputs)

#                 results_dict = crew_final_output.json_dict if hasattr(crew_final_output, 'json_dict') else json.loads(str(crew_final_output))

#                 # Populate full_task_outputs with actual dynamic content after generation
#                 st.session_state.full_task_outputs = {} # Reset for new run
#                 if hasattr(crew_final_output, 'tasks_output') and isinstance(crew_final_output.tasks_output, list):
#                     task_names_ordered = [
#                         "Lead Market Analyst (Research)",
#                         "Chief Marketing Strategist (Project Understanding)",
#                         "Chief Marketing Strategist (Marketing Strategy)",
#                         "Creative Content Creator (Campaign Idea)",
#                         "Creative Content Creator (Copy Creation)",
#                         "Chief Creative Director (Consolidate Output)"
#                     ]

#                     for i, task_result_item in enumerate(crew_final_output.tasks_output):
#                         step_id_key = f"step{i+1}" # Key for full_task_outputs matches SVG IDs
                        
#                         task_content = ""
#                         if isinstance(task_result_item, (dict, list)):
#                             task_content = json.dumps(task_result_item, indent=2)
#                         elif hasattr(task_result_item, 'model_dump_json'):
#                             task_content = task_result_item.model_dump_json(indent=2)
#                         elif hasattr(task_result_item, 'json'):
#                             task_content = task_result_item.json(indent=2)
#                         else:
#                             task_content = str(task_result_item)

#                         st.session_state.full_task_outputs[step_id_key] = task_content # Store using 'stepX' key
#                 else:
#                     st.session_state.full_task_outputs["step1"] = str(crew_final_output) # Fallback for expander

#             st.success("Campaign Generation Complete!")
#             st.markdown("---")

#             # --- Display Full Step Outputs (Dynamic Content) ---
#             st.markdown("### 📋 View Full Step Outputs")
#             # Loop through static_step_descriptions keys to ensure correct order and titles
#             # But use content from st.session_state.full_task_outputs
#             for step_id in sorted(static_step_descriptions.keys(), key=lambda x: int(x.replace('step',''))):
#                 # Use the full static title for the expander
#                 full_expander_title = f"{step_id.replace('step', 'Step ')}: {static_step_descriptions[step_id]}"
#                 content = st.session_state.full_task_outputs.get(step_id, "No output generated for this step.")
#                 with st.expander(full_expander_title):
#                     st.code(content)

#             # --- Final Campaign Output ---
#             st.markdown("---")
#             st.header("✨ Generated Marketing Campaign")

#             st.subheader("📚 Research Summary")
#             st.markdown(results_dict.get("research_summary", "Not available."))

#             st.subheader("🧠 Project Understanding")
#             st.markdown(results_dict.get("project_understanding", "Not available."))

#             st.markdown("---")
#             st.subheader("📊 Marketing Strategy")
#             strategy = results_dict.get("marketing_strategy")
#             if strategy:
#                 st.markdown(f"**Name:** {strategy.get('name', 'N/A')}")
#                 st.markdown("**Tactics:**")
#                 for t in strategy.get("tactics", []):
#                     st.markdown(f"- {t}")
#                 st.markdown("**Channels:**")
#                 for c in strategy.get("channels", []):
#                     st.markdown(f"- {c}")
#                 st.markdown("**KPIs:**")
#                 for k in strategy.get("KPIs", []):
#                     st.markdown(f"- {k}")
#             else:
#                 st.info("Strategy not found.")

#             st.markdown("---")
#             st.subheader("💡 Creative Campaign Ideas")
#             ideas_obj = results_dict.get("campaign_ideas", {})
#             ideas_list = ideas_obj.get("ideas", [])
#             st.markdown(f"**Title:** {ideas_obj.get('title', 'N/A')}")
#             for i, idea in enumerate(ideas_list):
#                 st.markdown(f"**Campaign {i+1}: {idea.get('name', '')}**")
#                 st.markdown(f"**Description:** {idea.get('description', '')}")
#                 st.markdown(f"**Audience:** {idea.get('audience', '')}")
#                 st.markdown(f"**Channel:** {idea.get('channel', '')}")
#                 st.markdown("---")

#             st.subheader("✍️ Marketing Copies")
#             copies = results_dict.get("marketing_copies", [])
#             for i, copy_item in enumerate(copies):
#                 st.markdown(f"**Copy {i+1}: {copy_item.get('title', '')}**")
#                 st.write(copy_item.get("body", ""))
#                 st.markdown("---")

#         except Exception as e:
#             st.error("❌ Error running CrewAI:")
#             st.exception(e)

# st.markdown("---")
# st.caption("🔗 Powered by CrewAI, OpenAI, Serper & Streamlit")




# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# from marketing_posts.crew import MarketingPostsCrew
# import streamlit.components.v1 as components


# # --- API Key Loading ---
# load_dotenv()

# serper_api_key = os.getenv("SERPER_API_KEY")
# openai_secret_path = "/run/secrets/openai-api-key"
# openai_api_key = None

# if os.path.exists(openai_secret_path):
#     try:
#         with open(openai_secret_path, "r") as f:
#             openai_api_key = f.read().strip()
#     except Exception as e:
#         st.error(f"Error reading OpenAI secret: {e}")
#         st.stop()
# else:
#     st.error(f"OpenAI secret file not found at {openai_secret_path}. Please ensure it's correctly mounted as a Docker secret.")
#     st.stop()

# os.environ['SERPER_API_KEY'] = serper_api_key if serper_api_key else ''
# os.environ['OPENAI_API_KEY'] = openai_api_key if openai_api_key else ''

# if not serper_api_key:
#     st.error("SERPER_API_KEY is missing. Please check your .env file and docker-compose.openai.yaml configuration.")
#     st.stop()
# if not openai_api_key:
#     st.error("OPENAI_API_KEY is missing. Please ensure the 'secret.openai-api-key' file exists and is correctly mounted as a Docker secret.")
#     st.stop()


# # --- Static Step Descriptions for Diagram Tooltips and Expander Titles ---
# static_step_descriptions = {
#     "step1": ("🔍 Lead Market Analyst (Research)", "Performs domain-specific market research based on the customer domain and industry trends."),
#     "step2": ("🧠 Chief Marketing Strategist (Understanding)", "Interprets the project goal and research to design a strategic marketing plan."),
#     "step3": ("📊 Chief Marketing Strategist (Strategy)", "Uses context from earlier steps to create a tactical marketing strategy."),
#     "step4": ("💡 Creative Content Creator (Campaign)", "Generates creative campaign ideas using the strategy from step 3."),
#     "step5": ("✍️ Creative Content Creator (Copy)", "Writes multiple marketing copies using ideas + strategy."),
#     "step6": ("🎯 Chief Creative Director (Consolidate)", "Reviews and consolidates all outputs (research summary, project understanding, marketing strategy, campaign ideas, marketing copies) into one clean JSON result for UI consumption.")
# }

# static_descriptions_json_for_js = json.dumps({k: v[1] for k, v in static_step_descriptions.items()})


# # --- Streamlit Page Configuration ---
# st.set_page_config(layout="wide")
# st.title("AI Marketing Studio")
# st.markdown("---")


# # --- Main Content Area ---
# st.header("Define Your Project")

# customer_domain = st.text_input("Customer Domain (e.g., startup.com)", placeholder="e.g., quantumleaptech.com", key="customer_domain_input")
# project_description = st.text_area("Project Description (Describe your product, goals, and audience.)", height=200, placeholder="e.g., Quantum Leap Tech is launching a new enterprise-grade cybersecurity solution...", key="project_description_input")

# st.markdown("---")

# # Initialize session state for storing full task outputs if not already present
# if 'full_task_outputs' not in st.session_state:
#     st.session_state.full_task_outputs = {step_id: "Click 'Generate' to see the full output for this step." for step_id in static_step_descriptions.keys()}
#     st.session_state.final_consolidated_output = {}


# # --- SVG Diagram (always displayed on load) ---
# st.subheader("Agent Flow Diagram (Hover for Description)")

# svg = f"""
# <svg width="100%" height="450">
#   <style>
#     .step {{ font: 14px sans-serif; }}
#     .box {{ fill: #f0f0f0; stroke: #aaa; stroke-width: 1; rx: 5; ry: 5; cursor: pointer; }}
#     .line {{ stroke: #555; stroke-width: 1.5; marker-end: url(#arrow); }}
#     #custom-tooltip {{
#         position: absolute;
#         display: none;
#         background-color: rgba(0, 0, 0, 0.8);
#         color: white;
#         padding: 5px 10px;
#         border-radius: 5px;
#         font-size: 12px;
#         pointer-events: none;
#         z-index: 1000;
#         white-space: normal;
#         max-width: 400px;
#         overflow: visible;
#         text-overflow: clip;
#     }}
#   </style>
#   <defs>
#     <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
#       <path d="M0,0 L0,6 L9,3 z" fill="#555" />
#     </marker>
#   </defs>

#   <rect id="step1" x="20" y="20" width="270" height="40" class="box"/>
#   <text x="30" y="45" class="step">{static_step_descriptions["step1"][0]}</text>

#   <rect id="step2" x="320" y="20" width="270" height="40" class="box"/>
#   <text x="330" y="45" class="step">{static_step_descriptions["step2"][0]}</text>

#   <rect id="step3" x="170" y="90" width="270" height="40" class="box"/>
#   <text x="180" y="115" class="step">{static_step_descriptions["step3"][0]}</text>

#   <rect id="step4" x="170" y="160" width="270" height="40" class="box"/>
#   <text x="180" y="185" class="step">{static_step_descriptions["step4"][0]}</text>

#   <rect id="step5" x="170" y="230" width="270" height="40" class="box"/>
#   <text x="180" y="255" class="step">{static_step_descriptions["step5"][0]}</text>

#   <rect id="step6" x="470" y="230" width="270" height="40" class="box"/>
#   <text x="480" y="255" class="step">{static_step_descriptions["step6"][0]}</text>

#   <line x1="290" y1="40" x2="320" y2="40" class="line"/>

#   <line x1="155" y1="60" x2="155" y2="90" class="line"/>

#   <line x1="455" y1="60" x2="305" y2="90" class="line"/>

#   <line x1="305" y1="130" x2="305" y2="160" class="line"/>

#   <line x1="305" y1="130" x2="305" y2="230" class="line"/>

#   <line x1="305" y1="200" x2="305" y2="230" class="line"/>

#   <line x1="155" y1="60" x2="470" y2="250" class="line"/>
#   <line x1="455" y1="60" x2="470" y2="250" class="line"/>
#   <line x1="305" y1="130" x2="470" y2="250" class="line"/>
#   <line x1="305" y1="200" x2="470" y2="250" class="line"/>
#   <line x1="305" y1="250" x2="470" y2="250" class="line"/>

# </svg>
# <div id="custom-tooltip"></div>
# <script>
#     const descriptions = {static_descriptions_json_for_js};
#     const tooltip = document.getElementById('custom-tooltip');

#     document.querySelectorAll('.box').forEach(box => {{
#         box.addEventListener('mouseover', (e) => {{
#             const id = e.target.id;
#             const text = descriptions[id];
#             if (text) {{
#                 tooltip.innerHTML = text;
#                 tooltip.style.display = 'block';
#                 tooltip.style.left = (e.pageX + 10) + 'px';
#                 tooltip.style.top = (e.pageY + 10) + 'px';
#             }}
#         }});

#         box.addEventListener('mouseout', () => {{
#             tooltip.style.display = 'none';
#         }});

#         box.addEventListener('click', (e) => {{
#             const id = e.target.id;
#             // No direct routing here. The expanders below provide the details.
#             // You could potentially scroll to the expander here if you wish.
#         }});
#     }});
# </script>
# """
# components.html(svg, height=470)


# # --- Generate Button and Dynamic Output Section ---
# if st.button("Generate Marketing Campaign", type="primary"):
#     if not customer_domain or not project_description:
#         st.error("Please provide both inputs.")
#     else:
#         st.subheader("Generating Campaign...")
#         st.info("The AI Marketing Crew is at work! This might take a few minutes as they perform research and formulate the strategy.")

#         inputs = {"customer_domain": customer_domain, "project_description": project_description}

#         try:
#             with st.spinner("Running CrewAI..."):
#                 # kickoff returns the output of the final task (consolidate_output_task)
#                 crew_final_output_result = MarketingPostsCrew().crew().kickoff(inputs=inputs)

#                 # Access the final consolidated JSON from the crew_final_output_result.
#                 # Assuming consolidate_output_task outputs a dict that becomes crew_final_output_result.json_dict
#                 results_dict = crew_final_output_result.json_dict if hasattr(crew_final_output_result, 'json_dict') else json.loads(str(crew_final_output_result))


#                 # Store consolidated output in session state
#                 st.session_state.final_consolidated_output = results_dict

#                 # Populate full_task_outputs with actual dynamic content from individual tasks
#                 st.session_state.full_task_outputs = {} # Reset for new run
                
#                 # Access tasks_output directly from the `CrewOutput` object returned by kickoff
#                 if hasattr(crew_final_output_result, 'tasks_output') and isinstance(crew_final_output_result.tasks_output, list):
#                     for i, task_output_item in enumerate(crew_final_output_result.tasks_output):
#                         step_id_key = f"step{i+1}" # Key for full_task_outputs matches SVG IDs
                        
#                         task_content = ""
#                         # Convert task_output_item (which can be a BaseModel instance, dict, or string) to JSON string
#                         if isinstance(task_output_item, (dict, list)):
#                             task_content = json.dumps(task_output_item, indent=2)
#                         elif hasattr(task_output_item, 'model_dump_json'): # Pydantic v2
#                             task_content = task_output_item.model_dump_json(indent=2)
#                         elif hasattr(task_output_item, 'json'): # Pydantic v1
#                             task_content = task_output_item.json(indent=2)
#                         else: # Fallback for raw string output or other types
#                             task_content = str(task_output_item)

#                         st.session_state.full_task_outputs[step_id_key] = task_content
#                 else:
#                     st.warning("Could not retrieve individual task outputs from CrewAI. Only final consolidated output will be available.")
#                     st.session_state.full_task_outputs["step6"] = json.dumps(results_dict, indent=2) # Fallback for expander


#             st.success("✅ Done. Outputs loaded! Scroll down to view the results.")
#             st.rerun() # Use st.rerun() instead of st.experimental_rerun()

#         except Exception as e:
#             st.error("❌ An error occurred during CrewAI execution:")
#             st.exception(e)
#             st.session_state.full_task_outputs = {step_id: f"Error: {e}" for step_id in static_step_descriptions.keys()}
#             st.session_state.final_consolidated_output = {}


# # --- Display Full Step Outputs (Dynamic Content in Expanders) ---
# st.markdown("### 📋 View Full Step Outputs")
# for step_id, (label, desc) in static_step_descriptions.items():
#     content = st.session_state.get("full_task_outputs", {}).get(step_id, "No output generated for this step yet.")
#     with st.expander(f"{label} Output"):
#         st.code(content, language="json")


# # --- Final Campaign Output (Displayed at the bottom) ---
# st.markdown("---")
# st.header("✨ Generated Marketing Campaign")

# final_results_for_display = st.session_state.get("final_consolidated_output", {})

# if final_results_for_display:
#     st.subheader("📚 Research Summary")
#     st.markdown(final_results_for_display.get("research_summary", "Not available."))

#     st.subheader("🧠 Project Understanding")
#     st.markdown(final_results_for_display.get("project_understanding", "Not available."))

#     st.markdown("---")
#     st.subheader("📊 Marketing Strategy")
#     strategy = final_results_for_display.get("marketing_strategy")
#     if strategy:
#         st.markdown(f"**Name:** {strategy.get('name', 'N/A')}")
#         st.markdown("**Tactics:**")
#         for t in strategy.get("tactics", []):
#             st.markdown(f"- {t}")
#         st.markdown("**Channels:**")
#         for c in strategy.get("channels", []):
#             st.markdown(f"- {c}")
#         st.markdown("**KPIs:**")
#         for k in strategy.get("KPIs", []):
#             st.markdown(f"- {k}")
#     else:
#         st.info("Strategy not found.")

#     st.markdown("---")
#     st.subheader("💡 Creative Campaign Ideas")
#     ideas_obj = final_results_for_display.get("campaign_ideas", {})
#     ideas_list = ideas_obj.get("ideas", [])
#     st.markdown(f"**Title:** {ideas_obj.get('title', 'N/A')}")
#     for i, idea in enumerate(ideas_list):
#         st.markdown(f"**Campaign {i+1}: {idea.get('name', '')}**")
#         st.markdown(f"**Description:** {idea.get('description', '')}")
#         st.markdown(f"**Audience:** {idea.get('audience', '')}")
#         st.markdown(f"**Channel:** {idea.get('channel', '')}")
#         st.markdown("---")

#     st.subheader("✍️ Marketing Copies")
#     copies = final_results_for_display.get("marketing_copies", [])
#     for i, copy_item in enumerate(copies):
#         st.markdown(f"**Copy {i+1}: {copy_item.get('title', '')}**")
#         st.write(copy_item.get("body", ""))
#         st.markdown("---")
# else:
#     st.info("Generated marketing campaign details will appear here after execution.")


# st.markdown("---")
# st.caption("🔗 Powered by CrewAI, OpenAI, Serper & Streamlit")


# # GPT Code 
# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# from marketing_posts.crew import MarketingPostsCrew
# import streamlit.components.v1 as components

# # --- Load API Keys ---
# load_dotenv()
# serper_api_key = os.getenv("SERPER_API_KEY")
# openai_secret_path = "/run/secrets/openai-api-key"

# if os.path.exists(openai_secret_path):
#     try:
#         with open(openai_secret_path, "r") as f:
#             openai_api_key = f.read().strip()
#     except Exception as e:
#         st.error(f"Error reading OpenAI secret: {e}")
#         st.stop()
# else:
#     st.error(f"OpenAI secret file not found at {openai_secret_path}. Please ensure it's mounted.")
#     st.stop()

# os.environ["SERPER_API_KEY"] = serper_api_key or ''
# os.environ["OPENAI_API_KEY"] = openai_api_key or ''

# if not serper_api_key or not openai_api_key:
#     st.error("API keys missing. Check your .env and Docker secrets.")
#     st.stop()

# # --- Static Descriptions for Each Step ---
# static_step_descriptions = {
#     "step1": ("Lead Market Analyst (Research)", "Performs domain-specific market research."),
#     "step2": ("Chief Marketing Strategist (Understanding)", "Interprets goals and research."),
#     "step3": ("Chief Marketing Strategist (Strategy)", "Creates tactical marketing strategy."),
#     "step4": ("Creative Content Creator (Campaign)", "Generates creative campaign ideas."),
#     "step5": ("Creative Content Creator (Copy)", "Writes marketing copies."),
#     "step6": ("Chief Creative Director (Consolidate)", "Consolidates all outputs for display.")
# }

# # --- Streamlit App Config ---
# st.set_page_config(layout="wide")
# st.title("AI Marketing Studio")
# st.markdown("---")

# query_params = st.query_params
# selected_step_id = query_params.get("step", None)

# # --- STEP DETAIL PAGE ---
# if selected_step_id:
#     if "full_task_outputs" not in st.session_state or not st.session_state.full_task_outputs:
#         st.warning("You must generate a campaign first.")
#         st.markdown("[Back to Home](/)")
#         st.stop()

#     step_label, step_desc = static_step_descriptions.get(selected_step_id, ("Unknown Step", ""))
#     st.header(f"{step_label}")
#     st.caption(step_desc)
#     st.markdown("---")
#     st.subheader("Output from this step:")
#     output = st.session_state.full_task_outputs.get(selected_step_id, "No output for this step.")
#     st.code(output, language="json")
#     st.markdown("[Back to Home](/)")
#     st.stop()

# # --- MAIN PAGE ---
# st.header("Define Your Project")
# customer_domain = st.text_input("Customer Domain", placeholder="e.g., startup.com")
# project_description = st.text_area("Project Description", height=200, placeholder="Describe your product...")
# st.markdown("---")

# if 'full_task_outputs' not in st.session_state:
#     st.session_state.full_task_outputs = {}
#     st.session_state.final_consolidated_output = {}

# if st.button("Generate Marketing Campaign"):
#     if not customer_domain or not project_description:
#         st.error("Please provide both inputs.")
#     else:
#         st.subheader("Generating Campaign...")
#         st.info("The AI Marketing Crew is at work. This may take a minute.")
#         try:
#             with st.spinner("Running CrewAI..."):
#                 inputs = {"customer_domain": customer_domain, "project_description": project_description}
#                 crew_result = MarketingPostsCrew().crew().kickoff(inputs=inputs)

#                 results_dict = crew_result.json_dict if hasattr(crew_result, 'json_dict') else json.loads(str(crew_result))
#                 st.session_state.final_consolidated_output = results_dict
#                 st.session_state.full_task_outputs = {}

#                 if hasattr(crew_result, 'tasks_output'):
#                     for i, task_output in enumerate(crew_result.tasks_output):
#                         step_key = f"step{i+1}"
#                         if isinstance(task_output, (dict, list)):
#                             output_str = json.dumps(task_output, indent=2)
#                         elif hasattr(task_output, "model_dump_json"):
#                             output_str = task_output.model_dump_json(indent=2)
#                         else:
#                             output_str = str(task_output)
#                         st.session_state.full_task_outputs[step_key] = output_str
#                 else:
#                     st.session_state.full_task_outputs["step6"] = json.dumps(results_dict, indent=2)

#             st.success("Campaign generated!")
#             st.rerun()

#         except Exception as e:
#             st.error("An error occurred during generation.")
#             st.exception(e)
#             st.session_state.full_task_outputs = {}
#             st.session_state.final_consolidated_output = {}

# # --- SVG + Outputs ---
# if st.session_state.get("full_task_outputs"):
#     st.subheader("Agent Flow Diagram (Click to View Outputs)")
#     static_descriptions_json_for_js = json.dumps({k: v[1] for k, v in static_step_descriptions.items()})

#     svg = f"""
#     <svg width="100%" height="450">
#       <style>
#         .step {{ font: 14px sans-serif; }}
#         .box {{ fill: #f0f0f0; stroke: #aaa; stroke-width: 1; rx: 5; ry: 5; cursor: pointer; }}
#         .line {{ stroke: #555; stroke-width: 1.5; marker-end: url(#arrow); }}
#         #custom-tooltip {{
#             position: absolute;
#             display: none;
#             background-color: rgba(0, 0, 0, 0.8);
#             color: white;
#             padding: 5px 10px;
#             border-radius: 5px;
#             font-size: 12px;
#             pointer-events: none;
#             z-index: 1000;
#             white-space: normal;
#             max-width: 400px;
#         }}
#       </style>
#       <defs>
#         <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
#           <path d="M0,0 L0,6 L9,3 z" fill="#555" />
#         </marker>
#       </defs>

#       <a xlink:href="/?step=step1"><rect id="step1" x="20" y="20" width="270" height="40" class="box"/></a>
#       <text x="30" y="45" class="step">{static_step_descriptions['step1'][0]}</text>

#       <a xlink:href="/?step=step2"><rect id="step2" x="320" y="20" width="270" height="40" class="box"/></a>
#       <text x="330" y="45" class="step">{static_step_descriptions['step2'][0]}</text>

#       <a xlink:href="/?step=step3"><rect id="step3" x="170" y="90" width="270" height="40" class="box"/></a>
#       <text x="180" y="115" class="step">{static_step_descriptions['step3'][0]}</text>

#       <a xlink:href="/?step=step4"><rect id="step4" x="170" y="160" width="270" height="40" class="box"/></a>
#       <text x="180" y="185" class="step">{static_step_descriptions['step4'][0]}</text>

#       <a xlink:href="/?step=step5"><rect id="step5" x="170" y="230" width="270" height="40" class="box"/></a>
#       <text x="180" y="255" class="step">{static_step_descriptions['step5'][0]}</text>

#       <a xlink:href="/?step=step6"><rect id="step6" x="470" y="230" width="270" height="40" class="box"/></a>
#       <text x="480" y="255" class="step">{static_step_descriptions['step6'][0]}</text>

#       <line x1="290" y1="40" x2="320" y2="40" class="line"/>
#       <line x1="155" y1="60" x2="155" y2="90" class="line"/>
#       <line x1="455" y1="60" x2="305" y2="90" class="line"/>
#       <line x1="305" y1="130" x2="305" y2="160" class="line"/>
#       <line x1="305" y1="130" x2="305" y2="230" class="line"/>
#       <line x1="305" y1="200" x2="305" y2="230" class="line"/>
#       <line x1="155" y1="60" x2="470" y2="250" class="line"/>
#       <line x1="455" y1="60" x2="470" y2="250" class="line"/>
#       <line x1="305" y1="130" x2="470" y2="250" class="line"/>
#       <line x1="305" y1="200" x2="470" y2="250" class="line"/>
#       <line x1="305" y1="250" x2="470" y2="250" class="line"/>
#     </svg>
#     <div id="custom-tooltip"></div>
#     <script>
#         const descriptions = {static_descriptions_json_for_js};
#         const tooltip = document.getElementById('custom-tooltip');
#         document.querySelectorAll('.box').forEach(box => {{
#             box.addEventListener('mouseover', (e) => {{
#                 const id = e.target.id;
#                 const text = descriptions[id];
#                 if (text) {{
#                     tooltip.innerHTML = text;
#                     tooltip.style.display = 'block';
#                     tooltip.style.left = (e.pageX + 10) + 'px';
#                     tooltip.style.top = (e.pageY + 10) + 'px';
#                 }}
#             }});
#             box.addEventListener('mouseout', () => {{ tooltip.style.display = 'none'; }});
#         }});
#     </script>
#     """
#     components.html(svg, height=470)

#     st.markdown("### View Step Outputs")
#     for step_id, (label, _) in static_step_descriptions.items():
#         with st.expander(f"{label} Output"):
#             output = st.session_state.full_task_outputs.get(step_id, "No output for this step.")
#             st.code(output, language="json")

#     st.markdown("---")
#     st.header("Generated Marketing Campaign")
#     final = st.session_state.get("final_consolidated_output", {})
#     if final:
#         st.subheader("Research Summary")
#         st.markdown(final.get("research_summary", "Not available."))

#         st.subheader("Project Understanding")
#         st.markdown(final.get("project_understanding", "Not available."))

#         st.markdown("---")
#         st.subheader("Marketing Strategy")
#         strategy = final.get("marketing_strategy", {})
#         if strategy:
#             st.markdown(f"**Name:** {strategy.get('name', '')}")
#             st.markdown("**Tactics:**")
#             for t in strategy.get("tactics", []):
#                 st.markdown(f"- {t}")
#             st.markdown("**Channels:**")
#             for c in strategy.get("channels", []):
#                 st.markdown(f"- {c}")
#             st.markdown("**KPIs:**")
#             for k in strategy.get("KPIs", []):
#                 st.markdown(f"- {k}")
#         else:
#             st.info("Strategy not found.")

#         st.markdown("---")
#         st.subheader("Creative Campaign Ideas")
#         ideas = final.get("campaign_ideas", {})
#         st.markdown(f"**Title:** {ideas.get('title', 'N/A')}")
#         for i, idea in enumerate(ideas.get("ideas", [])):
#             st.markdown(f"**Campaign {i+1}: {idea.get('name', '')}**")
#             st.markdown(f"**Description:** {idea.get('description', '')}")
#             st.markdown(f"**Audience:** {idea.get('audience', '')}")
#             st.markdown(f"**Channel:** {idea.get('channel', '')}")
#             st.markdown("---")

#         st.subheader("Marketing Copies")
#         for i, copy in enumerate(final.get("marketing_copies", [])):
#             st.markdown(f"**Copy {i+1}: {copy.get('title', '')}**")
#             st.write(copy.get("body", ""))
#             st.markdown("---")
#     else:
#         st.info("Campaign output will appear here after generation.")

# st.markdown("---")
# st.caption("Powered by CrewAI, OpenAI, Serper & Streamlit")




# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# from marketing_posts.crew import MarketingPostsCrew
# import streamlit.components.v1 as components

# # --- Load API Keys ---
# load_dotenv()
# serper_api_key = os.getenv("SERPER_API_KEY")
# openai_secret_path = "/run/secrets/openai-api-key"

# if os.path.exists(openai_secret_path):
#     with open(openai_secret_path, "r") as f:
#         openai_api_key = f.read().strip()
# else:
#     st.error("Missing OpenAI secret file.")
#     st.stop()

# os.environ["SERPER_API_KEY"] = serper_api_key or ''
# os.environ["OPENAI_API_KEY"] = openai_api_key or ''

# if not serper_api_key or not openai_api_key:
#     st.error("API keys missing. Check .env or Docker secrets.")
#     st.stop()

# # --- Static Descriptions for Each Step ---
# static_step_descriptions = {
#     "step1": ("Lead Market Analyst (Research)", "Performs domain-specific market research."),
#     "step2": ("Chief Marketing Strategist (Understanding)", "Interprets goals and research."),
#     "step3": ("Chief Marketing Strategist (Strategy)", "Creates tactical marketing strategy."),
#     "step4": ("Creative Content Creator (Campaign)", "Generates creative campaign ideas."),
#     "step5": ("Creative Content Creator (Copy)", "Writes marketing copies."),
#     "step6": ("Chief Creative Director (Consolidate)", "Consolidates all outputs for display.")
# }

# # --- Streamlit App Config ---
# st.set_page_config(layout="wide", page_title="AI Marketing Studio")
# st.title("AI Marketing Studio")
# st.markdown("---")

# query_params = st.query_params
# selected_step_id = query_params.get("step", None)

# # --- STEP DETAIL PAGE ---
# if selected_step_id:
#     if "full_task_outputs" not in st.session_state or not st.session_state.full_task_outputs:
#         st.warning("You must generate a campaign first.")
#         st.markdown("[Back to Home](/)")
#         st.stop()

#     step_label, step_desc = static_step_descriptions.get(selected_step_id, ("Unknown Step", ""))
#     st.header(step_label)
#     st.caption(step_desc)
#     st.markdown("---")
#     st.subheader("Output from this step:")
#     output = st.session_state.full_task_outputs.get(selected_step_id, "No output for this step.")
#     st.code(output, language="json")
#     st.markdown("[Back to Home](/)")
#     st.stop()

# # --- MAIN PAGE ---
# st.header("Define Your Project")
# customer_domain = st.text_input("Customer Domain", placeholder="e.g., fintech, healthcare")
# project_description = st.text_area("Project Description", height=200, placeholder="Describe your product...")

# st.markdown("---")

# # Initialize session states
# if 'full_task_outputs' not in st.session_state:
#     st.session_state.full_task_outputs = {}
#     st.session_state.final_consolidated_output = {}

# # --- Run Crew & Cache Output ---
# @st.cache_data(show_spinner=False)
# def run_crew_ai(domain, desc):
#     inputs = {"customer_domain": domain, "project_description": desc}
#     crew_result = MarketingPostsCrew().crew().kickoff(inputs=inputs)

#     results_dict = crew_result.json_dict if hasattr(crew_result, 'json_dict') else json.loads(str(crew_result))
#     outputs = {}
#     if hasattr(crew_result, 'tasks_output'):
#         for i, task_output in enumerate(crew_result.tasks_output):
#             key = f"step{i+1}"
#             if isinstance(task_output, (dict, list)):
#                 outputs[key] = json.dumps(task_output, indent=2)
#             elif hasattr(task_output, "model_dump_json"):
#                 outputs[key] = task_output.model_dump_json(indent=2)
#             else:
#                 outputs[key] = str(task_output)
#     else:
#         outputs["step6"] = json.dumps(results_dict, indent=2)

#     return outputs, results_dict

# # --- Button Logic ---
# if st.button("Generate Marketing Campaign"):
#     if not customer_domain or not project_description:
#         st.error("Please provide both inputs.")
#     else:
#         st.subheader("Generating Campaign...")
#         with st.spinner("Running CrewAI..."):
#             try:
#                 step_outputs, final_output = run_crew_ai(customer_domain, project_description)
#                 st.session_state.full_task_outputs = step_outputs
#                 st.session_state.final_consolidated_output = final_output
#                 st.rerun()
#             except Exception as e:
#                 st.error("Error occurred while generating campaign.")
#                 st.exception(e)

# # --- SVG + Outputs ---
# if st.session_state.get("full_task_outputs"):
#     st.subheader("Agent Flow Diagram (Click to View Outputs)")
#     static_descriptions_json_for_js = json.dumps({k: v[1] for k, v in static_step_descriptions.items()})

#     svg = f"""
#     <svg width="100%" height="450">
#       <style>
#         .step {{ font: 14px sans-serif; }}
#         .box {{ fill: #f0f0f0; stroke: #aaa; stroke-width: 1; rx: 5; ry: 5; cursor: pointer; }}
#         .line {{ stroke: #555; stroke-width: 1.5; marker-end: url(#arrow); }}
#         #custom-tooltip {{
#             position: absolute;
#             display: none;
#             background-color: rgba(0, 0, 0, 0.8);
#             color: white;
#             padding: 5px 10px;
#             border-radius: 5px;
#             font-size: 12px;
#             pointer-events: none;
#             z-index: 1000;
#             white-space: normal;
#             max-width: 400px;
#         }}
#       </style>
#       <defs>
#         <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
#           <path d="M0,0 L0,6 L9,3 z" fill="#555" />
#         </marker>
#       </defs>

#       <!-- SVG Boxes and Text -->
#       {''.join([
#         f'''
#         <a xlink:href="/?step={step}">
#           <rect id="{step}" x="{x}" y="{y}" width="270" height="40" class="box"/>
#         </a>
#         <text x="{x + 10}" y="{y + 25}" class="step">{label}</text>
#         '''
#         for (step, (label, _)), (x, y) in zip(static_step_descriptions.items(), [
#             (20, 20), (320, 20), (170, 90), (170, 160), (170, 230), (470, 230)
#         ])
#       ])}
#     </svg>
#     <div id="custom-tooltip"></div>
#     <script>
#         const descriptions = {static_descriptions_json_for_js};
#         const tooltip = document.getElementById('custom-tooltip');
#         document.querySelectorAll('.box').forEach(box => {{
#             box.addEventListener('mouseover', (e) => {{
#                 const id = e.target.id;
#                 const text = descriptions[id];
#                 if (text) {{
#                     tooltip.innerHTML = text;
#                     tooltip.style.display = 'block';
#                     tooltip.style.left = (e.pageX + 10) + 'px';
#                     tooltip.style.top = (e.pageY + 10) + 'px';
#                 }}
#             }});
#             box.addEventListener('mouseout', () => {{ tooltip.style.display = 'none'; }});
#         }});
#     </script>
#     """
#     components.html(svg, height=470)

#     # Display Outputs
#     st.markdown("### View Step Outputs")
#     for step_id, (label, _) in static_step_descriptions.items():
#         with st.expander(f"{label} Output"):
#             output = st.session_state.full_task_outputs.get(step_id, "No output for this step.")
#             st.code(output, language="json")

#     st.markdown("---")
#     st.header("Generated Marketing Campaign")
#     final = st.session_state.get("final_consolidated_output", {})
#     if final:
#         st.subheader("Research Summary")
#         st.markdown(final.get("research_summary", "Not available."))

#         st.subheader("Project Understanding")
#         st.markdown(final.get("project_understanding", "Not available."))

#         st.subheader("Marketing Strategy")
#         strategy = final.get("marketing_strategy", {})
#         if strategy:
#             st.markdown(f"**Name:** {strategy.get('name', '')}")
#             st.markdown("**Tactics:**")
#             for t in strategy.get("tactics", []):
#                 st.markdown(f"- {t}")
#             st.markdown("**Channels:**")
#             for c in strategy.get("channels", []):
#                 st.markdown(f"- {c}")
#             st.markdown("**KPIs:**")
#             for k in strategy.get("KPIs", []):
#                 st.markdown(f"- {k}")
#         else:
#             st.info("Strategy not found.")

#         st.markdown("---")
#         st.subheader("Creative Campaign Ideas")
#         ideas = final.get("campaign_ideas", {})
#         st.markdown(f"**Title:** {ideas.get('title', 'N/A')}")
#         for i, idea in enumerate(ideas.get("ideas", [])):
#             st.markdown(f"**Campaign {i+1}: {idea.get('name', '')}**")
#             st.markdown(f"**Description:** {idea.get('description', '')}")
#             st.markdown(f"**Audience:** {idea.get('audience', '')}")
#             st.markdown(f"**Channel:** {idea.get('channel', '')}")
#             st.markdown("---")

#         st.subheader("Marketing Copies")
#         for i, copy in enumerate(final.get("marketing_copies", [])):
#             st.markdown(f"**Copy {i+1}: {copy.get('title', '')}**")
#             st.write(copy.get("body", ""))
#             st.markdown("---")
#     else:
#         st.info("Campaign output will appear here after generation.")

# st.markdown("---")
# st.caption("Powered by CrewAI, OpenAI, Serper & Streamlit")




# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# from marketing_posts.crew import MarketingPostsCrew
# import streamlit.components.v1 as components

# # --- Load API Keys ---
# load_dotenv()
# serper_api_key = os.getenv("SERPER_API_KEY")
# openai_secret_path = "/run/secrets/openai-api-key"

# if os.path.exists(openai_secret_path):
#     with open(openai_secret_path, "r") as f:
#         openai_api_key = f.read().strip()
# else:
#     st.error("Missing OpenAI secret file.")
#     st.stop()

# os.environ["SERPER_API_KEY"] = serper_api_key or ''
# os.environ["OPENAI_API_KEY"] = openai_api_key or ''

# if not serper_api_key or not openai_api_key:
#     st.error("API keys missing. Check .env or Docker secrets.")
#     st.stop()

# # --- Static Descriptions for Each Step ---
# static_step_descriptions = {
#     "step1": ("Lead Market Analyst (Research)", "Performs domain-specific market research."),
#     "step2": ("Chief Marketing Strategist (Understanding)", "Interprets goals and research."),
#     "step3": ("Chief Marketing Strategist (Strategy)", "Creates tactical marketing strategy."),
#     "step4": ("Creative Content Creator (Campaign)", "Generates creative campaign ideas."),
#     "step5": ("Creative Content Creator (Copy)", "Writes marketing copies."),
#     "step6": ("Chief Creative Director (Consolidate)", "Consolidates all outputs for display.")
# }

# # --- Streamlit App Config ---
# st.set_page_config(layout="wide", page_title="AI Marketing Studio")
# st.title("AI Marketing Studio")
# st.markdown("---")

# query_params = st.query_params
# selected_step_id = query_params.get("step", None)

# # --- STEP DETAIL PAGE ---
# if selected_step_id:
#     if "full_task_outputs" not in st.session_state or not st.session_state.full_task_outputs:
#         st.warning("You must generate a campaign first.")
#         st.markdown("[Back to Home](/)")
#         st.stop()

#     step_label, step_desc = static_step_descriptions.get(selected_step_id, ("Unknown Step", ""))
#     st.header(step_label)
#     st.caption(step_desc)
#     st.markdown("---")
#     st.subheader("Output from this step:")
#     output = st.session_state.full_task_outputs.get(selected_step_id, "No output for this step.")
#     st.code(output, language="json")
#     st.markdown("[Back to Home](/)")
#     st.stop()

# # --- MAIN PAGE ---
# st.header("Define Your Project")
# customer_domain = st.text_input("Customer Domain", placeholder="e.g., fintech, healthcare")
# project_description = st.text_area("Project Description", height=200, placeholder="Describe your product...")

# st.markdown("---")

# # Initialize session states
# if 'full_task_outputs' not in st.session_state:
#     st.session_state.full_task_outputs = {}
#     st.session_state.final_consolidated_output = {}

# # --- Run Crew & Cache Output ---
# @st.cache_data(show_spinner=False)
# def run_crew_ai(domain, desc):
#     inputs = {"customer_domain": domain, "project_description": desc}
#     crew_result = MarketingPostsCrew().crew().kickoff(inputs=inputs)

#     results_dict = crew_result.json_dict if hasattr(crew_result, 'json_dict') else json.loads(str(crew_result))
#     outputs = {}
#     if hasattr(crew_result, 'tasks_output'):
#         for i, task_output in enumerate(crew_result.tasks_output):
#             key = f"step{i+1}"
#             if isinstance(task_output, (dict, list)):
#                 outputs[key] = json.dumps(task_output, indent=2)
#             elif hasattr(task_output, "model_dump_json"):
#                 outputs[key] = task_output.model_dump_json(indent=2)
#             else:
#                 outputs[key] = str(task_output)
#     else:
#         outputs["step6"] = json.dumps(results_dict, indent=2)

#     return outputs, results_dict

# # --- Button Logic ---
# if st.button("Generate Marketing Campaign"):
#     if not customer_domain or not project_description:
#         st.error("Please provide both inputs.")
#     else:
#         st.subheader("Generating Campaign...")
#         with st.spinner("Running CrewAI..."):
#             try:
#                 step_outputs, final_output = run_crew_ai(customer_domain, project_description)
#                 st.session_state.full_task_outputs = step_outputs
#                 st.session_state.final_consolidated_output = final_output
#                 st.rerun()
#             except Exception as e:
#                 st.error("Error occurred while generating campaign.")
#                 st.exception(e)

# # --- Storyline Visualization ---
# # --- Storyline Visualization ---
# # --- Storyline Visualization ---
# if st.session_state.get("full_task_outputs"):
#     st.subheader("🗺️ Workflow Overview")

#     st.title("Crew Agent Workflow")

#     st.graphviz_chart("""
#     digraph CrewWorkflow {
#         rankdir=TB
#         node [shape=box, style=rounded, fontname="Helvetica", fontsize=11, color=black, width=2, height=0.8]

#         // Nodes
#         Analyst [label="Lead Market Analyst\\n(Research)"]
#         Strategist [label="Chief Marketing Strategist\\n(Understanding)"]
#         Creator1 [label="Creative Content Creator\\n(Campaign Ideas)"]
#         Creator2 [label="Creative Content Creator\\n(Copywriting)"]
#         Director [label="Chief Creative Director\\n(Consolidation)"]

#         // Invisible helper nodes for text descriptions
#         desc1 [label="Performs domain-specific market research", shape=none, fontcolor=gray, fontsize=10]
#         desc2 [label="Interprets goals and research", shape=none, fontcolor=gray, fontsize=10]
#         desc3 [label="Generates creative campaign ideas", shape=none, fontcolor=gray, fontsize=10]
#         desc4 [label="Writes marketing copies", shape=none, fontcolor=gray, fontsize=10]
#         desc5 [label="Consolidates all outputs for display", shape=none, fontcolor=gray, fontsize=10]

#         // Layout edges
#         Analyst -> Strategist
#         Strategist -> Creator1
#         Strategist -> Creator2
#         Creator1 -> Director
#         Creator2 -> Director

#         // Descriptions connected to respective nodes
#         Analyst -> desc1 [style=invis]
#         Strategist -> desc2 [style=invis]
#         Creator1 -> desc3 [style=invis]
#         Creator2 -> desc4 [style=invis]
#         Director -> desc5 [style=invis]

#         {rank=same; Creator1; Creator2}
#     }
#     """, use_container_width=True)

#     st.markdown("---")

#     st.subheader("🎬 Campaign Storyline View")
#     storyline_steps = [
#         ("Scene 1: The Analyst Arrives", "step1"),
#         ("Scene 2: Strategist Understands Goals", "step2"),
#         ("Scene 3: Strategy is Designed", "step3"),
#         ("Scene 4: Campaign Ideas Flow", "step4"),
#         ("Scene 5: Words that Persuade", "step5"),
#         ("Scene 6: Everything Comes Together", "step6")
#     ]

#     for title, step_id in storyline_steps:
#         label, _ = static_step_descriptions.get(step_id, (step_id, ""))
#         with st.expander(f"{title} - {label}"):
#             output = st.session_state.full_task_outputs.get(step_id, "No output available.")
#             st.code(output, language="json")

#     st.markdown("---")

#     st.header("Final Consolidated Output")
#     final = st.session_state.get("final_consolidated_output", {})
#     if final:
#         st.subheader("Research Summary")
#         st.markdown(final.get("research_summary", "Not available."))

#         st.subheader("Project Understanding")
#         st.markdown(final.get("project_understanding", "Not available."))

#         st.subheader("Marketing Strategy")
#         strategy = final.get("marketing_strategy", {})
#         if strategy:
#             st.markdown(f"**Name:** {strategy.get('name', '')}")
#             st.markdown("**Tactics:**")
#             for t in strategy.get("tactics", []):
#                 st.markdown(f"- {t}")
#             st.markdown("**Channels:**")
#             for c in strategy.get("channels", []):
#                 st.markdown(f"- {c}")
#             st.markdown("**KPIs:**")
#             for k in strategy.get("KPIs", []):
#                 st.markdown(f"- {k}")
#         else:
#             st.info("Strategy not found.")

#         st.markdown("---")
#         st.subheader("Creative Campaign Ideas")
#         ideas = final.get("campaign_ideas", {})
#         st.markdown(f"**Title:** {ideas.get('title', 'N/A')}")
#         for i, idea in enumerate(ideas.get("ideas", [])):
#             st.markdown(f"**Campaign {i+1}: {idea.get('name', '')}**")
#             st.markdown(f"**Description:** {idea.get('description', '')}")
#             st.markdown(f"**Audience:** {idea.get('audience', '')}")
#             st.markdown(f"**Channel:** {idea.get('channel', '')}")
#             st.markdown("---")

#         st.subheader("Marketing Copies")
#         for i, copy in enumerate(final.get("marketing_copies", [])):
#             st.markdown(f"**Copy {i+1}: {copy.get('title', '')}**")
#             st.write(copy.get("body", ""))
#             st.markdown("---")
#     else:
#         st.info("Campaign output will appear here after generation.")


# st.markdown("---")
# st.caption("Powered by CrewAI, OpenAI, Serper & Streamlit")




# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# from marketing_posts.crew import MarketingPostsCrew
# import streamlit.components.v1 as components

# # --- Load API Keys ---
# load_dotenv()
# serper_api_key = os.getenv("SERPER_API_KEY")
# openai_secret_path = "/run/secrets/openai-api-key"

# if os.path.exists(openai_secret_path):
#     with open(openai_secret_path, "r") as f:
#         openai_api_key = f.read().strip()
# else:
#     st.error("Missing OpenAI secret file.")
#     st.stop()

# os.environ["SERPER_API_KEY"] = serper_api_key or ''
# os.environ["OPENAI_API_KEY"] = openai_api_key or ''

# if not serper_api_key or not openai_api_key:
#     st.error("API keys missing. Check .env or Docker secrets.")
#     st.stop()

# # --- Static Descriptions for Each Step ---
# static_step_descriptions = {
#     "step1": ("Lead Market Analyst (Research)", "Performs domain-specific market research."),
#     "step2": ("Chief Marketing Strategist (Understanding)", "Interprets goals and research."),
#     "step3": ("Chief Marketing Strategist (Strategy)", "Creates tactical marketing strategy."),
#     "step4": ("Creative Content Creator (Campaign)", "Generates creative campaign ideas."),
#     "step5": ("Creative Content Creator (Copy)", "Writes marketing copies."),
#     "step6": ("Chief Creative Director (Consolidate)", "Consolidates all outputs for display.")
# }

# # --- Streamlit App Config ---
# st.set_page_config(layout="wide", page_title="AI Marketing Studio")
# st.title("AI Marketing Studio")
# st.markdown("---")

# query_params = st.query_params
# selected_step_id = query_params.get("step", None)

# # --- STEP DETAIL PAGE ---
# if selected_step_id:
#     if "full_task_outputs" not in st.session_state or not st.session_state.full_task_outputs:
#         st.warning("You must generate a campaign first.")
#         st.markdown("[Back to Home](/)")
#         st.stop()

#     step_label, step_desc = static_step_descriptions.get(selected_step_id[0], ("Unknown Step", ""))
#     st.header(step_label)
#     st.caption(step_desc)
#     st.markdown("---")
#     st.subheader("Output from this step:")
#     output = st.session_state.full_task_outputs.get(selected_step_id[0], "No output for this step.")
#     st.code(output, language="json")
#     st.markdown("[Back to Home](/)")
#     st.stop()

# # --- MAIN PAGE ---
# st.header("Define Your Project")
# customer_domain = st.text_input("Customer Domain", placeholder="e.g., fintech, healthcare")
# project_description = st.text_area("Project Description", height=200, placeholder="Describe your product...")

# st.markdown("---")

# # Initialize session states
# if 'full_task_outputs' not in st.session_state:
#     st.session_state.full_task_outputs = {}
#     st.session_state.final_consolidated_output = {}

# # --- Run Crew & Cache Output ---
# @st.cache_data(show_spinner=False)
# def run_crew_ai(domain, desc):
#     inputs = {"customer_domain": domain, "project_description": desc}
#     crew_result = MarketingPostsCrew().crew().kickoff(inputs=inputs)

#     results_dict = crew_result.json_dict if hasattr(crew_result, 'json_dict') else json.loads(str(crew_result))
#     outputs = {}
#     if hasattr(crew_result, 'tasks_output'):
#         for i, task_output in enumerate(crew_result.tasks_output):
#             key = f"step{i+1}"
#             if isinstance(task_output, (dict, list)):
#                 outputs[key] = json.dumps(task_output, indent=2)
#             elif hasattr(task_output, "model_dump_json"):
#                 outputs[key] = task_output.model_dump_json(indent=2)
#             else:
#                 outputs[key] = str(task_output)
#     else:
#         outputs["step6"] = json.dumps(results_dict, indent=2)

#     return outputs, results_dict

# # --- Button Logic ---
# if st.button("Generate Marketing Campaign"):
#     if not customer_domain or not project_description:
#         st.error("Please provide both inputs.")
#     else:
#         st.subheader("Generating Campaign…")
#         with st.spinner("Running CrewAI…"):
#             try:
#                 step_outputs, final_output = run_crew_ai(customer_domain, project_description)
#                 st.session_state.full_task_outputs = step_outputs
#                 st.session_state.final_consolidated_output = final_output
#                 st.rerun()
#             except Exception as e:
#                 st.error("Error occurred while generating campaign.")
#                 st.exception(e)

# # --- Storyline Visualization ---
# if st.session_state.get("full_task_outputs"):
#     st.subheader("🗺️ Workflow Overview")
#     st.title("Crew Agent Workflow")

#     st.graphviz_chart("""
#     digraph CrewWorkflow {
#         rankdir=TB
#         node [shape=box, style=rounded, fontname="Helvetica", fontsize=11, color=black, width=2, height=0.8]
#         Analyst [label="Lead Market Analyst\\n(Research)"]
#         Strategist [label="Chief Marketing Strategist\\n(Understanding)"]
#         Creator1 [label="Creative Content Creator\\n(Campaign Ideas)"]
#         Creator2 [label="Creative Content Creator\\n(Copywriting)"]
#         Director [label="Chief Creative Director\\n(Consolidation)"]
#         Analyst -> Strategist
#         Strategist -> Creator1
#         Strategist -> Creator2
#         Creator1 -> Director
#         Creator2 -> Director
#     }
#     """, use_container_width=True)

#     st.markdown("---")
#     st.subheader("🎬 Campaign Storyline View")
#     storyline_steps = [
#         ("Scene 1: The Analyst Arrives", "step1"),
#         ("Scene 2: Strategist Understands Goals", "step2"),
#         ("Scene 3: Strategy is Designed", "step3"),
#         ("Scene 4: Campaign Ideas Flow", "step4"),
#         ("Scene 5: Words that Persuade", "step5"),
#         ("Scene 6: Everything Comes Together", "step6")
#     ]

#     for title, step_id in storyline_steps:
#         label, _ = static_step_descriptions.get(step_id, (step_id, ""))
#         with st.expander(f"{title} - {label}"):
#             output = st.session_state.full_task_outputs.get(step_id, "No output available.")
#             st.code(output, language="json")

#     # --- Agent-wise Grouped Output ---
#     st.markdown("---")
#     st.header("📦 Agent‑wise Final Output")

#     final = st.session_state.final_consolidated_output or {}

#     with st.expander("👨‍💼 Lead Market Analyst"):
#         out1 = st.session_state.full_task_outputs.get("step1")
#         if out1:
#             st.subheader("Step 1 Output (Research)")
#             st.code(out1, language="json")
#         st.subheader("Research Summary")
#         st.markdown(final.get("research_summary", "Not available."))

#     with st.expander("👩‍💼 Chief Marketing Strategist"):
#         out2 = st.session_state.full_task_outputs.get("step2")
#         if out2:
#             st.subheader("Step 2 Output (Understanding)")
#             st.code(out2, language="json")
#         st.subheader("Project Understanding")
#         st.markdown(final.get("project_understanding", "Not available."))
#         out3 = st.session_state.full_task_outputs.get("step3")
#         if out3:
#             st.subheader("Step 3 Output (Strategy)")
#             st.code(out3, language="json")
#         strat = final.get("marketing_strategy", {})
#         st.subheader("Marketing Strategy")
#         if strat:
#             st.markdown(f"**Name:** {strat.get('name', '')}")
#             for heading, items in [("Tactics", strat.get("tactics", [])),
#                                    ("Channels", strat.get("channels", [])),
#                                    ("KPIs", strat.get("KPIs", []))]:
#                 st.markdown(f"**{heading}:**")
#                 for item in items:
#                     st.markdown(f"- {item}")

#     with st.expander("✍️ Creative Content Creator"):
#         out4 = st.session_state.full_task_outputs.get("step4")
#         if out4:
#             st.subheader("Step 4 Output (Campaign Ideas)")
#             st.code(out4, language="json")
#         ci = final.get("campaign_ideas", {})
#         st.subheader("Final Campaign Ideas")
#         st.markdown(f"**Title:** {ci.get('title', '')}")
#         for idea in ci.get("ideas", []):
#             st.markdown(f"**{idea.get('name', '')}:** {idea.get('description', '')}")
#         out5 = st.session_state.full_task_outputs.get("step5")
#         if out5:
#             st.subheader("Step 5 Output (Copies)")
#             st.code(out5, language="json")
#         st.subheader("Final Marketing Copies")
#         for copy in final.get("marketing_copies", []):
#             st.markdown(f"**{copy.get('title', '')}**")
#             st.write(copy.get("body", ""))

#     with st.expander("🎬 Chief Creative Director"):
#         out6 = st.session_state.full_task_outputs.get("step6")
#         if out6:
#             st.subheader("Step 6 Output (Consolidation)")
#             st.code(out6, language="json")
#         st.subheader("Final Consolidated Output (JSON)")
#         st.code(json.dumps(final, indent=2), language="json")

# st.markdown("---")
# st.caption("Powered by CrewAI, OpenAI, Serper & Streamlit")






# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# from marketing_posts.crew import MarketingPostsCrew
# import streamlit.components.v1 as components

# # --- Load API Keys ---
# load_dotenv()
# serper_api_key = os.getenv("SERPER_API_KEY")
# openai_secret_path = "/run/secrets/openai-api-key"

# if os.path.exists(openai_secret_path):
#     with open(openai_secret_path, "r") as f:
#         openai_api_key = f.read().strip()
# else:
#     st.error("Missing OpenAI secret file.")
#     st.stop()

# os.environ["SERPER_API_KEY"] = serper_api_key or ''
# os.environ["OPENAI_API_KEY"] = openai_api_key or ''

# if not serper_api_key or not openai_api_key:
#     st.error("API keys missing. Check .env or Docker secrets.")
#     st.stop()

# # --- Static Descriptions for Each Step ---
# static_step_descriptions = {
#     "step1": ("Lead Market Analyst (Research)", "Performs domain-specific market research."),
#     "step2": ("Chief Marketing Strategist (Understanding)", "Interprets goals and research."),
#     "step3": ("Chief Marketing Strategist (Strategy)", "Creates tactical marketing strategy."),
#     "step4": ("Creative Content Creator (Campaign)", "Generates creative campaign ideas."),
#     "step5": ("Creative Content Creator (Copy)", "Writes marketing copies."),
#     "step6": ("Chief Creative Director (Consolidate)", "Consolidates all outputs for display.")
# }

# # --- Streamlit App Config ---
# st.set_page_config(layout="wide", page_title="AI Marketing Studio")
# st.title("AI Marketing Studio")
# st.markdown("---")

# query_params = st.query_params
# selected_step_id = query_params.get("step", None)

# # --- STEP DETAIL PAGE ---
# if selected_step_id:
#     if "full_task_outputs" not in st.session_state or not st.session_state.full_task_outputs:
#         st.warning("You must generate a campaign first.")
#         st.markdown("[Back to Home](/)")
#         st.stop()

#     step_label, step_desc = static_step_descriptions.get(selected_step_id[0], ("Unknown Step", ""))
#     st.header(step_label)
#     st.caption(step_desc)
#     st.markdown("---")
#     st.subheader("Output from this step:")
#     output = st.session_state.full_task_outputs.get(selected_step_id[0], "No output for this step.")
#     st.code(output, language="json")
#     st.markdown("[Back to Home](/)")
#     st.stop()

# # --- MAIN PAGE ---
# st.header("Define Your Project")
# customer_domain = st.text_input("Customer Domain", placeholder="e.g., fintech, healthcare")
# project_description = st.text_area("Project Description", height=200, placeholder="Describe your product...")
# st.markdown("---")

# # Initialize session states
# if 'full_task_outputs' not in st.session_state:
#     st.session_state.full_task_outputs = {}
#     st.session_state.final_consolidated_output = {}

# # --- Run Crew & Cache Output ---
# @st.cache_data(show_spinner=False)
# def run_crew_ai(domain, desc):
#     inputs = {"customer_domain": domain, "project_description": desc}
#     crew_result = MarketingPostsCrew().crew().kickoff(inputs=inputs)
#     results_dict = crew_result.json_dict if hasattr(crew_result, 'json_dict') else json.loads(str(crew_result))
#     outputs = {}
#     if hasattr(crew_result, 'tasks_output'):
#         for i, task_output in enumerate(crew_result.tasks_output):
#             key = f"step{i+1}"
#             if isinstance(task_output, (dict, list)):
#                 outputs[key] = json.dumps(task_output, indent=2)
#             elif hasattr(task_output, "model_dump_json"):
#                 outputs[key] = task_output.model_dump_json(indent=2)
#             else:
#                 outputs[key] = str(task_output)
#     else:
#         outputs["step6"] = json.dumps(results_dict, indent=2)
#     return outputs, results_dict

# # --- Button Logic ---
# if st.button("Generate Marketing Campaign"):
#     if not customer_domain or not project_description:
#         st.error("Please provide both inputs.")
#     else:
#         st.subheader("Generating Campaign…")
#         with st.spinner("Running CrewAI…"):
#             try:
#                 step_outputs, final_output = run_crew_ai(customer_domain, project_description)
#                 st.session_state.full_task_outputs = step_outputs
#                 st.session_state.final_consolidated_output = final_output
#                 st.rerun()
#             except Exception as e:
#                 st.error("Error occurred while generating campaign.")
#                 st.exception(e)

# # --- Agent-wise Grouped Output ---
# if st.session_state.get("full_task_outputs"):
#     st.markdown("---")
#     st.header("📦 Agent‑wise Final Output")
#     final = st.session_state.final_consolidated_output or {}

#     with st.expander("👨‍💼 Lead Market Analyst"):
#         out1 = st.session_state.full_task_outputs.get("step1")
#         if out1:
#             st.subheader("Step 1 Output (Research)")
#             st.code(out1, language="json")
#         st.subheader("Research Summary")
#         st.markdown(final.get("research_summary", "Not available."))

#     with st.expander("👩‍💼 Chief Marketing Strategist"):
#         out2 = st.session_state.full_task_outputs.get("step2")
#         if out2:
#             st.subheader("Step 2 Output (Understanding)")
#             st.code(out2, language="json")
#         st.subheader("Project Understanding")
#         st.markdown(final.get("project_understanding", "Not available."))
#         out3 = st.session_state.full_task_outputs.get("step3")
#         if out3:
#             st.subheader("Step 3 Output (Strategy)")
#             st.code(out3, language="json")
#         strat = final.get("marketing_strategy", {})
#         st.subheader("Marketing Strategy")
#         if strat:
#             st.markdown(f"**Name:** {strat.get('name', '')}")
#             for heading, items in [("Tactics", strat.get("tactics", [])),
#                                    ("Channels", strat.get("channels", [])),
#                                    ("KPIs", strat.get("KPIs", []))]:
#                 st.markdown(f"**{heading}:**")
#                 for item in items:
#                     st.markdown(f"- {item}")

#     with st.expander("✍️ Creative Content Creator"):
#         out4 = st.session_state.full_task_outputs.get("step4")
#         if out4:
#             st.subheader("Step 4 Output (Campaign Ideas)")
#             st.code(out4, language="json")
#         ci = final.get("campaign_ideas", {})
#         st.subheader("Final Campaign Ideas")
#         st.markdown(f"**Title:** {ci.get('title', '')}")
#         for idea in ci.get("ideas", []):
#             st.markdown(f"**{idea.get('name', '')}:** {idea.get('description', '')}")
#         out5 = st.session_state.full_task_outputs.get("step5")
#         if out5:
#             st.subheader("Step 5 Output (Copies)")
#             st.code(out5, language="json")
#         st.subheader("Final Marketing Copies")
#         for copy in final.get("marketing_copies", []):
#             st.markdown(f"**{copy.get('title', '')}**")
#             st.write(copy.get("body", ""))

#     with st.expander("🎬 Chief Creative Director"):
#         final_text_output = final.get("final_consolidation_output")
#         if final_text_output:
#             st.subheader("✅ Final Creative Content")
#             st.markdown(final_text_output)
#         else:
#             out6 = st.session_state.full_task_outputs.get("step6")
#             if out6:
#                 st.subheader("Step 6 Output (Consolidation)")
#                 st.code(out6, language="json")
#             st.subheader("Final Consolidated Output (JSON)")
#             st.code(json.dumps(final, indent=2), language="json")

# st.markdown("---")
# st.caption("Powered by CrewAI, OpenAI, Serper & Streamlit")


# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# from marketing_posts.crew import MarketingPostsCrew
# import streamlit.components.v1 as components

# # --- Load API Keys ---
# load_dotenv()
# serper_api_key = os.getenv("SERPER_API_KEY")
# openai_secret_path = "/run/secrets/openai-api-key"

# if os.path.exists(openai_secret_path):
#     with open(openai_secret_path, "r") as f:
#         openai_api_key = f.read().strip()
# else:
#     st.error("Missing OpenAI secret file.")
#     st.stop()

# os.environ["SERPER_API_KEY"] = serper_api_key or ''
# os.environ["OPENAI_API_KEY"] = openai_api_key or ''

# if not serper_api_key or not openai_api_key:
#     st.error("API keys missing. Check .env or Docker secrets.")
#     st.stop()

# # --- Static Descriptions for Each Step ---
# static_step_descriptions = {
#     "step1": ("Lead Market Analyst (Research)", "Performs domain-specific market research."),
#     "step2": ("Chief Marketing Strategist (Understanding)", "Interprets goals and research."),
#     "step3": ("Chief Marketing Strategist (Strategy)", "Creates tactical marketing strategy."),
#     "step4": ("Creative Content Creator (Campaign)", "Generates creative campaign ideas."),
#     "step5": ("Creative Content Creator (Copy)", "Writes marketing copies."),
#     "step6": ("Chief Creative Director (Consolidate)", "Consolidates all outputs for display.")
# }

# # --- Streamlit App Config ---
# st.set_page_config(layout="wide", page_title="AI Marketing Studio")
# st.title("AI Marketing Studio")
# st.markdown("---")

# query_params = st.query_params
# selected_step_id = query_params.get("step", None)

# # --- STEP DETAIL PAGE ---
# if selected_step_id:
#     if "full_task_outputs" not in st.session_state or not st.session_state.full_task_outputs:
#         st.warning("You must generate a campaign first.")
#         st.markdown("[Back to Home](/)")
#         st.stop()

#     step_label, step_desc = static_step_descriptions.get(selected_step_id[0], ("Unknown Step", ""))
#     st.header(step_label)
#     st.caption(step_desc)
#     st.markdown("---")
#     st.subheader("Output from this step:")
#     output = st.session_state.full_task_outputs.get(selected_step_id[0], "No output for this step.")
#     st.code(output, language="json")
#     st.markdown("[Back to Home](/)")
#     st.stop()

# # --- MAIN PAGE ---
# st.header("Define Your Project")
# customer_domain = st.text_input("Customer Domain", placeholder="e.g., fintech, healthcare")
# project_description = st.text_area("Project Description", height=200, placeholder="Describe your product...")
# st.markdown("---")

# # Initialize session states
# if 'full_task_outputs' not in st.session_state:
#     st.session_state.full_task_outputs = {}
#     st.session_state.final_consolidated_output = {}

# # --- Run Crew & Cache Output ---
# @st.cache_data(show_spinner=False)
# def run_crew_ai(domain, desc):
#     inputs = {"customer_domain": domain, "project_description": desc}
#     crew_result = MarketingPostsCrew().crew().kickoff(inputs=inputs)
#     results_dict = crew_result.json_dict if hasattr(crew_result, 'json_dict') else json.loads(str(crew_result))
#     outputs = {}
#     if hasattr(crew_result, 'tasks_output'):
#         for i, task_output in enumerate(crew_result.tasks_output):
#             key = f"step{i+1}"
#             if isinstance(task_output, (dict, list)):
#                 outputs[key] = json.dumps(task_output, indent=2)
#             elif hasattr(task_output, "model_dump_json"):
#                 outputs[key] = task_output.model_dump_json(indent=2)
#             else:
#                 outputs[key] = str(task_output)
#     else:
#         outputs["step6"] = json.dumps(results_dict, indent=2)
#     return outputs, results_dict

# # --- Button Logic ---
# if st.button("Generate Marketing Campaign"):
#     if not customer_domain or not project_description:
#         st.error("Please provide both inputs.")
#     else:
#         st.subheader("Generating Campaign…")
#         with st.spinner("Running CrewAI…"):
#             try:
#                 step_outputs, final_output = run_crew_ai(customer_domain, project_description)
#                 st.session_state.full_task_outputs = step_outputs
#                 st.session_state.final_consolidated_output = final_output
#                 st.rerun()
#             except Exception as e:
#                 st.error("Error occurred while generating campaign.")
#                 st.exception(e)

# # --- Agent-wise Grouped Output ---
# if st.session_state.get("full_task_outputs"):
#     st.markdown("---")
#     st.header("📦 Agent‑wise Final Output")
#     final = st.session_state.final_consolidated_output or {}

#     with st.expander("👨‍💼 Lead Market Analyst"):
#         out1 = st.session_state.full_task_outputs.get("step1")
#         if out1:
#             st.subheader("Step 1 Output (Research)")
#             st.code(out1, language="json")
#         st.subheader("Research Summary")
#         st.markdown(final.get("research_summary", "Not available."))

#     with st.expander("👩‍💼 Chief Marketing Strategist"):
#         out2 = st.session_state.full_task_outputs.get("step2")
#         if out2:
#             st.subheader("Step 2 Output (Understanding)")
#             st.code(out2, language="json")
#         st.subheader("Project Understanding")
#         st.markdown(final.get("project_understanding", "Not available."))
#         out3 = st.session_state.full_task_outputs.get("step3")
#         if out3:
#             st.subheader("Step 3 Output (Strategy)")
#             st.code(out3, language="json")
#         strat = final.get("marketing_strategy", {})
#         st.subheader("Marketing Strategy")
#         if strat:
#             st.markdown(f"**Name:** {strat.get('name', '')}")
#             for heading, items in [("Tactics", strat.get("tactics", [])),
#                                    ("Channels", strat.get("channels", [])),
#                                    ("KPIs", strat.get("KPIs", []))]:
#                 st.markdown(f"**{heading}:**")
#                 for item in items:
#                     st.markdown(f"- {item}")

#     with st.expander("✍️ Creative Content Creator"):
#         out4 = st.session_state.full_task_outputs.get("step4")
#         if out4:
#             st.subheader("Step 4 Output (Campaign Ideas)")
#             st.code(out4, language="json")
#         ci = final.get("campaign_ideas", {})
#         st.subheader("Final Campaign Ideas")
#         st.markdown(f"**Title:** {ci.get('title', '')}")
#         for idea in ci.get("ideas", []):
#             st.markdown(f"**{idea.get('name', '')}:** {idea.get('description', '')}")
#         out5 = st.session_state.full_task_outputs.get("step5")
#         if out5:
#             st.subheader("Step 5 Output (Copies)")
#             st.code(out5, language="json")
#         st.subheader("Final Marketing Copies")
#         for copy in final.get("marketing_copies", []):
#             st.markdown(f"**{copy.get('title', '')}**")
#             st.write(copy.get("body", ""))

#     with st.expander("🎬 Chief Creative Director"):
#         final = st.session_state.final_consolidated_output or {}

#         st.subheader("✅ Final Creative Content")

#         # Research Summary
#         st.markdown("### 🧪 Research Summary")
#         st.markdown(final.get("research_summary", "Not available."))

#         # Project Understanding
#         st.markdown("### 🧠 Project Understanding")
#         st.markdown(final.get("project_understanding", "Not available."))

#         # Marketing Strategy
#         strategy = final.get("marketing_strategy", {})
#         if strategy:
#             st.markdown("### 📊 Marketing Strategy")
#             st.markdown(f"**Name:** {strategy.get('name', '')}")

#             st.markdown("**Tactics:**")
#             for tactic in strategy.get("tactics", []):
#                 st.markdown(f"- {tactic}")

#             st.markdown("**Channels:**")
#             for channel in strategy.get("channels", []):
#                 st.markdown(f"- {channel}")

#             st.markdown("**KPIs:**")
#             for kpi in strategy.get("KPIs", []):
#                 st.markdown(f"- {kpi}")

#         # Campaign Ideas
#         campaign = final.get("campaign_ideas", {})
#         if campaign:
#             st.markdown("### 🎯 Campaign Ideas")
#             st.markdown(f"**Title:** {campaign.get('title', '')}")
#             for idea in campaign.get("ideas", []):
#                 st.markdown(f"#### {idea.get('name', '')}")
#                 st.markdown(f"- **Description:** {idea.get('description', '')}")
#                 st.markdown(f"- **Audience:** {idea.get('audience', '')}")
#                 st.markdown(f"- **Channel:** {idea.get('channel', '')}")

#         # Marketing Copies
#         copies = final.get("marketing_copies", [])
#         if copies:
#             st.markdown("### ✍️ Marketing Copies")
#             for copy in copies:
#                 st.markdown(f"#### {copy.get('title', '')}")
#                 st.markdown(copy.get("body", ""))

# st.markdown("---")
# st.caption("Powered by CrewAI, OpenAI, Serper & Streamlit")




import streamlit as st
import os
import json
from dotenv import load_dotenv
from marketing_posts.crew import MarketingPostsCrew

# --- Load API Keys ---
load_dotenv()
serper_api_key = os.getenv("SERPER_API_KEY")
openai_secret_path = "/run/secrets/openai-api-key"

if os.path.exists(openai_secret_path):
    with open(openai_secret_path, "r") as f:
        openai_api_key = f.read().strip()
else:
    st.error("Missing OpenAI secret file.")
    st.stop()

os.environ["SERPER_API_KEY"] = serper_api_key or ''
os.environ["OPENAI_API_KEY"] = openai_api_key or ''

if not serper_api_key or not openai_api_key:
    st.error("API keys missing. Check .env or Docker secrets.")
    st.stop()

# --- Streamlit App Config ---
st.set_page_config(layout="wide", page_title="AI Marketing Studio")
st.title("AI Marketing Studio")
st.markdown("---")

# Project input
customer_domain = st.text_input("🌐 Project Domain (e.g., fintech)")
project_description = st.text_area("📝 Project Description", height=150)

if 'full_task_outputs' not in st.session_state:
    st.session_state.full_task_outputs = {}
    st.session_state.final_consolidated_output = {}

# --- Run CrewAI ---
@st.cache_data(show_spinner=False)
def run_crew_ai(domain, desc):
    inputs = {"customer_domain": domain, "project_description": desc}
    crew_result = MarketingPostsCrew().crew().kickoff(inputs=inputs)
    results_dict = crew_result.json_dict if hasattr(crew_result, 'json_dict') else json.loads(str(crew_result))
    outputs = {}
    if hasattr(crew_result, 'tasks_output'):
        for i, task_output in enumerate(crew_result.tasks_output):
            key = f"step{i+1}"
            if isinstance(task_output, (dict, list)):
                outputs[key] = json.dumps(task_output, indent=2)
            elif hasattr(task_output, "model_dump_json"):
                outputs[key] = task_output.model_dump_json(indent=2)
            else:
                outputs[key] = str(task_output)
    else:
        outputs["step6"] = json.dumps(results_dict, indent=2)
    return outputs, results_dict

# --- Button ---
if st.button("🚀 Generate Campaign"):
    if not customer_domain or not project_description:
        st.error("Please provide both domain and description.")
    else:
        with st.spinner("Running CrewAI Agents..."):
            try:
                step_outputs, final_output = run_crew_ai(customer_domain, project_description)
                st.session_state.full_task_outputs = step_outputs
                st.session_state.final_consolidated_output = final_output
                st.rerun()
            except Exception as e:
                st.error("Something went wrong.")
                st.exception(e)

# --- Final Output Display ---
if st.session_state.get("final_consolidated_output"):
    final = st.session_state["final_consolidated_output"]
    st.markdown("---")
    st.header("📦 Agent‑wise Final Output")

    # Step 1: Lead Market Analyst
    with st.expander("👨‍💼 Lead Market Analyst"):
        out1 = st.session_state.full_task_outputs.get("step1")
        text1 = final.get("research_summary", "Not available.")
        with st.expander("JSON Output"):
            if out1:
                st.code(out1, language="json")
            else:
                st.write("No JSON output available.")
        with st.expander("Text Output"):
            st.markdown(text1)

    # Step 2: Chief Marketing Strategist
    with st.expander("👩‍💼 Chief Marketing Strategist"):
        out2 = st.session_state.full_task_outputs.get("step2")
        text2 = final.get("project_understanding", "Not available.")
        with st.expander("JSON Output"):
            if out2:
                st.code(out2, language="json")
            else:
                st.write("No JSON output available.")
        with st.expander("Text Output"):
            st.markdown(text2)

        out3 = st.session_state.full_task_outputs.get("step3")
        text3 = final.get("marketing_strategy", {})
        with st.expander("Step 3 Output (Strategy) - JSON Output"):
            if out3:
                st.code(out3, language="json")
            else:
                st.write("No JSON output available.")
        with st.expander("Step 3 Output (Strategy) - Text Output"):
            if text3:
                st.markdown(f"**Name:** {text3.get('name', '')}")
                st.markdown("**KPIs:**")
                for kpi in text3.get("KPIs", []):
                    st.markdown(f"- {kpi}")

                if text3.get("tactic_channel_pairs"):
                    st.markdown("#### Tactic → Channel → Why This Fits")
                    for pair in text3["tactic_channel_pairs"]:
                        st.markdown(f"- **{pair['tactic']}** → **{pair['channel']}**")
                        st.markdown(f"  • _Why_: {pair['rationale']}")
            else:
                st.write("No text output available.")

    # Step 4: Creative Content Creator (No changes here)
    with st.expander("✍️ Creative Content Creator"):
        out4 = st.session_state.full_task_outputs.get("step4")
        if out4:
            st.subheader("Step 4 Output (Campaign Ideas)")
            st.code(out4, language="json")

        ci = final.get("campaign_ideas", {})
        st.subheader("Final Campaign Ideas")
        if ci:
            st.markdown(f"**Title:** {ci.get('title', '')}")
            for idea in ci.get("ideas", []):
                st.markdown(f"#### {idea.get('name', '')}")
                st.markdown(f"- **Description:** {idea.get('description', '')}")
                st.markdown(f"- **Audience:** {idea.get('audience', '')}")
                st.markdown(f"- **Channel:** {idea.get('channel', '')}")
                if "tactic_used" in idea:
                    st.markdown(f"- **Tactic Used:** {idea['tactic_used']}")
                if "channel_fit" in idea:
                    st.markdown(f"- **Why this channel fits:** {idea['channel_fit']}")

        out5 = st.session_state.full_task_outputs.get("step5")
        if out5:
            st.subheader("Step 5 Output (Copies)")
            st.code(out5, language="json")

        st.subheader("Final Marketing Copies")
        for copy in final.get("marketing_copies", []):
            st.markdown(f"**{copy.get('title', '')}**")
            st.write(copy.get("body", ""))

        if final.get("refined_marketing_copies"):
            st.subheader("🏁 Refined Marketing Copies")
            for c in final["refined_marketing_copies"]:
                st.markdown(f"#### {c['title']}")
                st.markdown(c['body'])

    # ... rest of your code unchanged


    with st.expander("🎬 Chief Creative Director"):
        st.subheader("✅ Final Creative Content")

        st.markdown("### 🧪 Research Summary")
        st.markdown(final.get("research_summary", "Not available."))

        st.markdown("### 🧠 Project Understanding")
        st.markdown(final.get("project_understanding", "Not available."))

        strategy = final.get("marketing_strategy", {})
        if strategy:
            st.markdown("### 📊 Marketing Strategy")
            st.markdown(f"**Name:** {strategy.get('name', '')}")
            st.markdown("**KPIs:**")
            for kpi in strategy.get("KPIs", []):
                st.markdown(f"- {kpi}")

            if strategy.get("tactic_channel_pairs"):
                st.markdown("#### Tactic ↔ Channel ↔ Justification")
                for pair in strategy["tactic_channel_pairs"]:
                    st.markdown(f"- **{pair['tactic']}** → **{pair['channel']}**")
                    st.markdown(f"  • _Why_: {pair['rationale']}")

        campaign = final.get("campaign_ideas", {})
        if campaign:
            st.markdown("### 🎯 Campaign Ideas")
            st.markdown(f"**Title:** {campaign.get('title', '')}")
            for idea in campaign.get("ideas", []):
                st.markdown(f"#### {idea.get('name', '')}")
                st.markdown(f"- **Description:** {idea.get('description', '')}")
                st.markdown(f"- **Audience:** {idea.get('audience', '')}")
                st.markdown(f"- **Channel:** {idea.get('channel', '')}")
                if "tactic_used" in idea:
                    st.markdown(f"- **Tactic Used:** {idea['tactic_used']}")
                if "channel_fit" in idea:
                    st.markdown(f"- **Why this channel fits:** {idea['channel_fit']}")

        copies = final.get("marketing_copies", [])
        if copies:
            st.markdown("### ✍️ Marketing Copies")
            for copy in copies:
                st.markdown(f"#### {copy.get('title', '')}")
                st.markdown(copy.get("body", ""))

        refined = final.get("refined_marketing_copies", [])
        if refined:
            st.markdown("### 🏁 Refined Marketing Copies")
            for c in refined:
                st.markdown(f"#### {c['title']}")
                st.markdown(c['body'])

        competitors = final.get("competitor_analysis")
        if competitors:
            st.markdown("### 🕵️ Competitor Analysis")
            st.markdown(competitors)

    

from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# PDF Generator for Chief Creative Director section only
def generate_director_pdf(final):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=18)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='CustomHeading1', fontSize=18, leading=22, spaceAfter=14))
    styles.add(ParagraphStyle(name='CustomHeading2', fontSize=14, leading=18, spaceAfter=10))
    styles.add(ParagraphStyle(name='CustomBodyText', fontSize=11, leading=14))

    elements = []

    def add_section(title, content):
        elements.append(Paragraph(title, styles['CustomHeading1']))
        if isinstance(content, list):
            for item in content:
                if isinstance(item, dict):
                    for k, v in item.items():
                        elements.append(Paragraph(f"<b>{k}:</b> {v}", styles['CustomBodyText']))
                    elements.append(Spacer(1, 6))
                else:
                    elements.append(Paragraph(str(item), styles['CustomBodyText']))
        elif isinstance(content, dict):
            for k, v in content.items():
                if isinstance(v, list):
                    elements.append(Paragraph(f"<b>{k}:</b>", styles['CustomHeading2']))
                    for i in v:
                        elements.append(Paragraph(str(i), styles['CustomBodyText']))
                else:
                    elements.append(Paragraph(f"<b>{k}:</b> {v}", styles['CustomBodyText']))
        elif isinstance(content, str):
            elements.append(Paragraph(content.replace('\n', '<br />'), styles['CustomBodyText']))
        elements.append(Spacer(1, 12))

    add_section("🧪 Research Summary", final.get("research_summary"))
    add_section("🧠 Project Understanding", final.get("project_understanding"))

    strategy = final.get("marketing_strategy", {})
    if strategy:
        elements.append(Paragraph("📊 Marketing Strategy", styles['CustomHeading1']))
        elements.append(Paragraph(f"<b>Name:</b> {strategy.get('name', '')}", styles['CustomBodyText']))
        elements.append(Paragraph("<b>KPIs:</b>", styles['CustomHeading2']))
        for kpi in strategy.get("KPIs", []):
            elements.append(Paragraph(f"- {kpi}", styles['CustomBodyText']))
        elements.append(Paragraph("<b>Tactic → Channel → Why:</b>", styles['CustomHeading2']))
        for pair in strategy.get("tactic_channel_pairs", []):
            elements.append(Paragraph(f"• {pair['tactic']} → {pair['channel']}<br/><i>Why:</i> {pair['rationale']}", styles['CustomBodyText']))
        elements.append(Spacer(1, 12))

    campaign = final.get("campaign_ideas", {})
    if campaign:
        elements.append(Paragraph("🎯 Campaign Ideas", styles['CustomHeading1']))
        elements.append(Paragraph(f"<b>Title:</b> {campaign.get('title', '')}", styles['CustomBodyText']))
        for idea in campaign.get("ideas", []):
            elements.append(Paragraph(f"<b>{idea.get('name', '')}</b>", styles['CustomHeading2']))
            elements.append(Paragraph(f"- Description: {idea.get('description', '')}", styles['CustomBodyText']))
            elements.append(Paragraph(f"- Audience: {idea.get('audience', '')}", styles['CustomBodyText']))
            elements.append(Paragraph(f"- Channel: {idea.get('channel', '')}", styles['CustomBodyText']))
            if "tactic_used" in idea:
                elements.append(Paragraph(f"- Tactic Used: {idea['tactic_used']}", styles['CustomBodyText']))
            if "channel_fit" in idea:
                elements.append(Paragraph(f"- Channel Fit: {idea['channel_fit']}", styles['CustomBodyText']))
            elements.append(Spacer(1, 6))

    copies = final.get("marketing_copies", [])
    if copies:
        elements.append(Paragraph("✍️ Marketing Copies", styles['CustomHeading1']))
        for copy in copies:
            elements.append(Paragraph(f"{copy.get('title', '')}", styles['CustomHeading2']))
            elements.append(Paragraph(copy.get("body", ""), styles['CustomBodyText']))

    refined = final.get("refined_marketing_copies", [])
    if refined:
        elements.append(Paragraph("🏁 Refined Marketing Copies", styles['CustomHeading1']))
        for c in refined:
            elements.append(Paragraph(c['title'], styles['CustomHeading2']))
            elements.append(Paragraph(c['body'], styles['CustomBodyText']))

    competitors = final.get("competitor_analysis")
    if competitors:
        elements.append(Paragraph("🕵️ Competitor Analysis", styles['CustomHeading1']))
        elements.append(Paragraph(competitors.replace('\n', '<br />'), styles['CustomBodyText']))

    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf

# -- Show PDF Download Button (only if final is present) --
if st.session_state.get("final_consolidated_output"):
    pdf = generate_director_pdf(st.session_state["final_consolidated_output"])
    st.download_button(
        label="📥 Download Final Report (Chief Creative Director PDF)",
        data=pdf,
        file_name="final_creative_director_report.pdf",
        mime="application/pdf"
    )



# --- Footer ---
st.markdown("---")
st.caption("Powered by CrewAI, OpenAI, Serper & Streamlit")






# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# from marketing_posts.crew import MarketingPostsCrew
# from io import BytesIO
# from reportlab.lib.pagesizes import letter
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# # --- Load API Keys ---
# load_dotenv()
# serper_api_key = os.getenv("SERPER_API_KEY")
# openai_secret_path = "/run/secrets/openai-api-key"

# if os.path.exists(openai_secret_path):
#     with open(openai_secret_path, "r") as f:
#         openai_api_key = f.read().strip()
# else:
#     st.error("Missing OpenAI secret file.")
#     st.stop()

# os.environ["SERPER_API_KEY"] = serper_api_key or ''
# os.environ["OPENAI_API_KEY"] = openai_api_key or ''

# if not serper_api_key or not openai_api_key:
#     st.error("API keys missing. Check .env or Docker secrets.")
#     st.stop()

# # --- Streamlit App Config ---
# st.set_page_config(layout="wide", page_title="AI Marketing Studio")
# st.title("AI Marketing Studio")
# st.markdown("---")

# # Project input
# customer_domain = st.text_input("🌐 Project Domain (e.g., fintech)")
# project_description = st.text_area("📝 Project Description", height=150)

# if 'full_task_outputs' not in st.session_state:
#     st.session_state.full_task_outputs = {}
#     st.session_state.final_consolidated_output = {}

# # --- Run CrewAI ---
# @st.cache_data(show_spinner=False)
# def run_crew_ai(domain, desc):
#     inputs = {"customer_domain": domain, "project_description": desc}
#     crew_result = MarketingPostsCrew().crew().kickoff(inputs=inputs)
#     results_dict = crew_result.json_dict if hasattr(crew_result, 'json_dict') else json.loads(str(crew_result))
#     outputs = {}
#     if hasattr(crew_result, 'tasks_output'):
#         for i, task_output in enumerate(crew_result.tasks_output):
#             key = f"step{i+1}"
#             if isinstance(task_output, (dict, list)):
#                 outputs[key] = json.dumps(task_output, indent=2)
#             elif hasattr(task_output, "model_dump_json"):
#                 outputs[key] = task_output.model_dump_json(indent=2)
#             else:
#                 outputs[key] = str(task_output)
#     else:
#         outputs["step6"] = json.dumps(results_dict, indent=2)
#     return outputs, results_dict

# # --- PDF Generation Function ---
# def generate_pdf(final_output):
#     buffer = BytesIO()
#     doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=18)
#     styles = getSampleStyleSheet()
#     styles.add(ParagraphStyle(name='CustomHeading1', fontSize=18, leading=22, spaceAfter=14, spaceBefore=14))
#     styles.add(ParagraphStyle(name='CustomHeading2', fontSize=14, leading=18, spaceAfter=10, spaceBefore=10))
#     styles.add(ParagraphStyle(name='CustomBodyText', fontSize=11, leading=14))

#     elements = []

#     def add_section(title, content):
#         if content:
#             elements.append(Paragraph(title, styles['Heading1']))
#             if isinstance(content, dict):
#                 for k, v in content.items():
#                     if isinstance(v, (list, dict)):
#                         elements.append(Paragraph(f"<b>{k}:</b>", styles['Heading2']))
#                         if isinstance(v, list):
#                             for item in v:
#                                 if isinstance(item, dict):
#                                     for ik, iv in item.items():
#                                         elements.append(Paragraph(f"{ik}: {iv}", styles['BodyText']))
#                                     elements.append(Spacer(1, 6))
#                                 else:
#                                     elements.append(Paragraph(str(item), styles['BodyText']))
#                         elif isinstance(v, dict):
#                             for dk, dv in v.items():
#                                 elements.append(Paragraph(f"{dk}: {dv}", styles['BodyText']))
#                     else:
#                         elements.append(Paragraph(f"<b>{k}:</b> {v}", styles['BodyText']))
#                     elements.append(Spacer(1, 8))
#             else:
#                 elements.append(Paragraph(str(content).replace('\n', '<br />'), styles['BodyText']))
#             elements.append(Spacer(1, 12))

#     # Add main sections from the final output:
#     add_section("Research Summary", final_output.get("research_summary"))
#     add_section("Project Understanding", final_output.get("project_understanding"))
#     add_section("Marketing Strategy", final_output.get("marketing_strategy"))
#     add_section("Campaign Ideas", final_output.get("campaign_ideas"))
#     add_section("Marketing Copies", final_output.get("marketing_copies"))
#     add_section("Refined Marketing Copies", final_output.get("refined_marketing_copies"))
#     add_section("Competitor Analysis", final_output.get("competitor_analysis"))

#     doc.build(elements)
#     pdf = buffer.getvalue()
#     buffer.close()
#     return pdf


# # --- Button ---
# if st.button("🚀 Generate Campaign"):
#     if not customer_domain or not project_description:
#         st.error("Please provide both domain and description.")
#     else:
#         with st.spinner("Running CrewAI Agents..."):
#             try:
#                 step_outputs, final_output = run_crew_ai(customer_domain, project_description)
#                 st.session_state.full_task_outputs = step_outputs
#                 st.session_state.final_consolidated_output = final_output
#                 st.rerun()
#             except Exception as e:
#                 st.error("Something went wrong.")
#                 st.exception(e)

# # --- Final Output Display ---
# if st.session_state.get("final_consolidated_output"):
#     final = st.session_state["final_consolidated_output"]
#     st.markdown("---")
#     st.header("📦 Agent‑wise Final Output")

#     with st.expander("👨‍💼 Lead Market Analyst"):
#         out1 = st.session_state.full_task_outputs.get("step1")
#         if out1:
#             st.subheader("Step 1 Output (Research)")
#             st.code(out1, language="json")
#         st.subheader("Research Summary")
#         st.markdown(final.get("research_summary", "Not available."))

#     with st.expander("👩‍💼 Chief Marketing Strategist"):
#         out2 = st.session_state.full_task_outputs.get("step2")
#         if out2:
#             st.subheader("Step 2 Output (Understanding)")
#             st.code(out2, language="json")
#         st.subheader("Project Understanding")
#         st.markdown(final.get("project_understanding", "Not available."))

#         out3 = st.session_state.full_task_outputs.get("step3")
#         if out3:
#             st.subheader("Step 3 Output (Strategy)")
#             st.code(out3, language="json")

#         strat = final.get("marketing_strategy", {})
#         st.subheader("Marketing Strategy")
#         if strat:
#             st.markdown(f"**Name:** {strat.get('name', '')}")
#             st.markdown("**KPIs:**")
#             for kpi in strat.get("KPIs", []):
#                 st.markdown(f"- {kpi}")

#             if strat.get("tactic_channel_pairs"):
#                 st.markdown("#### Tactic → Channel → Why This Fits")
#                 for pair in strat["tactic_channel_pairs"]:
#                     st.markdown(f"- **{pair['tactic']}** → **{pair['channel']}**")
#                     st.markdown(f"  • _Why_: {pair['rationale']}")

#     with st.expander("✍️ Creative Content Creator"):
#         out4 = st.session_state.full_task_outputs.get("step4")
#         if out4:
#             st.subheader("Step 4 Output (Campaign Ideas)")
#             st.code(out4, language="json")

#         ci = final.get("campaign_ideas", {})
#         st.subheader("Final Campaign Ideas")
#         if ci:
#             st.markdown(f"**Title:** {ci.get('title', '')}")
#             for idea in ci.get("ideas", []):
#                 st.markdown(f"#### {idea.get('name', '')}")
#                 st.markdown(f"- **Description:** {idea.get('description', '')}")
#                 st.markdown(f"- **Audience:** {idea.get('audience', '')}")
#                 st.markdown(f"- **Channel:** {idea.get('channel', '')}")
#                 if "tactic_used" in idea:
#                     st.markdown(f"- **Tactic Used:** {idea['tactic_used']}")
#                 if "channel_fit" in idea:
#                     st.markdown(f"- **Why this channel fits:** {idea['channel_fit']}")

#         out5 = st.session_state.full_task_outputs.get("step5")
#         if out5:
#             st.subheader("Step 5 Output (Copies)")
#             st.code(out5, language="json")

#         st.subheader("Final Marketing Copies")
#         for copy in final.get("marketing_copies", []):
#             st.markdown(f"**{copy.get('title', '')}**")
#             st.write(copy.get("body", ""))

#         if final.get("refined_marketing_copies"):
#             st.subheader("🏁 Refined Marketing Copies")
#             for c in final["refined_marketing_copies"]:
#                 st.markdown(f"#### {c['title']}")
#                 st.markdown(c['body'])

#     with st.expander("🎬 Chief Creative Director"):
#         st.subheader("✅ Final Creative Content")

#         st.markdown("### 🧪 Research Summary")
#         st.markdown(final.get("research_summary", "Not available."))

#         st.markdown("### 🧠 Project Understanding")
#         st.markdown(final.get("project_understanding", "Not available."))

#         strategy = final.get("marketing_strategy", {})
#         if strategy:
#             st.markdown("### 📊 Marketing Strategy")
#             st.markdown(f"**Name:** {strategy.get('name', '')}")
#             st.markdown("**KPIs:**")
#             for kpi in strategy.get("KPIs", []):
#                 st.markdown(f"- {kpi}")

#             if strategy.get("tactic_channel_pairs"):
#                 st.markdown("#### Tactic ↔ Channel ↔ Justification")
#                 for pair in strategy["tactic_channel_pairs"]:
#                     st.markdown(f"- **{pair['tactic']}** → **{pair['channel']}**")
#                     st.markdown(f"  • _Why_: {pair['rationale']}")

#         campaign = final.get("campaign_ideas", {})
#         if campaign:
#             st.markdown("### 🎯 Campaign Ideas")
#             st.markdown(f"**Title:** {campaign.get('title', '')}")
#             for idea in campaign.get("ideas", []):
#                 st.markdown(f"#### {idea.get('name', '')}")
#                 st.markdown(f"- **Description:** {idea.get('description', '')}")
#                 st.markdown(f"- **Audience:** {idea.get('audience', '')}")
#                 st.markdown(f"- **Channel:** {idea.get('channel', '')}")
#                 if "tactic_used" in idea:
#                     st.markdown(f"- **Tactic Used:** {idea['tactic_used']}")
#                 if "channel_fit" in idea:
#                     st.markdown(f"- **Why this channel fits:** {idea['channel_fit']}")

#         copies = final.get("marketing_copies", [])
#         if copies:
#             st.markdown("### ✍️ Marketing Copies")
#             for copy in copies:
#                 st.markdown(f"#### {copy.get('title', '')}")
#                 st.markdown(copy.get("body", ""))

#         refined = final.get("refined_marketing_copies", [])
#         if refined:
#             st.markdown("### 🏁 Refined Marketing Copies")
#             for c in refined:
#                 st.markdown(f"#### {c['title']}")
#                 st.markdown(c['body'])

#         competitors = final.get("competitor_analysis")
#         if competitors:
#             st.markdown("### 🕵️ Competitor Analysis")
#             st.markdown(competitors)

#     # --- PDF Download Button ---
#     pdf_data = generate_pdf(final)
#     st.download_button(
#         label="📥 Download Final Report (PDF)",
#         data=pdf_data,
#         file_name="final_marketing_report.pdf",
#         mime="application/pdf"
#     )

# # --- Footer ---
# st.markdown("---")
# st.caption("Powered by CrewAI, OpenAI, Serper & Streamlit")





# code without step wise output -just final pdf

# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# from marketing_posts.crew import MarketingPostsCrew
# from io import BytesIO
# from reportlab.lib.pagesizes import letter
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# # --- Load API Keys ---
# load_dotenv()
# serper_api_key = os.getenv("SERPER_API_KEY")
# openai_secret_path = "/run/secrets/openai-api-key"

# if os.path.exists(openai_secret_path):
#     with open(openai_secret_path, "r") as f:
#         openai_api_key = f.read().strip()
# else:
#     st.error("Missing OpenAI secret file.")
#     st.stop()

# os.environ["SERPER_API_KEY"] = serper_api_key or ''
# os.environ["OPENAI_API_KEY"] = openai_api_key or ''

# if not serper_api_key or not openai_api_key:
#     st.error("API keys missing. Check .env or Docker secrets.")
#     st.stop()

# # --- Streamlit App Config ---
# st.set_page_config(layout="wide", page_title="AI Marketing Studio")
# st.title("AI Marketing Studio")
# st.markdown("---")

# # Project input
# customer_domain = st.text_input("🌐 Project Domain (e.g., fintech)")
# project_description = st.text_area("📝 Project Description", height=150)

# if 'full_task_outputs' not in st.session_state:
#     st.session_state.full_task_outputs = {}
#     st.session_state.final_consolidated_output = {}

# # --- Run CrewAI ---
# @st.cache_data(show_spinner=False)
# def run_crew_ai(domain, desc):
#     inputs = {"customer_domain": domain, "project_description": desc}
#     crew_result = MarketingPostsCrew().crew().kickoff(inputs=inputs)
#     results_dict = crew_result.json_dict if hasattr(crew_result, 'json_dict') else json.loads(str(crew_result))
#     outputs = {}
#     if hasattr(crew_result, 'tasks_output'):
#         for i, task_output in enumerate(crew_result.tasks_output):
#             key = f"step{i+1}"
#             if isinstance(task_output, (dict, list)):
#                 outputs[key] = json.dumps(task_output, indent=2)
#             elif hasattr(task_output, "model_dump_json"):
#                 outputs[key] = task_output.model_dump_json(indent=2)
#             else:
#                 outputs[key] = str(task_output)
#     else:
#         outputs["step6"] = json.dumps(results_dict, indent=2)
#     return outputs, results_dict

# # --- PDF Generation Function ---
# def generate_pdf(final_output):
#     buffer = BytesIO()
#     doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=18)
#     styles = getSampleStyleSheet()

#     # Define custom styles to avoid conflicts
#     styles.add(ParagraphStyle(name='CustomHeading1', fontSize=18, leading=22, spaceAfter=14, spaceBefore=14))
#     styles.add(ParagraphStyle(name='CustomHeading2', fontSize=14, leading=18, spaceAfter=10, spaceBefore=10))
#     styles.add(ParagraphStyle(name='CustomBodyText', fontSize=11, leading=14))

#     elements = []

#     def add_section(title, content):
#         if content:
#             elements.append(Paragraph(title, styles['CustomHeading1']))
#             if isinstance(content, dict):
#                 for k, v in content.items():
#                     if isinstance(v, (list, dict)):
#                         elements.append(Paragraph(f"<b>{k}:</b>", styles['CustomHeading2']))
#                         if isinstance(v, list):
#                             for item in v:
#                                 if isinstance(item, dict):
#                                     for ik, iv in item.items():
#                                         elements.append(Paragraph(f"{ik}: {iv}", styles['CustomBodyText']))
#                                     elements.append(Spacer(1, 6))
#                                 else:
#                                     elements.append(Paragraph(str(item), styles['CustomBodyText']))
#                         elif isinstance(v, dict):
#                             for dk, dv in v.items():
#                                 elements.append(Paragraph(f"{dk}: {dv}", styles['CustomBodyText']))
#                     else:
#                         elements.append(Paragraph(f"<b>{k}:</b> {v}", styles['CustomBodyText']))
#                     elements.append(Spacer(1, 8))
#             else:
#                 elements.append(Paragraph(str(content).replace('\n', '<br />'), styles['CustomBodyText']))
#             elements.append(Spacer(1, 12))

#     add_section("Research Summary", final_output.get("research_summary"))
#     add_section("Project Understanding", final_output.get("project_understanding"))
#     add_section("Marketing Strategy", final_output.get("marketing_strategy"))
#     add_section("Campaign Ideas", final_output.get("campaign_ideas"))
#     add_section("Marketing Copies", final_output.get("marketing_copies"))
#     add_section("Refined Marketing Copies", final_output.get("refined_marketing_copies"))
#     add_section("Competitor Analysis", final_output.get("competitor_analysis"))

#     doc.build(elements)
#     pdf = buffer.getvalue()
#     buffer.close()
#     return pdf

# # --- Button ---
# if st.button("🚀 Generate Campaign"):
#     if not customer_domain or not project_description:
#         st.error("Please provide both domain and description.")
#     else:
#         with st.spinner("Running CrewAI Agents..."):
#             try:
#                 step_outputs, final_output = run_crew_ai(customer_domain, project_description)
#                 st.session_state.full_task_outputs = step_outputs
#                 st.session_state.final_consolidated_output = final_output
#                 st.rerun()
#             except Exception as e:
#                 st.error("Something went wrong.")
#                 st.exception(e)

# # --- Final Output Display ---
# if st.session_state.get("final_consolidated_output"):
#     final = st.session_state["final_consolidated_output"]
#     st.markdown("---")
#     st.header("📦 Agent‑wise Final Output")

#     # EXPANDERS OMITTED FOR BREVITY (you already have them fully working)

#     # --- PDF Download Button ---
#     pdf_data = generate_pdf(final)
#     st.download_button(
#         label="📥 Download Final Report (PDF)",
#         data=pdf_data,
#         file_name="final_marketing_report.pdf",
#         mime="application/pdf"
#     )

# # --- Footer ---
# st.markdown("---")
# st.caption("Powered by CrewAI, OpenAI, Serper & Streamlit")




