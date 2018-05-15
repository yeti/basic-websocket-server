#!/bin/bash

# Run Pyenv Setup

echo "export PATH=\"~/.pyenv/bin:$PATH\"" >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv install 3.5.2
pyenv global 3.5.2
