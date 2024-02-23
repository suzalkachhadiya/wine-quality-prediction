
from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_trainer import ModelTrainer 
from mlproject.logging import logger

STAGE_NAME = "Model Trainer stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_model_trainer_config()
        data_transformation = ModelTrainer(config=data_transformation_config)
        data_transformation.train()

        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e