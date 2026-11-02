import json
from typing import Dict, List, Tuple, Union

import streamlit as st
from langchain_core.agents import AgentFinish


def step_callback(
    self,
    agent_output: Union[str, List[Tuple[Dict, str]], AgentFinish],
    agent_name,
    *args,
):
    with st.chat_message("AI"):
        # Try to parse the output if it is a JSON string
        if isinstance(agent_output, str):
            try:
                agent_output = json.loads(agent_output)
            except json.JSONDecodeError:
                pass

        if isinstance(agent_output, list) and all(
            isinstance(item, tuple) for item in agent_output
        ):

            for action, description in agent_output:
                # Print attributes based on assumed structure
                st.write(f"Agent Name: {agent_name}")
                st.write(f"Tool used: {getattr(action, 'tool', 'Unknown')}")
                st.write(f"Tool input: {getattr(action, 'tool_input', 'Unknown')}")
                st.write(f"{getattr(action, 'log', 'Unknown')}")
                with st.expander("Show observation"):
                    st.markdown(f"Observation\n\n{description}")

        # Check if the output is a dictionary as in the second case
        elif isinstance(agent_output, AgentFinish):
            st.write(f"Agent Name: {agent_name}")
            output = agent_output.return_values
            st.write(f"I finished my task:\n{output['output']}")

        # Handle unexpected formats
        else:
            st.write(type(agent_output))
            st.write(agent_output)
