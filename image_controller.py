import io
import os
from image_compression import compress_image

def compress_image_file(image_file, target_size_mb=1.0):
    temp_input_file = "temp_input.png"
    image_file.save(temp_input_file)

    temp_output_file = "temp_output.png"
    compress_image(temp_input_file, temp_output_file, target_size_mb)

    with open(temp_output_file, "rb") as file:
        compressed_image_bytes = file.read()

    os.remove(temp_input_file)
    os.remove(temp_output_file)

    compressed_image_buffer = io.BytesIO(compressed_image_bytes)
    compressed_size = compressed_image_buffer.getbuffer().nbytes / (1024 * 1024)  # Convert bytes to MB
    
    return compressed_image_buffer, compressed_size