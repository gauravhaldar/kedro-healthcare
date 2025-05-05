
from kedro.framework.hooks import _create_hook_manager
from kedro_healthcare.pipelines.healthcare.pipeline import create_pipeline

HOOKS = _create_hook_manager()

PIPELINE_REGISTRY = {
    "__default__": create_pipeline()
}
