from PIL import Image

# Function to get user's choice of format
def get_output_format():
    while True:
        choice = input("Enter the desired output format (PNG, JPEG, BMP, GIF): ").strip().upper()
        if choice in ['PNG', 'JPEG', 'BMP', 'GIF']:
            return choice
        else:
            print("Invalid format. Please enter one of PNG, JPEG, BMP, GIF.")

# Main code
image_path = input("Enter the full path of the PDF file: ")
image = Image.open(image_path)
image = image.convert('RGB')

output_format = get_output_format()

# Save the image based on user's choice
output_filename = f"converted-image.{output_format.lower()}"
image.save(output_filename)

print(f"Image saved as {output_filename}")
