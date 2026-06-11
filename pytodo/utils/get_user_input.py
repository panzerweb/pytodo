from pytodo.services.speech_to_text_cubit import voiceCommand

def get_user_input(voice_mode: bool) -> str:
    if voice_mode:
        return voiceCommand()

    return input("\nYour Command: ")