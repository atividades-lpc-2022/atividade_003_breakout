from pygame import mixer


def play_sound(sound: str):
    sound_effect = mixer.Sound(sound)
    sound_effect.play()
