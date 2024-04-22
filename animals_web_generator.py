import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

def generate_animal_cards(animals_data):
    """Generates HTML for animal cards"""
    cards_html = ""
    for animal in animals_data:
        card_html = f"""
        <li class="cards__item">
            <div class="card__title">{animal.get("Name", "")}</div>
            <div class="card__text">Diet: {animal.get("Diet", "")}</div>
            <div class="card__text">Location: {animal.get("Locations", [""])[0]}</div>
            <div class="card__text">Type: {animal.get("Type", "")}</div>
        </li>
        """
        cards_html += card_html
    return cards_html

# Load data from JSON file
animals_data = load_data('animals_data.json')

# Generate HTML for animal cards
animal_cards_html = generate_animal_cards(animals_data)

# Read HTML template from file
with open('animals_template.html', 'r') as f:
    html_template = f.read()

# Replace __REPLACE_ANIMALS_INFO__ in the HTML template with the generated animal cards HTML
final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_cards_html)

# Output the final HTML content
print(final_html)
