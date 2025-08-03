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
| **BeautifulSoup** | A Python library for pulling data out of HTML and XML files. | ![BeautifulSoup Logo](https://private-us-east-1.manuscdn.com/sessionFile/f0pLx9jPZdkSy8aj6lpcvY/sandbox/cQBZWbzbnZFhzOz6bld61B-images_1754222168506_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL1ZROG1DVkZrYlIxNg.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvZjBwTHg5alBaZGtTeThhajZscGN2WS9zYW5kYm94L2NRQlpXYnpiblpGaHpPejZibGQ2MUItaW1hZ2VzXzE3NTQyMjIxNjg1MDZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMVpST0cxRFZrWnJZbEl4TmcucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk4NzYxNjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=iiEqqTBNipFYArgK4CGxvxH8iFhbBdEPK7oAdxXXiKesHga~P94HYkeEIYI9jWqedoAJ83huBYndTKJwjyPssapy9zoEY5z7cMcRn~BqbCnxRDl8UNOPfaQUZwdzy~M-uv~poruRhyqNc7e-2lWESodP9429gGLffSaMrmb9zBPq~-r-qSgidNW-zDIozZEuoNW7mISlBUqaY2RikxAhgEzE-3IvwJhcQEjsbM9A8DQmQIaxuheJBm1vDO7fvW9LPU1rlQg5zbrC5JJ1NzJRzZmwJx4WTbnZ-NAH45qf~1ENoqf67hRCd6~WtfVq-ryKFkDGLsYgod3N8nkfzBjkPw__) |
| **Requests** | An elegant and simple HTTP library for Python, designed for human beings. | ![Requests Logo](https://private-us-east-1.manuscdn.com/sessionFile/f0pLx9jPZdkSy8aj6lpcvY/sandbox/cQBZWbzbnZFhzOz6bld61B-images_1754222168506_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL3ZiVEx4QkU3S29wSw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvZjBwTHg5alBaZGtTeThhajZscGN2WS9zYW5kYm94L2NRQlpXYnpiblpGaHpPejZibGQ2MUItaW1hZ2VzXzE3NTQyMjIxNjg1MDZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMM1ppVkV4NFFrVTNTMjl3U3cucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk4NzYxNjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=jWZOVENIQbEHk7dGzJVOoK6v7URUjX~yttaF44kYcV4lkaYqVSHHURQsPpXaCqFLm10IMgcXbsdNSV95wagGHV0jMO8D4gpomDHchDkqeRcRzaDrtRx~kwtudDBr~fqK2ua3ej80o5QunuqzTpuiS8z86K9wGSrXEmRE4woXa5yaAbivXm8TNi5y02XVUaQ67PNTsLx2JY1R~ee7r-zFaU6-A3YlGs7MrnstZFaFqmo6ZjRsjrNO8b2Jc0JKvkFGAwBnteNpN8OeMYs9ioSPoe84HGU2~sNJjg2ZM5LM04Vo6fhK4kz9QoObBlBVpldPUW2k4B6pU6q2dTuz2oaYOw__) |
| **python-dotenv** | Reads key-value pairs from a .env file and sets them as environment variables. | ![python-dotenv Logo](https://private-us-east-1.manuscdn.com/sessionFile/f0pLx9jPZdkSy8aj6lpcvY/sandbox/cQBZWbzbnZFhzOz6bld61B-images_1754222168507_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL2lNcGtLQ25PMVZqUA.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvZjBwTHg5alBaZGtTeThhajZscGN2WS9zYW5kYm94L2NRQlpXYnpiblpGaHpPejZibGQ2MUItaW1hZ2VzXzE3NTQyMjIxNjg1MDdfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMmxOY0d0TFEyNVBNVlpxVUEucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk4NzYxNjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=ZEiRLCY30djEcdQuLvo50TXNw0PZRoA6uyEV5P8RoSaO6IJeEvNjgpZ2aEkhucvKZ3RC9YG5EasLlUf10LHrXbUyrY8wj9gXz1Bd6NUc6NC6ah4l0Y4Zj0VztxLdnLJ3jYIfFrDFbTe~YDRPiZcmVhAN-T5oDG~EJkQW4U13pA-5nKlV-dMnstsaCZAPAjFnvajKHezDNJuyrjA2yGw0J5mZX~-Q7vStcJOa8-9BVFrUkl8l1R74QRenwrmfmeR~eaVKasXSGURq1BoUuCQGLI5xFp~lA2bSCHHnbp1Bbt9V3r3wQNtwlvwfoc7arQwp-y7C07vRKJqCFidWUtErMw__) |
| **Pandas** | A fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language. | ![Pandas Logo](https://private-us-east-1.manuscdn.com/sessionFile/f0pLx9jPZdkSy8aj6lpcvY/sandbox/cQBZWbzbnZFhzOz6bld61B-images_1754222168507_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL0x2aW9vSUZxOVY0Nw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvZjBwTHg5alBaZGtTeThhajZscGN2WS9zYW5kYm94L2NRQlpXYnpiblpGaHpPejZibGQ2MUItaW1hZ2VzXzE3NTQyMjIxNjg1MDdfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMHgyYVc5dlNVWnhPVlkwTncucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk4NzYxNjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=JLkWpXznkZ7A2fm~oz9KaQ5gffmSGCQjcrrpBFT3I1eTQDvfD066mA86OJNQjJF86MAcpSsFUrym~sSLeF755J3zrB0Ylcer0~9o6jcPCFDgr6s7m5nArM~mvJx1A1oogzErSut26ZUkC8ZOwfigbUxymwI3zHhk2-NSfLqwmBORY5ThYTAb9FffjEB-0sWmLPxpRcvls~SdHQVdqVgSFDgVRmGq0hPOrzYERLiNlQ5VpoGolBFIhAvdjpBTkeEpfLfdvFPiJWQC~qfeDcXdgumuMKcMiHgbfRH8fBkuOjQ9cMSPHWJ--ZkNWg6DtBr9xlx~mltHYdnvfgCmnJDBBQ__) |
| **Streamlit** | The fastest way to build and share data apps. | ![Streamlit Logo](https://private-us-east-1.manuscdn.com/sessionFile/f0pLx9jPZdkSy8aj6lpcvY/sandbox/cQBZWbzbnZFhzOz6bld61B-images_1754222168508_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzL1NxOEQ1alRkUTdyWQ.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvZjBwTHg5alBaZGtTeThhajZscGN2WS9zYW5kYm94L2NRQlpXYnpiblpGaHpPejZibGQ2MUItaW1hZ2VzXzE3NTQyMjIxNjg1MDhfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMMU54T0VRMWFsUmtVVGR5V1EucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk4NzYxNjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=ovbPjR~Zd-T0iqph1wYHIFmIJb4lfZ7Zx9Rcvz~vkY0eb6ageUg9Du3xv4MKuBL4Om8ajgsc~xGSB0YbrKOLCD5MuOHrsi9S-qZZvCNdcTkMSHMezKciuvAMmaxKBj3~b52kOuhTninIPibwVg7fWcsc1u4rCi0DJMwZPI0p~6SWWNeKi-EeFqfAmhfYbNCq-c91hSjlWfyWuWZ2olnJ-CQBsLbOwGoFH5pYGV6C-IrilDFelfG0UIEaXD6Yc40NhkKJq-dN5GHZyq8t91a-LMVJPISNPnxyFcBmUkrLQ5FFOVumNBbGtcSzHFYi5fC1fSCctKGz6kMsyFsZI9Yh0A__) |
| **Groq** | A leading company in AI inference technology, providing fast and efficient processing for AI models. | ![Groq Logo](https://private-us-east-1.manuscdn.com/sessionFile/f0pLx9jPZdkSy8aj6lpcvY/sandbox/cQBZWbzbnZFhzOz6bld61B-images_1754222168508_na1fn_L2hvbWUvdWJ1bnR1L3VwbG9hZC9zZWFyY2hfaW1hZ2VzLzZuZGhzbWx6UzRuTw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvZjBwTHg5alBaZGtTeThhajZscGN2WS9zYW5kYm94L2NRQlpXYnpiblpGaHpPejZibGQ2MUItaW1hZ2VzXzE3NTQyMjIxNjg1MDhfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzVndiRzloWkM5elpXRnlZMmhmYVcxaFoyVnpMelp1WkdoemJXeDZVelJ1VHcucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk4NzYxNjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=M~oSCH9Fx677rveVoGrn430XIarKGsLxTGDC3f8PC3ZWmwhvTxtuLwdyiw397JbcKuPTSTEV6EOgIYxsPSXIfX7EG9gjwZMH2KdxkxLSso4dnlF8yEnK1Vvw3PnY5REOJjrJquh0-vygtWSIKD7Z3s7ksDSz~l3-UidxL6EV2KHEc777xe4BOzLXn9bJ5-Bqd4gpGTHqWkQGHvqwJ-P-mZmzQQFwSX8srfNHRKapEZ5zQMsTMauTBEl~KMMilMONQ3DxbBJFDeT5Sc0RBqG8cEeZMcGvdW1B7jYR4Hb3o-YYCF8GkM0QDVkA3Hs6-zgfhKomLkB7yNoAMTUNBAM6Xg__) |

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for any bugs or feature requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Contact

For any questions or inquiries, please contact.

Ronak Bansal(VNIT Nagpur).
ronaksspw@gmail.com
https://github.com/Codrecronak
