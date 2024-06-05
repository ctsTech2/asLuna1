from agency_swarm import Agency
from UserInterfaceAgent import UserInterfaceAgent
from LumberCEO import LumberCEO


agency = Agency([lumber_ceo, user_interface_agent, [lumber_ceo, user_interface_agent],
 [user_interface_agent, code_compliance_agent],
 [user_interface_agent, estimate_generator_agent]],
                shared_instructions='./agency_manifesto.md', # shared instructions for all agents
                max_prompt_tokens=25000, # default tokens in conversation for all agents
                temperature=0.3, # default temperature for all agents
                )
                
if __name__ == '__main__':
    agency.demo_gradio()
