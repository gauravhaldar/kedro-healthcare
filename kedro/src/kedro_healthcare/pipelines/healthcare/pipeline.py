
from kedro.pipeline import Pipeline, node, pipeline
from kedro_healthcare.pipelines.healthcare.nodes import *

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(clean_doctor_data, "dim_doctor", "cleaned_doctor"),
        node(clean_patient_data, "dim_patient", "cleaned_patient"),
        node(clean_insurance_data, "dim_insurance", "cleaned_insurance"),
        node(merge_patient_insurance, ["cleaned_patient", "cleaned_insurance"], "patient_insurance_merged"),
        node(merge_with_doctor, ["patient_insurance_merged", "cleaned_doctor"], "doctor_merged"),
        node(final_transform, "doctor_merged", "final_enriched_data")
    ])
