# Transformers
## Introduction
A transformer is a deep learning architecture developed by Google and based on the multi-head attention mechanism. It is based on the softmax-based attention 
mechanism. Before transformers, predecessors of attention mechanism were added to gated recurrent neural networks, such as LSTMs and gated recurrent units (GRUs), which 
processed datasets sequentially. Dependency on previous token computations prevented them from being able to parallelize the attention mechanism.

## Key Concepts

## Architecture

## Implementation
### Theory
Text is converted to numerical representations called tokens, and each token is converted into a vector via looking up from a word embedding table. 
At each layer, each token is then contextualized within the scope of the context window with other tokens via a parallel multi-head attention mechanism 
allowing the signal for key tokens to be amplified and less important tokens to be diminished.

### HuggingFace

### Tensorflow and Keras

### PyTorch
