# DEPict Host Software

Host-side Python tooling that talks to the sensor node, trains and exports the fusion
model, and provides a local UI.

## Layout

```
depict/
  common/        # shared schemas, serial protocol, config
  acquisition/   # connect to the device, run assays, log raw data
  ml/
    training/    # dataset assembly + model training
    inference/   # host-side inference / model evaluation + export to firmware
  ui/            # local visualization/labeling UI (Streamlit)
models/          # exported/trained model artifacts (git-ignored payloads)
datasets/        # prepared training datasets (git-ignored payloads)
tests/           # pytest suite
```

## Install

```bash
pip install -e ".[ml,ui,dev]"
```

## Console scripts

| Command          | Purpose                                        |
|------------------|------------------------------------------------|
| `depict-acquire` | Connect to a board and capture assays.         |
| `depict-train`   | Train the fusion model from a dataset.         |
| `depict-infer`   | Run/evaluate inference; export model to fw.    |

## Relationship to `datapipeline/`

`acquisition/` produces raw records → `../datapipeline/` cleans/featurizes them into
training datasets → `ml/training/` trains → `ml/inference/` exports the model back to
`../firmware/src/fusion/`.
