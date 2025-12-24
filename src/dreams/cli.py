import argparse
import logging
from dreams.config import get_config_for_env
from dreams.logging_config import setup_logging
from dreams.services.hf_client_local import LocalHFClient
from dreams.services.nlp_pipeline import process_csv

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", default="dev")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    cfg = get_config_for_env(args.env)
    setup_logging(cfg)

    logger.info("Starting DreamSense NLP pipeline")

    hf_client = LocalHFClient(
        default_sentiment_model=cfg["HF_MODEL"]
    )

    process_csv(
        input_path=args.input,
        output_path=args.output,
        hf_client=hf_client
    )

    logger.info(
        "Pipeline completed successfully",
        extra={"output": args.output}
    )

if __name__ == "__main__":
    main()
