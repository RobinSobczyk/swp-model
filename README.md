# single-word-processing-model

### Quick Start:
```
git clone [link hidden for anonymization]
git submodule init
git submodule update

pip install -r requirements.txt
python -m spacy download en_core_web_lg
python -m nltk.downloader "averaged_perceptron_tagger" "cmudict"
```

### Scripts

`train_repetition.py` to train a model.  
`test_repetition.py` to test a model or an ablated version of this model.  
`ablation_search.py` to ablate every neuron of a model one by one and get the results.  
`neural_trajectories.py` for PCA of activation trajectories.

`generate_queuer.py` to generate an easy to run grid search on supercomputers (require slurm)
