import streamlit as st
import time
import pandas as pd
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- Configuration (Replace with your actual keys and email for real usage) ---
# For demonstration, these will be placeholders.
# In a real application, you would load these securely from environment variables.
TOGETHER_API_KEY_1 = "tgp_v1_ecSsk1__FlO2mB_gAaaP2i-Affa6Dv8OCVngkWzBJUY" # User provided
TOGETHER_API_KEY_2 = "tgp_v1_4hJBRX0XDlwnw_hhUnhP0e_lpI-u92Xhnqny2QIDAIM" # User provided
EMAIL_ADDRESS = "akashvishnu6680@gmail.com" # User provided
EMAIL_PASSWORD = "swpe pwsx ypqo hgnk" # User provided - Note: App passwords are safer than main password

# --- Agentic AI Simulation Class ---
class AgenticAI:
    def __init__(self, problem_statement, together_api_key_1, together_api_key_2, email_address, email_password):
        self.problem_statement = problem_statement
        self.together_api_key_1 = together_api_key_1
        self.together_api_key_2 = together_api_key_2
        self.email_address = email_address
        self.email_password = email_password
        self.report_content = ""
        self.chat_history = [] # To store agent's communication

    def _log_message(self, role, message, is_user=False):
        """Logs messages to the chat history and displays them in Streamlit."""
        self.chat_history.append({"role": role, "message": message})
        if role == "Agent":
            st.info(f"**Agent:** {message}")
        elif role == "User":
            st.success(f"**You:** {message}")
        else:
            st.write(message)
        time.sleep(1) # Simulate thinking time

    def _simulate_llm_call(self, prompt):
        """
        Simulates an LLM call using the provided prompt.
        In a real scenario, this would make a fetch call to the Together AI API.
        For this demo, it returns a predefined response based on the prompt.
        """
        # This is where you would integrate with Together AI
        # Example:
        # payload = {"contents": [{"role": "user", "parts": [{"text": prompt}]}]}
        # headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {self.together_api_key_1}'}
        # response = requests.post("https://api.together.xyz/v1/chat/completions", json=payload, headers=headers)
        # return response.json()['choices'][0]['message']['content']

        if "problem definition" in prompt.lower():
            return "The problem is formally defined as: 'Optimizing customer engagement through personalized content delivery.' This means we want to make sure the right messages reach the right people at the right time to keep them interested."
        elif "assumptions" in prompt.lower():
            return "We assume customers prefer personalized content, we have access to their interaction data, and our content library is diverse enough for personalization."
        elif "why solve" in prompt.lower():
            return "Solving this problem will lead to happier customers, increased sales, and better use of our marketing efforts. Our current approach is generic and often misses the mark, leading to low engagement."
        elif "data description" in prompt.lower():
            return "We have customer demographics, past purchase history, website browsing behavior, and email open rates. We'd love to have social media sentiment data, but we don't have it yet. We don't need raw server logs for this task."
        elif "data processing" in prompt.lower():
            return "Data will be cleaned by handling missing values (e.g., using average for missing age) and removing unusual entries (like extremely high purchase values). We'll sample data to ensure we have a good representation of all customer types."
        elif "data transformation" in prompt.lower():
            return "We'll create new features like 'days since last purchase' and 'total items bought'. We'll also convert categories like 'product type' into separate yes/no indicators."
        elif "data summarization" in prompt.lower():
            return "We'll look at simple graphs showing customer age distribution, how often they buy, and how different product categories perform. We'll also see how these relate to engagement."
        elif "test harness" in prompt.lower():
            return "We'll set aside a portion of our customer data as a 'final exam' for our models. We'll use a method called 'cross-validation' to fairly test different personalization strategies, and we'll measure success by how much customer engagement increases."
        elif "candidate algorithms" in prompt.lower():
            return "We'll try different 'smart helpers' like 'Recommendation Engines', 'Decision Trees', and 'Neural Networks' to see which one is best at predicting what content customers will like."
        elif "algorithm tuning" in prompt.lower():
            return "We'll fine-tune the settings of our best 'smart helpers' to make them even more accurate, like adjusting the 'learning speed' of a neural network."
        elif "ensemble methods" in prompt.lower():
            return "We'll combine a few of our best 'smart helpers' together, so they can 'vote' on the best content, making the overall recommendation even stronger and more reliable."
        elif "model selection" in prompt.lower():
            return "We'll pick the top 3-5 'smart helpers' and test them on our 'final exam' data to ensure they perform well on new, unseen customers. The one that shows the most engagement improvement will be chosen."
        elif "present results" in prompt.lower():
            return "We'll create easy-to-understand charts and a simple report showing how personalized content has increased customer engagement and sales. This will be shared with the marketing team."
        elif "operationalize results" in prompt.lower():
            return "We'll set up the chosen personalization system to automatically deliver content to customers. We'll also monitor its performance regularly to make sure it continues to work well and adapt to new trends."
        elif "final report" in prompt.lower():
            return """
### Agentic AI Project: Personalized Content Delivery for Enhanced Customer Engagement

**1. The Big Picture (Problem Definition):**
Our goal was to make sure our customers feel more connected and engaged by giving them content that truly interests them. The old way was like sending the same message to everyone, which often didn't work.

**2. Getting Our Information Ready (Data Preparation):**
We gathered all sorts of customer information – what they've bought, what they've looked at on our website, and how they interact with our emails. We cleaned it up, filled in any blanks, and organized it so our AI could understand it easily. We even created new insights, like how long it's been since a customer last bought something.

**3. Trying Out Smart Helpers (Spot Check Algorithms):**
We tried a bunch of different "smart helpers" (AI models) to see which ones were good at guessing what content customers would like. We used a fair testing method to make sure we weren't just lucky.

**4. Making Them Even Smarter (Improve Results):**
We fine-tuned the best "smart helpers" and even combined a few of them, so they could work together to give even better recommendations. This made our predictions much more reliable.

**5. Putting It All to Work (Finalize Project):**
We picked the very best personalized content delivery system. It's now set up to automatically send the right content to the right customer. We'll keep an eye on it to make sure it keeps our customers happy and our business growing.

**Key Benefits:**
* **Happier Customers:** Content that matters to them.
* **More Sales:** Engaged customers buy more.
* **Smarter Marketing:** Our marketing efforts are now much more effective.

This new system is fully automated and designed to adapt, ensuring we always provide the best possible experience for our customers.
"""
        else:
            return "I'm processing your request. Please wait a moment."

    def run_agent_workflow(self):
        """Orchestrates the entire Agentic AI workflow."""
        self._log_message("Agent", "Hello! I'm your Agentic AI assistant. I'm ready to take full responsibility for your task.")
        self._log_message("Agent", f"My main mission is: '{self.problem_statement}'. Let's get started!")

        st.subheader("1. Defining the Problem")
        with st.spinner("Agent is thinking about the problem..."):
            formal_definition = self._simulate_llm_call("Provide a formal problem definition for: " + self.problem_statement)
            self._log_message("Agent", f"Okay, I've formally defined the problem: '{formal_definition}'")
            assumptions = self._simulate_llm_call("List the assumptions about the problem.")
            self._log_message("Agent", f"Here are the assumptions I'm making: '{assumptions}'")
            why_solve = self._simulate_llm_call("Why does this problem need to be solved? Describe current solution and benefits.")
            self._log_message("Agent", f"This problem is important to solve because: '{why_solve}'")

        st.subheader("2. Preparing the Data")
        with st.spinner("Agent is gathering and preparing data..."):
            data_description = self._simulate_llm_call("Describe the data available, desirable, and not needed.")
            self._log_message("Agent", f"I've assessed the data landscape: '{data_description}'")
            data_processing = self._simulate_llm_call("Explain data processing steps.")
            self._log_message("Agent", f"I will now clean and prepare the data: '{data_processing}'")
            data_transformation = self._simulate_llm_call("Explain data transformation steps.")
            self._log_message("Agent", f"Next, I'll transform the data to reveal hidden patterns: '{data_transformation}'")
            data_summarization = self._simulate_llm_call("Explain data summarization steps.")
            self._log_message("Agent", f"Finally, I'll summarize the data to understand its key characteristics: '{data_summarization}'")

        st.subheader("3. Spot Checking Algorithms")
        with st.spinner("Agent is evaluating different smart helpers..."):
            test_harness = self._simulate_llm_call("Describe the test harness.")
            self._log_message("Agent", f"I'm setting up a fair testing ground for our smart helpers: '{test_harness}'")
            candidate_algorithms = self._simulate_llm_call("List candidate algorithms.")
            self._log_message("Agent", f"I'll now try out various smart helpers to see their initial performance: '{candidate_algorithms}'")

        st.subheader("4. Improving Results")
        with st.spinner("Agent is fine-tuning and combining models..."):
            algorithm_tuning = self._simulate_llm_call("Explain algorithm tuning.")
            self._log_message("Agent", f"Now, I'm fine-tuning the best smart helpers for peak performance: '{algorithm_tuning}'")
            ensemble_methods = self._simulate_llm_call("Explain ensemble methods.")
            self._log_message("Agent", f"I'm also exploring combining multiple smart helpers for even better results: '{ensemble_methods}'")
            model_selection = self._simulate_llm_call("Explain model selection.")
            self._log_message("Agent", f"I've selected the top performing smart helpers and validated them: '{model_selection}'")

        st.subheader("5. Finalizing Project")
        with st.spinner("Agent is preparing the final report and operationalizing..."):
            present_results = self._simulate_llm_call("Explain how results will be presented.")
            self._log_message("Agent", f"I'm preparing the results in a clear and understandable way: '{present_results}'")
            operationalize_results = self._simulate_llm_call("Explain how results will be operationalized.")
            self._log_message("Agent", f"Finally, I'm setting up the solution to run automatically: '{operationalize_results}'")

        self._log_message("Agent", "My task is complete! I've gone through all the necessary steps.")
        self._log_message("Agent", "I'm now generating a comprehensive report for you.")
        self.report_content = self._simulate_llm_call("Generate a final report.")
        self._log_message("Agent", "Report generated successfully!")

    def get_report(self):
        """Returns the generated report content."""
        return self.report_content

    def send_report_email(self, recipient_email, subject, body):
        """Sends the generated report via email."""
        if not self.email_address or not self.email_password:
            st.error("Email credentials not provided. Cannot send email.")
            return False

        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.email_address, self.email_password)
                smtp.send_message(msg)
            st.success(f"Report successfully sent to {recipient_email}!")
            return True
        except Exception as e:
            st.error(f"Failed to send email: {e}. Please check your email address, password, and ensure 'Less secure app access' or 'App passwords' are enabled for your Gmail account if you are using Gmail.")
            return False

# --- Streamlit UI ---
st.set_page_config(layout="wide", page_title="Agentic AI Demonstrator")

st.title("🚀 Your Agentic AI Assistant")
st.markdown("I'm here to demonstrate how an Agentic AI can take full responsibility for a complex task, communicate its progress, and deliver results in a clear, non-technical way.")

st.sidebar.header("Agent Configuration")
problem_input = st.sidebar.text_area(
    "What problem do you want the Agentic AI to solve?",
    "Automate market research and report generation for new product ideas.",
    height=100
)

st.sidebar.markdown("---")
st.sidebar.subheader("API Keys & Email (For Demo/Future Use)")
st.sidebar.info("These keys are for demonstration purposes. In a real app, they would be securely managed.")

together_key_1_input = st.sidebar.text_input("Together API Key 1", TOGETHER_API_KEY_1, type="password")
together_key_2_input = st.sidebar.text_input("Together API Key 2", TOGETHER_API_KEY_2, type="password")
email_address_input = st.sidebar.text_input("Your Email Address (for sending reports)", EMAIL_ADDRESS)
email_password_input = st.sidebar.text_input("Your Email Password (or App Password)", EMAIL_PASSWORD, type="password")

st.sidebar.markdown("---")
start_button = st.sidebar.button("Start Agentic AI Workflow")

st.markdown("---")

if 'agent' not in st.session_state:
    st.session_state.agent = None
if 'report_generated' not in st.session_state:
    st.session_state.report_generated = False
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if start_button:
    st.session_state.agent = AgenticAI(
        problem_input,
        together_key_1_input,
        together_key_2_input,
        email_address_input,
        email_password_input
    )
    st.session_state.chat_history = [] # Clear history for new run
    st.session_state.report_generated = False
    st.session_state.agent.run_agent_workflow()
    st.session_state.report_generated = True

# Display chat history if available
if st.session_state.agent:
    st.subheader("Agent's Communication Log")
    for chat_entry in st.session_state.agent.chat_history:
        if chat_entry["role"] == "Agent":
            st.info(f"**Agent:** {chat_entry['message']}")
        elif chat_entry["role"] == "User":
            st.success(f"**You:** {chat_entry['message']}")
        else:
            st.write(chat_entry['message'])

    if st.session_state.report_generated:
        st.markdown("---")
        st.subheader("Final Report from Agentic AI")
        st.markdown(st.session_state.agent.get_report())

        st.markdown("---")
        st.subheader("Share the Report")
        recipient_email = st.text_input("Enter recipient email to send the report:", EMAIL_ADDRESS)
        if st.button("Send Report via Email"):
            if st.session_state.agent.send_report_email(recipient_email, "Agentic AI Project Report", st.session_state.agent.get_report()):
                st.balloons()
