# Humans Adaptively Deploy-Forward and Backward Planning Repository

Preprint: https://psyarxiv.com/wdbg4/

Paul B. Sharp and Eran Eldar

### Brief summary of findings

RL models assume agents rely on learned forward predictions to plan their future choices, but the authors of the paper show that backward predictions can be more efficient in some situations, particularly in environments where the number of states an agent may occupy increases with time.

In three preregistered experiments, the authors find that humans adaptively deploy forward and backward learning in the service of efficient planning. Specifically, humans engage in backward learning and planning in a diverging environment, where backward predictions can be more compactly represented than forward predictions. Conversely, in a converging environment, humans favor forward learning and planning.

The authors validate the applicability of these findings to real-life learning in a large-scale real-world prediction task.

### General structure of repository

- Each of the 4 studies has its own folder
  - [Study1](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study1)
    - [task](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study1/task)
    - [data](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study1/data)
      - Main analysis in [models.ipynb](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study1/data/models.ipynb)
    - [graph_task](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study1/graph_task)
  - [Study2](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study2)
    - [task](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study2/task)
    - [data](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study2/data)
      - Main analysis in [models.ipynb](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study2/data/models.ipynb)
    - [graph_task](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study2/graph_task)
  - [Study3](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study3)
    - [task](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study3/task)
    - [data](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study3/data)
      - Main analysis in [models.ipynb](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study3/data/models.ipynb)
    - [graph_task](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study3/graph_task)
  - [Study4](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study4)
    - [task](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study4/task)
    - [data](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study4/data)
      - Main analysis in [models.ipynb](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study4/data/models.ipynb)
    - [graph_task](https://github.com/psharp1289/Humans-Adaptively-Deploy-Forward-and-Backward-Planning/tree/main/Study4/graph_task)

- All raw data is its a zipped file outside of study folder

### OSF Repository

To see all preregistrations and data see DOI: [10.17605/OSF.IO/S286Z](https://doi.org/10.17605/OSF.IO/S286Z)

