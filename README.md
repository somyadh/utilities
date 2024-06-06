# Utilities

This repository contains a collection of utility tools and scripts that can be used to perform variety of tasks locally. The motivation behind this project is to have a set of handy utilities that can be run locally on  machine, eliminating the need to upload my own data on random servers on the internet

## Tools

### Image Compression CLI

The image compression tool compresses PNG images to a specified target size while maintaining image quality.

#### Usage

```
python image_compression_cli.py input.png output.png --target_size 1.5
```

### PDF Splitter CLI

The PDF splitter tool extracts a range of pages from a PDF file and create a new PDF file with the selected pages. This works good if we have to process pdf further and the "save as pdf" option o Print functionality does not work

#### Usage

```
python pdf_splitter_cli.py input.pdf output.pdf --start_page 1 --end_page 5
```

## Getting Started

To use the utilities in this repository, follow these steps:

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/your-username/utilities.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Follow the usage instructions depending on the requirement directly. 


I am currently working on a Flask based web app version as well.

## Contributing

Contributions to this repository are welcome! If you have any ideas for new utilities, improvements to existing tools, or bug fixes, please open an issue or submit a pull request. Make sure to follow the established coding style and guidelines.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

The utilities provided in this repository are intended for personal and educational purposes. While efforts have been made to ensure their reliability and effectiveness, the authors and contributors of this repository are not responsible for any damage, loss, or unintended consequences resulting from the use of these utilities. Use them at your own risk.

Remember to always review and understand the code before running any scripts or tools from this repository. It is recommended to create backups of your important data before using any utilities that modify or process files.

If you have any questions, suggestions, or feedback, please don't hesitate to reach out by opening an issue or contacting the repository owner.

Happy coding and enjoy the utilities!