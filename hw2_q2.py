from collections import namedtuple
from enum import Enum
from itertools import zip_longest

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))

def improve(condition:Condition) -> Condition:
    """
    Improve the condition of an agent.
    """
    condition_order = [Condition.HEALTHY, Condition.SICK, Condition.DYING, Condition.DEAD]
    if condition in condition_order:
        #getting the index of the current condition in the order
        index = condition_order.index(condition)
        #avoiding going out of bounds
        if index > 0:
            return condition_order[index - 1]
    return condition
def cure(healer: Agent, patient:Agent) -> tuple[Agent, Agent]:
    """
    Cure an agent if they are sick or dying.
    """
    if patient.category in (Condition.SICK, Condition.DYING):
        improved= patient._replace(category=improve(patient.category))
        return healer, improved
    return healer, patient
def worsen(condition: Condition) -> Condition:
    """
    Worsen the condition of an agent.
    """
    condition_order = [Condition.HEALTHY, Condition.SICK, Condition.DYING, Condition.DEAD]
    if condition in condition_order:
        #getting the index of the current condition in the order
        index = condition_order.index(condition)
        #avoiding going out of bounds
        if index < len(condition_order) - 1:
            return condition_order[index + 1]
    return condition

def pandem_effect(agent1: Agent,agent2) -> tuple[Agent, Agent]:
    """
    Apply the pandemic effect between two agents.
    """
    #setting the new condition of the agents based on the rules given
    agent1_Ncond=agent1._replace(category=worsen(agent1.category))
    agent2_Ncond=agent2._replace(category=worsen(agent2.category))
    return agent1_Ncond, agent2_Ncond


            
        
    
def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Condition.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """
    #as i understand the question, the meeting is between two agents, there is only one iteraation,meaning only one round of meetings
    #so i will iterate over the agents in pairs, and update their condition based on the rules given
    updated_listing = []
    #adding the agents that are dead or healthy to the updated listing
    updated_listing.extend([a for a in agent_listing if a.category == Condition.DEAD or a.category == Condition.HEALTHY])
    #remove from list all agents that are dead or healthy for meetup
    agent_listing_meetup = [a for a in agent_listing if a.category != Condition.DEAD and a.category != Condition.HEALTHY]
    for a, b in zip_longest(agent_listing_meetup[::2], agent_listing_meetup[1::2], fillvalue=None):
        if b is None:
            updated_listing.append(a)
            continue
        elif a.category == Condition.CURE:
            updated_listing.extend(cure(a,b))
            continue
        elif b.category == Condition.CURE:
            updated_listing.extend(cure(b,a))
            continue
        else:       
            #apply the pandemic effect between the two agents
            updated_listing.extend(pandem_effect(a,b))
    
    
    try:
        if len(updated_listing) != len(set(updated_listing)):
            raise ValueError("Duplicate agents found in the updated listing.")
    except ValueError as e:
        print(e)

    return updated_listing
