class set_machine():
    def __init__(self):
        pass

    def state(self):
        return ["initial", "save_text", "load_text", "show_image", "dinner", "sticker"]
    
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
        {"trigger": "go_back", "source": ["save_text", "load_text", "show_image", "sticker"], "dest": "initial"},
        ]
    
    def initial(self):
        return "initial"
    
    def auto_transitions(self):
        return False
    def show_conditions(self):
        return True


def help_message():
    text = ""
    return text