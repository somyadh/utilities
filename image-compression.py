from PIL import Image
import os
import argparse

#usage
#python image_compression_cli.py input_folder output_folder --target_size 1.0

def get_initial_quality(input_size_mb):
    if input_size_mb > 20:
        return 30
    elif input_size_mb > 10:
        return 40
    elif input_size_mb > 5:
        return 50
    elif input_size_mb > 2:
        return 60
    else:
        return 70

def compress_image(input_file, output_file, target_size_mb=1.0):
    image = Image.open(input_file)

    input_size_bytes = os.path.getsize(input_file)
    input_size_mb = input_size_bytes / (1024 * 1024)
    print(f"Input size: {input_size_mb:.2f} MB")

    quality = get_initial_quality(input_size_mb)
    target_size_bytes = target_size_mb * 1024 * 1024

    prev_compressed_size_bytes = float('inf')
    same_size_count = 0

    # Compress the image until the target size is reached or compression stalls
    while True:
        temp_file = "temp.png"
        print(f"Compressing with quality: {quality}")
        image.save(temp_file, "PNG", optimize=True, quality=quality)

        compressed_size_bytes = os.path.getsize(temp_file)
        print(f"Compressed size: {compressed_size_bytes / (1024 * 1024):.2f} MB")

        if compressed_size_bytes <= target_size_bytes:
            break

        # If the compressed size remains the same for 3 iterations, break the loop
        if compressed_size_bytes == prev_compressed_size_bytes:
            same_size_count += 1
            if same_size_count >= 3:
                print("Compression stalled. Breaking the loop.")
                break
        else:
            same_size_count = 0

        prev_compressed_size_bytes = compressed_size_bytes
        quality -= 5
        if quality <= 0:
            break

    image.save(output_file, "PNG", optimize=True, quality=quality)
    os.remove(temp_file)

    print(f"Compressed image saved as {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Image Compression CLI')
    parser.add_argument('input_folder', help='Path to the input folder containing images')
    parser.add_argument('output_folder', help='Path to the output folder to save compressed images')
    parser.add_argument('--target_size', type=float, default=1.0, help='Target size in MB for compressed images (default: 1.0)')

    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder
    target_size_mb = args.target_size

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename)

            input_size_mb = os.path.getsize(input_file) / (1024 * 1024)

            if input_size_mb > 1.5:
                print(f"Compressing {filename}...")
                compress_image(input_file, output_file, target_size_mb)
            else:
                print(f"Skipping {filename}. Image size is already below 1.5 MB.")

if __name__ == '__main__':
    main()


