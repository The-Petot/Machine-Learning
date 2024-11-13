# Questions Generate

This repository contains a Jupyter Notebook for generating questions using the SQuAD dataset and Hugging Face's Transformers library. The notebook demonstrates how to preprocess the dataset, train a model, and evaluate its performance.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started, clone the repository and install the required packages:

```bash
git clone https://github.com/yourusername/questions-generate.git
cd questions-generate
pip install -r requirements.txt
```

## Usage

Open the Jupyter Notebook and follow the steps to preprocess the dataset, train the model, and evaluate its performance.

```bash
jupyter notebook QUESTIONSGENERATE.ipynb
```

## Dataset

The notebook uses the SQuAD dataset, which is loaded and preprocessed as follows:

```python
df = pd.read_json('https://raw.githubusercontent.com/Wikidepia/SQuAD-id/refs/heads/master/data/train-SQuAD-id.json')
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
