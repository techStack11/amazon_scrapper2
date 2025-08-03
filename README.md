# Amazon Scraper Web Application

## Project Overview

This project is a web application designed to scrape product information from Amazon. It leverages various Python libraries to achieve efficient and robust data extraction, providing a user-friendly interface for interaction.

## Features

- **Efficient Web Scraping**: Utilizes `BeautifulSoup` and `requests` for fast and reliable data extraction from Amazon.
- **Data Management**: Employs `pandas` for structured data handling and analysis.
- **Interactive User Interface**: Built with `Streamlit` for an intuitive and dynamic web application experience.
- **Environment Configuration**: Manages sensitive information and configurations using `python-dotenv`.
- **AI Integration**: Integrates `Groq` for advanced AI capabilities, potentially for natural language processing or intelligent data analysis.

## Getting Started

Follow these steps to set up and run the Amazon Scraper Web Application on your local machine.

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- pip (Python package installer)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/techStack11/amazon_scrapper2.git
    cd amazon_scrapper2
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**

    Create a `.env` file in the root directory of the project and add any necessary environment variables (e.g., API keys, if applicable). Refer to the application's specific requirements for details.

    ```
    # Example .env content (replace with actual variables)
    # API_KEY=your_api_key_here
    ```

### Running the Application

To start the Streamlit application, run the following command:

```bash
streamlit run app.py
```

This will open the application in your web browser.

## Tech Stack

This project is built using the following technologies:

| Technology | Description | Logo |
|---|---|---|
| **BeautifulSoup** | A Python library for pulling data out of HTML and XML files. | <img src="/home/ubuntu/upload/search_images/VQ8mCVFkbR16.png" width="100"> |
| **Requests** | An elegant and simple HTTP library for Python, designed for human beings. | <img src="/home/ubuntu/upload/search_images/vbTLxBE7KopK.png" width="100"> |
| **python-dotenv** | Reads key-value pairs from a .env file and sets them as environment variables. | <img src="/home/ubuntu/upload/search_images/iMpkKCnO1VjP.png" width="100"> |
| **Pandas** | A fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language. | <img src="/home/ubuntu/upload/search_images/LviooIFq9V47.png" width="100"> |
| **Streamlit** | The fastest way to build and share data apps. | <img src="/home/ubuntu/upload/search_images/Sq8D5jTdQ7rY.png" width="100"> |
| **Groq** | A leading company in AI inference technology, providing fast and efficient processing for AI models. | <img src="/home/ubuntu/upload/search_images/6ndhsmlzS4nO.png" width="100"> |

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for any bugs or feature requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Contact

For any questions or inquiries, please contact 
Ronak Bansal
ronaksspw@gmail.com


