from PIL import Image
import os

def compress_image(input_path, output_path, quality=60):
    try:
        input_image = Image.open(input_path)

        if input_image.mode == 'RGBA':
            input_image = input_image.convert('RGB')

        # Determine output format based on file extension
        output_format = os.path.splitext(output_path)[1][1:].upper()  # Get file extension and convert to uppercase
        if output_format not in ['JPEG', 'JPG', 'PNG']:
            raise ValueError("Unsupported output format. Supported formats: JPEG, JPG, PNG")

        # Save the compressed image
        compressed_image = input_image.copy()
        compressed_image.save(output_path, format=output_format, quality=quality)

        print(f"Compressed image saved at: {output_path}")

    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    input_path = r'D:\Python-Programming-Internship\Chauhan_Shyam_R\Task_12\be_better.png'  # Adjust this path
    output_folder = 'compressed_images'
    os.makedirs(output_folder, exist_ok=True) 

    # Interactive quality adjustment
    try:
        quality = int(input("Enter compression quality (0 - 95): "))
        if quality < 0 or quality > 95:
            raise ValueError("Compression quality must be between 0 and 95.")
    except ValueError:
        quality = 60  # Default value if invalid input

    # Compress image
    output_path = os.path.join(output_folder, 'compressed_image.png')
    compress_image(input_path, output_path, quality)

if __name__ == "__main__":
    main()
