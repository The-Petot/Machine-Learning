# Text Summarization API

This repository contains a FastAPI-based application that provides text summarization services using a pre-trained T5 model.

## Prerequisites

- Docker
- Python 3.x
- TensorFlow
- Transformers Library

## Installation

1. **Clone the repository:**
    ```sh
    git clone [<repository-url>](https://github.com/The-Petot/Machine-Learning.git) -b feat/sumarize
    cd Machine-Learning
    ```

2. **Create a `requirements.txt` file with the following content:**
    ```plaintext
    annotated-types==0.7.0
    anyio==4.6.2.post1
    cachetools==5.5.0
    certifi==2024.8.30
    charset-normalizer==3.4.0
    click==8.1.7
    colorama==0.4.6
    dnspython==2.7.0
    docstring_parser==0.16
    email_validator==2.2.0
    fastapi==0.115.5
    fastapi-cli==0.0.5
    google-api-core==2.23.0
    google-auth==2.36.0
    google-cloud-aiplatform==1.73.0
    google-cloud-bigquery==3.27.0
    google-cloud-core==2.4.1
    google-cloud-resource-manager==1.13.1
    google-cloud-storage==2.18.2
    google-crc32c==1.6.0
    google-resumable-media==2.7.2
    googleapis-common-protos==1.66.0
    grpc-google-iam-v1==0.13.1
    grpcio==1.68.0
    grpcio-status==1.68.0
    h11==0.14.0
    httpcore==1.0.7
    httptools==0.6.4
    httpx==0.27.2
    idna==3.10
    Jinja2==3.1.4
    markdown-it-py==3.0.0
    MarkupSafe==3.0.2
    mdurl==0.1.2
    numpy==2.1.3
    packaging==24.2
    proto-plus==1.25.0
    protobuf==5.28.3
    pyasn1==0.6.1
    pyasn1_modules==0.4.1
    pydantic==2.10.0
    pydantic_core==2.27.0
    Pygments==2.18.0
    python-dateutil==2.9.0.post0
    python-dotenv==1.0.1
    python-multipart==0.0.17
    PyYAML==6.0.2
    requests==2.32.3
    rich==13.9.4
    rsa==4.9
    shapely==2.0.6
    shellingham==1.5.4
    six==1.16.0
    sniffio==1.3.1
    starlette==0.41.3
    typer==0.13.1
    typing_extensions==4.12.2
    urllib3==2.2.3
    uvicorn==0.32.1
    watchfiles==0.24.0
    websockets==14.1
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the FastAPI application:**
    ```sh
    uvicorn main:app --reload
    ```

2. **Access the API:**
    - Open a browser and navigate to `http://localhost:8000`
    - Use the `/summarize` endpoint to generate text summaries.

## Endpoints

- **GET /**: Returns a message indicating that the API is running.
- **POST /summarize**: Summarizes the provided text.

## Example

To summarize text, send a POST request to `/summarize` with a JSON payload containing the `text` field.

## License

This project is licensed under the MIT License.
