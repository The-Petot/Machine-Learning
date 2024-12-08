![image](https://github.com/user-attachments/assets/1090c2f1-e1f6-4c71-a9ce-37d8e457bf75)


# Bangkit 2024 Capstone Team : Machine Learning's Team

This repository contains a Jupyter Notebook for generating questions using the SQuAD dataset and Hugging Face's Transformers library. The notebook demonstrates how to preprocess the dataset, train a model, and evaluate its performance.

## Our Team Machine Learning
|          Nama         | Bangkit-ID |       Path       |
|:---------------------:|:----------:|:----------------:|
|   Yosep Firano La Ngari  |   M286B4KY4545  | Machine Learning |
|  Dhimas Pramudya Tridharma  |  M269B4KY1098   | Machine Learning |
|   Malika Putri Rahmawati    |  M318B4KX2392   |  Machine Learning |

## Question Answer Generate
This feature helps you create multiple-choice questions from a given text and provides the correct answers as the answer key. Simply input your text, and it will generate well-structured questions along with the corresponding answer key.

## Summarization Generate
This feature takes lengthy texts and condenses them into concise summaries designed to help students learn more efficiently. It makes studying easier and more effective.

## Tech Stacks
![stacks](https://github.com/user-attachments/assets/45339587-e6be-45d7-b030-b434e11e8aa1)

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
