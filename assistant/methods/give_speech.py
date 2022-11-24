from assistant.utils.text_to_speech import TextToSpeech

SPEECHES = {
    "madara uchiha": [
        (150, .5, "Wake up to reality, nothing ever goes as planned in this accursed world"),
        (150, .5, "The longer you live the more you will realize that the only things that truly exist in this reality are merely pain, suffering and futility"),
        (150, .5, "Listen, everywhere you go wherever there is light, there will always be shadows to be found as well"),
        (150, .5, "As long as there is a concept of victors, the vanquished will also exist"),
        (150, .5, "The selfish intent of wanting to preserve peace, initiates wars. And hatred is born in order to protect love."),
        (150, .5, "There are nexuses, causal relationships that cannot be separated"),
        (130, .5, "I want to sever the fate of this world. A world full of victors, a world of peace, a world of love"),
        (115, .5, "I will create such a world"),
        (115, .6, "For truly this reality, is a hell"),
    ]
}

def main(person):
    tts = TextToSpeech()
    org_rate = tts.get_speed()
    org_volume = tts.get_volume()

    if person.lower() in SPEECHES:
        for entry in SPEECHES[person.lower()]:
            rate = entry[0]
            volume = entry[1]
            line = entry[2]
            tts.set_speed(rate)
            tts.set_volume(volume)
            tts.speak(line)

    tts.set_speed(org_rate)
    tts.set_volume(org_volume)