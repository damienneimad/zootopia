import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def generate_animal_info(animals_data):
    """Generates a string with the animals' data."""
    output = ''
    for animal in animals_data:
        output += '<li class="cards__item">'
        if 'name' in animal:
            output += f"<div class='card__title'>{animal['name']}</div>"
        output += "<p class='card__text'><ul>"
        if 'characteristics' in animal:
            if 'diet' in animal['characteristics']:
                output += f"<li>Diet: {animal['characteristics']['diet']}</li>"
            if 'type' in animal['characteristics']:
                output += f"<li>Type: {animal['characteristics']['type']}</li>"
        if 'locations' in animal and len(animal['locations']) > 0:
            output += f"<li>Location: {animal['locations'][0]}</li>"
        output += "</ul></p></li>"
    return output

def replace_placeholder(template_content, animal_info):
    """Replaces the placeholder in the template with the animal info."""
    return template_content.replace('__REPLACE_ANIMALS_INFO__', animal_info)

def read_template(file_path):
    """Reads the HTML template file."""
    with open(file_path, "r") as file:
        return file.read()

def write_html(file_path, content):
    """Writes the content to an HTML file."""
    with open(file_path, "w") as file:
        file.write(content)

if __name__ == "__main__":
    # Load the data from the JSON file
    animals_data = load_data('animals_data.json')

    # Generate the animal information string
    animal_info = generate_animal_info(animals_data)

    # Read the HTML template content
    template_content = read_template('animals_template.html')

    # Replace the placeholder with the animal info
    new_html_content = replace_placeholder(template_content, animal_info)

    # Write the new HTML content to a file
    write_html('animals.html', new_html_content)

    print("HTML file generated: animals.html")
