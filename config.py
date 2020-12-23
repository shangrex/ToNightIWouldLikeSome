class set_machine():
    def __init__(self):
        pass

    def state(self):
        return ["initial", "save_text", "load_text", "show_image", "dinner", "sticker", "clear_text"]
    
    def transition(self):
        return [
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "save_text",
            "conditions": "is_going_to_save_text",
        },
        {
            "trigger": "advance",
            "source": "save_text",
            "dest": "initial",
            "conditions": "is_going_to_initial_from_save_text",
        },
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "load_text",
            "conditions": "is_going_to_load_text",
        },
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "dinner",
            "conditions": "is_going_to_dinner",
        },
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "show_image",
            "conditions": "is_going_to_show_image",
        },
        {
            "trigger": "advance",
            "source": "dinner",
            "dest": "initial",
            "conditions": "is_going_to_initial_from_dinner",
        },
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "sticker",
            "conditions": "is_going_to_sticker",
        },
        {
            "trigger": "advance",
            "source": "sticker",
            "dest": "initial",
            "conditions": "is_going_to_initial_from_sticker",
        },
        {
            "trigger": "advance",
            "source": "initial",
            "dest": "clear_text",
            "conditions": "is_going_to_clear_text",
        },
        {"trigger": "go_back", "source": ["save_text", "load_text", "show_image", "sticker", "clear_text"], "dest": "initial"},
        ]
    
    def initial(self):
        return "initial"
    
    def auto_transitions(self):
        return False
    def show_conditions(self):
        return True


def help_message():
    text = "The bot have 5 function \n\
            1. save text \n\
            2. load text \n\
            3. show iamge"                  
    return text