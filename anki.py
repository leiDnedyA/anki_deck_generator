import genanki
import random
import tts

# Generating ANKI deck
def _gen_id():
    return random.randrange(1, 31)

# model for notes
_model = genanki.Model(
    _gen_id(),
    'Card Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'MyMedia'}
    ],
    css="* {text-align: center}",
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<h1>{{Question}}</h1>',
            'afmt': '<h3>{{Question}}</h3> <hr id="answer"><h1>{{Answer}}</h1>{{MyMedia}}'
        }
    ]
)

# Generates a new anki deck with the title "title"
def get_deck(title):
    return genanki.Deck(_gen_id(), title)

# Adds a card to the given deck
def add_card(deck, card, lang="en"):
    term = card['term']
    audio_file = tts.create_tts_file(term, term, lang)
    print(audio_file)
    note = genanki.Note(
        model=_model,
        fields=[term, card['def'], f'[sound:{audio_file}]']
    )
    deck.add_note(note)

# Exports a given deck
# do not include file extension in file_name variable
def export_deck(deck, file_name):
    genanki.Package(deck).write_to_file(file_name + ".apkg")
