from roles.strategist import STRATEGIST_PROMPT
from roles.product_manager import PRODUCT_MANAGER_PROMPT
from roles.engineer import ENGINEER_PROMPT
from roles.marketer import MARKETER_PROMPT
from roles.critic import CRITIC_PROMPT


ROLES = {
    'strategist': {
        'system_prompt': STRATEGIST_PROMPT
    },
    'product_manager': {
        'system_prompt': PRODUCT_MANAGER_PROMPT

    },
    'engineer': {
        'system_prompt': ENGINEER_PROMPT
    },
    'marketer': {
        'system_prompt': MARKETER_PROMPT
    },
    'critic': {
        'system_prompt': CRITIC_PROMPT
    }
}
