# Explicit YouTube

`⚠️ Warning: This is an explicit content detector. You may find content that is not suitable for children.`

## Description

Videos that should `not` be on [YouTube](https://www.youtube.com/). Explicit is a `python` based YouTube scraper that efficiently collects links to videos containing explicit content. It generates a comprehensive list of such content and saves it in a CSV file. Additionally, it takes the responsible initiative to report these explicit videos. By automating the process, it contributes to ensuring a safer and more suitable environment on YouTube by actively identifying and reporting inappropriate content.

## Features

- Scrapes YouTube for videos containing explicit content.
- Collects links to explicit content videos.
- Generates a CSV file with a comprehensive list of explicit content.
- Automates the reporting process for identified explicit videos.

## Dependencies

- [python](https://www.python.org/)
- [pip](https://pypi.org/project/pip/)
- [google-api-python-client](https://pypi.org/project/google-api-python-client/)
- [requests](https://pypi.org/project/requests/)

## Resources

- [Youtube Data API](https://developers.google.com/youtube/v3)

## Installation

- Fork and clone the [repository](https://github.com/prajeshElEvEn/explicit)

```bash
git clone <repo-url>
```

- Navigate to the project directory

```bash
cd explicit
```

- Create a virtual environment

```bash
python -m venv venv
```

- Activate the virtual environment

```bash
source venv/bin/activate
```

- Install the dependencies

```bash
pip install -r requirements.txt
```

- Download `OAuth2.0` secret key `.json` file from [Google Cloud Platform](https://console.cloud.google.com/apis/credentials) and move it to the project directory
- Run the `main.ipynb` file

## Status

In progress...

## References

- [YouTube Data API](https://developers.google.com/youtube/v3)
- [YouTube Data API - Python Quickstart](https://developers.google.com/youtube/v3/quickstart/python)
- [YouTube Data API - Reporting Abuse](https://developers.google.com/youtube/v3/docs/videos/reportAbuse)
- [ChatGPT](https://chat.openai.com/)

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please submit a pull request or open an issue.

## Author

[@prajeshElEvEn](https://github.com/prajeshElEvEn)
