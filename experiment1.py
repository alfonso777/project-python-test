import mlflow
from mlflow import log_metric, log_param, log_artifact

mlflow.set_experiment("My_Experiment")
with mlflow.start_run() as run:
    # Log a parameter (key-value pair)
    log_param("param1", 7)
    # Log a metric; metrics can be updated throughout the run
    log_metric("foo", 1)
    log_metric("foo2", 2)
    log_metric("foo3", 3)
    # Log an artifact (output file)
    with open("output1.txt", "w") as f:
        f.write("Hello world!")
        log_artifact("output1.txt")
